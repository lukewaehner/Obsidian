---
tags:
  - rust
  - generics
  - types
type: note
related:
  - '[[Rust]]'
  - '[[Traits]]'
  - '[[Lifetimes]]'
  - '[[Closures]]'
---
# Generics

Writing code that works with multiple types through type parameters.

## Overview

Generics allow you to write flexible, reusable code that works with any type. Combined with trait bounds, they provide powerful abstraction without runtime cost—Rust monomorphizes generics at compile time.

## Basic Usage

### Generic Functions

```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}

largest(&[1, 5, 3]);       // Works with i32
largest(&[1.0, 5.0, 3.0]); // Works with f64
```

### Generic Structs

```rust
struct Point<T> {
    x: T,
    y: T,
}

let int_point = Point { x: 5, y: 10 };
let float_point = Point { x: 1.0, y: 4.0 };
```

### Multiple Type Parameters

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

let mixed = Point { x: 5, y: 4.0 };  // i32 and f64
```

### Generic Enums

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}

enum Option<T> {
    Some(T),
    None,
}
```

### Generic Methods

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
    
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

// Implement only for specific types
impl Point<f64> {
    fn distance_from_origin(&self) -> f64 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

## Key Concepts

### Trait Bounds

Constrain generics to types implementing specific traits:

```rust
// Basic bound
fn print<T: std::fmt::Display>(value: T) {
    println!("{}", value);
}

// Multiple bounds with +
fn compare<T: PartialOrd + Display>(a: T, b: T) {
    if a > b {
        println!("{} > {}", a, b);
    }
}

// Where clause (cleaner for complex bounds)
fn process<T, U>(t: T, u: U) -> String
where
    T: Display + Clone,
    U: Debug + Default,
{
    format!("{}: {:?}", t, u)
}
```

### Default Type Parameters

```rust
struct Container<T = i32> {
    value: T,
}

let c1 = Container { value: 42 };      // T = i32 (default)
let c2: Container<String> = Container { value: "hi".into() };
```

### Const Generics

```rust
fn print_array<T: Debug, const N: usize>(arr: [T; N]) {
    println!("{:?}", arr);
}

print_array([1, 2, 3]);      // N = 3
print_array([1, 2, 3, 4]);   // N = 4

struct Buffer<const SIZE: usize> {
    data: [u8; SIZE],
}
```

### impl Trait

Simplified syntax for trait bounds:

```rust
// In argument position (same as <T: Iterator>)
fn process(iter: impl Iterator<Item = i32>) {
    for i in iter {
        println!("{}", i);
    }
}

// In return position (hides concrete type)
fn make_iter() -> impl Iterator<Item = i32> {
    (0..10).filter(|x| x % 2 == 0)
}
```

### Turbofish Syntax

Explicitly specify type parameters:

```rust
let numbers = "1,2,3,4,5";
let parsed: Vec<i32> = numbers
    .split(',')
    .map(|s| s.parse::<i32>().unwrap())  // Turbofish ::<i32>
    .collect();

// Or on collect
let parsed = numbers
    .split(',')
    .map(|s| s.parse().unwrap())
    .collect::<Vec<i32>>();  // Turbofish on collect
```

## Common Patterns

### Generic Constructors

```rust
impl<T> Vec<T> {
    pub fn new() -> Self {
        // ...
    }
    
    pub fn with_capacity(capacity: usize) -> Self {
        // ...
    }
}
```

### Conditional Implementation

```rust
struct Pair<T> {
    x: T,
    y: T,
}

// Available for all T
impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

// Only available when T implements Display + PartialOrd
impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("Largest: {}", self.x);
        } else {
            println!("Largest: {}", self.y);
        }
    }
}
```

### Phantom Type Parameters

Mark types without storing them:

```rust
use std::marker::PhantomData;

struct Meters;
struct Feet;

struct Distance<Unit> {
    value: f64,
    _unit: PhantomData<Unit>,
}

impl<Unit> Distance<Unit> {
    fn new(value: f64) -> Self {
        Distance { value, _unit: PhantomData }
    }
}

let d1: Distance<Meters> = Distance::new(100.0);
let d2: Distance<Feet> = Distance::new(328.0);
// d1 and d2 are different types - can't be mixed accidentally
```

### Generic Closures

```rust
fn apply<F, T, R>(f: F, value: T) -> R
where
    F: FnOnce(T) -> R,
{
    f(value)
}

let result = apply(|x| x * 2, 5);  // 10
```

## Monomorphization

Rust generates specialized code for each concrete type used:

```rust
fn add<T: std::ops::Add<Output = T>>(a: T, b: T) -> T {
    a + b
}

add(1, 2);     // Compiler generates add_i32
add(1.0, 2.0); // Compiler generates add_f64
```

**Benefits**: Zero runtime cost, same as hand-written specialized code
**Tradeoff**: Larger binary size, longer compile times

## Tips

- Use trait bounds to specify what capabilities a generic type needs
- Prefer `impl Trait` for simpler function signatures
- Use `where` clauses when bounds get complex
- Const generics are great for array sizes and compile-time values
- Turbofish (`::<Type>`) helps when type inference fails
- Remember: generics are resolved at compile time, not runtime

## See Also

- [[Traits]] — Defining behavior for generics
- [[Lifetimes]] — Generic lifetime parameters
- [[Code/Languages/Rust/Closures|Closures]] — Generic function types
- [[Rust]]
