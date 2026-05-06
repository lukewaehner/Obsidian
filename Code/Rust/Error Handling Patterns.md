---
tags:
  - rust
  - error-handling
type: note
related:
  - "[[Rust]]"
  - "[[Result & Option]]"
  - "[[Code/Languages/Rust/Pattern Matching]]"
  - "[[Traits]]"
---
# Error Handling Patterns

Advanced error handling techniques beyond basic Result and Option.

## Overview

While `Result` and `Option` are foundational, real applications need custom error types, error conversion, and ergonomic error propagation. This note covers patterns for robust error handling.

## Basic Usage

### Custom Error Types

```rust
#[derive(Debug)]
pub enum AppError {
    NotFound(String),
    InvalidInput(String),
    Database(String),
    Network(String),
}

impl std::fmt::Display for AppError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            AppError::NotFound(msg) => write!(f, "Not found: {}", msg),
            AppError::InvalidInput(msg) => write!(f, "Invalid input: {}", msg),
            AppError::Database(msg) => write!(f, "Database error: {}", msg),
            AppError::Network(msg) => write!(f, "Network error: {}", msg),
        }
    }
}

impl std::error::Error for AppError {}
```

### The Error Trait

```rust
use std::error::Error;
use std::fmt;

#[derive(Debug)]
struct ParseConfigError {
    line: usize,
    message: String,
}

impl fmt::Display for ParseConfigError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Line {}: {}", self.line, self.message)
    }
}

impl Error for ParseConfigError {
    fn source(&self) -> Option<&(dyn Error + 'static)> {
        None  // Or return underlying cause
    }
}
```

## Key Concepts

### Error Conversion with From

```rust
use std::io;
use std::num::ParseIntError;

#[derive(Debug)]
enum AppError {
    Io(io::Error),
    Parse(ParseIntError),
}

impl From<io::Error> for AppError {
    fn from(err: io::Error) -> Self {
        AppError::Io(err)
    }
}

impl From<ParseIntError> for AppError {
    fn from(err: ParseIntError) -> Self {
        AppError::Parse(err)
    }
}

// Now ? automatically converts errors
fn read_number(path: &str) -> Result<i32, AppError> {
    let content = std::fs::read_to_string(path)?;  // io::Error -> AppError
    let num = content.trim().parse()?;             // ParseIntError -> AppError
    Ok(num)
}
```

### The `?` Operator in Depth

```rust
// ? is syntactic sugar for:
let value = match result {
    Ok(v) => v,
    Err(e) => return Err(e.into()),
};

// Works with Option too (returns None)
fn first_even(nums: &[i32]) -> Option<i32> {
    let first = nums.first()?;
    if first % 2 == 0 {
        Some(*first)
    } else {
        None
    }
}

// In main with Result
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content = std::fs::read_to_string("file.txt")?;
    println!("{}", content);
    Ok(())
}
```

### Boxing Errors

```rust
// Accept any error type
type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

fn do_something() -> Result<()> {
    let _file = std::fs::File::open("file.txt")?;
    let _num: i32 = "42".parse()?;
    Ok(())
}

// With Send + Sync for threads
type Result<T> = std::result::Result<T, Box<dyn std::error::Error + Send + Sync>>;
```

## Common Patterns

### Result Combinators

```rust
let result: Result<i32, &str> = Ok(5);

// map: transform Ok value
result.map(|x| x * 2);  // Ok(10)

// map_err: transform Err value
result.map_err(|e| format!("Error: {}", e));

// and_then: chain Results (like flatMap)
result.and_then(|x| if x > 0 { Ok(x) } else { Err("negative") });

// unwrap_or: default on error
result.unwrap_or(0);

// unwrap_or_else: lazy default
result.unwrap_or_else(|_| expensive_default());

// ok: convert to Option
result.ok();  // Some(5)
```

### Option Combinators

```rust
let opt: Option<i32> = Some(5);

// map, and_then work similarly
opt.map(|x| x * 2);  // Some(10)
opt.and_then(|x| if x > 0 { Some(x) } else { None });

// or: provide alternative
None.or(Some(5));  // Some(5)

// or_else: lazy alternative
opt.or_else(|| expensive_computation());

// filter: conditional Some
opt.filter(|x| *x > 3);  // Some(5)
opt.filter(|x| *x > 10); // None

// zip: combine two Options
Some(1).zip(Some(2));  // Some((1, 2))
Some(1).zip(None);     // None

// flatten: Option<Option<T>> -> Option<T>
Some(Some(5)).flatten();  // Some(5)
```

### Error Context

```rust
// Add context to errors
fn read_config() -> Result<Config, AppError> {
    std::fs::read_to_string("config.toml")
        .map_err(|e| AppError::Config(format!("Failed to read config: {}", e)))?;
    // ...
}

// With anyhow crate (simpler)
use anyhow::{Context, Result};

fn read_config() -> Result<Config> {
    let content = std::fs::read_to_string("config.toml")
        .context("Failed to read config file")?;
    // ...
}
```

### Collecting Results

```rust
let strings = vec!["1", "2", "three", "4"];

// Stop at first error
let numbers: Result<Vec<i32>, _> = strings
    .iter()
    .map(|s| s.parse::<i32>())
    .collect();
// Err(ParseIntError)

// Collect successes and failures separately
let (successes, failures): (Vec<_>, Vec<_>) = strings
    .iter()
    .map(|s| s.parse::<i32>())
    .partition(Result::is_ok);
```

### try Blocks (Nightly)

```rust
#![feature(try_blocks)]

fn process() -> Result<(), Error> {
    let result: Result<i32, Error> = try {
        let x = might_fail()?;
        let y = might_also_fail()?;
        x + y
    };
    // result is Ok or Err, function continues
    println!("Got: {:?}", result);
    Ok(())
}
```

## Popular Error Crates

### thiserror (Custom Errors)

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum DataError {
    #[error("Failed to read data: {0}")]
    Read(#[from] std::io::Error),
    
    #[error("Failed to parse data at line {line}")]
    Parse { line: usize },
    
    #[error("Invalid data: {0}")]
    Invalid(String),
}
```

### anyhow (Application Errors)

```rust
use anyhow::{anyhow, bail, Context, Result};

fn process() -> Result<()> {
    let config = load_config()
        .context("Failed to load configuration")?;
    
    if !config.valid {
        bail!("Invalid configuration");  // Early return with error
    }
    
    if config.value < 0 {
        return Err(anyhow!("Value must be positive"));
    }
    
    Ok(())
}
```

## Tips

- Use `thiserror` for libraries (custom error types)
- Use `anyhow` for applications (convenience)
- Implement `From` for automatic error conversion with `?`
- Add context to errors to create useful error chains
- Use `map_err` to convert errors inline
- `Box<dyn Error>` is fine for simple applications
- Prefer `expect()` over `unwrap()` for better panic messages

## See Also

- [[Result & Option]] — Basic error handling
- [[Code/Languages/Rust/Pattern Matching]] — Matching on errors
- [[Traits]] — The Error trait
- [[Rust]]
