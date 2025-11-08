

**Buddy allocation** is a memory allocation algorithm that divides memory into power-of-two sized blocks and makes [[Coalescing]] simple and fast through a clever addressing scheme.

## Core Concept

Memory is viewed as a binary tree where each node can be **split** into two equal "buddy" blocks, or buddies can be **merged** back together.

### Starting Point
Begin with one large block of size 2^N:
```
[=================== 64 KB ===================]
```

### Recursive Splitting
Split blocks in half until you find one large enough:
```
Level 0:                [64 KB]
                       /        \
Level 1:          [32 KB]      [32 KB]
                 /      \
Level 2:     [16 KB]  [16 KB]
            /      \
Level 3: [8 KB]  [8 KB]
```

## Allocation Process

### Request: 7 KB

**Step 1**: Round up to next power of two → 8 KB

**Step 2**: Split blocks until we reach 8 KB size:

```
                    [64 KB]
                   /        \
              [32 KB]       [32 KB]  (split 64)
             /      \
        [16 KB]    [16 KB]           (split 32)
       /      \
   [8 KB]    [8 KB]                  (split 16)
     ^
     Return this one!
```

**Result**: 
- Allocated: 8 KB (dark gray, leftmost)
- Free: 8 KB, 16 KB, 32 KB (remaining tree)

```
[8KB] [8KB] [16KB]     [32KB]
 ^     ^      ^           ^
 used  free   free       free
```

## The Buddy Property

Two blocks are **buddies** if:
1. They are the same size
2. They are adjacent in memory  
3. They came from splitting the same parent block

**Key Insight**: Buddy addresses differ by exactly one bit!

### Example: 64 KB block starting at address 0

```
Address (binary):
[0000000000000000]  → 0      (64 KB block)

Split into 32 KB buddies:
[0000000000000000]  → 0      (left 32 KB)
[0000000000001000]  → 32768  (right 32 KB)
                 ^
                 Differs by bit 15!

Split left 32 KB into 16 KB buddies:
[0000000000000000]  → 0      (left 16 KB)
[0000000000000100]  → 16384  (right 16 KB)
                ^
                Differs by bit 14!
```

## Coalescing (The Magic Part!)

When a block is freed, **find its buddy by flipping one bit** in the address!

```c
// Find buddy address (XOR with block size)
void *find_buddy(void *block, size_t size) {
    return (void *)((uintptr_t)block ^ size);
}
```

### Example: Free 8 KB block at address 0

```
Buddy address = 0 ^ 8192 = 8192

Check if buddy (address 8192, size 8KB) is free:
- If YES: Coalesce into 16 KB block at address 0
- If NO: Just mark this block as free
```

### Recursive Coalescing

After coalescing 8 KB blocks into 16 KB, check if that 16 KB block's buddy is free:

```
[8KB + 8KB] = [16KB]
               ^
               Now check this block's buddy (at address 16384)
```

Continue recursively up the tree until you can't coalesce anymore.

## Complete Example

### Initial State: 64 KB free
```
Tree:                [64 KB - FREE]
Memory:             [64 KB free]
```

### Allocate 7 KB (rounded to 8 KB)
```
Tree:                [64 KB]
                    /        \
                [32 KB]      [32 KB - FREE]
               /      \
          [16 KB]    [16 KB - FREE]
         /      \
    [8KB-USED] [8KB-FREE]

Memory: [8KB used][8KB free][16KB free][32KB free]
```

### Allocate 7 KB (rounded to 8 KB) again
```
Tree:                [64 KB]
                    /        \
                [32 KB]      [32 KB - FREE]
               /      \
          [16 KB]    [16 KB - FREE]
         /      \
    [8KB-USED] [8KB-USED]

Memory: [8KB used][8KB used][16KB free][32KB free]
```

### Free first 8 KB block
```
Tree:                [64 KB]
                    /        \
                [32 KB]      [32 KB - FREE]
               /      \
          [16 KB]    [16 KB - FREE]
         /      \
    [8KB-FREE] [8KB-USED]

Memory: [8KB free][8KB used][16KB free][32KB free]
```
Cannot coalesce because buddy is still used.

### Free second 8 KB block
```
Now both 8KB buddies are free!

Coalesce into [16KB]:
Tree:                [64 KB]
                    /        \
                [32 KB]      [32 KB - FREE]
               /      \
          [16KB-FREE] [16KB-FREE]

Now both 16KB buddies are free!

Coalesce into [32KB]:
Tree:                [64 KB]
                    /        \
                [32KB-FREE] [32KB-FREE]

Now both 32KB buddies are free!

Coalesce into [64KB]:
Tree:           [64KB-FREE]

Back to original state!
```

