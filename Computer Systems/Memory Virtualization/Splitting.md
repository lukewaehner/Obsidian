

**Splitting** is the process of breaking a large free chunk into two pieces: one to satisfy an allocation request, and one to remain on the [[Free List]].

## When It Happens

Splitting occurs when:
- A free chunk is **larger than the requested size**
- The allocator chooses to use this chunk for the allocation

## The Process

### Before Splitting
```
head -> [size: 100] -> [size: 3980] -> NULL
         addr: 0        addr: 120
```

Request: 1 byte

### After Splitting (using second chunk)
```
head -> [size: 100] -> [size: 3979] -> NULL
         addr: 0        addr: 121

Returned to user: address 120 (1 byte allocated)
```

The second chunk was split:
- **Used portion**: 1 byte at address 120
- **Remaining free**: 3979 bytes starting at address 121

## Detailed Example with Headers

Request: 100 bytes from 4088-byte free chunk

### Before:
```
[size: 4088][next: NULL][......... 4088 bytes free ........]
 ^
 head (16KB)
```

### After:
```
[size: 100][magic][....100 bytes used....] [size: 3980][next: NULL][..free..]
                    ^                       ^
                    returned (16KB + 8)     head points here
```

What happened:
1. Found a 4088-byte chunk
2. Needed 108 bytes total (100 + 8-byte header)
3. Split: 108 bytes allocated, 3980 bytes remain free
4. Updated free list to point to remaining chunk

## Impact on Fragmentation

**Splitting creates smaller chunks**, which can lead to [[External Fragmentation]]:

```
After many allocations and splits:
head -> [10B] -> [5B] -> [15B] -> [8B] -> [12B] -> NULL
```

Even if total free space is 50 bytes, a 30-byte request would fail!

## Implementation Considerations

### Minimum Split Size
Allocators often have a **minimum chunk size** they'll split to:
- Must be large enough for a [[Free List]] node (size + next pointer)
- Prevents creating uselessly tiny chunks
- Typical minimum: 16-32 bytes

```c
#define MIN_CHUNK_SIZE 16

if (chunk->size - requested_size >= MIN_CHUNK_SIZE + sizeof(header_t)) {
    // Worth splitting
    split_chunk(chunk, requested_size);
} else {
    // Just allocate the entire chunk (small internal fragmentation)
    allocate_entire_chunk(chunk);
}
```

### Which Chunk to Split?

Different [[Allocation Strategies]] choose differently:
- [[Best Fit]]: Split the smallest sufficient chunk
- [[Worst Fit]]: Split the largest chunk
- [[First Fit]]: Split the first sufficient chunk found

## Trade-offs

**Splitting too aggressively:**
-  More [[External Fragmentation]]
-  Longer [[Free List]] to search
-  More overhead from many small chunks

**Not splitting enough:**
-  More [[Internal Fragmentation]] (waste inside allocations)
-  Faster allocation (shorter free list)
-  Less external fragmentation

## Related Concepts

- [[Coalescing]] - The opposite operation, combining chunks
- [[Free List]] - Updated when splitting occurs
- [[Headers and Metadata]] - Added to the newly allocated chunk
- [[Best Fit]] - Strategy that minimizes leftover from splits

---

*Breaking large chunks to satisfy smaller requests*