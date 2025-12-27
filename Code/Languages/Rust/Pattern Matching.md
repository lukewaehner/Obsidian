---
tags:
  - rust
  - control-flow
type: note
related:
  - '[[Rust]]'
  - '[[Result & Option]]'
  - '[[Structs]]'
---
# Pattern Matching

Match expressions and control flow patterns in Rust.

## Overview

Pattern matching is one of Rust's most powerful features. It enables exhaustive branching, destructuring, and safe handling of enums like `Option` and `Result`.

## Basic Match

```rust
let x = 5;

match x {
    1 => println!("one"),
    2 => println!("two"),
    3..=5 => println!("three to five"),
    _ => println!("something else"),
}
```

> **Exhaustive**: Match must cover all possibilities. Use `_` as a catch-all.

## Matching Enums

```rust
enum Side { Bid, Ask }

let side = Side::Bid;

match side {
    Side::Bid => println!("Buying"),
    Side::Ask => println!("Selling"),
}
```

## Option and Result

```rust
let maybe: Option<i32> = Some(42);

match maybe {
    Some(x) => println!("Got {}", x),
    None => println!("Nothing"),
}

let result: Result<i32, &str> = Ok(42);

match result {
    Ok(val) => println!("Success: {}", val),
    Err(e) => println!("Error: {}", e),
}
```

## if let

Shorthand for matching a single pattern:

```rust
let maybe = Some(42);

// Instead of full match
if let Some(x) = maybe {
    println!("Got {}", x);
}

// With else
if let Some(x) = maybe {
    println!("Got {}", x);
} else {
    println!("Nothing");
}
```

## let-else

Extract or exit early:

```rust
fn process(opt: Option<i32>) -> i32 {
    let Some(value) = opt else {
        return 0;  // Early return if None
    };
    value * 2
}
```

## while let

Loop while pattern matches:

```rust
let mut stack = vec![1, 2, 3];

while let Some(top) = stack.pop() {
    println!("{}", top);  // 3, 2, 1
}
```

## Destructuring

### Structs

```rust
struct Point { x: i32, y: i32 }

let p = Point { x: 1, y: 2 };

match p {
    Point { x: 0, y } => println!("On y-axis at {}", y),
    Point { x, y: 0 } => println!("On x-axis at {}", x),
    Point { x, y } => println!("At ({}, {})", x, y),
}

// Shorthand
let Point { x, y } = p;
```

### Tuples

```rust
let pair = (0, -2);

match pair {
    (0, y) => println!("On y-axis: {}", y),
    (x, 0) => println!("On x-axis: {}", x),
    (x, y) => println!("At ({}, {})", x, y),
}
```

## Match Guards

Add conditions to patterns:

```rust
let num = Some(4);

match num {
    Some(x) if x < 5 => println!("Less than 5"),
    Some(x) if x >= 5 => println!("5 or more"),
    None => println!("None"),
    _ => unreachable!(),
}
```

## Multiple Patterns

```rust
let x = 1;

match x {
    1 | 2 => println!("one or two"),
    3..=9 => println!("three through nine"),
    _ => println!("other"),
}
```

## Binding with @

Name a value while also testing it:

```rust
match some_value {
    val @ 1..=5 => println!("Got {} in range", val),
    val @ _ => println!("Got {} outside range", val),
}
```

## Common Patterns

### Matching References

```rust
let reference = &4;

match reference {
    &val => println!("Got value: {}", val),
}

// Or dereference with *
match *reference {
    val => println!("Got value: {}", val),
}
```

### Ignoring Parts

```rust
let tuple = (1, 2, 3);

match tuple {
    (first, _, _) => println!("First: {}", first),
    (_, second, ..) => println!("Second: {}", second),
}
```

### matches! Macro

Check if a value matches a pattern:

```rust
let side = Side::Bid;
let is_bid = matches!(side, Side::Bid);

// With guard
let x = Some(5);
let in_range = matches!(x, Some(n) if n > 0 && n < 10);
```

## Tips

- Match expressions return values—use them in assignments
- Prefer `if let` for single-pattern matches
- Use `let-else` for "unwrap or return" patterns
- Always handle all enum variants—compiler enforces this
- Guards (`if`) add conditions without creating new patterns
- Use `_` for values you don't need

## See Also

- [[Result & Option]] — Error handling with pattern matching
- [[Structs]] — Destructuring structs
- [[Rust]]
