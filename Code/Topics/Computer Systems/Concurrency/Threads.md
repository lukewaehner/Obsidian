

## Overview

**Threads** are lightweight processes that share the same address space. They allow concurrent execution within a single process.

**Key Idea:** Separate threads of execution within the same memory space.

---

## Why Threads?

### Problems with Processes

- **Processes are heavy** - Creating a process is expensive
- **Sharing is difficult** - Processes have separate address spaces
- **Communication overhead** - IPC mechanisms (pipes, shared memory) are complex

### Threads Solution

- **Lightweight** - Much cheaper to create than processes
- **Shared memory** - All threads share same address space
- **Easy communication** - Shared variables, no IPC needed
- **Fast** - Faster to create, switch between, and clean up

---

## What Threads Share

### Shared Between Threads

**Memory:**
- **Heap** - All dynamic allocations shared
- **Data segment** - Global variables shared
- **Code segment** - Program instructions shared

**Resources:**
- **File descriptors** - Open files shared
- **Current working directory** - Same for all threads
- **User and group IDs** - Process-level credentials
- **Page table** - Virtual memory mapping shared

### NOT Shared (Thread-Private)

- **Stack** - Each thread has own stack
- **Registers** - Each thread has own register state
- **Thread ID** - Unique identifier per thread
- **Signal mask** - Can block different signals
- **errno variable** - Thread-local error codes

---

## Comparison Table

| Feature | Processes | Threads |
|---------|-----------|---------|
| **Memory space** | Separate | Shared |
| **Creation cost** | High | Low |
| **Context switch** | Slow | Fast |
| **Communication** | IPC (complex) | Shared memory (simple) |
| **Isolation** | Strong | Weak |
| **Crash impact** | One process only | Entire process |

---

## Shared Data: Threads vs Processes

| Variable Type | fork() Processes | Threads |
|---------------|------------------|---------|
| **Global variables** | NOT shared | Shared |
| **Local variables** | NOT shared | NOT shared |
| **Local static variables** | NOT shared | Shared |
| **Heap (malloc)** | NOT shared (COW) | Shared |
| **Stack** | NOT shared | NOT shared (each thread has own) |

**Key insight:** Global and static variables are the main source of sharing (and potential data races) in threads.

---

## POSIX Threads (pthreads)

### Creating Threads

```c
#include <pthread.h>

int pthread_create(pthread_t *thread,
                   const pthread_attr_t *attr,
                   void *(*start_routine)(void *),
                   void *arg);
```

**Parameters:**
- `thread` - Pointer to thread handle (output)
- `attr` - Thread attributes (NULL = default)
- `start_routine` - Function to run in new thread
- `arg` - Argument to pass to function

**Returns:**
- 0 on success
- Error code on failure

### Example: Creating Threads

```c
#include <pthread.h>
#include <stdio.h>
#include <assert.h>

void *worker(void *arg) {
    int *no = (int *)arg;  // Cast void* to int*
    
    printf("Hello from worker %d\n", *no);
    
    // Do work
    for (unsigned long i = 0; i < 3e9; i++) {
        // Simulate work
    }
    
    printf("Worker %d done\n", *no);
    return NULL;
}

int main() {
    pthread_t th1, th2;
    int no1 = 1, no2 = 2;
    
    // Create threads
    assert(0 == pthread_create(&th1, NULL, worker, &no1));
    assert(0 == pthread_create(&th2, NULL, worker, &no2));
    
    // Wait for threads to complete
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    
    printf("All done!\n");
    return 0;
}
```

---

## Waiting for Threads

### pthread_join()

```c
int pthread_join(pthread_t thread, void **retval);
```

**Purpose:** Wait for a thread to terminate (like `wait()` for processes)

**Parameters:**
- `thread` - Thread to wait for
- `retval` - Pointer to store return value (or NULL)

**Behavior:**
- Blocks until specified thread terminates
- Retrieves thread's return value
- Cleans up thread resources

**Example:**
```c
void *thread_func(void *arg) {
    int *result = malloc(sizeof(int));
    *result = 42;
    return result;  // Return value
}

int main() {
    pthread_t th;
    pthread_create(&th, NULL, thread_func, NULL);
    
    void *retval;
    pthread_join(th, &retval);  // Wait and get return value
    
    int *result = (int *)retval;
    printf("Thread returned: %d\n", *result);
    free(result);
    
    return 0;
}
```

---

## Other Thread Functions

### pthread_self()

```c
pthread_t pthread_self(void);
```

Returns the thread ID of the calling thread.

```c
void *worker(void *arg) {
    pthread_t my_id = pthread_self();
    printf("My thread ID: %lu\n", (unsigned long)my_id);
    return NULL;
}
```

### pthread_cancel()

```c
int pthread_cancel(pthread_t thread);
```

Request cancellation of a thread.

```c
pthread_t th;
pthread_create(&th, NULL, worker, NULL);

// Later... cancel the thread
pthread_cancel(th);
pthread_join(th, NULL);
```

### pthread_exit()

```c
void pthread_exit(void *retval);
```

Terminate calling thread (can be called from any function in thread).

```c
void *worker(void *arg) {
    if (error_condition) {
        pthread_exit((void *)-1);  // Exit early with error code
    }
    // Normal processing
    pthread_exit((void *)0);
}
```

---

## Thread-Safe Programming

### The Problem: Data Races

