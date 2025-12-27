

The **slab allocator** is a sophisticated memory allocator designed by **Jeff Bonwick** for the Solaris kernel. It uses [[Segregated Lists]] with a key innovation: **keeping freed objects in a pre-initialized state** to avoid expensive initialization/destruction cycles.

## The Problem It Solves

### Traditional Kernel Object Allocation

```c
// Every time we need a lock:
lock_t *lock = malloc(sizeof(lock_t));
initialize_lock(lock);      // Expensive! Set up state
// ... use lock ...
destroy_lock(lock);          // Expensive! Clean up state
free(lock);

// Next time:
lock_t *lock = malloc(sizeof(lock_t));
initialize_lock(lock);      // REDUNDANT! Initialize again
// ... use lock ...
```

**Problem**: Repeatedly initializing and destroying the same type of object is **wasteful**.

### Slab Allocator Solution

```c
// First allocation:
lock_t *lock = slab_alloc(lock_cache);
// Object is ALREADY initialized! No setup needed
// ... use lock ...
slab_free(lock_cache, lock);
// Object stays INITIALIZED!

// Second allocation:
lock_t *lock = slab_alloc(lock_cache);
// Object is STILL initialized! Just use it!
```

**Key insight**: Keep freed objects in an initialized state, ready to use immediately.

## Architecture

### Three-Level Structure

```
Object Cache (for one type, e.g., locks)
    ↓
Slabs (one or more per cache)
    ↓
Objects (multiple per slab)
```

### Components

1. **Object Cache**: Manages objects of a specific type
   - Example: `lock_cache`, `inode_cache`, `process_cache`
   - One cache per frequently-used kernel structure

2. **Slab**: A contiguous chunk of memory (multiple pages)
   - Contains multiple objects of the cache's type
   - Three states: **full**, **partial**, **empty**

3. **Object**: Individual instance within a slab
   - Pre-initialized and ready to use
   - Two states: **allocated** or **free**

## Slab States

```
Empty Slab:   [Free][Free][Free][Free][Free][Free]
              (all objects free, can be reclaimed)

Partial Slab: [Used][Free][Used][Free][Used][Free]
              (some objects allocated, some free)

Full Slab:    [Used][Used][Used][Used][Used][Used]
              (all objects allocated)
```

**Allocation strategy**:
1. Try **partial slabs** first (fast, already has free objects)
2. If no partial slabs, use an **empty slab**
3. If no empty slabs, request new slab from page allocator

## Example: Lock Cache

```c
// At kernel boot time:
lock_cache = slab_cache_create(
    "lock_cache",           // Name
    sizeof(lock_t),         // Object size
    init_lock,              // Constructor function
    destroy_lock            // Destructor function
);
```

The cache pre-allocates several slabs:
```
Slab 1: [init_lock][init_lock][init_lock]...[init_lock]
Slab 2: [init_lock][init_lock][init_lock]...[init_lock]
Slab 3: [init_lock][init_lock][init_lock]...[init_lock]
         ^^^^^^^^^^
         All already initialized!
```

### Fast Allocation

```c
lock_t *lock = slab_alloc(lock_cache);
// Just returns pointer to pre-initialized lock
// No initialization needed!
```

### Fast Deallocation

```c
slab_free(lock_cache, lock);
// Lock goes back to free list
// Constructor DOES NOT run again
// Lock stays initialized!
```

## Coloring (Advanced Optimization)

**Problem**: All objects in different slabs might have the same offset, causing **cache conflicts**.

```
Slab 1: [obj at offset 0][obj at offset 64][obj at offset 128]...
Slab 2: [obj at offset 0][obj at offset 64][obj at offset 128]...
Slab 3: [obj at offset 0][obj at offset 64][obj at offset 128]...
         ^^^^^^^^^^^^^^
         All map to same CPU cache line!
```

**Solution**: Offset objects differently in each slab:

```
Slab 1: [obj][obj][obj]... (offset 0)
Slab 2:   [obj][obj][obj]... (offset 8)
Slab 3:     [obj][obj][obj]... (offset 16)
```

This spreads cache usage more evenly.

## Implementation Sketch

