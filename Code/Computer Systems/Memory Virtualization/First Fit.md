

**First Fit** searches the [[Free List]] and returns the **first chunk that is large enough** to satisfy the request, without searching further.

## Strategy

Given a request for N bytes:
1. Start at the head of the free list
2. Check each chunk sequentially
3. Return the **first** chunk where `size >= N`
4. Stop searching (don't look at the rest)

## Example

Free list:
```
head -> [10B] -> [30B] -> [20B] -> [50B] -> NULL
```

**Request: 15 bytes**

First fit searches:
- 10B: too small, continue
- 30B: **fits!** Use this one, stop searching

Never examines the 20B or 50B chunks.

After [[Splitting]]:
```
head -> [10B] -> [15B] -> [20B] -> [50B] -> NULL
                  ^
                  leftover
```

## Intuition

**Goal**: Minimize search time
- Don't waste time finding the "perfect" fit
- Good enough is good enough
- Early chunks are checked most often (locality)

## Implementation

```c
void *first_fit_malloc(size_t size) {
    node_t *current = head;
    
    // Search until we find a fit
    while (current != NULL) {
        if (current->size >= size) {
            // Found first fit - stop here!
            if (current->size > size + MIN_SPLIT) {
                split_chunk(current, size);
            }
            remove_from_list(current);
            return (void *)current;
        }
        current = current->next;
    }
    
    return NULL;  // No fit found
}
```

## Performance

**Time Complexity**: O(k) where k is the position of the first fit
- **Average case**: Much faster than [[Best Fit]] or [[Worst Fit]]
- **Worst case**: O(n) if no fit exists or fit is at end

**Key advantage**: Doesn't need to examine every chunk

## The List Pollution Problem

First fit tends to **pollute the beginning of the list** with small fragments:

```
Initially: [100B] [200B] [300B] [400B]

After many allocations/frees:
[10B] [15B] [8B] [25B] [12B] [200B] [300B] [400B]
 ^                            ^
 "polluted" head              useful chunks way down list
```

**Why this happens:**
- Small allocations satisfy quickly at the head
- Small chunks get freed and added back to head
- Over time, head accumulates small fragments

**Impact:**
- Later allocations must traverse many small chunks
- Performance degrades over time
- Search cost increases

## Solution: Address-Ordered List

Keep the [[Free List]] sorted by **memory address**:

```
head -> [addr:100] -> [addr:500] -> [addr:1000] -> NULL
```

**Benefits:**
1. **Better distribution**: Frees go to their address position, not head
2. **Easier [[Coalescing]]**: Adjacent chunks are adjacent in list (O(1))
3. **Less fragmentation**: Reduces the pollution problem
4. **Research proven**: Studies show address-ordered first fit performs best

**Trade-off:**
- Insertion is O(n) instead of O(1)
- But usually worth it!

## Advantages

 **Fast**: Stops at first fit, no exhaustive search  
 **Simple**: Easy to implement and understand  
 **Effective**: With address ordering, often best overall strategy  
 **Good locality**: Recently freed chunks reused quickly (cache-friendly)

## Disadvantages

 **List pollution**: Beginning of list fills with small fragments  
 **Unpredictable**: Performance depends on list structure  
 **Not optimal space usage**: May miss better fits later in list

## First Fit Variants

### Standard First Fit
Start from head every time.

### Address-Ordered First Fit (Recommended)
Keep list sorted by address for better performance and [[Coalescing]].

### Cached First Fit
Cache the last several chunks checked to avoid re-scanning them.

## Comparison with Other Strategies

| Request 15B from [10B][30B][20B][50B] |
|----------------------------------------|
| **First Fit**: Uses 30B (first found) |
| **[[Best Fit]]**: Uses 20B (smallest fit) |
| **[[Worst Fit]]**: Uses 50B (largest) |
| **[[Next Fit]]**: Uses 30B (or later if continued) |

## Real-World Usage

First fit is **very common** in practice because:
- Fast enough for most workloads
- Simple to implement correctly
- With address ordering, excellent overall performance
- Used in many production allocators (including glibc malloc)

## Example: Address-Ordered First Fit

```c
// Free list maintained in address order
void *address_ordered_first_fit(size_t size) {
    node_t *current = head;
    
    while (current != NULL) {
        if (current->size >= size) {
            // Found fit
            void *result = allocate_from_chunk(current, size);
            return result;
        }
        current = current->next;
    }
    return NULL;
}

// When freeing, insert in address order
void address_ordered_free(void *ptr) {
    node_t *chunk = (node_t *)ptr;
    node_t *current = head;
    node_t *prev = NULL;
    
    // Find position in address-ordered list
    while (current != NULL && current < chunk) {
        prev = current;
        current = current->next;
    }
    
    // Insert chunk between prev and current
    chunk->next = current;
    if (prev != NULL) {
        prev->next = chunk;
    } else {
        head = chunk;
    }
    
    // Try to coalesce with neighbors (O(1) since adjacent!)
    coalesce(prev, chunk, current);
}
```

## Key Insight

**First fit is deceptively simple but highly effective**, especially when combined with address ordering. Research shows it often outperforms more sophisticated strategies.

## Related Concepts

- [[Allocation Strategies]] - Overview of all strategies
- [[Next Fit]] - Variation that continues from last position
- [[Best Fit]] - Alternative that searches entire list
- [[Coalescing]] - Made easier by address ordering
- [[Free List]] - Structure being searched

---

*Stop at the first chunk that fits - simple, fast, and often the best choice*