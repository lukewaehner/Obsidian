---
tags:
  - rust
  - lifetimes
  - ownership
type: note
related:
  - '[[Rust]]'
  - '[[Borrowing]]'
  - '[[Generics]]'
  - '[[Structs]]'
---
# Lifetimes

Ensuring references remain valid through explicit lifetime annotations.

## Overview

Lifetimes are Rust's way of ensuring references don't outlive the data they point to. Most of the time, lifetimes are inferred, but sometimes you need to annotate them explicitly to help the compiler understand relationships between references.

## Basic Usage

### Lifetime Annotations

```rust
// 'a is a lifetime parameter
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

This says: "the returned reference will live as long as the shorter of the two input lifetimes."

### Why Lifetimes Matter

```rust
// This won't compile - dangling reference
fn dangling() -> &str {
    let s = String::from("hello");
    &s  // s is dropped here, reference would be invalid
}

// This is fine - string literal has 'static lifetime
fn static_str() -> &'static str {
    "hello"
}
```

## Key Concepts

### Lifetime Elision Rules

The compiler infers lifetimes in common cases:

```rust
// You write:
fn first_word(s: &str) -> &str { ... }

// Compiler sees:
fn first_word<'a>(s: &'a str) -> &'a str { ... }
```

**Elision rules:**
1. Each input reference gets its own lifetime
2. If there's exactly one input lifetime, it's assigned to all outputs
3. If there's `&self` or `&mut self`, its lifetime is assigned to outputs

```rust
// Rule 1: Multiple inputs get separate lifetimes
fn foo(x: &str, y: &str) -> i32
// Becomes: fn foo<'a, 'b>(x: &'a str, y: &'b str) -> i32

// Rule 2: Single input lifetime applies to output
fn foo(x: &str) -> &str
// Becomes: fn foo<'a>(x: &'a str) -> &'a str

// Rule 3: Methods use self's lifetime
impl Foo {
    fn bar(&self, x: &str) -> &str
    // Becomes: fn bar<'a, 'b>(&'a self, x: &'b str) -> &'a str
}
```

### Structs with References

```rust
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
    
    fn announce(&self, announcement: &str) -> &str {
        println!("Attention: {}", announcement);
        self.part
    }
}

let novel = String::from("Call me Ishmael...");
let first_sentence = novel.split('.').next().unwrap();
let excerpt = Excerpt { part: first_sentence };
```

### Multiple Lifetimes

```rust
fn longest_with_context<'a, 'b>(
    x: &'a str,
    y: &'a str,
    context: &'b str,
) -> &'a str {
    println!("Context: {}", context);
    if x.len() > y.len() { x } else { y }
}
```

### Lifetime Bounds

```rust
// T must live at least as long as 'a
fn print_ref<'a, T: 'a + Display>(t: &'a T) {
    println!("{}", t);
}

// T must live for the entire program
fn print_static<T: 'static + Display>(t: T) {
    println!("{}", t);
}
```

### Static Lifetime

```rust
// Lives for the entire program
let s: &'static str = "I live forever";

// String literals are always 'static
static GREETING: &str = "Hello";

// Owned data can be 'static if it contains no references
fn make_static() -> &'static str {
    let s = Box::new(String::from("leaked"));
    Box::leak(s)  // Deliberately leak memory
}
```

## Common Patterns

### Returning References

```rust
// Must return reference to input, not local data
fn first<'a>(items: &'a [i32]) -> &'a i32 {
    &items[0]
}

// Can return 'static references
fn default_name() -> &'static str {
    "Unknown"
}
```

### Struct Methods

```rust
struct Parser<'a> {
    input: &'a str,
    position: usize,
}

impl<'a> Parser<'a> {
    fn new(input: &'a str) -> Self {
        Parser { input, position: 0 }
    }
    
    fn remaining(&self) -> &'a str {
        &self.input[self.position..]
    }
}
```

### Lifetime in Trait Objects

```rust
// Trait object with explicit lifetime
fn process(handler: &dyn Fn(&str) -> &str) { ... }

// With lifetime bound
fn process<'a>(handler: &'a dyn Fn(&str) -> &str) { ... }

// Box with lifetime
fn make_handler<'a>() -> Box<dyn Fn(&'a str) -> &'a str + 'a> { ... }
```

### Higher-Ranked Trait Bounds (HRTB)

```rust
// "for any lifetime 'a"
fn call_with_ref<F>(f: F)
where
    F: for<'a> Fn(&'a str) -> &'a str,
{
    let s = String::from("hello");
    println!("{}", f(&s));
}
```

## Common Errors and Solutions

### Error: Missing Lifetime Specifier

```rust
// Error: missing lifetime specifier
struct Holder {
    data: &str,  // Needs lifetime
}

// Fix: add lifetime parameter
struct Holder<'a> {
    data: &'a str,
}
```

### Error: Lifetime May Not Live Long Enough

```rust
// Error: borrowed value doesn't live long enough
fn bad() -> &str {
    let s = String::from("hi");
    &s  // s dropped here
}

// Fix: return owned data
fn good() -> String {
    String::from("hi")
}
```

### Error: Cannot Return Reference to Local Variable

```rust
// Error: returns reference to data owned by function
fn first_word(s: String) -> &str {
    &s[..s.find(' ').unwrap_or(s.len())]
}

// Fix: borrow input instead of taking ownership
fn first_word(s: &str) -> &str {
    &s[..s.find(' ').unwrap_or(s.len())]
}
```

## Tips

- Most lifetimes are inferred—only annotate when the compiler asks
- Think of `'a` as "some lifetime that will be determined by the caller"
- Lifetimes don't change how long data lives—they describe existing relationships
- When in doubt, try returning owned data instead of references
- `'static` doesn't mean "lives forever"—it means "can live forever if needed"
- Use `String` instead of `&str` in structs to avoid lifetime complexity

## See Also

- [[Borrowing]] — How references work
- [[Generics]] — Lifetime parameters are a kind of generic
- [[Structs]] — Structs containing references
- [[Rust]]
