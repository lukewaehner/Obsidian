---
tags:
  - rust
  - systems-programming
type: moc
---
# Rust

A systems programming language focused on safety, speed, and concurrency.

## Core Concepts

### Ownership & Memory
- [[Borrowing]] — References and the borrow checker
- [[Copying]] — Copy vs Clone traits
- [[Memory Types]] — Stack vs heap allocation
- [[Lifetimes]] — Reference validity annotations
- [[Smart Pointers]] — Box, Rc, Arc, RefCell

### Type System
- [[Structs]] — Custom data types with named fields
- [[Enums]] — Algebraic data types and variants
- [[Traits]] — Shared behavior and interfaces
- [[Generics]] — Parameterized types
- [[Derives]] — Auto-implementing traits

### Control Flow
- [[Pattern Matching]] — Match expressions and destructuring
- [[Result & Option]] — Error handling basics
- [[Error Handling Patterns]] — Advanced error techniques
- [[Closures]] — Anonymous functions

### Code Organization
- [[Modules]] — Code organization and visibility
- [[Implementation]] — Methods and associated functions

### Collections & Data
- [[Collections]] — Vec, HashMap, BTreeMap, etc.
- [[Slices]] — Arrays, slices, unzip, partition, drain
- [[Strings]] — String vs &str, UTF-8 handling
- [[Iterators]] — Lazy sequence processing
- [[Destructuring]] — Unpacking tuples, arrays, structs, enums

### Concurrency
- [[Concurrency]] — Threads and synchronization
- [[Async Await]] — Asynchronous programming
- [[Send and Sync]] — Thread-safety marker traits
- [[Pin and Unpin]] — Pinning values in memory for async

### Development
- [[Testing]] — Unit tests and assertions
- [[Logging]] — Debug output and tracing
- [[Cargo]] — Package manager and build system
- [[Macros]] — Metaprogramming
- [[Unsafe]] — Bypassing safety guarantees
- [[Common Crates]] — Essential ecosystem libraries

## Learning

- [[Learning Plan]] — Structured exercises with expected inputs and outputs

## Projects

- [[HFTX]] — High-frequency trading exchange

## Quick Reference

```rust
// Variables
let x = 5;           // Immutable
let mut y = 10;      // Mutable

// Functions
fn add(a: i32, b: i32) -> i32 {
    a + b  // Implicit return
}

// Structs and impl
struct Point { x: i32, y: i32 }
impl Point {
    fn new(x: i32, y: i32) -> Self { Self { x, y } }
}

// Enums and match
enum Option<T> { Some(T), None }
match value {
    Some(x) => println!("{}", x),
    None => println!("nothing"),
}

// Error handling
let result: Result<i32, Error> = Ok(42);
let value = result?;

// Traits
trait Greet { fn greet(&self); }
impl Greet for Point { fn greet(&self) { /*...*/ } }

// Generics
fn print<T: Display>(item: T) { println!("{}", item); }

// Closures
let add = |a, b| a + b;
vec.iter().map(|x| x * 2).collect()
```

## Resources

- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [std library docs](https://doc.rust-lang.org/std/)
- [crates.io](https://crates.io/)

## See Also

- [[Languages]] — Other programming languages
- [[Code]] — Main programming hub
