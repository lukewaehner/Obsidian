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
- [[Cargo]] — Dependency management and Cargo.toml
- [[Projects]] — rustup, toolchains, compilation, cross-compilation, tooling
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

```folder-overview
id: 7ac8dba3-81a6-4bd1-be1b-78b8f2164b89
folderPath: Code/Rust
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="7ac8dba3-81a6-4bd1-be1b-78b8f2164b89"></span>
- [[Code/Rust/Async Await.md|Async Await]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Borrowing.md|Borrowing]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Cargo.md|Cargo]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Closures.md|Closures]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Collections.md|Collections]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Common Crates.md|Common Crates]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Concurrency.md|Concurrency]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Copying.md|Copying]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Derives.md|Derives]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Destructuring.md|Destructuring]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Enums.md|Enums]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Error Handling Patterns.md|Error Handling Patterns]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Generics.md|Generics]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Implementation.md|Implementation]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Iterators.md|Iterators]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Learning Plan.md|Learning Plan]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Lifetimes.md|Lifetimes]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Logging.md|Logging]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Macros.md|Macros]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Memory Types.md|Memory Types]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Modules.md|Modules]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Pattern Matching.md|Pattern Matching]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Pin and Unpin.md|Pin and Unpin]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Projects.md|Projects]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Result & Option.md|Result & Option]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Send and Sync.md|Send and Sync]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Slices.md|Slices]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Smart Pointers.md|Smart Pointers]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Strings.md|Strings]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Structs.md|Structs]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Testing.md|Testing]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Traits.md|Traits]] <span class="fv-link-list-item"></span>
- [[Code/Rust/Unsafe.md|Unsafe]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="7ac8dba3-81a6-4bd1-be1b-78b8f2164b89"></span>
