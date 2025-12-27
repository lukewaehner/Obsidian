---
tags:
  - rust
  - concurrency
  - threads
type: note
related:
  - '[[Rust]]'
  - '[[Smart Pointers]]'
  - '[[Closures]]'
  - '[[Async Await]]'
---
# Concurrency

Threads, synchronization, and fearless concurrency in Rust.

## Overview

Rust's ownership system prevents data races at compile time, enabling "fearless concurrency." The `Send` and `Sync` traits ensure thread safety is checked by the compiler.

## Basic Usage

### Spawning Threads

```rust
use std::thread;
use std::time::Duration;

// Spawn a thread
let handle = thread::spawn(|| {
    for i in 1..10 {
        println!("Spawned thread: {}", i);
        thread::sleep(Duration::from_millis(1));
    }
});

// Main thread continues
for i in 1..5 {
    println!("Main thread: {}", i);
    thread::sleep(Duration::from_millis(1));
}

// Wait for spawned thread to finish
handle.join().unwrap();
```

### Moving Data into Threads

```rust
use std::thread;

let v = vec![1, 2, 3];

// move keyword transfers ownership
let handle = thread::spawn(move || {
    println!("Vector: {:?}", v);
});

// v is no longer accessible here
handle.join().unwrap();
```

## Key Concepts

### Send and Sync Traits

```rust
// Send: safe to transfer between threads
// Most types are Send

// Sync: safe to reference from multiple threads
// T is Sync if &T is Send

// NOT Send: Rc<T>, raw pointers
// NOT Sync: RefCell<T>, Cell<T>

// Arc<T> is both Send and Sync (if T is)
use std::sync::Arc;
```

### Mutex - Mutual Exclusion

```rust
use std::sync::Mutex;

let m = Mutex::new(5);

{
    let mut num = m.lock().unwrap();
    *num = 6;
}  // Lock released here

println!("Value: {:?}", m);
```

### Sharing Across Threads with Arc<Mutex<T>>

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..10 {
    let counter = Arc::clone(&counter);
    let handle = thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    });
    handles.push(handle);
}

for handle in handles {
    handle.join().unwrap();
}

println!("Result: {}", *counter.lock().unwrap());  // 10
```

### RwLock - Read-Write Lock

```rust
use std::sync::RwLock;

let lock = RwLock::new(5);

// Multiple readers allowed
{
    let r1 = lock.read().unwrap();
    let r2 = lock.read().unwrap();
    println!("{} {}", r1, r2);
}

// Only one writer
{
    let mut w = lock.write().unwrap();
    *w += 1;
}
```

### Channels - Message Passing

```rust
use std::sync::mpsc;  // Multiple Producer, Single Consumer
use std::thread;

// Create channel
let (tx, rx) = mpsc::channel();

// Spawn sender
thread::spawn(move || {
    tx.send("hello").unwrap();
    tx.send("world").unwrap();
});

// Receive messages
for received in rx {
    println!("Got: {}", received);
}
```

### Multiple Producers

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();

for i in 0..3 {
    let tx = tx.clone();
    thread::spawn(move || {
        tx.send(i).unwrap();
    });
}

drop(tx);  // Drop original sender

for received in rx {
    println!("Got: {}", received);
}
```

## Common Patterns

### Thread Pool (with rayon)

```rust
use rayon::prelude::*;

let numbers: Vec<i32> = (0..1000).collect();

// Parallel iteration
let sum: i32 = numbers.par_iter().sum();

// Parallel map
let doubled: Vec<i32> = numbers.par_iter().map(|x| x * 2).collect();
```

### Scoped Threads

```rust
use std::thread;

let mut data = vec![1, 2, 3];

thread::scope(|s| {
    s.spawn(|| {
        println!("Thread 1: {:?}", data);
    });
    
    s.spawn(|| {
        println!("Thread 2: {:?}", data);
    });
});  // Threads guaranteed to finish here

// data is accessible again
data.push(4);
```

### Atomic Types

```rust
use std::sync::atomic::{AtomicUsize, Ordering};

let counter = AtomicUsize::new(0);

// No lock needed
counter.fetch_add(1, Ordering::SeqCst);
counter.fetch_sub(1, Ordering::SeqCst);

let value = counter.load(Ordering::SeqCst);
counter.store(42, Ordering::SeqCst);
```

### Condition Variables

```rust
use std::sync::{Arc, Mutex, Condvar};
use std::thread;

let pair = Arc::new((Mutex::new(false), Condvar::new()));
let pair2 = Arc::clone(&pair);

thread::spawn(move || {
    let (lock, cvar) = &*pair2;
    let mut started = lock.lock().unwrap();
    *started = true;
    cvar.notify_one();  // Wake waiting thread
});

let (lock, cvar) = &*pair;
let mut started = lock.lock().unwrap();
while !*started {
    started = cvar.wait(started).unwrap();  // Wait for notification
}
```

### Once - One-Time Initialization

```rust
use std::sync::Once;

static INIT: Once = Once::new();
static mut CONFIG: Option<Config> = None;

fn get_config() -> &'static Config {
    unsafe {
        INIT.call_once(|| {
            CONFIG = Some(load_config());
        });
        CONFIG.as_ref().unwrap()
    }
}

// Better: use once_cell or lazy_static
use once_cell::sync::Lazy;
static CONFIG: Lazy<Config> = Lazy::new(|| load_config());
```

### Deadlock Prevention

```rust
// Always acquire locks in the same order
let a = Mutex::new(1);
let b = Mutex::new(2);

// Thread 1: lock a, then b
// Thread 2: lock a, then b (same order!)

// Use try_lock to avoid blocking
if let Ok(guard) = mutex.try_lock() {
    // Got the lock
} else {
    // Lock is held by someone else
}
```

## Synchronization Primitives Summary

| Type | Purpose | When to Use |
|------|---------|-------------|
| `Mutex<T>` | Mutual exclusion | Single writer at a time |
| `RwLock<T>` | Read-write lock | Many readers, few writers |
| `Arc<T>` | Shared ownership | Share data across threads |
| `Atomic*` | Lock-free primitives | Simple counters/flags |
| `mpsc::channel` | Message passing | Thread communication |
| `Condvar` | Condition variable | Wait for condition |
| `Barrier` | Synchronization point | Wait for all threads |
| `Once` | One-time init | Global initialization |

## Tips

- Use `Arc<Mutex<T>>` for shared mutable state
- Prefer message passing (`mpsc`) over shared state when possible
- Use `RwLock` when reads vastly outnumber writes
- Use atomics for simple counters and flags
- Consider `rayon` for parallel iterators
- Scoped threads avoid the need for `Arc` when possible
- Always acquire locks in a consistent order to prevent deadlocks
- The compiler catches data races—trust the error messages!

## See Also

- [[Smart Pointers]] — Arc, Mutex, RwLock
- [[Closures]] — move closures for threads
- [[Async Await]] — Asynchronous programming
- [[Rust]]
