**Processes** and **threads** are two fundamental approaches to concurrent execution. Understanding their differences is critical for choosing the right concurrency model.

## Memory Layout Comparison

### Process
A process has its **own complete memory space**:

```
Process Memory Layout:
┌─────────────────┐
│      Code       │  ← Program instructions
├─────────────────┤
│      Data       │  ← Global variables, static data
├─────────────────┤
│      Heap       │  ← Dynamic memory (malloc)
├─────────────────┤
│       ↓         │
│                 │
│       ↑         │
├─────────────────┤
│      Stack      │  ← Local variables, function calls
├─────────────────┤
│    Registers    │  ← CPU registers (PC, SP, etc.)
└─────────────────┘
```

**Each process owns:**
-  Code (program instructions)
-  Data (global variables)
-  Heap (dynamically allocated memory)
-  Stack (function calls, local variables)
-  Registers (CPU state)

### Thread
A thread is a **lightweight unit within a process**:

```
Process with 3 Threads:
┌─────────────────────────────────────┐
│            Code (shared)            │  ← All threads share
├─────────────────────────────────────┤
│            Data (shared)            │  ← All threads share
├─────────────────────────────────────┤
│            Heap (shared)            │  ← All threads share
├─────────────────────────────────────┤
│  Thread 1  │  Thread 2  │  Thread 3 │
│  ┌──────┐  │  ┌──────┐  │  ┌──────┐ │
│  │Stack │  │  │Stack │  │  │Stack │ │  ← Each thread has own
│  └──────┘  │  └──────┘  │  └──────┘ │
│  ┌──────┐  │  ┌──────┐  │  ┌──────┐ │
│  │ Regs │  │  │ Regs │  │  │ Regs │ │  ← Each thread has own
│  └──────┘  │  └──────┘  │  └──────┘ │
└─────────────────────────────────────┘
```

**Each thread owns:**
-  Stack (separate function call stack)
-  Registers (separate CPU state)

**All threads share:**
-  Code (same program instructions)
-  Data (same global variables)
-  Heap (same dynamically allocated memory)

## Key Differences

### Isolation vs Sharing

**Processes:**
```c
// Process 1
int global = 10;

// Process 2 (after fork)
global = 20;  // Does NOT affect Process 1!
```

Processes have **complete isolation**:
-  Can't accidentally corrupt each other's memory
-  Crash in one process doesn't affect others
-  Difficult to share data (need IPC mechanisms)
-  Expensive to create and switch between

**Threads:**
```c
int global = 10;  // Shared by all threads

// Thread 1
global = 20;  // DOES affect Thread 2!

// Thread 2
printf("%d\n", global);  // Prints 20
```

Threads have **shared memory**:
-  Easy to share data (just use shared variables)
-  Lightweight to create and switch between
-  Can corrupt each other's data (race conditions)
-  Crash in one thread kills entire process

## Visual Example: Counter Program

### Process-Based

```c
int counter = 0;  // Each process has its own copy

pid_t child = fork();

if (child == 0) {
    // Child process
    counter++;
    printf("Child: %d\n", counter);   // Prints 1
    exit(0);
}

// Parent process
counter++;
printf("Parent: %d\n", counter);  // Prints 1 (separate copy!)
```

**Result**: Parent and child each have `counter = 1` (separate copies)

### Thread-Based

```c
int counter = 0;  // SHARED by all threads

void *increment(void *arg) {
    counter++;
    printf("Thread: %d\n", counter);
    return NULL;
}

pthread_t thread;
pthread_create(&thread, NULL, increment, NULL);

counter++;
printf("Main: %d\n", counter);

pthread_join(thread, NULL);
// Final counter value is 2 (shared and modified by both!)
```

**Result**: Single shared `counter` modified by both threads

## When to Use Each

### Use Processes When:

 **Need isolation**
```c
// Web server forking for each request
pid_t child = fork();
if (child == 0) {
    handle_client(client_fd);
    exit(0);  // Client crash won't affect server
}
```

 **Running different programs**
```c
// Execute external command
if (fork() == 0) {
    execvp("ls", args);  // Replace process with ls
    exit(1);
}
```

 **Security boundaries**
- Separate user processes can't access each other
- Privilege separation (drop privileges in child)

 **Fault isolation**
- One process crash doesn't take down others
- Example: Chrome uses process-per-tab

### Use Threads When:

 **Need to share data easily**
```c
// Worker threads sharing a task queue
queue_t *tasks = create_queue();  // Shared by all threads

pthread_create(&t1, NULL, worker, tasks);
pthread_create(&t2, NULL, worker, tasks);
pthread_create(&t3, NULL, worker, tasks);
// All workers access same queue
```

 **Need lightweight creation**
```c
// Quickly spawn many workers
for (int i = 0; i < 1000; i++) {
    pthread_create(&threads[i], NULL, compute, &data);
}
// Creating 1000 processes would be much slower!
```

 **Responsive UI**
```c
// GUI: UI thread + background worker thread
pthread_create(&worker, NULL, long_computation, NULL);
// UI thread stays responsive while worker computes
```

 **Parallel computation**
