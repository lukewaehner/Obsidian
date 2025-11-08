

**Coalescing** is the process of merging adjacent free chunks into a single larger chunk. This is critical for preventing [[External Fragmentation]].

## The Problem Without Coalescing

```
Initial state:
[used][used][used] (three 100-byte allocations)

After freeing all three (WITHOUT coalescing):
head -> [100B] -> [100B] -> [100B] -> NULL
        addr:0    addr:108  addr:216
```

Even though all 300 bytes are free, a 200-byte request would **fail** because there's no single contiguous chunk!

## The Solution: Coalescing

When freeing memory, check if adjacent chunks are also free and merge them:

```
After freeing all three (WITH coalescing):
head -> [300B] -> NULL
        addr:0
```

Now a 200-byte request succeeds!

## When to Coalesce

### On free()
When returning memory to the free list:
1. Check if the **previous** neighbor is free
2. Check if the **next** neighbor is free
3. Merge all contiguous free chunks

### Deferred Coalescing
Some allocators delay coalescing:
- Coalesce only when allocation fails
- Coalesce periodically
- Trade-off: simpler free() but potentially more fragmentation

## Implementation Strategies

### Address-Ordered Free List (Easy Coalescing)

If the [[Free List]] is sorted by address:

```c
void free(void *ptr) {
    // Find position in address-ordered list
    node_t *current = find_position_in_list(ptr);
    node_t *prev = current->prev;
    node_t *next = current->next;
    
    // Check if we can merge with next chunk
    if (ptr + size == next) {
        // Merge with next
        current->size += next->size;
        current->next = next->next;
    }
    
    // Check if we can merge with previous chunk
    if (prev + prev->size == ptr) {
        // Merge with previous
        prev->size += current->size;
        prev->next = current->next;
    }
}
```

**Key insight**: If addresses are ordered, neighbors in memory are neighbors in the list!

### Unordered List (Hard Coalescing)

Must search entire list to find adjacent chunks:
```c
void coalesce(node_t *chunk) {
    // Must scan entire list to find neighbors
    for (node_t *n = head; n != NULL; n = n->next) {
        if (n + n->size == chunk) {
            // Found left neighbor
        }
        if (chunk + chunk->size == n) {
            // Found right neighbor
        }
    }
}
```

**Cost**: O(n) to find neighbors, making free() expensive.

## Example: Detailed Coalescing

### Step 1: Initial Allocations
```
[A:100][B:100][C:100]  (3 chunks allocated)
0      108    216
```

### Step 2: Free B (middle chunk)
```
[A:100][FREE:100][C:100]
        ^
        Can't coalesce yet - neighbors still allocated
```

### Step 3: Free A (creates opportunity)
```
[FREE:100][FREE:100][C:100]
    ^         ^
    These are adjacent! Coalesce!

After coalescing A and B:
[FREE:200][C:100]
```

### Step 4: Free C
```
[FREE:200][FREE:100]
    ^         ^
    Adjacent! Coalesce!

Final result:
[FREE:300]
```

## Bidirectional Coalescing

To check both directions, you need to know the size of the previous chunk. Two approaches:

### 1. Boundary Tags (Headers and Footers)
```
[header][...data...][footer]
```
Footer contains size, allowing you to jump backward.

### 2. Address-Ordered List
Just traverse the list - neighbors in memory are adjacent in list.

## Performance Impact

| List Type | Coalesce Cost | Free List Length |
|-----------|---------------|------------------|
| Address-ordered | O(1) | Shorter (merged chunks) |
| Unordered | O(n) | Longer (fragmented) |
| No coalescing | O(1) | Longest (very fragmented) |

## Trade-offs

**With aggressive coalescing:**
-  Less [[External Fragmentation]]
-  Larger contiguous chunks available
-  More overhead on free()
-  More complex implementation

**Without coalescing:**
-  Faster free() operation
-  Simpler implementation
-  Severe [[External Fragmentation]]
-  Failed allocations despite free space

## Related Concepts

- [[Splitting]] - The opposite operation
- [[Free List]] - Must be carefully maintained during coalescing
- [[External Fragmentation]] - What coalescing prevents
- [[Headers and Metadata]] - Used to identify chunk boundaries

---

*Merging adjacent free chunks to combat fragmentation*