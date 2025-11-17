A p**mutex** (mutual exclusion lock) is a synchronization primitive that protects shared resources by ensuring only one thread can access the critical section at a time.

## Core Concept

A mutex provides **mutual exclusion** - when one thread holds the lock, all other threads attempting to acquire it must wait.

```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

pthread_mutex_lock(&lock);    // Acquire lock (blocks if held)
// Critical section - only one thread here
pthread_mutex_unlock(&lock);  // Release lock
```

## Key Operations

### Lock (Acquire)
```c
pthread_mutex_lock(&lock);
```
- **Blocks** if lock is already held
- Thread waits until lock becomes available
- Guarantees thread gets exclusive access

### Unlock (Release)
```c
pthread_mutex_unlock(&lock);
```
- Releases the lock
- Wakes up one waiting thread (if any)
- **Must be called by the thread that locked it**

### Try Lock (Non-blocking)
```c
int result = pthread_mutex_trylock(&lock);
if (result == 0) {
    // Got the lock
} else {
    // Lock was held, do something else
}
```

## Example: Protected Counter

```c
static long counter = 0;
static pthread_mutex_t counter_lock = PTHREAD_MUTEX_INITIALIZER;

void increment() {
    pthread_mutex_lock(&counter_lock);
    counter++;  // Critical section
    pthread_mutex_unlock(&counter_lock);
}
```

Without the mutex, multiple threads incrementing could cause a **race condition**:
- Thread A reads counter (100)
- Thread B reads counter (100)
- Thread A writes 101
- Thread B writes 101
- Result: Counter is 101, should be 102!

## Example: Protected Sum

```c
static long sum = 0;
static pthread_mutex_t sum_lock = PTHREAD_MUTEX_INITIALIZER;

void add_to_sum(long value) {
    pthread_mutex_lock(&sum_lock);
    sum += value;
    pthread_mutex_unlock(&sum_lock);
}
```

## Initialization

### Static Initialization
```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
```

### Dynamic Initialization
```c
pthread_mutex_t lock;
pthread_mutex_init(&lock, NULL);  // NULL = default attributes

// Later, clean up:
pthread_mutex_destroy(&lock);
```

## Important Properties

### Ownership
- Only the thread that **locked** can **unlock**
- Different from [[Semaphores]] which any thread can signal

### Non-Recursive (Default)
- A thread **cannot** lock the same mutex twice
- Would cause **deadlock** with itself
- Use `PTHREAD_MUTEX_RECURSIVE` if needed

### Fairness
- **No guarantee** which waiting thread gets lock next
- Could have starvation (thread never gets lock)
- Implementation-dependent

## Common Patterns

### Protecting Shared Data
```c
typedef struct {
    int data;
    pthread_mutex_t lock;
} protected_int;

void safe_update(protected_int *p, int value) {
    pthread_mutex_lock(&p->lock);
    p->data = value;
    pthread_mutex_unlock(&p->lock);
}
```

### Protecting Multiple Operations
```c
pthread_mutex_lock(&lock);
// Multiple operations that must happen together
balance -= amount;
other_balance += amount;
pthread_mutex_unlock(&lock);
```

## Common Pitfalls

### Forgetting to Unlock
```c
pthread_mutex_lock(&lock);
if (error) {
    return -1;  // BUG: Never unlocked!
}
pthread_mutex_unlock(&lock);
```

**Fix**: Always unlock on all paths:
```c
pthread_mutex_lock(&lock);
int result;
if (error) {
    result = -1;
} else {
    result = 0;
}
pthread_mutex_unlock(&lock);
return result;
```

### Lock Granularity Issues

**Too coarse** - Hold lock too long:
```c
pthread_mutex_lock(&lock);
// Long computation here
// Other threads blocked unnecessarily
pthread_mutex_unlock(&lock);
```

**Too fine** - Lock/unlock repeatedly:
```c
for (int i = 0; i < n; i++) {
    pthread_mutex_lock(&lock);
    data[i] = compute(i);  // Overhead of lock/unlock each iteration
    pthread_mutex_unlock(&lock);
}
```

### [[Deadlocks]]
Two threads waiting for each other's locks:
```c
// Thread 1
pthread_mutex_lock(&lock_a);
pthread_mutex_lock(&lock_b);  // Waits if Thread 2 has it

// Thread 2
pthread_mutex_lock(&lock_b);
pthread_mutex_lock(&lock_a);  // Waits if Thread 1 has it
```

## Performance Considerations

### Contention
- Multiple threads competing for same lock
- Reduces parallelism (threads wait instead of working)
- Consider using multiple locks for different data

### Critical Section Size
- **Keep it small**: Less time holding lock = more parallelism
- Only protect what needs protection
- Move computation outside critical section when possible

### Lock Overhead
- Locking/unlocking has cost
- For very short critical sections, overhead can dominate
- Consider atomic operations for simple cases

## Comparison with Other Primitives

### vs [[Semaphores]]
- Mutex: Binary (locked/unlocked), ownership concept
- Semaphore: Counter-based, no ownership, more flexible

### vs Spinlocks
- Mutex: Thread **sleeps** while waiting (yields CPU)
- Spinlock: Thread **spins** in loop checking lock (wastes CPU)
- Spinlocks faster for very short waits

### vs Atomic Operations
- Mutex: Can protect complex operations
- Atomics: Single operation only, no blocking, faster

## Related Concepts

- [[Threads]] - What mutexes synchronize
- [[Semaphores]] - More general synchronization primitive
- [[Deadlocks]] - Common problem with mutexes
- [[Condition Variables]] - For waiting on conditions, not just mutual exclusion

---

*The fundamental tool for protecting shared data in multi-threaded programs*