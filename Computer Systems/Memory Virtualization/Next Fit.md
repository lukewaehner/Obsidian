

**Next Fit** is a variation of [[First Fit]] that maintains a pointer to the last allocated position and continues searching from there, rather than always starting from the head of the [[Free List]].

## Strategy

Given a request for N bytes:
1. Start searching from the **last position** (not the head)
2. Find the first chunk where `size >= N`
3. Update the "last position" pointer for next allocation
4. Wrap around to the beginning if you reach the end

## The Key Difference

**[[First Fit]]:**
```
Request 1: head -> [10B] [30B] [20B] [50B] → uses 30B
Request 2: head -> [10B] [15B] [20B] [50B] → uses 15B
Request 3: head -> [10B] [15B] [20B] [50B] → uses 15B or 20B
           ^^^^^
           Always starts here
```

**Next Fit:**
```
Request 1: head -> [10B] [30B] [20B] [50B] → uses 30B
                          ↑
                          cursor here

Request 2: head -> [10B] [15B] [20B] [50B] → uses 20B
                                ↑
                                cursor continues

Request 3: head -> [10B] [15B] [20B] [50B] → uses 50B
                                       ↑
                                       cursor continues
           Doesn't go back to head!
```

## Implementation

```c
static node_t *last_allocated = NULL;  // Remember last position

void *next_fit_malloc(size_t size) {
    node_t *current = last_allocated ? last_allocated : head;
    node_t *start = current;
    
    // Search from last position
    do {
        if (current->size >= size) {
            // Found fit!
            last_allocated = current->next ? current->next : head;
            
            if (current->size > size + MIN_SPLIT) {
                split_chunk(current, size);
            }
            remove_from_list(current);
            return (void *)current;
        }
        
        // Move to next, wrap around if needed
        current = current->next;
        if (current == NULL) {
            current = head;  // Wrap to beginning
        }
        
    } while (current != start);  // Full circle
    
    return NULL;  // No fit found
}
```

## Intuition

**Goal**: Distribute allocations more evenly throughout the list
- [[First Fit]] tends to pollute the beginning of the list
- Next fit spreads allocations across the entire free space
- Avoids repeatedly checking the same small chunks at the head

## Example Scenario

Free list after some activity:
```
head -> [5B] [8B] [10B] [100B] [200B] [300B]
```

With **first fit**, every allocation checks those small chunks first:
```
Alloc 50B: checks [5B] [8B] [10B] then uses [100B]
Alloc 50B: checks [5B] [8B] [10B] then uses [50B from 100B]
Alloc 50B: checks [5B] [8B] [10B] [50B] then uses [200B]
```

With **next fit**, after first allocation from 100B chunk:
```
Alloc 50B: starts at head, checks [5B] [8B] [10B], uses [100B], cursor at [200B]
Alloc 50B: starts at [200B], immediately uses it, cursor at [300B]
Alloc 50B: starts at [300B], immediately uses it, cursor wraps to head
```

Less repeated work checking small chunks!

## Advantages

✅ **Spreads allocations evenly**: Avoids head pollution  
✅ **Fast**: Like first fit, stops at first match  
✅ **Good locality**: Recent frees near cursor are found quickly  
✅ **Simple**: Minor modification to first fit

## Disadvantages

❌ **Breaks up large chunks**: May fragment large contiguous regions  
❌ **Cache unfriendly**: Jumps around memory more  
❌ **Similar performance to first fit**: Not dramatically better  
❌ **More complex free()**: Need to handle cursor invalidation

## Performance

**Time Complexity**: O(k) where k is distance to first fit from cursor
- **Similar to first fit** on average
- Slightly better when head is polluted
- Slightly worse if good fits are at head

## The Cursor Problem

What happens when you free a chunk?

### Problem: Cursor points to freed chunk
```
last_allocated -> [FREED CHUNK]
```

**Solution**: Update cursor to next valid chunk or NULL

### Problem: Cursor points past where we insert
If list is address-ordered and we insert before cursor, cursor relationship breaks.

**Solution**: Keep cursor validation logic in free()

## Real-World Usage

Next fit is **less common** than first fit because:
- Performance gains are marginal
- Added complexity of cursor management
- Address-ordered first fit usually performs as well or better
- Most allocators prefer simpler first fit or [[Segregated Lists]]

## Comparison

| Strategy | Starting Point | Use Case |
|----------|---------------|----------|
| **First Fit** | Always head | Simple, effective with address ordering |
| **Next Fit** | Last position | Avoid head pollution in unordered list |
| **[[Best Fit]]** | Scan all | Minimize waste (but slow) |
| **[[Worst Fit]]** | Scan all | Not recommended |

## When to Use Next Fit

**Good for:**
- Unordered free lists (where first fit pollutes head)
- Workloads with similar-sized allocations
- When head pollution is observed

**Not needed for:**
- Address-ordered lists (first fit works great)
- [[Segregated Lists]] (different approach entirely)
- Size-ordered lists (pollute differently)

## Example: Head Pollution Comparison

```
Initial: [100B] [200B] [300B] [400B]

After 10 small allocs/frees:

First Fit:
[5B][8B][10B][6B][12B] [100B] [200B] [300B] [400B]
 ^^^^^^^^^^^^^^^^^^^^^^^^
 Must scan these repeatedly!

Next Fit:
[100B] [200B] [5B][8B][10B][6B][12B] [300B] [400B]
                                ↑
                                Cursor here, spreads pollution
```

## Key Insight

Next fit is a **clever optimization for unordered lists**, but address-ordered first fit usually provides similar or better benefits with simpler implementation.

## Related Concepts

- [[First Fit]] - The base strategy this modifies
- [[Allocation Strategies]] - Overview of all strategies
- [[Free List]] - Structure being searched
- [[Coalescing]] - Becomes more complex with next fit cursor

---

*Continue searching from where you left off - spreads allocations but rarely used in practice*