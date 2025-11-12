A **semaphore** is a synchronization primitive with an integer counter that can be used for signaling between threads, controlling access to resources, or implementing more complex synchronization patterns.

## Core Concept

Unlike [[Mutex Locks]] (which are binary: locked/unlocked), semaphores have a **counter** that can be:
- **Incremented** (signal/post) - increases count
- **Decremented** (wait) - decreases count, blocks if count is 0

```c
#include <semaphore.h>

sem_t sem;
sem_init(&sem, 0, 1);  // Initialize with count 1

sem_wait(&sem);    // Decrement (blocks if 0)
// Critical section
sem_post(&sem);    // Increment
```

## Key Operations

### Wait (Decrement, P, Down)
```c
sem_wait(&sem);
```
- **Decrements** counter
- If counter was 0, **blocks** until counter > 0
- Also called `P()` operation (from Dutch "proberen" - to test)

### Post (Increment, V, Up)
```c
sem_post(&sem);
```
- **Increments** counter
- Wakes up **one** waiting thread (if any)
- Also called `V()` operation (from Dutch "verhogen" - to increase)

### Try Wait (Non-blocking)
```c
int result = sem_trywait(&sem);
if (result == 0) {
    // Successfully decremented
} else {
    // Would have blocked
}
```

## Initialization

```c
sem_t sem;

// Initialize:
// - 0 = shared between threads (not processes)
// - 1 = initial value (counter starts at 1)
sem_init(&sem, 0, 1);

// Later, clean up:
sem_destroy(&sem);
```

**Initial value determines behavior:**
- `sem_init(&sem, 0, 0)` - Starts at 0 (for signaling)
- `sem_init(&sem, 0, 1)` - Binary semaphore (mutex-like)
- `sem_init(&sem, 0, n)` - Counting semaphore (n resources)

## Types of Semaphores

### Binary Semaphore (0 or 1)
Acts like a [[Mutex Locks|mutex]]:
```c
sem_t binary_sem;
sem_init(&binary_sem, 0, 1);  // Start at 1

sem_wait(&binary_sem);  // Acquires "lock"
// Critical section
sem_post(&binary_sem);  // Releases "lock"
```

**Key difference from mutex**: Any thread can post, not just the one that waited.

### Counting Semaphore (0 to N)
Controls access to multiple identical resources:
```c
sem_t resource_sem;
sem_init(&resource_sem, 0, 5);  // 5 resources available

sem_wait(&resource_sem);  // Take one resource
// Use resource
sem_post(&resource_sem);  // Return resource
```

## Common Use Cases

### 1. Signaling Between Threads

```c
sem_t signal;
sem_init(&signal, 0, 0);  // Start at 0!

// Thread 1
void *waiter(void *arg) {
    sem_wait(&signal);  // Blocks until Thread 2 posts
    printf("Received signal!\n");
    return NULL;
}

// Thread 2
void *signaler(void *arg) {
    // Do some work
    sem_post(&signal);  // Wake up Thread 1
    return NULL;
}
```

### 2. Producer-Consumer

```c
sem_t empty_slots;
sem_t filled_slots;

sem_init(&empty_slots, 0, BUFFER_SIZE);  // Initially all empty
sem_init(&filled_slots, 0, 0);            // No items yet

// Producer
void produce(item_t item) {
    sem_wait(&empty_slots);  // Wait for empty slot
    // Add item to buffer
    sem_post(&filled_slots);  // Signal item available
}

// Consumer
item_t consume() {
    sem_wait(&filled_slots);  // Wait for item
    // Remove item from buffer
    sem_post(&empty_slots);   // Signal slot now empty
    return item;
}
```

### 3. Resource Pool (Multiple Resources)

```c
#define NUM_CONNECTIONS 10
sem_t connection_pool;
sem_init(&connection_pool, 0, NUM_CONNECTIONS);

void use_connection() {
    sem_wait(&connection_pool);  // Get a connection
    // Use connection
    sem_post(&connection_pool);  // Return connection
}
```

### 4. Rendezvous (Two-Way Barrier)

```c
sem_t barrier1, barrier2;
sem_init(&barrier1, 0, 0);
sem_init(&barrier2, 0, 0);

// Thread 1
work1();
sem_post(&barrier1);  // Signal: I'm done
sem_wait(&barrier2);  // Wait for Thread 2
continue1();

// Thread 2
work2();
sem_post(&barrier2);  // Signal: I'm done
sem_wait(&barrier1);  // Wait for Thread 1
continue2();
```

