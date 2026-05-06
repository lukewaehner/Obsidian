User-level allocators like `malloc()` don't have infinite memory - they must **request memory from the operating system** when they run out. This note covers how allocators grow the heap and interact with the kernel.

## The Problem

Your [[Free List]] is empty. What now?

```
Free list: head -> NULL
User requests: malloc(1000)

Where do you get the memory from?
```

## Two Approaches

### 1. Fail Gracefully
```c
void *malloc(size_t size) {
    node_t *chunk = find_free_chunk(size);
    if (chunk == NULL) {
        return NULL;  // No memory available
    }
    return allocate_from_chunk(chunk, size);
}
```

**When this is appropriate:**
- Embedded systems with fixed memory
- Real-time systems that can't tolerate system calls
- When failure is acceptable

### 2. Request More Memory from the OS
**Most allocators** grow the heap dynamically by asking the kernel for more memory.

## System Calls for Getting Memory

### Historical: brk() and sbrk()

The **program break** is the end of the heap. Moving it "up" grows the heap.

```c
#include <unistd.h>

// Set the program break to addr
int brk(void *addr);

// Increment the program break by increment bytes
void *sbrk(intptr_t increment);
```

**Example: Growing heap by 4096 bytes**
```c
void *old_break = sbrk(0);           // Get current break
void *new_mem = sbrk(4096);          // Grow by 4096 bytes
if (new_mem == (void *)-1) {
    // Failed - out of memory
    return NULL;
}
// new_mem now points to 4096 bytes of usable memory
```

**Problems with sbrk:**
- Can only grow the heap **contiguously** (must be adjacent to existing heap)
- Can't easily return memory to the OS (must shrink from the end)
- Only one heap per process
- Not thread-safe without additional locking

### Modern: mmap()

**Memory mapping** - ask the kernel for arbitrary chunks of virtual memory.

```c
#include <sys/mman.h>

void *mmap(
    void *addr,        // Hint for address (usually NULL)
    size_t length,     // Size in bytes
    int prot,          // Protection flags
    int flags,         // Mapping flags
    int fd,            // File descriptor (or -1)
    off_t offset       // Offset in file (or 0)
);

int munmap(void *addr, size_t length);  // Return memory to OS
```

## Complete mmap Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>

int main(int argc, char **argv) {
    // Get system page size (typically 4096 bytes)
    size_t pg_size = sysconf(_SC_PAGESIZE);
    
    // Request 2 pages of memory from the kernel
    void *mem = mmap(
        NULL,                           // Let kernel choose address
        2 * pg_size,                    // Size: 2 pages (8192 bytes)
        PROT_WRITE | PROT_READ,         // Permissions: read + write
        MAP_ANONYMOUS | MAP_PRIVATE,    // No file, private to process
        -1,                             // No file descriptor
        0                               // No offset
    );
    
    // Check for failure (mmap returns MAP_FAILED, which is (void *)-1)
    if (mem == MAP_FAILED) {
        perror("mmap failed");
        exit(1);
    }
    
    // Use the memory like any allocated memory
    int *array = (int *)mem;
    array[0] = 42;
    array[1] = 100;
    
    printf("Allocated %zu bytes at address %p\n", 2 * pg_size, mem);
    printf("array[0] = %d, array[1] = %d\n", array[0], array[1]);
    
    // Return memory to OS when done
    if (munmap(mem, 2 * pg_size) == -1) {
        perror("munmap failed");
        exit(1);
    }
    
    return 0;
}
```

## Understanding mmap Parameters

### addr (first parameter)
```c
NULL  // Let kernel choose address (recommended)
```
- Usually pass `NULL` to let the kernel pick an optimal address
- Can specify an address hint, but kernel may ignore it

### length (second parameter)
```c
2 * pg_size  // Request 2 pages (typically 8192 bytes)
```
- **Must be multiple of page size** (usually 4096 bytes)
- Use `sysconf(_SC_PAGESIZE)` to get system page size

### prot (third parameter) - Protection Flags
```c
PROT_READ   // Can read
PROT_WRITE  // Can write
PROT_EXEC   // Can execute (for code pages)
PROT_NONE   // No access
```

Combine with `|`:
```c
PROT_READ | PROT_WRITE        // Read/write data
PROT_READ | PROT_EXEC         // Read-only code
```

### flags (fourth parameter) - Mapping Flags

**MAP_ANONYMOUS**
```c
MAP_ANONYMOUS  // Not backed by a file (for heap memory)
```
- Memory not associated with any file
- Used for dynamic allocation
- Content initialized to zero

**MAP_PRIVATE**
```c
MAP_PRIVATE   // Private to this process
```
- Changes not visible to other processes
- Copy-on-write if forked

**MAP_SHARED** (alternative)
```c
MAP_SHARED    // Shared with other processes
```
- Used for inter-process communication
- Changes visible to other processes mapping same region

### fd and offset (fifth and sixth parameters)
```c
-1, 0  // For anonymous mapping (no file)
```
- When `MAP_ANONYMOUS`, pass `-1` for fd and `0` for offset
- When mapping a file, pass file descriptor and offset into file

## Why Pages?

**Page size** (typically 4096 bytes = 4 KB) is the fundamental unit of virtual memory.

```c
size_t pg_size = sysconf(_SC_PAGESIZE);  // Usually 4096
```

**Why this matters:**
- The MMU (Memory Management Unit) works in page-sized chunks
- Virtual-to-physical address translation happens per page
- Page tables map virtual pages to physical pages
- mmap allocations are **always rounded up to page boundaries**

**Example:**
```c
// Request 1000 bytes
void *mem = mmap(NULL, 1000, ...);

