---
tags:
  - rust
  - types
type: note
related:
  - '[[Rust]]'
  - '[[Pattern Matching]]'
  - '[[Result & Option]]'
  - '[[Traits]]'
---
# Enums

Algebraic data types for representing values that can be one of several variants.

## Overview

Enums (enumerations) define a type by listing its possible variants. Unlike enums in other languages, Rust enums can hold data, making them powerful algebraic data types. They're the foundation for `Option` and `Result`.

## Basic Usage

### Simple Enums

```rust
enum Direction {
    North,
    South,
    East,
    West,
}

let dir = Direction::North;
```

### Enums with Data

```rust
enum Message {
    Quit,                       // No data
    Move { x: i32, y: i32 },    // Named fields (struct-like)
    Write(String),              // Single value (tuple-like)
    ChangeColor(u8, u8, u8),    // Multiple values
}

let msg = Message::Move { x: 10, y: 20 };
let quit = Message::Quit;
let write = Message::Write(String::from("hello"));
```

### Option and Result

Rust's most important enums:

```rust
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}

let some_number: Option<i32> = Some(5);
let no_number: Option<i32> = None;

let success: Result<i32, &str> = Ok(42);
let failure: Result<i32, &str> = Err("something went wrong");
```

## Key Concepts

### Pattern Matching

Enums are used with `match` for exhaustive handling:

```rust
fn describe(dir: Direction) -> &'static str {
    match dir {
        Direction::North => "going up",
        Direction::South => "going down",
        Direction::East => "going right",
        Direction::West => "going left",
    }
}
```

### Extracting Data

```rust
fn process(msg: Message) {
    match msg {
        Message::Quit => println!("Quitting"),
        Message::Move { x, y } => println!("Moving to ({}, {})", x, y),
        Message::Write(text) => println!("Writing: {}", text),
        Message::ChangeColor(r, g, b) => println!("Color: {}, {}, {}", r, g, b),
    }
}
```

### if let for Single Variants

```rust
let msg = Message::Write(String::from("hello"));

if let Message::Write(text) = msg {
    println!("Got text: {}", text);
}
```

### Methods on Enums

```rust
impl Direction {
    fn opposite(&self) -> Direction {
        match self {
            Direction::North => Direction::South,
            Direction::South => Direction::North,
            Direction::East => Direction::West,
            Direction::West => Direction::East,
        }
    }
    
    fn is_vertical(&self) -> bool {
        matches!(self, Direction::North | Direction::South)
    }
}
```

### Deriving Traits

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
enum Status {
    Active,
    Inactive,
    Pending,
}
```

## Common Patterns

### State Machines

```rust
enum ConnectionState {
    Disconnected,
    Connecting { attempt: u32 },
    Connected { session_id: String },
    Error { message: String },
}

impl ConnectionState {
    fn connect(&self) -> ConnectionState {
        match self {
            ConnectionState::Disconnected => {
                ConnectionState::Connecting { attempt: 1 }
            }
            ConnectionState::Connecting { attempt } if *attempt < 3 => {
                ConnectionState::Connecting { attempt: attempt + 1 }
            }
            ConnectionState::Connecting { .. } => {
                ConnectionState::Error { message: "Max retries".into() }
            }
            other => other.clone(),
        }
    }
}
```

### Recursive Types with Box

```rust
enum List<T> {
    Cons(T, Box<List<T>>),
    Nil,
}

let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
```

### Converting with From/Into

```rust
enum AppError {
    Io(std::io::Error),
    Parse(std::num::ParseIntError),
}

impl From<std::io::Error> for AppError {
    fn from(err: std::io::Error) -> Self {
        AppError::Io(err)
    }
}
```

### C-like Enums

```rust
#[repr(u8)]
enum HttpStatus {
    Ok = 200,
    NotFound = 404,
    InternalError = 500,
}

let status = HttpStatus::Ok as u8;  // 200
```

## Tips

- Use enums instead of boolean flags when there are more than two states
- Prefer `Option<T>` over nullable values
- Use `Result<T, E>` for operations that can fail
- Derive `Copy` for simple enums without heap data
- Use `matches!` macro for simple boolean checks
- Enums are sized to fit their largest variant plus discriminant

## See Also

- [[Pattern Matching]] — Working with enum variants
- [[Result & Option]] — Error handling enums
- [[Traits]] — Implementing traits for enums
- [[Rust]]
