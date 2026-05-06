---
tags:
  - rust
  - concurrency
  - traits
type: note
related:
  - "[[Rust]]"
  - "[[Concurrency]]"
  - "[[Smart Pointers]]"
  - "[[Async Await]]"
---
# Send and Sync

Marker traits that tell the compiler which types are safe to use across threads.

## What They Mean

```rust
// Send: ownership of T can be transferred to another thread
// Sync: T can be shared by reference across threads (&T is Send)
```

In practice:
- A type is **`Send`** if moving it to another thread is safe
- A type is **`Sync`** if sharing a reference to it across threads is safe
- If `T: Sync`, then `&T: Send`

These are **marker traits** — no methods, just a compile-time assertion. The compiler auto-derives them for most types.

## Why They Exist

Rust can't know at runtime whether you're sharing data unsafely across threads. `Send` and `Sync` encode thread-safety in the type system so violations are caught at compile time, not at 3am in production.

## What Is and Isn't Send/Sync

| Type | Send | Sync | Why |
|------|------|------|-----|
| `i32`, `String`, `Vec<T>` | Yes | Yes | No shared mutable state |
| `Arc<T>` | Yes (if `T: Send + Sync`) | Yes | Atomic reference counting |
| `Rc<T>` | **No** | **No** | Reference count is not atomic |
| `Mutex<T>` | Yes (if `T: Send`) | Yes | Lock enforces exclusive access |
| `RefCell<T>` | Yes (if `T: Send`) | **No** | Borrow checking is not thread-safe |
| `Cell<T>` | Yes (if `T: Send`) | **No** | Interior mutability without locking |
| `*mut T` (raw pointer) | **No** | **No** | No safety guarantees |
| `MutexGuard<T>` | **No** | Yes | Must be unlocked on same thread |

### The core rule

If all fields of a struct are `Send`, the struct is `Send`. Same for `Sync`. The compiler derives this automatically — you only think about it when something breaks.

## Common Error Messages

### Error: `Rc<T>` across a thread boundary

```rust
use std::rc::Rc;
use std::thread;

let rc = Rc::new(5);
thread::spawn(move || {        // ERROR
    println!("{}", rc);
});
// `Rc<i32>` cannot be sent between threads safely
// the trait `Send` is not implemented for `Rc<i32>`
```

Fix: use `Arc` instead of `Rc`.

### Error: `tokio::spawn` requires `Send`

```rust
use std::rc::Rc;

async fn bad() {
    let rc = Rc::new(5);
    tokio::spawn(async move {  // ERROR
        println!("{}", rc);
    });
}
// future cannot be sent between threads safely
// within `impl Future`, the trait `Send` is not implemented for `Rc<i32>`
```

Fix: use `Arc`, or use `tokio::task::spawn_local` for single-threaded runtimes.

### Error: holding a `MutexGuard` across `.await`

```rust
use std::sync::Mutex;

async fn bad() {
    let m = Mutex::new(0);
    let guard = m.lock().unwrap();
    some_async_fn().await;    // ERROR — guard held across await point
    println!("{}", *guard);
}
// future cannot be sent between threads safely
// `MutexGuard<i32>` cannot be sent between threads safely
```

Fix: drop the guard before awaiting, or use `tokio::sync::Mutex`.

```rust
async fn good() {
    let m = std::sync::Mutex::new(0);
    {
        let mut guard = m.lock().unwrap();
        *guard += 1;
    }  // guard dropped here
    some_async_fn().await;   // now fine
}
```

## Send + 'static in tokio::spawn

`tokio::spawn` requires both bounds:

```rust
pub fn spawn<F>(future: F) -> JoinHandle<F::Output>
where
    F: Future + Send + 'static,
```

- **`Send`**: the future can be moved between threads in the Tokio thread pool
- **`'static`**: the future owns all its data — no borrowed references that could dangle

This means you can't borrow local variables across a `spawn`:

```rust
async fn bad() {
    let data = vec![1, 2, 3];
    tokio::spawn(async {
        println!("{:?}", data);  // ERROR: borrows `data`
    });
}

async fn good() {
    let data = vec![1, 2, 3];
    tokio::spawn(async move {   // move transfers ownership
        println!("{:?}", data);
    });
}
```

## Implementing Manually

You can implement `Send` or `Sync` manually with `unsafe`, but you're asserting to the compiler that you know it's safe:

```rust
struct MyType {
    ptr: *mut i32,  // raw pointers aren't Send
}

// You are asserting: "I guarantee this is safe to send between threads"
unsafe impl Send for MyType {}
unsafe impl Sync for MyType {}
```

Only do this in wrapper types where you've verified the invariants yourself (e.g., `Arc` does this internally).

## Quick Reference

| I want to... | Use |
|---|---|
| Share data across threads (read-only) | `Arc<T>` |
| Share mutable data across threads | `Arc<Mutex<T>>` |
| Share data in single-threaded async | `Rc<T>` or `Rc<RefCell<T>>` |
| Spawn a task that uses borrowed data | use `thread::scope` or clone/`Arc` |
| Spawn async task that captures data | `move` the data into the async block |

## See Also

- [[Concurrency]] — Threads, Mutex, channels
- [[Smart Pointers]] — Arc, Rc, RefCell
- [[Async Await]] — spawn and async task requirements
- [[Lifetimes]] — The 'static bound
- [[Rust]]