```c
typedef struct slab {
    void *objects;          // Array of objects
    int num_objects;        // Total objects in slab
    int num_free;           // Free objects
    bitmap_t free_map;      // Bitmap of free objects
    struct slab *next;      // Next slab in cache
} slab_t;

typedef struct object_cache {
    char *name;             // Cache name
    size_t object_size;     // Size of each object
    void (*ctor)(void *);   // Constructor
    void (*dtor)(void *);   // Destructor
    
    slab_t *partial_slabs;  // Slabs with some free objects
    slab_t *full_slabs;     // Slabs with no free objects
    slab_t *empty_slabs;    // Slabs with all objects free
} object_cache_t;

void *slab_alloc(object_cache_t *cache) {
    // Try partial slabs first
    if (cache->partial_slabs) {
        slab_t *slab = cache->partial_slabs;
        void *obj = get_free_object(slab);
        
        // Update slab state
        slab->num_free--;
        if (slab->num_free == 0) {
            // Move to full list
            move_slab(&cache->partial_slabs, &cache->full_slabs, slab);
        }
        
        return obj;
    }
    
    // No partial slabs, try empty slabs
    if (cache->empty_slabs) {
        slab_t *slab = cache->empty_slabs;
        void *obj = get_free_object(slab);
        
        slab->num_free--;
        // Move to partial list
        move_slab(&cache->empty_slabs, &cache->partial_slabs, slab);
        
        return obj;
    }
    
    // No slabs available, allocate new slab
    slab_t *new_slab = allocate_new_slab(cache);
    return slab_alloc(cache);  // Retry
}

void slab_free(object_cache_t *cache, void *obj) {
    slab_t *slab = find_slab_for_object(obj);
    
    slab->num_free++;
    mark_object_free(slab, obj);
    
    // Update slab lists based on new state
    if (slab->num_free == 1) {
        // Was full, now partial
        move_slab(&cache->full_slabs, &cache->partial_slabs, slab);
    } else if (slab->num_free == slab->num_objects) {
        // Now completely empty
        move_slab(&cache->partial_slabs, &cache->empty_slabs, slab);
        
        // Consider returning slab to system if too many empty slabs
        maybe_free_empty_slab(cache);
    }
}
```

## Memory Pressure Handling

When the system needs memory:

1. **Reap empty slabs**: Return completely free slabs to page allocator
2. **Keep partial/full slabs**: These are actively being used
3. **Balance**: Don't be too aggressive (avoid repeated alloc/free of slabs)

```c
void slab_cache_reap(object_cache_t *cache) {
    // Return some empty slabs to system
    while (cache->empty_slabs && should_free_slab(cache)) {
        slab_t *slab = cache->empty_slabs;
        cache->empty_slabs = slab->next;
        free_slab(slab);  // Return to page allocator
    }
}
```

## Performance Benefits

### Before Slab Allocator
```
Time:
- Allocate: 100 cycles
- Initialize: 500 cycles  ← EXPENSIVE
- Use: 1000 cycles
- Destroy: 300 cycles     ← EXPENSIVE
- Free: 100 cycles
Total per use: 2000 cycles
```

### With Slab Allocator (after first use)
```
Time:
- Allocate: 100 cycles (from pre-initialized cache)
- Use: 1000 cycles
- Free: 100 cycles
Total per use: 1200 cycles (40% faster!)
```

## Advantages

 **Eliminates redundant initialization**: Huge win for complex objects  
 **Fast allocation**: O(1) from partial slabs  
 **Fast deallocation**: O(1) to free list  
 **Reduced fragmentation**: Objects of same type together  
 **Cache coloring**: Better CPU cache utilization  
 **Memory reclamation**: Can return empty slabs under pressure

## Disadvantages

 **Complexity**: Much more complex than simple allocators  
 **Memory overhead**: Metadata for caches and slabs  
 **Only for known types**: Need to create cache for each type  
 **Kernel-specific**: Not useful for general-purpose malloc

## Real-World Usage

### Solaris Kernel (Original)
- Lock objects
- File system inodes
- Process descriptors
- Network packet headers
- Many other kernel structures

### Linux Kernel (Adapted)
- Uses slab allocator (or variants: SLUB, SLOB)
- `kmalloc()` family built on top of slab
- Thousands of object caches

### Other Systems
- FreeBSD, NetBSD
- Some high-performance user-space allocators inspired by slab

## Comparison with Other Allocators

| Feature | Slab | [[Buddy Allocation]] | [[Segregated Lists]] |
|---------|------|---------------------|---------------------|
| **Initialization** | Once (pre-initialized) | Every alloc | Every alloc |
| **Speed** | Fastest (O(1)) | Fast | Fast |
| **Fragmentation** | Low (same types) | High (internal) | Low |
| **Use case** | Kernel objects | Page allocation | User malloc |
| **Complexity** | High | Medium | Medium |

## Jeff Bonwick's Innovation

**Context**: In the early 1990s, kernel memory allocation was a bottleneck. Bonwick observed that:

1. Kernel allocates/frees **same object types** repeatedly
2. **Initialization was expensive** (setting up locks, lists, etc.)
3. Traditional allocators **threw away this work** on every free

**Insight**: Keep objects in an initialized state!

**Impact**: 
- Huge performance gains in Solaris kernel
- Adopted by Linux and other systems
- Changed how OS developers think about memory allocation

## Related Concepts

- [[Segregated Lists]] - Slab is a sophisticated form of segregation
- [[Internal Fragmentation]] - Slab has minimal internal fragmentation
- [[Free List]] - Slabs maintain free lists of pre-initialized objects
- [[Processes|Kernel Memory]] - Slab is for kernel, not user space

---

*Pre-initialized object caching - Jeff Bonwick's brilliant optimization that changed kernel memory allocation forever*