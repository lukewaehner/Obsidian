

Every allocated chunk of memory needs **metadata** to track its size and state. This information is typically stored in a **header** immediately before the user's data.

## Why Headers Are Needed

The `free()` interface doesn't take a size parameter:
```c
void *ptr = malloc(100);
free(ptr);  // How does free() know it's 100 bytes?
```

The answer: **hidden header before the pointer!**

## Basic Header Structure

```c
typedef struct {
    int size;      // Size of the allocated region
    int magic;     // Magic number for integrity checking
} header_t;
```

## Memory Layout

```
[header: 8 bytes][........ user data: 100 bytes ........]
 ^                ^
 |                ptr (returned to user)
 |
 hptr (hidden from user)
```

### What the user sees:
- `ptr` pointing to 100 bytes of usable memory

### What the allocator maintains:
- `hptr` pointing to the header
- Header contains size (100) and magic number (1234567)

## Finding the Header

When `free(ptr)` is called, use pointer arithmetic:

```c
void free(void *ptr) {
    // Jump back by one header_t
    header_t *hptr = (header_t *) ptr - 1;
    
    // Sanity check
    assert(hptr->magic == 1234567);
    
    // Now we know the size!
    int size = hptr->size;
    
    // Total free space = header + user data
    int total = sizeof(header_t) + size;
    
    // Add back to free list
    add_to_free_list(hptr, total);
}
```

## Actual Allocation Size

When a user requests N bytes, the allocator must find:
```
N + sizeof(header_t) bytes
```

**Example:**
- User requests: 100 bytes
- Allocator searches for: 108 bytes (100 + 8-byte header)
- Allocator returns: pointer to the 100-byte region (header hidden)

## Magic Numbers

The magic number serves as a **sanity check**:

```c
#define MAGIC 0x12345678

// On malloc:
hptr->magic = MAGIC;

// On free:
if (hptr->magic != MAGIC) {
    // Corruption detected!
    // - Double free?
    // - Buffer overflow?
    // - Invalid pointer?
    abort();
}
```

Common corruption scenarios:
- **Buffer overflow**: User wrote past their allocation
- **Double free**: Freed the same pointer twice
- **Invalid free**: Freed a pointer that wasn't from malloc()

## Extended Headers

Production allocators often include more metadata:

```c
typedef struct {
    size_t size;              // Allocation size
    unsigned int magic;       // Integrity check
    struct block *next;       // For free list
    struct block *prev;       // For bidirectional free list
    int is_free;              // Allocation state
    char padding[...];        // Alignment padding
} header_t;
```

## Footers (Boundary Tags)

Some allocators add a **footer** after the user data:

```
[header][........ user data ........][footer]
```

**Purpose**: Enable backward traversal during [[Coalescing]]

```c
typedef struct {
    size_t size;  // Duplicate of header size
} footer_t;
```

With footers, you can find the previous chunk:
```c
footer_t *prev_footer = (footer_t *) current_header - 1;
header_t *prev_header = (header_t *) ((char *)current_header - prev_footer->size);
```

## Alignment Considerations

Headers must respect alignment requirements:

```c
// Ensure header is properly aligned
typedef struct __attribute__((aligned(8))) {
    size_t size;
    unsigned int magic;
} header_t;
```

**Why alignment matters:**
- CPU efficiency (aligned memory accesses are faster)
- Architecture requirements (some CPUs crash on unaligned access)
- [[../C/Pointers/Pointers|Pointer validity]] (some low bits may be assumed zero)

## Overhead Analysis

**Per allocation overhead:**
- Minimum: 8 bytes (size + magic)
- With boundary tags: 16 bytes (header + footer)
- With free list pointers: 24+ bytes

**For small allocations, this is significant:**
- Allocate 8 bytes, overhead is 8 bytes = 50% waste!
- Allocate 1000 bytes, overhead is 8 bytes = 0.8% waste

This is why [[Segregated Lists]] and [[Slab Allocator]] exist for small objects.

## Related Concepts

- [[Free List]] - Free chunks also need metadata (size + next pointer)
- [[Splitting]] - Must create new headers when splitting chunks
- [[Coalescing]] - Uses headers to identify chunk boundaries
- [[../C/Pointers/Pointers|Pointer Arithmetic]] - Essential for header manipulation

## Example: Complete malloc/free with Headers

```c
void *my_malloc(size_t size) {
    // Search for chunk of size + header
    node_t *chunk = find_free_chunk(size + sizeof(header_t));
    if (!chunk) return NULL;
    
    // Set up header
    header_t *hptr = (header_t *)chunk;
    hptr->size = size;
    hptr->magic = MAGIC;
    
    // Return pointer past header
    return (void *)(hptr + 1);
}

void my_free(void *ptr) {
    // Get header
    header_t *hptr = (header_t *)ptr - 1;
    
    // Validate
    assert(hptr->magic == MAGIC);
    
    // Add back to free list
    add_to_free_list(hptr, hptr->size + sizeof(header_t));
}
```

---

*The hidden bookkeeping data that makes malloc/free work*