```c
// Matrix multiplication using 4 threads
for (int i = 0; i < 4; i++) {
    pthread_create(&threads[i], NULL, compute_chunk, &chunks[i]);
}
// All threads work on parts of shared matrix
```

## Performance Comparison

### Creation Cost

```c
// Process creation (expensive)
clock_t start = clock();
for (int i = 0; i < 100; i++) {
    if (fork() == 0) exit(0);
    wait(NULL);
}
// ~1000x slower than threads

// Thread creation (cheap)
clock_t start = clock();
for (int i = 0; i < 100; i++) {
    pthread_create(&t, NULL, func, NULL);
    pthread_join(t, NULL);
}
// Much faster!
```

**Why?**
- Process: OS must copy page tables, set up new address space
- Thread: Just allocate stack, duplicate minimal state

### Context Switch Cost

Switching between processes:
1. Save all registers
2. Switch page tables (expensive!)
3. Flush TLB (translation lookaside buffer)
4. Load new process state

Switching between threads (same process):
1. Save all registers
2. Switch stack pointer
3. Load new thread state
4. No page table switch needed!

**Result**: Thread switches are ~10x faster

### Memory Overhead

**Per process:**
- Page tables: ~4 MB
- Kernel structures: ~10 KB
- **Total**: ~4+ MB per process

**Per thread:**
- Stack: ~2 MB (configurable)
- Kernel structures: ~10 KB
- **Total**: ~2 MB per thread

Threads are ~2x more memory efficient.

## Synchronization Needs

### Processes
```c
// Minimal synchronization needed
// Each has its own memory
int x = 0;  // Process 1's x
int x = 0;  // Process 2's x (different variable!)

// To communicate, must use explicit IPC:
// - Pipes
// - Shared memory segments
// - Message queues
// - Sockets
```

### Threads
```c
// Heavy synchronization needed
// All share same memory
int x = 0;  // Shared by ALL threads!

// Thread 1
x++;  // RACE CONDITION!

// Thread 2
x++;  // RACE CONDITION!

// Need locks:
pthread_mutex_lock(&mutex);
x++;
pthread_mutex_unlock(&mutex);
```

## Comparison Table

| Aspect | Processes | Threads |
|--------|-----------|---------|
| **Memory** | Separate address spaces | Shared address space |
| **Code** | Own copy | Shared |
| **Data/Heap** | Own copy | Shared |
| **Stack** | Own stack | Each thread has own |
| **Registers** | Own registers | Each thread has own |
| **Creation** | Expensive (fork) | Cheap (pthread_create) |
| **Switching** | Slow (~10 µs) | Fast (~1 µs) |
| **Communication** | IPC required | Direct (shared memory) |
| **Isolation** | Strong (can't corrupt) | None (can corrupt) |
| **Crash impact** | Isolated | Takes down process |
| **Debugging** | Easier (isolated) | Harder (race conditions) |
| **Use case** | Isolation, security | Performance, sharing |

## Code Examples Side-by-Side

### Concurrent Counter (Processes)

```c
int counter = 0;

int main() {
    for (int i = 0; i < 10; i++) {
        if (fork() == 0) {
            counter++;
            printf("Child %d: counter = %d\n", i, counter);
            exit(0);
        }
    }
    
    // Wait for all children
    for (int i = 0; i < 10; i++) {
        wait(NULL);
    }
    
    printf("Parent: counter = %d\n", counter);
    // Parent counter is still 0!
    // Each child had its own copy
}
```

### Concurrent Counter (Threads)

```c
int counter = 0;  // SHARED
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void *increment(void *arg) {
    pthread_mutex_lock(&lock);
    counter++;
    pthread_mutex_unlock(&lock);
    return NULL;
}

int main() {
    pthread_t threads[10];
    
    for (int i = 0; i < 10; i++) {
        pthread_create(&threads[i], NULL, increment, NULL);
    }
    
    for (int i = 0; i < 10; i++) {
        pthread_join(threads[i], NULL);
    }
    
    printf("Counter = %d\n", counter);
    // Counter is 10 - shared by all threads!
}
```

## Hybrid Approach

Modern systems often use **both**:

```c
// Web server example:
// - Fork multiple worker processes (isolation)
// - Each process has thread pool (performance)

for (int i = 0; i < NUM_WORKERS; i++) {
    if (fork() == 0) {
        // Child process: create thread pool
        for (int j = 0; j < THREADS_PER_WORKER; j++) {
            pthread_create(&threads[j], NULL, handle_requests, NULL);
        }
        // Handle requests with threads
        pthread_join(...);
        exit(0);
    }
}
```

**Benefits:**
- Process isolation (crash in one worker doesn't affect others)
- Thread performance (fast request handling within each worker)
- Best of both worlds!

## Related Concepts

- [[Concurrency]] - Both processes and threads enable concurrency
- [[Concurrency vs Parallelism]] - Both can be parallel on multiple cores
- [[Processes|Process Management]] - Details on process creation and management
- [[Pointers|Pointers]] - Essential for understanding shared memory in threads

---

*Processes provide isolation; threads provide sharing and performance*