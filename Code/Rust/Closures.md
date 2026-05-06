---
tags:
  - rust
  - closures
  - functional
type: note
related:
  - '[[Rust]]'
  - '[[Iterators]]'
  - '[[Traits]]'
  - '[[Generics]]'
---
# Closures

Anonymous functions that capture their environment.

## Overview

Closures are anonymous functions that can capture variables from their enclosing scope. They're more flexible than regular functions—they can be stored in variables, passed as arguments, and returned from functions.

## Basic Usage

### Closure Syntax

```rust
// Full syntax
let add = |a: i32, b: i32| -> i32 { a + b };

// Type inference (most common)
let add = |a, b| a + b;

// No parameters
let greet = || println!("Hello!");

// Multi-line with braces
let complex = |x| {
    let y = x * 2;
    y + 1
};

add(2, 3);   // 5
greet();     // "Hello!"
complex(5);  // 11
```

### Type Inference

Closures infer types from first use:

```rust
let identity = |x| x;

let s = identity("hello");  // x is now &str
// let n = identity(5);     // Error! Already inferred as &str
```

## Key Concepts

### Capturing Variables

Closures capture variables from their environment:

```rust
let x = 4;

let equal_to_x = |z| z == x;  // Captures x by reference

assert!(equal_to_x(4));
```

### Capture Modes

```rust
let s = String::from("hello");

// Borrow immutably (Fn)
let print = || println!("{}", s);
print();
println!("{}", s);  // s still usable

// Borrow mutably (FnMut)
let mut count = 0;
let mut increment = || count += 1;
increment();
increment();
println!("{}", count);  // 2

// Take ownership (FnOnce)
let consume = || drop(s);
consume();
// println!("{}", s);  // Error! s was moved
```

### The `move` Keyword

Force ownership transfer:

```rust
let s = String::from("hello");

// Without move: borrows s
let print = || println!("{}", s);

// With move: takes ownership of s
let print = move || println!("{}", s);
// s is no longer accessible here

// Essential for threads
let handle = std::thread::spawn(move || {
    println!("{}", s);  // s moved into thread
});
```

### Closure Traits

Closures implement one or more of these traits:

| Trait | Signature | Captures | Can Call |
|-------|-----------|----------|----------|
| `FnOnce` | `call_once(self)` | By value | Once |
| `FnMut` | `call_mut(&mut self)` | By mutable reference | Multiple times |
| `Fn` | `call(&self)` | By shared reference | Multiple times |

```rust
fn call_once<F: FnOnce()>(f: F) {
    f();  // Consumes f
}

fn call_mut<F: FnMut()>(mut f: F) {
    f();
    f();  // Can call multiple times
}

fn call_fn<F: Fn()>(f: F) {
    f();
    f();  // Can call multiple times
}
```

**Hierarchy**: `Fn` ⊂ `FnMut` ⊂ `FnOnce`

All closures implement `FnOnce`. If they don't move captured values, they also implement `FnMut`. If they don't mutate, they also implement `Fn`.

## Common Patterns

### Closures as Arguments

```rust
fn apply<F>(value: i32, f: F) -> i32
where
    F: Fn(i32) -> i32,
{
    f(value)
}

let double = |x| x * 2;
let result = apply(5, double);  // 10

// Inline closure
let result = apply(5, |x| x + 1);  // 6
```

### Returning Closures

```rust
// Must use impl Trait or Box<dyn>
fn make_adder(n: i32) -> impl Fn(i32) -> i32 {
    move |x| x + n
}

let add_5 = make_adder(5);
add_5(10);  // 15

// With Box for dynamic dispatch
fn make_adder_boxed(n: i32) -> Box<dyn Fn(i32) -> i32> {
    Box::new(move |x| x + n)
}
```

### Closures with Iterator Methods

```rust
let numbers = vec![1, 2, 3, 4, 5];

// map
let doubled: Vec<_> = numbers.iter().map(|x| x * 2).collect();

// filter
let evens: Vec<_> = numbers.iter().filter(|x| *x % 2 == 0).collect();

// fold
let sum = numbers.iter().fold(0, |acc, x| acc + x);

// for_each
numbers.iter().for_each(|x| println!("{}", x));
```

### Storing Closures in Structs

```rust
struct Cacher<F>
where
    F: Fn(u32) -> u32,
{
    calculation: F,
    value: Option<u32>,
}

impl<F> Cacher<F>
where
    F: Fn(u32) -> u32,
{
    fn new(calculation: F) -> Cacher<F> {
        Cacher {
            calculation,
            value: None,
        }
    }
    
    fn value(&mut self, arg: u32) -> u32 {
        match self.value {
            Some(v) => v,
            None => {
                let v = (self.calculation)(arg);
                self.value = Some(v);
                v
            }
        }
    }
}
```

### Closure vs Function Pointer

```rust
// Function pointer (no captures)
fn add_one(x: i32) -> i32 { x + 1 }
let f: fn(i32) -> i32 = add_one;

// Can use closure that doesn't capture
let f: fn(i32) -> i32 = |x| x + 1;

// But not if it captures
let n = 5;
// let f: fn(i32) -> i32 = |x| x + n;  // Error!
let f: Box<dyn Fn(i32) -> i32> = Box::new(|x| x + n);  // OK
```

## Tips

- Closures infer types from usage—be explicit if needed
- Use `move` when the closure needs to own its captures (especially for threads)
- Prefer `Fn` bounds unless you need mutation (`FnMut`) or consumption (`FnOnce`)
- Use `impl Fn()` in return types for simpler APIs
- Function pointers (`fn`) work where closures with no captures are expected
- Closures are zero-cost—they're monomorphized like generics

## See Also

- [[Iterators]] — Closures power iterator adapters
- [[Traits]] — Fn, FnMut, FnOnce traits
- [[Generics]] — Closures use generic bounds
- [[Rust]]