// Kernel actually allocates 4096 bytes (1 full page)
// You get 1000 usable bytes + 3096 wasted (internal fragmentation)
```

## mmap vs sbrk

| Feature | mmap | sbrk |
|---------|------|------|
| **Flexibility** | Can allocate anywhere | Must be contiguous |
| **Return memory** | Easy with munmap() | Hard (must shrink from end) |
| **Thread safety** | Thread-safe | Not thread-safe |
| **Minimum size** | 1 page (4 KB) | 1 byte |
| **Speed** | Slower (system call overhead) | Faster (simple) |
| **Modern use** |  Preferred | Legacy |

## How malloc Uses mmap

Modern allocators use **both** strategies:

### Small Allocations (< 128 KB typically)
Use `sbrk()` to grow a contiguous heap:
```c
// Malloc's internal heap
[existing heap]...[sbrk grows here]→
```

**Why:** 
- Lower overhead for small allocations
- Better locality (everything near each other)
- Can use [[Coalescing]] efficiently

### Large Allocations (≥ 128 KB typically)
Use `mmap()` to get dedicated memory:
```c
// Large allocation gets its own mapping
[heap] ... [mmap region 1] ... [mmap region 2] ...
```

**Why:**
- Easy to return large chunks with `munmap()`
- Doesn't fragment the main heap
- Isolated from other allocations

## Example: Allocator Growing Logic

```c
#include <sys/mman.h>
#include <unistd.h>

#define LARGE_ALLOCATION_THRESHOLD (128 * 1024)  // 128 KB
#define HEAP_INCREMENT (64 * 1024)               // 64 KB

void *my_malloc(size_t size) {
    // Try to allocate from existing free list
    void *chunk = find_free_chunk(size);
    if (chunk != NULL) {
        return chunk;
    }
    
    // No free chunks - need to get more memory
    
    if (size >= LARGE_ALLOCATION_THRESHOLD) {
        // Large allocation: use mmap
        size_t pages = (size + PAGE_SIZE - 1) / PAGE_SIZE;
        void *mem = mmap(NULL, pages * PAGE_SIZE,
                        PROT_READ | PROT_WRITE,
                        MAP_ANONYMOUS | MAP_PRIVATE,
                        -1, 0);
        if (mem == MAP_FAILED) {
            return NULL;
        }
        // Mark as mmap allocation (for later munmap on free)
        mark_as_mmap_chunk(mem, pages * PAGE_SIZE);
        return mem;
    } else {
        // Small allocation: grow heap with sbrk
        void *new_mem = sbrk(HEAP_INCREMENT);
        if (new_mem == (void *)-1) {
            return NULL;
        }
        // Add new memory to free list
        add_to_free_list(new_mem, HEAP_INCREMENT);
        // Retry allocation
        return my_malloc(size);
    }
}

void my_free(void *ptr) {
    if (is_mmap_chunk(ptr)) {
        // Large allocation: unmap it
        size_t size = get_mmap_chunk_size(ptr);
        munmap(ptr, size);
    } else {
        // Small allocation: add back to free list
        add_to_free_list(ptr, get_chunk_size(ptr));
    }
}
```

## Error Handling

### sbrk Errors
```c
void *mem = sbrk(4096);
if (mem == (void *)-1) {
    perror("sbrk failed");
    // Out of address space or hit process limits
}
```

### mmap Errors
```c
void *mem = mmap(NULL, size, PROT_READ | PROT_WRITE,
                 MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
if (mem == MAP_FAILED) {  // Same as (void *)-1
    perror("mmap failed");
    // Possible reasons:
    // - Out of virtual address space
    // - Hit process memory limits
    // - Invalid parameters
}
```

**Important:** mmap returns `MAP_FAILED` (which equals `(void *)-1`), **not NULL**!

## Real-World Examples

### glibc malloc (ptmalloc2)
- Small allocations (< 128 KB): Uses sbrk/brk to grow the heap
- Large allocations (≥ 128 KB): Uses mmap for dedicated mappings
- Can return large mmap chunks with munmap
- Main heap stays contiguous

### jemalloc (Facebook, Firefox)
- Uses mmap exclusively (no sbrk)
- Manages multiple "arenas" (separate heaps)
- Each arena grows via mmap
- Better for multi-threaded applications

### tcmalloc (Google)
- Also uses mmap primarily
- Thread-local caches to reduce contention
- Central page heap managed with mmap

## Connection to Virtual Memory

When you call mmap:
1. **Kernel allocates virtual pages** in your process's address space
2. **No physical memory allocated yet!** (lazy allocation)
3. On first access (read/write), **page fault** occurs
4. Kernel allocates **physical page** and updates page table
5. Access succeeds

See: [[Processes|Virtual Memory]] for details

## Related Concepts

- [[Free List]] - What the allocator does with memory from mmap/sbrk
- [[Coalescing]] - Works on the main heap (sbrk region)
- [[Segregated Lists]] - Often use mmap for large size classes
- [[Code/Topics/Computer Systems/C/File IO|System Calls]] - sbrk and mmap are system calls
- [[Processes|Process Memory]] - How virtual memory works

## Key Takeaways

1. **Allocators don't have infinite memory** - they request it from the OS
2. **mmap is modern, flexible approach** - works in page-sized chunks
3. **sbrk is legacy but still used** - for small allocations
4. **Page size matters** - mmap works in 4 KB (typically) increments
5. **Large allocations use dedicated mmap** - easier to return memory
6. **Small allocations grow contiguous heap** - better locality and less overhead

---

*How malloc gets memory from the kernel - the bridge between user-space allocation and OS memory management*