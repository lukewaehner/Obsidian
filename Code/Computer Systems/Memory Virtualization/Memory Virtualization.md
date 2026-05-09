Memory management is a fundamental aspect of both user-level programs and operating systems. This covers how systems allocate, track, and free variable-sized chunks of memory.

## Core Problem

The central challenge in memory management is handling **variable-sized allocation requests** efficiently while minimizing fragmentation and maintaining fast allocation/deallocation times.

See: [[External Fragmentation]], [[Internal Fragmentation]]

## Key Concepts

### The Free List
A data structure that tracks available memory chunks in the heap.

See: [[Free List]]

### Fundamental Mechanisms
- [[Splitting]] - Breaking large chunks into smaller allocations
- [[Coalescing]] - Merging adjacent free chunks back together
- [[Headers and Metadata]] - Tracking allocation information
- [[Growing the Heap]] - Getting more memory

### Allocation Strategies
Different approaches to selecting which free chunk to use:

See: [[Allocation Strategies]] for overview
- [[Best Fit]] - Smallest sufficient chunk
- [[Worst Fit]] - Largest available chunk
- [[First Fit]] - First sufficient chunk found
- [[Next Fit]] - Continue search from last position

### Advanced Techniques
- [[Segregated Lists]] - Specialized allocators for common sizes
- [[Buddy Allocation]] - Binary tree-based allocation
- [[Slab Allocator]] - Kernel object caching (Solaris)

## Connections to Other Topics

### C Programming
- [[C|Dynamic Memory Allocation]] - malloc() and free() interface
- [[Pointers|Pointers]] - Essential for memory operations
- [[Code/Topics/Computer Systems/C/File IO|System Calls]] - sbrk() for heap growth

### System Level
- [[Processes|Process Memory]] - Heap management in process address space
- [[Stack & Functions|Stack vs Heap]] - Different memory regions

### Assembly
- [[Assembly|Low-level Memory Operations]] - How allocation works at the instruction level

## Key Takeaways

1. **Fragmentation is inevitable** with variable-sized requests
2. **Coalescing is critical** to maintain usable free space
3. **No single strategy is best** - depends on workload
4. **Trade-offs exist** between speed and space efficiency

---

*Based on: Operating Systems: Three Easy Pieces, Chapter 17*

%% Begin Waypoint %%
- [[Allocation Strategies]]
- [[Best Fit]]
- [[Buddy Allocation]]
- [[Coalescing]]
- [[External Fragmentation]]
- [[First Fit]]
- [[Free List]]
- [[Growing the Heap]]
- [[Headers and Metadata]]
- [[Internal Fragmentation]]
- [[Memory Protection]]
- [[Next Fit]]
- [[Page Tables]]
- [[Paging]]
- [[Segregated Lists]]
- [[Shared Memory]]
- [[Slab Allocator]]
- [[Splitting]]
- [[Virtual Address Translation]]
- [[Worst Fit]]

%% End Waypoint %%
