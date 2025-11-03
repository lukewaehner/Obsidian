

A **free list** is the fundamental data structure used to track available memory chunks in a heap. Despite its name, it doesn't have to be a literal linked list - it's any data structure that manages free space.

## Basic Structure

```c
typedef struct __node_t {
    int size;              // Size of this free chunk
    struct __node_t *next; // Pointer to next free chunk
} node_t;
```

Each node represents a contiguous chunk of free memory.

## Key Insight: Embedded in Free Space

The free list is **stored inside the free memory itself** - there's nowhere else to put it! 

```
[size: 4088][next: 0][... rest of free space ...]
     ^
     |
   head pointer
```

This is different from typical data structures where you'd call `malloc()` to allocate nodes - here, you ARE implementing malloc!

## Example: Simple Free List

Initial 4KB heap:
```
head -> [size: 4088][next: NULL][........................]
         ^
         16KB address
```

After allocating 100 bytes:
```
[size:100][magic][...100 bytes...]  [size:3980][next:NULL][...]
                   ^                 ^
                   returned to user  head points here
```

## Free List Operations

### Search
Traverse the list to find a suitable chunk:
- [[Best Fit]]: Search entire list, find smallest sufficient chunk
- [[First Fit]]: Stop at first sufficient chunk
- [[Worst Fit]]: Search entire list, find largest chunk
- [[Next Fit]]: Continue from last search position

### Insert (on free())
When memory is freed, add it back to the list:
- Insert at head (fast, O(1))
- Insert in address order (helps [[Coalescing]])
- Insert in size order (helps certain strategies)

### Remove (on malloc())
When allocating, remove chunk from list (or update if [[Splitting]]).

## List Ordering Strategies

### Address Order
```
head -> [addr:100] -> [addr:500] -> [addr:1000] -> NULL
```
**Advantages:**
- Easy [[Coalescing]] (neighbors are adjacent in list)
- Reduces [[External Fragmentation]]

### Size Order
```
head -> [size:10] -> [size:100] -> [size:1000] -> NULL
```
**Advantages:**
- Fast [[Best Fit]] (just take first that fits)
- Fast [[Worst Fit]] (take last or first depending on order)

### Unordered (LIFO)
```
head -> [most recently freed] -> [...] -> NULL
```
**Advantages:**
- Fastest insertion (O(1))
- Good locality (recently freed often reused soon)

## Advanced Data Structures

Simple linked lists can be slow. Advanced allocators use:
- **Balanced binary trees** (Red-Black trees)
- **Splay trees** (self-adjusting)
- **Segregated free lists** (multiple lists by size)

See: [[Segregated Lists]]

## Performance Considerations

| Operation | Unordered | Address-Ordered | Size-Ordered |
|-----------|-----------|-----------------|--------------|
| Insert | O(1) | O(n) | O(n) |
| [[Best Fit]] search | O(n) | O(n) | O(log n) or O(1) |
| [[First Fit]] search | O(n) | O(n) | O(n) |
| [[Coalescing]] | O(n) | O(1) | O(n) |

## Related Concepts

- [[Splitting]] - Modifies free list when chunk is too large
- [[Coalescing]] - Combines adjacent entries in free list
- [[Headers and Metadata]] - Information stored in allocated chunks
- [[Allocation Strategies]] - Different ways to search the free list

---

*The core data structure for managing free memory*