## Semaphore vs Mutex

| Feature | Semaphore | Mutex |
|---------|-----------|-------|
| **Counter** | 0 to N | 0 or 1 (binary) |
| **Ownership** | None (any thread can post) | Owner thread must unlock |
| **Purpose** | Signaling, counting resources | Mutual exclusion |
| **Recursive** | Not applicable | Can be recursive |
| **Use case** | Coordination between threads | Protecting shared data |

### When to Use Each

**Use [[Mutex Locks]]** for:
- Protecting shared data
- Critical sections
- When same thread locks and unlocks

**Use Semaphores** for:
- Signaling between threads
- Producer-consumer patterns
- Limiting concurrent access to N resources
- When different threads signal/wait

## Common Patterns

### Ordering Execution

```c
sem_t order1, order2;
sem_init(&order1, 0, 0);
sem_init(&order2, 0, 0);

// Thread 1
step_a();
sem_post(&order1);  // Signal A done
sem_wait(&order2);  // Wait for B
step_c();

// Thread 2
sem_wait(&order1);  // Wait for A
step_b();
sem_post(&order2);  // Signal B done
```

Guarantees: A → B → C

### Barrier (N threads)

```c
int count = 0;
sem_t mutex, barrier;
sem_init(&mutex, 0, 1);
sem_init(&barrier, 0, 0);

void wait_at_barrier() {
    sem_wait(&mutex);
    count++;
    if (count == N) {
        for (int i = 0; i < N; i++) {
            sem_post(&barrier);  // Wake everyone
        }
    }
    sem_wait(&barrier);
    sem_post(&mutex);
}
```

## Important Properties

### No Ownership
```c
// Valid: Different threads can wait and post
// Thread 1
sem_wait(&sem);

// Thread 2
sem_post(&sem);  // OK! No ownership required
```

### Cannot "Read" Counter
- No way to check current value without changing it
- Must track state separately if needed

### No Priority
- No guarantee which waiting thread is woken
- Could have starvation

## Common Pitfalls

### Forgetting to Post
```c
sem_wait(&sem);
if (error) {
    return -1;  // BUG: Never posted!
}
sem_post(&sem);
```

### Wrong Initial Value
```c
sem_init(&signal, 0, 1);  // WRONG for signaling
// First wait() succeeds before any post()!

sem_init(&signal, 0, 0);  // CORRECT for signaling
// First wait() blocks until post()
```

### [[Deadlocks]] with Multiple Semaphores
```c
// Thread 1
sem_wait(&sem_a);
sem_wait(&sem_b);  // Could deadlock

// Thread 2
sem_wait(&sem_b);
sem_wait(&sem_a);  // Could deadlock
```

**Fix**: Always acquire in same order, or use timeouts.

## Performance Considerations

### Blocking Overhead
- Waiting threads go to sleep (context switch)
- Fine for long waits
- Expensive for very short waits

### Thundering Herd
- Multiple threads wake up on post()
- But only one succeeds in wait()
- Others go back to sleep (wasted work)

## POSIX Semaphore Functions

```c
#include <semaphore.h>

sem_t sem;

// Initialize
sem_init(&sem, 0, initial_value);

// Operations
sem_wait(&sem);      // Block until decrementable
sem_trywait(&sem);   // Non-blocking wait
sem_timedwait(&sem, &timeout);  // Wait with timeout
sem_post(&sem);      // Increment

// Cleanup
sem_destroy(&sem);

// Query (non-standard)
int value;
sem_getvalue(&sem, &value);  // Don't rely on this
```

## Related Concepts

- [[Mutex Locks]] - Binary exclusion primitive
- [[Threads]] - What semaphores coordinate
- [[Condition Variables]] - Alternative for signaling with predicates
- [[Deadlocks]] - Risk when using multiple semaphores

## Classic Problems Using Semaphores

- **Producer-Consumer** (bounded buffer)
- **Readers-Writers** (multiple readers, exclusive writers)
- **Dining Philosophers** (resource allocation, deadlock)

---

*A flexible counting primitive for thread synchronization and signaling*