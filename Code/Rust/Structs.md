---
tags:
  - rust
  - types
type: note
related:
  - "[[Rust]]"
  - "[[Implementation]]"
  - "[[Derives]]"
  - "[[Pattern Matching]]"
---
# Structs

Custom data types with named fields in Rust.

## Overview

Structs group related data together. They're the foundation of Rust's type system and pair with `impl` blocks to add behavior.

## Basic Structs

```rust
struct Point {
    x: f64,
    y: f64,
}

let origin = Point { x: 0.0, y: 0.0 };
println!("x: {}", origin.x);
```

## Struct Update Syntax

Create a new struct from an existing one:

```rust
let p1 = Point { x: 1.0, y: 2.0 };
let p2 = Point { x: 3.0, ..p1 };  // y comes from p1
```

## Tuple Structs

Named tuples—fields accessed by index:

```rust
struct Color(u8, u8, u8);
struct Point3D(f64, f64, f64);

let red = Color(255, 0, 0);
println!("R: {}", red.0);
```

## Unit Structs

No fields—useful for traits:

```rust
struct Marker;
```

## Visibility

Fields are private by default:

```rust
pub struct User {
    pub name: String,      // Public
    email: String,         // Private to module
    pub(crate) id: u64,    // Public within crate
}
```

## Methods with `impl`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    // Associated function (no self) - constructor
    pub fn new(width: u32, height: u32) -> Self {
        Self { width, height }
    }
    
    // Method - immutable borrow
    pub fn area(&self) -> u32 {
        self.width * self.height
    }
    
    // Method - mutable borrow
    pub fn scale(&mut self, factor: u32) {
        self.width *= factor;
        self.height *= factor;
    }
    
    // Method - takes ownership
    pub fn into_square(self) -> Self {
        let side = self.width.max(self.height);
        Self { width: side, height: side }
    }
}

// Usage
let mut rect = Rectangle::new(10, 20);
println!("Area: {}", rect.area());
rect.scale(2);
let square = rect.into_square();
```

## Deriving Traits

```rust
#[derive(Debug, Clone, PartialEq)]
struct Order {
    id: u64,
    symbol: String,
    qty: i64,
}

let order = Order { id: 1, symbol: "AAPL".into(), qty: 100 };
println!("{:?}", order);  // Debug output
let copy = order.clone(); // Clone access
assert_eq!(order, copy);  // PartialEq comparison
```

## Common Patterns

### Builder Pattern

```rust
struct ServerConfig {
    host: String,
    port: u16,
    timeout: u64,
}

impl ServerConfig {
    pub fn new() -> Self {
        Self {
            host: "localhost".into(),
            port: 8080,
            timeout: 30,
        }
    }
    
    pub fn host(mut self, host: &str) -> Self {
        self.host = host.into();
        self
    }
    
    pub fn port(mut self, port: u16) -> Self {
        self.port = port;
        self
    }
}

let config = ServerConfig::new()
    .host("0.0.0.0")
    .port(3000);
```

### Newtype Pattern

Wrap a type to add meaning:

```rust
struct OrderId(u64);
struct UserId(u64);

// These are different types - can't mix them up!
fn get_order(id: OrderId) { }
fn get_user(id: UserId) { }
```

## Tips

- Use `Self` instead of repeating the struct name
- Prefer `&self` methods over `self` unless you need ownership
- Derive `Debug` on almost everything for easier debugging
- Use the newtype pattern to prevent mixing up IDs
- Private fields + public constructor = encapsulation

## See Also

- [[Implementation]] — Adding methods
- [[Derives]] — Auto-implementing traits
- [[Pattern Matching]] — Destructuring structs
- [[Rust]]
