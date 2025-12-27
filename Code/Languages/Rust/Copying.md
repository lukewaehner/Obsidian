---
tags:
  - rust
  - ownership
  - traits
type: note
related:
  - '[[Rust]]'
  - '[[Borrowing]]'
  - '[[Memory Types]]'
  - '[[Derives]]'
---
# Copying

Understanding Copy vs Clone traits for duplicating values in Rust.

## Overview

Rust has two ways to duplicate values: implicit `Copy` (bitwise copy) and explicit `Clone` (deep copy). Understanding when each applies is key to working with ownership.

## Copy Trait

Types that implement `Copy` are duplicated implicitly on assignment or passing:

```rust
let x = 5;
let y = x;  // x is copied, not moved
println!("{} {}", x, y);  // Both valid
```

### Copy Types

- Integers: `i8`, `i16`, `i32`, `i64`, `i128`, `u8`, `u16`, `u32`, `u64`, `u128`
- Floats: `f32`, `f64`
- `bool`, `char`
- Tuples of Copy types: `(i32, i32)`
- Arrays of Copy types: `[i32; 3]`
- References: `&T` (but not `&mut T`)

### Non-Copy Types

- `String` — owns heap memory
- `Vec<T>` — owns heap memory
- Any type with heap allocation
- Types containing non-Copy fields

## Clone Trait

Explicit duplication with `.clone()`:

```rust
let s1 = String::from("hello");
let s2 = s1.clone();  // Deep copy
println!("{} {}", s1, s2);  // Both valid
```

### Why String Isn't Copy

```rust
let s1 = String::from("hello");
let s2 = s1;  // s1 MOVED to s2
// println!("{}", s1);  // ERROR: s1 no longer valid
```

If `String` were `Copy`, both would point to the same heap memory, causing double-free on drop.

## Deriving Copy and Clone

```rust
#[derive(Copy, Clone)]
struct Point {
    x: i32,
    y: i32,
}

// Only Clone (has String field)
#[derive(Clone)]
struct Person {
    name: String,
    age: u32,
}
```

> **Rule**: `Copy` requires all fields to also be `Copy`. If any field is heap-allocated, you can only derive `Clone`.

## When to Clone

Clone explicitly when you need a separate owned copy:

```rust
// Pushing owned data into a collection
let name = String::from("Alice");
let mut names = Vec::new();
names.push(name.clone());  // Clone if you need name later
names.push(name);          // Or move if you don't

// Returning owned data from a borrow
fn get_copy(s: &String) -> String {
    s.clone()
}
```

## Performance Considerations

| Operation | Cost |
|-----------|------|
| Copy | Cheap bitwise copy (stack only) |
| Clone | Can be expensive (heap allocation) |
| Borrow | Free (just a pointer) |

```rust
// Prefer borrowing over cloning
fn process(data: &String) { }  // Good: borrows
fn process(data: String) { }   // Takes ownership
fn process(data: String) {     // Bad if caller clones just to call this
    // ...
}
```

## Tips

- Prefer borrowing (`&T`) over cloning when possible
- Small, stack-only types should derive `Copy`
- Clone at ownership boundaries, not everywhere
- Consider `Arc<T>` or `Rc<T>` for shared ownership instead of cloning
- Use `Cow<'a, str>` for "clone on write" semantics

## See Also

- [[Borrowing]] — References and borrowing
- [[Derives]] — Deriving traits
- [[Memory Types]] — Stack vs heap
- [[Rust]]
