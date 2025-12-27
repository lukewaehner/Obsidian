---
tags:
  - rust
  - traits
  - polymorphism
type: note
related:
  - '[[Rust]]'
  - '[[Generics]]'
  - '[[Derives]]'
  - '[[Enums]]'
---
# Traits

Shared behavior through interfaces and polymorphism in Rust.

## Overview

Traits define shared functionality that types can implement. They're similar to interfaces in other languages but more powerful—supporting default implementations, associated types, and trait bounds for generics.

## Basic Usage

### Defining a Trait

```rust
trait Greet {
    fn greet(&self) -> String;
}
```

### Implementing a Trait

```rust
struct Person {
    name: String,
}

impl Greet for Person {
    fn greet(&self) -> String {
        format!("Hello, I'm {}!", self.name)
    }
}

let person = Person { name: "Alice".into() };
println!("{}", person.greet());  // "Hello, I'm Alice!"
```

### Default Implementations

```rust
trait Greet {
    fn greet(&self) -> String {
        String::from("Hello!")  // Default
    }
    
    fn greet_loudly(&self) -> String {
        format!("{}!!!", self.greet().to_uppercase())
    }
}

struct Robot;
impl Greet for Robot {}  // Uses defaults

Robot.greet()        // "Hello!"
Robot.greet_loudly() // "HELLO!!!!"
```

## Key Concepts

### Trait Bounds

Restrict generics to types implementing certain traits:

```rust
// Function syntax
fn print_greeting<T: Greet>(item: T) {
    println!("{}", item.greet());
}

// Where clause (cleaner for multiple bounds)
fn process<T, U>(t: T, u: U)
where
    T: Greet + Clone,
    U: Debug + Send,
{
    // ...
}

// impl Trait (simpler syntax)
fn make_greeter() -> impl Greet {
    Person { name: "Bob".into() }
}
```

### Multiple Traits

```rust
trait Speak {
    fn speak(&self) -> String;
}

trait Walk {
    fn walk(&self) -> String;
}

// Implement multiple traits
impl Speak for Person {
    fn speak(&self) -> String { "Hello!".into() }
}

impl Walk for Person {
    fn walk(&self) -> String { "Walking...".into() }
}

// Require multiple traits
fn perform<T: Speak + Walk>(actor: &T) {
    println!("{}", actor.speak());
    println!("{}", actor.walk());
}
```

### Associated Types

```rust
trait Iterator {
    type Item;  // Associated type
    
    fn next(&mut self) -> Option<Self::Item>;
}

struct Counter {
    count: u32,
}

impl Iterator for Counter {
    type Item = u32;  // Specify the type
    
    fn next(&mut self) -> Option<Self::Item> {
        self.count += 1;
        Some(self.count)
    }
}
```

### Supertraits

Require another trait as a prerequisite:

```rust
trait Animal {
    fn name(&self) -> &str;
}

trait Pet: Animal {  // Pet requires Animal
    fn cuddle(&self) {
        println!("{} is being cuddled!", self.name());
    }
}
```

### Trait Objects (Dynamic Dispatch)

```rust
// dyn Trait for runtime polymorphism
fn greet_all(greeters: Vec<Box<dyn Greet>>) {
    for g in greeters {
        println!("{}", g.greet());
    }
}

// Or with references
fn greet_any(greeter: &dyn Greet) {
    println!("{}", greeter.greet());
}
```

## Common Standard Library Traits

### Display and Debug

```rust
use std::fmt;

struct Point { x: i32, y: i32 }

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

impl fmt::Debug for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Point {{ x: {}, y: {} }}", self.x, self.y)
    }
}

println!("{}", point);   // Display
println!("{:?}", point); // Debug
```

### From and Into

```rust
struct Meters(f64);

impl From<f64> for Meters {
    fn from(value: f64) -> Self {
        Meters(value)
    }
}

let m: Meters = 5.0.into();  // Into is auto-implemented
let m = Meters::from(5.0);
```

### Default

```rust
#[derive(Default)]
struct Config {
    timeout: u32,    // defaults to 0
    retries: u32,    // defaults to 0
    enabled: bool,   // defaults to false
}

let config = Config::default();
let custom = Config { timeout: 30, ..Default::default() };
```

### Clone and Copy

```rust
#[derive(Clone)]        // Explicit .clone()
struct Buffer { data: Vec<u8> }

#[derive(Clone, Copy)]  // Implicit copy on assignment
struct Point { x: i32, y: i32 }
```

### PartialEq, Eq, PartialOrd, Ord

```rust
#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Version {
    major: u32,
    minor: u32,
}

let v1 = Version { major: 1, minor: 0 };
let v2 = Version { major: 2, minor: 0 };
assert!(v1 < v2);
```

### Hash

```rust
use std::collections::HashMap;

#[derive(Hash, PartialEq, Eq)]
struct UserId(u64);

let mut users: HashMap<UserId, String> = HashMap::new();
users.insert(UserId(1), "Alice".into());
```

## Common Patterns

### Extension Traits

Add methods to existing types:

```rust
trait StringExt {
    fn is_blank(&self) -> bool;
}

impl StringExt for str {
    fn is_blank(&self) -> bool {
        self.trim().is_empty()
    }
}

"  ".is_blank()  // true
```

### Blanket Implementations

Implement for all types matching a bound:

```rust
trait Printable {
    fn print(&self);
}

// Implement for ALL types that implement Display
impl<T: std::fmt::Display> Printable for T {
    fn print(&self) {
        println!("{}", self);
    }
}

42.print();      // Works for i32
"hello".print(); // Works for &str
```

### Newtype Pattern for Orphan Rule

```rust
// Can't impl Display for Vec<T> (orphan rule)
// Wrap it in a newtype
struct Wrapper(Vec<String>);

impl std::fmt::Display for Wrapper {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}
```

## Tips

- Use trait bounds to write generic, reusable code
- Prefer `impl Trait` in return position for simpler APIs
- Use `dyn Trait` when you need runtime polymorphism
- Derive common traits (`Debug`, `Clone`, `PartialEq`) liberally
- The orphan rule: you can only implement a trait if you own the trait OR the type
- Associated types are better than generics when there's only one implementation per type

## See Also

- [[Generics]] — Using traits with generic types
- [[Derives]] — Auto-deriving common traits
- [[Enums]] — Implementing traits for enums
- [[Rust]]
