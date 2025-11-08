

**Best Fit** searches the entire [[Free List]] and returns the **smallest chunk that is large enough** to satisfy the request.

## Strategy

Given a request for N bytes:
1. Search through **entire** free list
2. Find all chunks with `size >= N`
3. Return the **smallest** from that set

## Example

Free list:
```
head -> [10B] -> [30B] -> [20B] -> [50B] -> NULL
```

**Request: 15 bytes**

Best fit examines all chunks:
- 10B: too small 
- 30B: fits (30 >= 15) 
- 20B: fits (20 >= 15)   ← **SMALLEST that fits**
- 50B: fits (50 >= 15) 

**Result**: Allocate from 20B chunk

After [[Splitting]]:
```
head -> [10B] -> [30B] -> [5B] -> [50B] -> NULL
                           ^
                           leftover
```

## Intuition

**Goal**: Minimize wasted space by choosing the "tightest fit"
- If you need 15B, don't use a 50B chunk when a 20B chunk exists
- Preserve larger chunks for larger future requests
- Reduce [[Internal Fragmentation]]

## Implementation

```c
void *best_fit_malloc(size_t size) {
    node_t *current = head;
    node_t *best = NULL;
    size_t best_size = SIZE_MAX;  // Infinity
    
    // Search entire list
    while (current != NULL) {
        if (current->size >= size && current->size < best_size) {
            best = current;
            best_size = current->size;
        }
        current = current->next;
    }
    
    if (best == NULL) {
        return NULL;  // No fit found
    }
    
    // Allocate from best chunk
    if (best->size > size + MIN_SPLIT) {
        split_chunk(best, size);
    }
    remove_from_list(best);
    return (void *)best;
}
```

## Performance

**Time Complexity**: O(n) - must search entire list

**Optimization**: If free list is **size-ordered (ascending)**:
```
head -> [10B] -> [20B] -> [30B] -> [50B] -> NULL
```

Then best fit becomes **first fit** - stop at first chunk that fits!
- Time complexity: O(k) where k is position of fit
- Much faster on average

## Advantages

 **Better space utilization**: Chooses tightest fit  
 **Preserves large chunks**: Doesn't waste big chunks on small requests  
 **Intuitive**: Makes logical sense  
 **Can be optimized**: O(k) with size-ordered list

## Disadvantages

 **Slow**: Must search entire list (unless optimized)  
 **Creates tiny fragments**: Often leaves very small unusable chunks  
 **More fragmentation than expected**: Counter-intuitively, can increase [[External Fragmentation]]

## The Fragmentation Problem

Best fit often leaves **tiny leftover chunks** that are too small to be useful:

```
Request pattern: 100B, 100B, 100B

Free list: [110B] [110B] [110B] [200B]

After best fit allocations:
[10B] [10B] [10B] [200B]
  ^     ^     ^
  These are likely unusable!
```

These "splinters" accumulate and contribute to external fragmentation.

## When to Use Best Fit

**Good for:**
- Workloads with **varied request sizes**
- When **large allocations are rare** and must be preserved
- Systems where **minimizing waste is critical** (embedded systems)

**Bad for:**
- Workloads with **similar-sized requests** (use [[Segregated Lists]] instead)
- When **speed is critical** (use [[First Fit]] instead)
- Real-time systems needing **predictable performance**

## Comparison with Other Strategies

| Request 15B from [10B][30B][20B][50B] |
|----------------------------------------|
| **Best Fit**: Uses 20B (smallest fit) |
| **[[Worst Fit]]**: Uses 50B (largest) |
| **[[First Fit]]**: Uses 30B (first found) |
| **[[Next Fit]]**: Uses 30B (first from last position) |

## Research Findings

Studies show best fit is **not actually the best** in practice:
- Creates many tiny unusable fragments
- [[Worst Fit]] often performs worse
- [[First Fit]] with address ordering often performs best overall
- [[Segregated Lists]] outperform all single-strategy approaches

## Related Concepts

- [[Allocation Strategies]] - Overview of all strategies
- [[Worst Fit]] - Opposite approach (choose largest)
- [[First Fit]] - Often performs better in practice
- [[Splitting]] - Creates the leftover fragments
- [[External Fragmentation]] - What we're trying to avoid

---

*Choose the smallest chunk that fits - seems optimal, but often isn't*