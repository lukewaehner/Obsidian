**Deadlock** occurs when two or more threads are permanently blocked, each waiting for a resource held by another thread in the cycle. The threads cannot proceed, and the program hangs.

## Core Concept

A deadlock is a **circular wait**: each thread holds a resource and waits for another resource held by the next thread in the cycle.

```c
// Classic deadlock scenario
pthread_mutex_t lock_a, lock_b;

// Thread 1
pthread_mutex_lock(&lock_a);    // Gets A
pthread_mutex_lock(&lock_b);    // Waits for B (Thread 2 has it)

// Thread 2
pthread_mutex_lock(&lock_b);    // Gets B
pthread_mutex_lock(&lock_a);    // Waits for A (Thread 1 has it)

// Result: Both threads blocked forever
```

## Necessary Conditions (Coffman Conditions)

Deadlock can only occur if **all four** of these conditions are true:

### 1. Mutual Exclusion
- At least one resource must be held in non-shareable mode
- Only one thread can use the resource at a time
- Example: [[Mutex Locks]] can only be held by one thread

### 2. Hold and Wait
- A thread holds at least one resource
- While waiting to acquire additional resources
- Example: Thread holds lock A while requesting lock B

### 3. No Preemption
- Resources cannot be forcibly taken away
- Only the holding thread can release the resource
- Example: Can't force a thread to release a mutex

### 4. Circular Wait
- There exists a cycle in the resource allocation graph
- Thread 1 waits for Thread 2, Thread 2 waits for Thread 1
- Can involve more than 2 threads

**All four must be true for deadlock to occur!**

## Simple Deadlock Example

```c
pthread_mutex_t lock_x = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t lock_y = PTHREAD_MUTEX_INITIALIZER;

void *thread1_func(void *arg) {
    pthread_mutex_lock(&lock_x);
    sleep(1);  // Increase chance of deadlock
    pthread_mutex_lock(&lock_y);
    
    // Do work with both locks
    
    pthread_mutex_unlock(&lock_y);
    pthread_mutex_unlock(&lock_x);
    return NULL;
}

void *thread2_func(void *arg) {
    pthread_mutex_lock(&lock_y);
    sleep(1);  // Increase chance of deadlock
    pthread_mutex_lock(&lock_x);
    
    // Do work with both locks
    
    pthread_mutex_unlock(&lock_x);
    pthread_mutex_unlock(&lock_y);
    return NULL;
}
```

**What happens:**
1. Thread 1 locks X
2. Thread 2 locks Y
3. Thread 1 tries to lock Y → **blocks** (Thread 2 has it)
4. Thread 2 tries to lock X → **blocks** (Thread 1 has it)
5. **Deadlock!** Neither can proceed

## Resource Allocation Graph

Visual way to detect circular wait:
- **Nodes**: Threads and resources
- **Edges**: Request (thread → resource) or assignment (resource → thread)
- **Cycle** = potential deadlock

```
Thread 1 → Lock A → Thread 2 → Lock B → Thread 1
          (holds)           (holds)
                ↑_________________________↑
                        (cycle!)
```

## Prevention Strategies

### 1. Lock Ordering (Break Circular Wait)

**Solution**: Always acquire locks in the same order globally.

```c
// Define global ordering: lock_a < lock_b
pthread_mutex_t lock_a, lock_b;

// Thread 1
pthread_mutex_lock(&lock_a);  // Lower-numbered first
pthread_mutex_lock(&lock_b);
// Work
pthread_mutex_unlock(&lock_b);
pthread_mutex_unlock(&lock_a);

// Thread 2
pthread_mutex_lock(&lock_a);  // Same order!
pthread_mutex_lock(&lock_b);
// Work
pthread_mutex_unlock(&lock_b);
pthread_mutex_unlock(&lock_a);
```

**Benefits**: Simple, effective
**Challenge**: Must enforce across entire codebase

### 2. Lock Ordering with Multiple Locks

```c
void transfer(account_t *from, account_t *to, int amount) {
    // Always lock account with lower address first
    account_t *first = (from < to) ? from : to;
    account_t *second = (from < to) ? to : from;
    
    pthread_mutex_lock(&first->lock);
    pthread_mutex_lock(&second->lock);
    
    from->balance -= amount;
    to->balance += amount;
    
    pthread_mutex_unlock(&second->lock);
    pthread_mutex_unlock(&first->lock);
}
```

### 3. Try-Lock and Backoff (Avoid Hold and Wait)

**Solution**: Use non-blocking locks, release all if can't get all.

```c
pthread_mutex_lock(&lock_a);
if (pthread_mutex_trylock(&lock_b) != 0) {
    // Couldn't get lock_b, release lock_a and retry
    pthread_mutex_unlock(&lock_a);
    // Maybe sleep briefly
    usleep(rand() % 1000);
    goto retry;
}
// Got both locks
// Work
pthread_mutex_unlock(&lock_b);
pthread_mutex_unlock(&lock_a);
```

**Benefits**: Guarantees no deadlock
**Challenges**: More complex, potential livelock, performance overhead

