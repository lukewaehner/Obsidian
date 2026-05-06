Concurrency is about managing **multiple units of execution** that can potentially interact with each other. Modern systems use concurrency to improve responsiveness, utilize multiple CPU cores, and handle multiple tasks simultaneously.

## Core Concept

**Concurrent programs** involve multiple units of execution that:
- Can "run at the same time" (conceptually or actually)
- May interact with each other (synchronization)
- Enable true parallelism on multiple cores

## Key Distinctions

### [[Concurrency vs Parallelism]]
- **Concurrency**: Multiple executions that interact and coordinate
- **Parallelism**: Multiple executions happening simultaneously

Understanding the difference is crucial for designing efficient concurrent systems.

### [[Processes vs Threads]]
Two fundamental approaches to concurrent execution:
- **Processes**: Full isolation with separate memory spaces
- **Threads**: Shared memory within the same process

## Why Concurrency?

### Performance
- **Utilize multiple cores**: Modern CPUs have 4, 8, 16+ cores
- **Overlap I/O and computation**: While waiting for disk/network, do other work
- **Responsive applications**: Handle multiple requests simultaneously

### Design
- **Natural modeling**: Some problems are inherently concurrent (web servers, GUIs)
- **Modularity**: Separate concerns into independent execution units

## Challenges

### Synchronization
When multiple executions access shared resources:
- **Race conditions**: Unpredictable results from interleaved operations
- **[[Deadlocks|Deadlock]]**: Circular waiting for resources
- **Coordination**: Ensuring operations happen in correct order

**Synchronization Primitives:**
- [[Mutex Locks]] - Mutual exclusion for protecting shared data
- [[Semaphores]] - Counting primitives for signaling and resource control

### Debugging
- **Non-deterministic**: Same program, different results each run
- **Heisenbugs**: Bugs that disappear when you try to observe them
- **Timing-dependent**: Issues only appear under specific timing conditions

## Approaches to Concurrency

### Process-Based
Using [[Processes|processes]] with `fork()`:
```c
pid_t child = fork();
if (child == 0) {
    // Child process
    work(1);
    exit(0);
}
// Parent continues
```

**Characteristics:**
- Complete isolation
- Can't corrupt each other's memory
- Expensive to create
- Difficult to share data

### [[Threads|Thread]]-Based
Using threads within a single process:
```c
pthread_t thread;
pthread_create(&thread, NULL, work_function, arg);
pthread_join(thread, NULL);
```

**Characteristics:**
- Lightweight creation
- Easy data sharing
- No isolation - can corrupt shared memory
- Requires careful synchronization

See: [[Processes vs Threads]] for detailed comparison

## Concurrency Models

### Shared Memory
Multiple executions access common memory:
- Threads in the same process
- Processes with shared memory segments
- Requires synchronization primitives

### Message Passing
Executions communicate by sending messages:
- No shared state
- Explicit communication
- Examples: MPI, Actor model

## Hardware Support

### Multiple Cores
- **True parallelism**: Different cores execute different threads simultaneously
- **Scheduling**: OS decides which threads run on which cores

### Single Core
- **Time slicing**: OS rapidly switches between executions
- **Appears concurrent**: Humans can't perceive the switching
- **Not truly parallel**: Only one instruction executing at a time

## Programming Challenges

### Correctness
- Ensuring operations are **atomic** when they need to be
- Preventing **race conditions** on shared data
- Avoiding **[[Deadlocks|deadlock]]** and **livelock**

**Key Tools:**
- [[Mutex Locks]] - For mutual exclusion and protecting critical sections
- [[Semaphores]] - For signaling and coordinating between threads

### Performance
- Minimizing **contention** for locks
- Balancing **load** across threads/processes
- Avoiding **false sharing** in caches

## Connections to Other Topics

### System Level
- [[Processes|Processes]] - Process-based concurrency
- [[CPU Basics|CPU Scheduling]] - How OS manages concurrent executions
- [[../Memory Management/Memory Management|Memory Management]] - Thread stacks and heap sharing

### C Programming
- [[C|C]] - Language features for concurrency
- [[Pointers|Pointers]] - Essential for shared memory
- System calls: `fork()`, `pthread_create()`, etc.

## What's Next?

As we explore concurrency, we'll cover:
1. **Fundamentals**: [[Concurrency vs Parallelism]], [[Processes vs Threads]]
2. **Thread APIs**: Creating and managing threads [[Threads]]
3. **Synchronization**: [[Mutex Locks]], [[Semaphores]], condition variables
4. **Problems**: [[Deadlocks]] and classic synchronization problems
5. **Classic Problems**: Producer-consumer, readers-writers, dining philosophers
6. **Advanced Topics**: Lock-free programming, memory models

## Key Takeaways

1. **Concurrency ≠ Parallelism**: They're related but distinct concepts
2. **Two main approaches**: Processes (isolated) vs Threads (shared memory)
3. **Synchronization is critical**: Uncoordinated access to shared data causes bugs
4. **Hardware enables**: Multiple cores provide true parallelism
5. **OS manages**: Scheduling, context switching, resource allocation

---

*Managing multiple units of execution - the foundation of modern high-performance systems*