

**Segregated lists** (also called **segregated free lists** or **size classes**) maintain **multiple separate free lists**, each dedicated to a specific size or range of sizes.

## The Core Idea

Instead of one free list for all sizes:
```
Single list: [10B] -> [100B] -> [25B] -> [200B] -> [50B] -> NULL
```

Use multiple lists, each for a size range:
```
List 1-16:    [10B] -> [12B] -> [15B] -> NULL
List 17-32:   [25B] -> [30B] -> NULL
List 33-64:   [50B] -> [60B] -> NULL
List 65-128:  [100B] -> NULL
List 129-256: [200B] -> NULL
```

## Why Segregated Lists?

### Problem with Single List
- **Search overhead**: Must traverse entire list for [[Best Fit]]
- **Fragmentation**: Mixed sizes make [[Coalescing]] harder
- **Cache behavior**: Jumping between different-sized chunks is cache-unfriendly

### Benefits of Segregation
- **Fast allocation**: O(1) for popular sizes
- **Less fragmentation**: Similar-sized objects together
- **Predictable performance**: No long list traversals
- **Better cache locality**: Objects of same size near each other

## Allocation Strategy

### Request for N bytes:

1. **Determine size class**: Which list should this request use?
2. **Check dedicated list**: Is there a free chunk in that size class?
   - **If yes**: Return it immediately (O(1))
   - **If no**: Fall back to general allocator or grow the cache

3. **General allocator**: Request larger chunk from main allocator
4. **Populate size class**: Split large chunk into multiple objects of size N

## Example: Object Caches

```c
// Segregated lists for common sizes
typedef struct {
    node_t *size_16;     // List of 16-byte chunks
    node_t *size_32;     // List of 32-byte chunks
    node_t *size_64;     // List of 64-byte chunks
    node_t *size_128;    // List of 128-byte chunks
    node_t *general;     // General-purpose list for other sizes
} segregated_allocator;

void *segregated_malloc(size_t size) {
    // Try dedicated list first
    if (size <= 16 && allocator.size_16) {
        return pop_from_list(&allocator.size_16);
    }
    if (size <= 32 && allocator.size_32) {
        return pop_from_list(&allocator.size_32);
    }
    // ... more size classes ...
    
    // Fall back to general allocator
    return general_malloc(&allocator.general, size);
}
```

## Power-of-Two Segregation

Common approach: Use power-of-two size classes

```
Class 0:  1-2 bytes      → Round up to 2
Class 1:  3-4 bytes      → Round up to 4
Class 2:  5-8 bytes      → Round up to 8
Class 3:  9-16 bytes     → Round up to 16
Class 4:  17-32 bytes    → Round up to 32
Class 5:  33-64 bytes    → Round up to 64
Class 6:  65-128 bytes   → Round up to 128
Class 7:  129-256 bytes  → Round up to 256
...
```

**Trade-off**: Some [[Internal Fragmentation]] from rounding up, but fast and simple.

## The Slab Allocator

One of the most famous segregated allocators: **Jeff Bonwick's Slab Allocator** for the Solaris kernel.

See: [[Slab Allocator]] for details

### Key Innovation: Pre-initialized Objects

```
Normal allocator:
malloc() → memset() → use object → free() → later malloc() → memset() again
         ^^^^^^^^^^                                        ^^^^^^^^^^
         Initialize each time!

Slab allocator:
Initial: [pre-initialized object] [pre-initialized object] ...
malloc() → use object → free() (stays initialized)
Later malloc() → use object immediately (no initialization!)
```

**Benefit**: Avoid expensive initialization/destruction cycles for kernel objects (locks, inodes, etc.)

## Implementation: Simple Segregated Storage

```c
#define NUM_SIZE_CLASSES 10

typedef struct allocator {
    node_t *size_class[NUM_SIZE_CLASSES];
    node_t *general;  // For sizes that don't fit classes
} allocator_t;

// Size class mapping
size_t get_size_class(size_t size) {
    if (size <= 16) return 0;
    if (size <= 32) return 1;
    if (size <= 64) return 2;
    if (size <= 128) return 3;
    if (size <= 256) return 4;
    if (size <= 512) return 5;
    if (size <= 1024) return 6;
    if (size <= 2048) return 7;
    if (size <= 4096) return 8;
    return 9;  // Or use general allocator
}

void *segregated_malloc(allocator_t *a, size_t size) {
    int class = get_size_class(size);
    
    // Try to allocate from size class
    if (a->size_class[class] != NULL) {
        node_t *chunk = a->size_class[class];
        a->size_class[class] = chunk->next;
        return (void *)chunk;
    }
    
    // Size class empty - need to populate it
    return populate_and_allocate(a, class);
}

void segregated_free(allocator_t *a, void *ptr, size_t size) {
    int class = get_size_class(size);
    node_t *chunk = (node_t *)ptr;
    
    // Add back to appropriate size class
    chunk->next = a->size_class[class];
    a->size_class[class] = chunk;
}
```

## Challenges

### 1. Memory Dedication
**How much memory to dedicate to each size class?**

Too little → frequent refills from general allocator  
Too much → wasted memory in underused classes

**Bonwick's solution (slab allocator)**: Dynamic adjustment
- Request slabs (multiple pages) from general allocator
- Return empty slabs when unused
- Automatically balances between size classes

### 2. Size Class Granularity
**Fine-grained** (many size classes):
-  Less internal fragmentation
-  More lists to manage
-  More memory overhead

**Coarse-grained** (few size classes):
-  Simpler implementation
-  Less metadata overhead
-  More internal fragmentation

### 3. Large Allocations
Segregated lists work best for **small, common sizes**. Large allocations should use a different strategy (general-purpose allocator or direct page allocation).

## Real-World Allocators Using Segregation

### glibc malloc (ptmalloc)
- Fastbins: Small chunks (16-80 bytes)
- Small bins: Medium chunks (up to 512 bytes)
- Large bins: Large chunks
- Unsorted bin: Recently freed chunks

### jemalloc (Facebook, Firefox)
- Small size classes: < 4KB
- Large size classes: 4KB - 4MB
- Huge allocations: > 4MB (direct mmap)

### tcmalloc (Google)
- Small objects: < 256KB (thread-local caches)
- Large objects: ≥ 256KB (central page heap)

## Performance

| Operation | Segregated Lists | Single List |
|-----------|------------------|-------------|
| **Small alloc** | O(1) | O(n) |
| **Small free** | O(1) | O(n) or O(1) |
| **Large alloc** | Fall back to O(n) | O(n) |
| **Fragmentation** | Lower (same sizes together) | Higher (mixed sizes) |

## When to Use Segregated Lists

**Excellent for:**
- Known common allocation sizes (e.g., kernel objects)
- Applications with predictable memory patterns
- Real-time systems needing O(1) guarantees
- High-performance allocators

**Overkill for:**
- Simple programs with few allocations
- Unpredictable allocation patterns
- When simplicity is paramount

## Related Concepts

- [[Allocation Strategies]] - Segregation is an alternative approach
- [[Slab Allocator]] - Famous implementation by Bonwick
- [[Buddy Allocation]] - Another advanced technique
- [[Internal Fragmentation]] - Trade-off for speed
- [[Free List]] - Multiple lists instead of one

---

*Multiple specialized free lists for different size classes - the foundation of modern high-performance allocators*