```c
static long counter = 0;  // Shared global variable

void *increment(void *arg) {
    for (int i = 0; i < 100000; i++) {
        counter++;  // NOT ATOMIC! Race condition!
    }
    return NULL;
}

int main() {
    pthread_t th1, th2;
    pthread_create(&th1, NULL, increment, NULL);
    pthread_create(&th2, NULL, increment, NULL);
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    
    printf("Counter: %ld\n", counter);
    // Expected: 200000
    // Actual: Less! (maybe 150000, depends on timing)
}
```

### Solution: Mutexes

```c
static long counter = 0;
static pthread_mutex_t counter_lock = PTHREAD_MUTEX_INITIALIZER;

void *increment(void *arg) {
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&counter_lock);
        counter++;  // Protected!
        pthread_mutex_unlock(&counter_lock);
    }
    return NULL;
}

// Now counter will be exactly 200000
```

See: [[Mutex Locks]]

---

## Complete Example: Multi-threaded Sum

```c
// Multi-threaded sum using mutex for protection
#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

static long sum = 0;
static pthread_mutex_t sum_lock = PTHREAD_MUTEX_INITIALIZER;

typedef struct {
    long from;
    long to;
} sum_args_t;

static void sum_from_to(long from, long to) {
    if (from > to) return;
    
    for (long i = from; i <= to; ++i) {
        pthread_mutex_lock(&sum_lock);
        sum += i;
        pthread_mutex_unlock(&sum_lock);
    }
    
    fprintf(stdout, "Completed %ld to %ld\n", from, to);
}

static void *sum_thread(void *args) {
    sum_args_t *a = (sum_args_t *)args;
    sum_from_to(a->from, a->to);
    return NULL;
}

int main(int argc, char **argv) {
    assert(argc >= 3);
    
    long from = strtol(argv[1], NULL, 10);
    long to   = strtol(argv[2], NULL, 10);
    
    // Split range at midpoint
    long mid = from + (to - from) / 2;
    
    // Thread 1: Sum from...mid
    pthread_t th;
    sum_args_t a = {.from = from, .to = mid};
    assert(0 == pthread_create(&th, NULL, sum_thread, &a));
    
    // Main thread: Sum mid+1...to
    sum_from_to(mid + 1, to);
    
    // Wait for thread 1
    assert(0 == pthread_join(th, NULL));
    
    printf("Sum: %ld\n", sum);
    return 0;
}
```

**Usage:**
```bash
$ ./sum 1 100
Sum: 5050
```

---

## Thread Benefits

**1. Faster Creation**
- Creating thread: ~10-100 μs
- Creating process: ~1-10 ms
- 100× faster!

**2. Faster Context Switching**
- Thread switch: ~1-2 μs
- Process switch: ~10-20 μs
- 10× faster!

**3. Faster Cleanup**
- Thread exit: minimal cleanup
- Process exit: close all FDs, free memory, etc.

**4. Easier Communication**
- Threads: Just use shared variables
- Processes: Need IPC (pipes, sockets, shared memory)

**5. Better Cache Performance**
- Threads share code/data → better cache locality
- Processes have separate memory → more cache misses

---

## Thread Challenges

**1. Data Races**
- Multiple threads accessing same data
- At least one writes
- No synchronization
- **Solution:** Mutexes, semaphores, atomic operations

**2. Deadlocks**
- Threads waiting for each other's locks
- **Solution:** Lock ordering, timeouts, deadlock detection

**3. Debugging Difficulty**
- Race conditions are nondeterministic
- Hard to reproduce bugs
- **Solution:** Thread sanitizers, careful testing

**4. Crash Propagation**
- One thread crashes → entire process dies
- **Contrast:** One process crashes → other processes OK

---

## Thread Models

### User-Level Threads (Green Threads)
- Managed by application/library
- Kernel unaware of threads
- Fast context switching
- Can't use multiple cores

### Kernel-Level Threads (Native Threads)
- Managed by kernel
- Kernel schedules threads directly
- Can use multiple cores
- Slightly slower context switching
- **POSIX threads (pthreads) are kernel-level**

### Hybrid (M:N Model)
- M user threads mapped to N kernel threads
- Best of both worlds
- Complex to implement

---

## Performance Considerations

### When Threads Help

**CPU-bound tasks on multi-core:**
```c
// Matrix multiplication
// Split work across cores
for (int i = 0; i < num_cores; i++) {
    pthread_create(&threads[i], NULL, multiply_rows, &args[i]);
}
```

**I/O-bound tasks:**
```c
// Web server handling requests
// One thread per connection
// While one blocks on I/O, others can run
```

### When Threads Don't Help

**Single core CPU:**
- Context switching overhead
- No parallelism possible

**Lock contention:**
- If threads constantly wait for same lock
- No parallelism achieved

**False sharing:**
- Threads access different variables in same cache line
- Cache coherence overhead

---

## Thread Safety

### Thread-Safe Functions

**reentrant functions** can be called by multiple threads:
```c
// Thread-safe (reentrant)
int add(int a, int b) {
    return a + b;  // No shared state
}

// NOT thread-safe
int add_to_global(int a) {
    static int sum = 0;  // Shared state!
    sum += a;
    return sum;
}
```

### Standard Library Thread Safety

Some C library functions are **not thread-safe**:
- `strtok()` - use `strtok_r()` instead
- `rand()` - use `rand_r()` instead  
- `asctime()` - use `asctime_r()` instead

Safer versions end in `_r` (reentrant).

---

## Related Concepts

- [[Processes vs Threads]] - Comparison
- [[Mutex Locks]] - Thread synchronization
- [[Semaphores]] - Alternative synchronization
- [[Deadlocks]] - Common threading problem
- [[Concurrency vs Parallelism]] - Conceptual difference

## Tags
#computer-systems #threads #concurrency #pthreads #multi-threading #parallelism