---
tags:
  - rust
  - methods
type: note
related:
  - '[[Rust]]'
  - '[[Structs]]'
  - '[[Derives]]'
  - '[[Borrowing]]'
---
# Implementation

Adding methods and associated functions to types with `impl` blocks.

## Overview

`impl` blocks define methods and associated functions for structs and enums. They separate data (the struct) from behavior (the impl).

## Basic Implementation

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    // Associated function (no self) - often a constructor
    pub fn new(width: u32, height: u32) -> Self {
        Self { width, height }
    }
    
    // Method with immutable borrow
    pub fn area(&self) -> u32 {
        self.width * self.height
    }
}

// Usage
let rect = Rectangle::new(10, 20);
println!("Area: {}", rect.area());
```

## Method Receivers

```rust
impl MyStruct {
    // Borrows immutably - for reading
    fn read(&self) { }
    
    // Borrows mutably - for modifying
    fn mutate(&mut self) { }
    
    // Takes ownership - consumes self
    fn consume(self) { }
    
    // No self - associated function (not a method)
    fn create() -> Self { }
}
```

### Choosing the Right Receiver

| Receiver | When to Use |
|----------|-------------|
| `&self` | Read-only access, most common |
| `&mut self` | Needs to modify fields |
| `self` | Transforms or consumes the value |
| (none) | Constructor or utility function |

## Associated Functions

Functions without `self` are called on the type, not an instance:

```rust
impl Rectangle {
    // Called as Rectangle::square(10)
    pub fn square(size: u32) -> Self {
        Self { width: size, height: size }
    }
    
    // Called as Rectangle::default_size()
    pub fn default_size() -> u32 {
        100
    }
}

let sq = Rectangle::square(10);
let default = Rectangle::default_size();
```

## Multiple impl Blocks

Split implementations for organization:

```rust
impl Rectangle {
    pub fn new(w: u32, h: u32) -> Self {
        Self { width: w, height: h }
    }
}

impl Rectangle {
    pub fn area(&self) -> u32 {
        self.width * self.height
    }
    
    pub fn perimeter(&self) -> u32 {
        2 * (self.width + self.height)
    }
}
```

## Implementing for Enums

```rust
enum Side { Bid, Ask }

impl Side {
    pub fn opposite(&self) -> Self {
        match self {
            Side::Bid => Side::Ask,
            Side::Ask => Side::Bid,
        }
    }
    
    pub fn is_bid(&self) -> bool {
        matches!(self, Side::Bid)
    }
}
```

## Method Chaining

Return `Self` or `&mut self` to enable chaining:

```rust
impl StringBuilder {
    pub fn new() -> Self {
        Self { buffer: String::new() }
    }
    
    pub fn append(mut self, s: &str) -> Self {
        self.buffer.push_str(s);
        self
    }
    
    pub fn build(self) -> String {
        self.buffer
    }
}

let result = StringBuilder::new()
    .append("Hello")
    .append(" World")
    .build();
```

## Implementing Traits

```rust
use std::fmt;

struct Point { x: i32, y: i32 }

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

println!("{}", Point { x: 1, y: 2 });  // (1, 2)
```

## Common Patterns

### Constructor Variations

```rust
impl Config {
    // Default constructor
    pub fn new() -> Self {
        Self::default()
    }
    
    // From specific values
    pub fn with_timeout(timeout: u64) -> Self {
        Self { timeout, ..Default::default() }
    }
    
    // Fallible constructor
    pub fn try_new(path: &str) -> Result<Self, Error> {
        // ...
    }
}
```

### Getter and Setter

```rust
impl User {
    pub fn name(&self) -> &str {
        &self.name
    }
    
    pub fn set_name(&mut self, name: String) {
        self.name = name;
    }
}
```

### Builder Pattern

```rust
impl ServerBuilder {
    pub fn new() -> Self { Self::default() }
    
    pub fn port(mut self, port: u16) -> Self {
        self.port = port;
        self
    }
    
    pub fn host(mut self, host: &str) -> Self {
        self.host = host.into();
        self
    }
    
    pub fn build(self) -> Server {
        Server { port: self.port, host: self.host }
    }
}
```

## Tips

- Use `Self` instead of repeating the type name
- Prefer `&self` unless you need mutation or ownership
- Use associated functions for constructors (`new`, `with_*`, `from_*`)
- Keep impl blocks close to the struct definition
- Split large impl blocks by functionality
- Consider the builder pattern for types with many optional fields

## See Also

- [[Structs]] — Defining types
- [[Derives]] — Auto-implementing traits
- [[Borrowing]] — Method receivers and borrowing
- [[Rust]]
