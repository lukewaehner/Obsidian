**Concurrency** and **parallelism** are related but distinct concepts that are often confused. Understanding the difference is crucial for designing concurrent systems.

## Definitions

### Concurrency
**Multiple executions interacting and coordinating with each other.**

- Focus: **Composition** - structuring a program as multiple independent units
- Key aspect: **Interaction** - units need to coordinate and synchronize
- Can happen on a **single core** through time-slicing
- About **dealing with** many things at once

### Parallelism  
**Multiple executions happening at the same time.**

- Focus: **Speed** - actually executing multiple things simultaneously
- Key aspect: **Independence** - units run truly simultaneously on different cores
- Requires **multiple cores** for true parallelism
- About **doing** many things at once

## The Coffee Machine Analogy

### Concurrency (One Machine, Two Queues)

```
Queue 1: [][][]  ↘
                      → [Coffee Machine] 
Queue 2: [][][]  ↗
```

**Scenario**: One coffee machine serves two queues
- At any moment, we must **choose** which queue to serve next
- Both queues make progress, but they need to **interact**
- One queue waits while the other is being served
- This is **concurrency** - multiple tasks being managed, even though only one executes at a time

**Key point**: The queues are **concurrent** - they both exist and need coordination, but the machine can only serve one at a time.

### Parallelism (Two Machines, Two Queues)

```
Queue 1: [][][] → [Coffee Machine 1]

Queue 2: [][][] → [Coffee Machine 2]
```

**Scenario**: Two independent coffee machines, each with its own queue
- Both queues progress **independently**
- No need to figure out who goes first
- Both machines work **at the same time**
- This is **parallelism** - truly simultaneous execution

**Key point**: The queues are **parallel** - they make progress at the same time without needing to interact.

## A More Technical Example

### Concurrent but Not Parallel (Single Core)

```
Time →
CPU: [Task A][Task B][Task A][Task B][Task A][Task B]
      ↑ context switch
```

- Two tasks exist and need coordination
- CPU rapidly switches between them (time-slicing)
- **Appears** to run simultaneously to humans
- Actually only one instruction executing at a time
- This is **concurrent** but not **parallel**

### Parallel (Multiple Cores)

```
Time →
Core 1: [Task A][Task A][Task A][Task A][Task A]
Core 2: [Task B][Task B][Task B][Task B][Task B]
```

- Two tasks execute **simultaneously** on different cores
- True simultaneous execution
- This is both **concurrent AND parallel**

## Real-World Examples

### Concurrency Without Parallelism

**Operating system on a single-core CPU:**
```c
// Multiple processes exist, but only one runs at a time
Process 1: Running → Waiting → Running
Process 2: Waiting → Running → Waiting
Process 3: Waiting → Waiting → Running
```

- Many processes are concurrent (all exist, need coordination)
- Only one executes at any instant (no parallelism)
- OS scheduler decides which runs when

**Web server handling requests:**
```c
// Handle multiple clients concurrently
while (1) {
    client = accept_connection();
    handle_request(client);  // Process one at a time
}
```

Even on single core, can handle multiple clients through quick switching.

### Parallelism With Concurrency

**Multi-threaded computation:**
```c
// Parallel matrix multiplication
pthread_create(&t1, NULL, compute_rows_0_to_100, &data);
pthread_create(&t2, NULL, compute_rows_101_to_200, &data);
pthread_create(&t3, NULL, compute_rows_201_to_300, &data);
pthread_create(&t4, NULL, compute_rows_301_to_400, &data);
```

- Four threads executing **simultaneously** on four cores (parallel)
- Threads coordinate on shared data structures (concurrent)

## Why the Distinction Matters

### For Design

**Concurrency** is about **program structure**:
- How to break a problem into independent pieces
- How pieces communicate and coordinate
- Relevant even on single-core systems

**Parallelism** is about **performance optimization**:
- How to use multiple cores effectively
- How to speed up computation
- Only relevant with multiple cores

### For Programming

You can write **concurrent** programs that:
- Work correctly on single-core systems (just concurrent)
- Automatically gain speedup on multi-core systems (become parallel)

```c
// This program is CONCURRENT
pthread_t threads[4];
for (int i = 0; i < 4; i++) {
    pthread_create(&threads[i], NULL, work, &data[i]);
}

// On 1 core: concurrent but not parallel (time-sliced)
// On 4 cores: concurrent AND parallel (simultaneous)
```

## Visual Summary

```
                    CONCURRENCY
                    (interaction, coordination)
                          │
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   Single Core       Multi-Core         Multi-Core
   Time-Sliced      All cores used     Some cores idle
        │                 │                 │
   Concurrent        Concurrent +       Concurrent
   NOT Parallel        Parallel        NOT Parallel
```

## Common Misconceptions

###  "Concurrency requires multiple cores"
**Wrong!** Concurrency is about structure and interaction, works fine on single core.

###  "Parallelism is just concurrency on multiple cores"  
**Not quite!** Parallelism is about simultaneous execution. You can have parallel operations that don't interact (not concurrent in nature).

###  "Threading = parallelism"
**Not always!** Threads enable concurrency. Whether they run in parallel depends on hardware and OS scheduling.

## Key Insights

### Concurrency Is About Structure
```c
// Concurrent design: separate producer and consumer
void producer() {
    while (1) {
        item = produce();
        put_in_queue(item);
    }
}

void consumer() {
    while (1) {
        item = get_from_queue();
        consume(item);
    }
}
```

This is concurrent design even if both run on one core.

### Parallelism Is About Execution
```c
// Check how many cores are being used
int cores_used = get_cpu_usage_per_core();
// If > 1 core active, we have parallelism
```

This is about actual simultaneous execution.

## Quote from Rob Pike

> "Concurrency is about **dealing with** lots of things at once.  
> Parallelism is about **doing** lots of things at once."

- **Dealing with**: Structure, composition, coordination (concurrency)
- **Doing**: Execution, performance, simultaneous work (parallelism)

## Relationship to Other Concepts

### [[Processes vs Threads]]
Both processes and threads can be:
- **Concurrent**: Multiple exist and coordinate
- **Parallel**: Actually run simultaneously on different cores

### [[Concurrency|Synchronization]]
Needed for **concurrency** (coordination between executions), regardless of whether execution is **parallel** (simultaneous) or not.

## Practical Implications

### Writing Concurrent Code
Focus on:
- Correct coordination (locks, semaphores)
- Clear interaction patterns
- Works on any number of cores (including 1)

### Optimizing for Parallelism
Focus on:
- Minimizing shared data (reduce contention)
- Balancing load across cores
- Cache-friendly data access patterns

## Summary Table

| Aspect | Concurrency | Parallelism |
|--------|-------------|-------------|
| **Definition** | Multiple executions interacting | Multiple executions simultaneous |
| **Focus** | Program structure | Performance/speed |
| **Requires** | Coordination mechanisms | Multiple cores |
| **Works on** | Single or multiple cores | Multiple cores only |
| **About** | Dealing with many things | Doing many things |
| **Example** | OS scheduling processes | Matrix computation on 4 cores |

---

*Concurrency is about structure and interaction; parallelism is about execution and speed*