### 4. Lock-Free Data Structures (Remove Mutual Exclusion)

**Solution**: Use atomic operations instead of locks.

```c
// Atomic increment, no locks needed
atomic_int counter;
atomic_fetch_add(&counter, 1);
```

**Benefits**: No deadlock possible
**Challenges**: Complex to implement, not always applicable

### 5. Coarse-Grained Locking (Reduce Number of Locks)

**Solution**: Use fewer, larger locks.

```c
// Instead of lock per account, one lock for all transfers
pthread_mutex_t global_transfer_lock;

void transfer(account_t *from, account_t *to, int amount) {
    pthread_mutex_lock(&global_transfer_lock);
    from->balance -= amount;
    to->balance += amount;
    pthread_mutex_unlock(&global_transfer_lock);
}
```

**Benefits**: Simple, no deadlock
**Challenges**: Reduced parallelism, contention

### 6. Timeouts (Detection and Recovery)

```c
struct timespec timeout;
clock_gettime(CLOCK_REALTIME, &timeout);
timeout.tv_sec += 5;  // 5-second timeout

pthread_mutex_lock(&lock_a);
int result = pthread_mutex_timedlock(&lock_b, &timeout);
if (result == ETIMEDOUT) {
    // Couldn't get lock_b in time
    pthread_mutex_unlock(&lock_a);
    // Handle error (retry, report, etc.)
}
```

## Detection

### Symptoms
- Program hangs
- No progress being made
- CPU usage drops to zero
- Threads in "waiting" state indefinitely

### Tools
```bash
# See what threads are doing
gdb -p <pid>
(gdb) info threads
(gdb) thread apply all bt  # Backtrace of all threads

# Check for lock ownership
pstack <pid>
```

### Runtime Detection
- Maintain resource allocation graph
- Periodically check for cycles
- Expensive in production

## Deadlock vs Other Issues

### Livelock
- Threads keep changing state but make no progress
- Example: Both threads try-lock, both fail, both retry, repeat
- **Not blocked** but **not progressing**

```c
// Both threads keep trying and backing off
while (1) {
    pthread_mutex_lock(&lock_a);
    if (pthread_mutex_trylock(&lock_b) != 0) {
        pthread_mutex_unlock(&lock_a);
        continue;  // Try again
    }
    break;
}
```

### Starvation
- Thread never gets required resources (but not deadlocked)
- Other threads keep getting priority
- Example: Low-priority thread never gets CPU time

## Real-World Examples

### Dining Philosophers Problem
Classic deadlock scenario:
- 5 philosophers sitting at round table
- 5 forks (one between each philosopher)
- Each needs 2 forks to eat
- If all grab left fork simultaneously → deadlock!

**Solution**: Number forks, always grab lower-numbered first.

### Database Transactions
```sql
-- Transaction 1
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Transaction 2
BEGIN;
UPDATE accounts SET balance = balance - 50 WHERE id = 2;
UPDATE accounts SET balance = balance + 50 WHERE id = 1;
COMMIT;
```
Could deadlock if locking rows 1 and 2 in different orders.

## Prevention Best Practices

### Design Guidelines
1. **Minimize lock holding time** - Get lock, do work quickly, release
2. **Minimize number of locks** - Fewer locks = less complexity
3. **Document lock ordering** - Make requirements clear
4. **Use lock hierarchy** - Enforce with assertions/tools
5. **Avoid nested locks** when possible

### Code Review Checklist
- [ ] Are multiple locks acquired?
- [ ] Is lock ordering consistent across all code?
- [ ] Can locks be avoided (read-only, atomic ops)?
- [ ] Is lock holding time minimized?
- [ ] Are all error paths unlocking properly?

## Debugging Deadlocks

### GDB Commands
```bash
# Attach to hung process
gdb -p <pid>

# Show all threads
info threads

# Switch to thread
thread <n>

# Show backtrace (where thread is stuck)
bt

# Show local variables
info locals
```

### DTrace/SystemTap
Can track lock acquisition patterns and detect cycles.

### Thread Sanitizer (TSan)
```bash
gcc -fsanitize=thread -g program.c
./a.out
```
Detects potential deadlocks at runtime.

## Related Concepts

- [[Mutex Locks]] - Primary synchronization primitive that can deadlock
- [[Semaphores]] - Can also deadlock with multiple semaphores
- [[Threads]] - What experiences deadlock
- [[Concurrency]] - Fundamental challenge in concurrent systems

## Summary Table

| Strategy | Breaks Condition | Pros | Cons |
|----------|------------------|------|------|
| Lock ordering | Circular wait | Simple, effective | Must enforce globally |
| Try-lock | Hold and wait | No deadlock | Livelock risk, complexity |
| Coarse locking | Circular wait | Simple | Reduced parallelism |
| Lock-free | Mutual exclusion | Fast, no deadlock | Complex, limited scope |
| Timeouts | Detection | Practical | Doesn't prevent |

---

*The silent killer of concurrent programs - when threads wait forever*