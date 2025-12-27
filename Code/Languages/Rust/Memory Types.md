---
tags:
  - rust
  - memory
  - performance
type: note
related:
  - '[[Rust]]'
  - '[[Borrowing]]'
  - '[[Copying]]'
  - '[[Collections]]'
---
# Memory Types

Stack vs heap allocation in Rust.

## Overview

Rust gives you control over where data lives in memory. Understanding stack vs heap helps you write efficient code and understand ownership.

## Stack Allocation

Fast, automatic, fixed-size data:

```rust
let x: i32 = 42;        // 4 bytes on stack
let point: (f64, f64) = (1.0, 2.0);  // 16 bytes on stack
let arr: [u8; 4] = [1, 2, 3, 4];     // 4 bytes on stack
```

### Stack Characteristics

- **Fixed size** — size known at compile time
- **Fast allocation** — just move stack pointer
- **Automatic cleanup** — dropped when scope ends
- **LIFO** — last in, first out

### Stack Types

| Type | Size |
|------|------|
| `bool` | 1 byte |
| `i8`, `u8` | 1 byte |
| `i32`, `u32`, `f32` | 4 bytes |
| `i64`, `u64`, `f64` | 8 bytes |
| `i128`, `u128` | 16 bytes |
| `&T` | pointer size (8 bytes on 64-bit) |

## Heap Allocation

Dynamic, growable, owned data:

```rust
let s = String::from("hello");  // Data on heap, pointer on stack
let v = vec![1, 2, 3];          // Data on heap, metadata on stack
let b = Box::new(42);           // i32 on heap (unusual but possible)
```

### Heap Characteristics

- **Dynamic size** — can grow/shrink at runtime
- **Slower allocation** — requires allocator
- **Explicit ownership** — must be freed (Rust does this automatically)
- **Accessible from anywhere** — via pointer

### Common Heap Types

| Type | Stack | Heap |
|------|-------|------|
| `String` | ptr + len + capacity (24 bytes) | actual characters |
| `Vec<T>` | ptr + len + capacity (24 bytes) | elements |
| `Box<T>` | ptr (8 bytes) | T |
| `HashMap<K,V>` | metadata | buckets + entries |

## Enums

Enums are sized to fit their largest variant:

```rust
enum Side { Bid, Ask }  // 1 byte (like a small integer)

enum Value {
    Int(i64),           // 8 bytes
    Text(String),       // 24 bytes (pointer + metadata)
}
// Value is 24 bytes + discriminant
```

## Structs

Structs contain their fields inline:

```rust
struct Order {
    id: u64,           // 8 bytes, stack
    side: Side,        // 1 byte, stack
    symbol: String,    // 24 bytes stack (ptr to heap data)
    qty: i64,          // 8 bytes, stack
}
// Order is ~41 bytes on stack, String data on heap
```

## Smart Pointers

| Type | Use Case |
|------|----------|
| `Box<T>` | Single owner, heap allocation |
| `Rc<T>` | Multiple owners, single-threaded |
| `Arc<T>` | Multiple owners, thread-safe |
| `Cow<'a, T>` | Clone on write |

```rust
use std::sync::Arc;

let shared: Arc<str> = Arc::from("hello");
let clone = Arc::clone(&shared);  // Cheap: just increments counter
```

## Tips

- Prefer stack allocation for small, fixed-size data
- `String` and `Vec` handle heap allocation for you
- Use `&str` instead of `String` in function parameters
- Consider `Arc<str>` for frequently cloned strings
- Profile before optimizing—Rust's allocator is fast

## See Also

- [[Borrowing]] — References to memory
- [[Copying]] — Copy vs Clone
- [[Collections]] — Heap-allocated containers
- [[Rust]]
