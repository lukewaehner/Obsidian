

**Worst Fit** searches the entire [[Free List]] and returns the **largest chunk available**, regardless of how much larger it is than needed.

## Strategy

Given a request for N bytes:
1. Search through **entire** free list
2. Find the **largest** chunk
3. Allocate from that chunk

## Example

Free list:
```
head -> [10B] -> [30B] -> [20B] -> [50B] -> NULL
```

**Request: 15 bytes**

Worst fit examines all chunks:
- 10B: too small
- 30B: fits
- 20B: fits
- 50B: fits ← **LARGEST available**

**Result**: Allocate from 50B chunk

After [[Splitting]]:
```
head -> [10B] -> [30B] -> [20B] -> [35B] -> NULL
                                     ^
                                     large leftover
```

## Intuition

**Goal**: Leave large chunks free instead of small splinters
- [[Best Fit]] tends to create tiny unusable fragments
- Worst fit tries to keep leftovers large and usable
- Theory: Large leftover chunks are more likely to be useful later

## Implementation

```c
void *worst_fit_malloc(size_t size) {
    node_t *current = head;
    node_t *worst = NULL;
    size_t worst_size = 0;  // Track largest
    
    // Search entire list for largest chunk
    while (current != NULL) {
        if (current->size >= size && current->size > worst_size) {
            worst = current;
            worst_size = current->size;
        }
        current = current->next;
    }
    
    if (worst == NULL) {
        return NULL;  // No fit found
    }
    
    // Allocate from largest chunk
    if (worst->size > size + MIN_SPLIT) {
        split_chunk(worst, size);
    }
    remove_from_list(worst);
    return (void *)worst;
}
```

## Performance

**Time Complexity**: O(n) - must search entire list

**Optimization**: If free list is **size-ordered (descending)**:
```
head -> [50B] -> [30B] -> [20B] -> [10B] -> NULL
```

Then worst fit becomes **O(1)** - just take the head!

## Advantages

✅ **Leaves large leftover chunks**: Avoids tiny fragments  
✅ **Simple intuition**: Use the biggest available  
✅ **Can be O(1)**: With descending size-ordered list

## Disadvantages

❌ **Slow**: Must search entire list (unless optimized)  
❌ **Wastes large chunks**: Splits big chunks for small requests  
❌ **Research shows it performs poorly**: Empirically bad in practice  
❌ **Increases fragmentation**: Contrary to intuition  
❌ **High overhead**: Still need to search whole list

## Why Worst Fit Fails in Practice

The theory seems sound, but empirical studies show **worst fit performs poorly**:

### Problem 1: Large chunks disappear quickly
```
Initial: [100B] [200B] [300B] [400B]

Request 50B (uses 400B): 
[100B] [200B] [300B] [350B]

Request 50B (uses 350B):
[100B] [200B] [300B] [300B]

Request 50B (uses 300B):
[100B] [200B] [250B] [300B]
```

Large chunks get eaten away, but medium chunks accumulate.

### Problem 2: Doesn't help with truly large allocations
When you need a 500B allocation, it doesn't matter if you have one 350B leftover or three 100B leftovers - **neither works**.

### Problem 3: Still creates fragmentation
Over time, worst fit leads to many medium-sized chunks that can't satisfy large requests:
```
[150B] [180B] [200B] [160B] [175B] [190B]
         ↑
    All "medium" - can't satisfy 300B request
```

## Comparison with Other Strategies

| Request 15B from [10B][30B][20B][50B] |
|----------------------------------------|
| **Worst Fit**: Uses 50B (largest available) |
| **[[Best Fit]]**: Uses 20B (smallest fit) |
| **[[First Fit]]**: Uses 30B (first found) |
| **[[Next Fit]]**: Uses 30B (first from last position) |

## Research Findings

Multiple studies (Wilson et al.) show:
- Worst fit has **highest fragmentation** among major strategies
- Worst fit has **similar or higher overhead** than best fit
- [[First Fit]] with address ordering outperforms worst fit
- **Not recommended** for general-purpose allocation

## When Worst Fit Might Make Sense

Rarely useful, but possible scenarios:
- **Known workload** where large allocations are very rare
- **Embedded systems** with specific memory patterns
- **Debugging/testing** to stress-test memory management

In practice: **Don't use worst fit**

## Example: Worst vs Best Fit

```
Free list: [100B] [50B] [200B]

Request: 30B

Best Fit:  Uses 50B  → Leftover: 20B
Worst Fit: Uses 200B → Leftover: 170B

Next request: 150B

Best Fit:  Uses 200B ✓
Worst Fit: Uses 170B → Fails ✗ (only has 170B, need 150B + header)
           OR barely fits but left with tiny fragment
```

Best fit preserved the large chunk; worst fit consumed it.

## Related Concepts

- [[Allocation Strategies]] - Overview of all strategies
- [[Best Fit]] - Opposite approach (choose smallest)
- [[First Fit]] - Usually performs better
- [[External Fragmentation]] - What worst fit fails to prevent
- [[Splitting]] - Creates the leftover chunks

---

*Choose the largest chunk - sounds reasonable, but empirically performs poorly*