## Implementation

```c
typedef struct buddy_block {
    size_t size;              // Power of two
    bool is_free;
    struct buddy_block *next; // For free list at this level
} buddy_block_t;

// Multiple free lists, one per size
typedef struct {
    buddy_block_t *free_lists[MAX_ORDER]; // free_lists[k] = blocks of size 2^k
} buddy_allocator_t;

void *buddy_malloc(buddy_allocator_t *a, size_t size) {
    // Round up to power of two
    size_t actual_size = next_power_of_two(size);
    int order = log2(actual_size);
    
    // Find smallest available block >= actual_size
    for (int i = order; i < MAX_ORDER; i++) {
        if (a->free_lists[i] != NULL) {
            // Found a block, may need to split
            buddy_block_t *block = a->free_lists[i];
            remove_from_list(&a->free_lists[i], block);
            
            // Split down to desired size
            while (i > order) {
                i--;
                buddy_block_t *buddy = get_buddy(block, 1 << i);
                add_to_list(&a->free_lists[i], buddy);
            }
            
            return (void *)block;
        }
    }
    
    return NULL; // Out of memory
}

void buddy_free(buddy_allocator_t *a, void *ptr, size_t size) {
    buddy_block_t *block = (buddy_block_t *)ptr;
    int order = log2(size);
    
    // Coalesce with buddy if possible
    while (order < MAX_ORDER - 1) {
        buddy_block_t *buddy = find_buddy(block, 1 << order);
        
        if (!is_free(buddy) || buddy->size != block->size) {
            break; // Can't coalesce
        }
        
        // Coalesce: remove buddy from list, merge blocks
        remove_from_list(&a->free_lists[order], buddy);
        block = (block < buddy) ? block : buddy; // Use lower address
        order++;
    }
    
    // Add coalesced block to appropriate free list
    add_to_list(&a->free_lists[order], block);
}
```

## Advantages

 **Fast coalescing**: O(1) to find buddy (XOR operation)  
 **Simple**: Clear structure, easy to implement  
 **Predictable**: Always power-of-two sizes  
 **No external fragmentation within size class**: Same-sized blocks

## Disadvantages

 **Internal fragmentation**: 7 KB request → 8 KB allocated (1 KB wasted)  
 **Can waste up to 50%** per allocation  
 **Not flexible**: Only power-of-two sizes  
 **Complex for general-purpose use**: Better alternatives exist

## Internal Fragmentation Example

```
Request 65 bytes  → Allocate 128 bytes (63 bytes wasted!)
Request 129 bytes → Allocate 256 bytes (127 bytes wasted!)
Request 513 bytes → Allocate 1024 bytes (511 bytes wasted!)
```

Up to **50% waste** in worst case!

## Real-World Usage

**Linux Kernel**: Uses buddy allocation for page-level allocation
- Allocation unit: Pages (4 KB)
- Max order typically: 2^10 = 1024 pages = 4 MB
- Good for kernel because most allocations are page-sized anyway

**Not used for**: User-space malloc/free (too much internal fragmentation)

## Buddy Allocation vs Other Strategies

| Feature | Buddy | [[Segregated Lists]] | [[First Fit]] |
|---------|-------|---------------------|---------------|
| **Coalescing** | O(log n) | N/A (same sizes) | O(1) w/ address order |
| **Internal frag** | Up to 50% | Moderate | Low |
| **Speed** | Fast | Fastest | Fast |
| **Complexity** | Medium | High | Low |
| **Use case** | Kernel pages | User malloc | General purpose |

## The Math Behind Finding Buddies

For a block of size S at address A, the buddy is at:
```
buddy_address = A XOR S
```

**Why this works:**

Blocks of size S are aligned on S-byte boundaries. In binary:
- Size 8: addresses end in ...000
- Size 16: addresses end in ...0000  
- Size 32: addresses end in ...00000

Buddies differ in exactly one bit position (log₂(S)):
```
8-byte buddies:
0000 1000  (8)
0001 0000  (16)
 ^^^^ ^^^^
 differ in bit 3

XOR:
  0000 1000
⊕ 0000 1000 (size 8)
  ---------
  0001 0000  (buddy at 16!)
```

## Related Concepts

- [[Coalescing]] - Made trivial by buddy system
- [[Internal Fragmentation]] - Major disadvantage of buddy allocation
- [[Segregated Lists]] - Alternative for user-space allocation
- [[Free List]] - Buddy uses multiple free lists by size

---

*Power-of-two allocation with clever bit-based buddy finding - simple coalescing at the cost of internal fragmentation*