

External fragmentation occurs when **free space is broken into small, non-contiguous chunks** that cannot satisfy larger allocation requests, even though the total free space is sufficient.

## The Problem

```
free  used  free
|----||----||----| 
0    10    20   30
```

In this example:
- Total free space: 20 bytes (10 + 10)
- A request for 15 bytes **fails**
- The free space is fragmented into two separate chunks

## Why It Happens

External fragmentation arises from the pattern of variable-sized allocations and deallocations over time:

1. Allocate various sized chunks
2. Free chunks in random order
3. Free space becomes "swiss cheese" - full of holes

## Contrast with Internal Fragmentation

- **External fragmentation**: Unusable space *between* allocated regions
- **Internal fragmentation**: Wasted space *within* an allocated region (when you allocate more than requested)

See: [[Internal Fragmentation]]

## Solutions

### Coalescing
Merge adjacent free chunks when memory is freed.

See: [[Coalescing]]

### Compaction
Move allocated regions to consolidate free space (not possible in C due to pointers).

### Better Allocation Strategies
Choose allocation strategies that minimize fragmentation.

See: [[Allocation Strategies]]

## Impact

- **Allocation failures** despite having enough total free space
- **Reduced memory utilization**
- **Performance degradation** from searching fragmented free lists

## Related Concepts

- [[Free List]] - Tracks fragmented free space
- [[Splitting]] - Can create fragmentation
- [[Best Fit]] - Attempts to minimize fragmentation
- [[Segregated Lists]] - Reduces fragmentation for common sizes

---

*The fundamental challenge in free-space management*