---
tags:
  - rust
  - error-handling
type: note
related:
  - "[[Rust]]"
  - "[[Code/Languages/Rust/Pattern Matching]]"
---
# Result & Option

Rust's approach to error handling without exceptions.

## Overview

Rust uses `Option<T>` for values that might be absent and `Result<T, E>` for operations that might fail. Both are enums that force you to handle all cases explicitly.

## Option

Represents an optional value:

```rust
enum Option<T> {
    Some(T),
    None,
}
```

### Basic Usage

```rust
fn find_user(id: u64) -> Option<User> {
    if id == 1 {
        Some(User { name: "Alice".into() })
    } else {
        None
    }
}

// Handle with match
match find_user(1) {
    Some(user) => println!("Found: {}", user.name),
    None => println!("User not found"),
}

// Handle with if let
if let Some(user) = find_user(1) {
    println!("Found: {}", user.name);
}
```

### Option Methods

```rust
let opt = Some(5);

opt.unwrap();           // Returns 5, panics if None
opt.unwrap_or(0);       // Returns 5, or 0 if None
opt.unwrap_or_default();// Returns 5, or default if None
opt.expect("msg");      // Returns 5, panics with "msg" if None

opt.is_some();          // true
opt.is_none();          // false

opt.map(|x| x * 2);     // Some(10)
opt.and_then(|x| Some(x * 2));  // Some(10), for chaining Options

let none: Option<i32> = None;
none.unwrap_or_else(|| expensive_default());  // Lazy default
```

## Result

Represents success or failure:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

### Basic Usage

```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Division by zero".into())
    } else {
        Ok(a / b)
    }
}

// Handle with match
match divide(10.0, 2.0) {
    Ok(result) => println!("Result: {}", result),
    Err(e) => println!("Error: {}", e),
}

// Handle with if let
if let Ok(result) = divide(10.0, 2.0) {
    println!("Result: {}", result);
}
```

### Result Methods

```rust
let result: Result<i32, &str> = Ok(5);

result.unwrap();        // Returns 5, panics if Err
result.unwrap_or(0);    // Returns 5, or 0 if Err
result.expect("msg");   // Returns 5, panics with "msg" if Err

result.is_ok();         // true
result.is_err();        // false

result.ok();            // Some(5) - converts to Option
result.err();           // None - converts to Option

result.map(|x| x * 2);  // Ok(10)
result.map_err(|e| format!("Error: {}", e));  // Transform error
```

## The `?` Operator

Propagate errors automatically:

```rust
fn read_username() -> Result<String, io::Error> {
    let mut file = File::open("username.txt")?;  // Returns early if Err
    let mut username = String::new();
    file.read_to_string(&mut username)?;
    Ok(username)
}
```

The `?` operator:
1. If `Ok(val)`, unwraps to `val`
2. If `Err(e)`, returns `Err(e)` from the function early

### Using `?` with Option

```rust
fn first_char(s: &str) -> Option<char> {
    let line = s.lines().next()?;  // Returns None if no lines
    line.chars().next()            // Returns None if empty
}
```

## Converting Between Types

```rust
// Option -> Result
let opt = Some(5);
opt.ok_or("was None");         // Ok(5) or Err("was None")
opt.ok_or_else(|| make_error()); // Lazy error creation

// Result -> Option
let result: Result<i32, &str> = Ok(5);
result.ok();    // Some(5)
result.err();   // None
```

## Custom Error Types

```rust
#[derive(Debug)]
pub enum EngineError {
    InvalidQuantity,
    InvalidPrice,
    SymbolNotFound,
}

pub fn submit_order(order: Order) -> Result<Trade, EngineError> {
    if order.qty <= 0 {
        return Err(EngineError::InvalidQuantity);
    }
    if order.price < 0 {
        return Err(EngineError::InvalidPrice);
    }
    // ... process order
    Ok(trade)
}
```

## Common Patterns

### Early Return with `?`

```rust
fn process(data: Option<String>) -> Result<i32, Error> {
    let s = data.ok_or(Error::NoData)?;
    let n: i32 = s.parse()?;
    Ok(n * 2)
}
```

### Combining Results

```rust
// Collect into a single Result
let results: Vec<Result<i32, _>> = vec![Ok(1), Ok(2), Ok(3)];
let combined: Result<Vec<i32>, _> = results.into_iter().collect();
// Ok([1, 2, 3]) or first Err
```

### Default on Error

```rust
let value = risky_operation().unwrap_or_default();
let value = risky_operation().unwrap_or_else(|e| {
    log::error!("Failed: {}", e);
    fallback_value()
});
```

## Tips

- Prefer `?` over `unwrap()` in production code
- Use `expect()` with descriptive messages during development
- Define custom error enums for domain-specific errors
- Use `anyhow` crate for simple error handling
- Use `thiserror` crate for deriving error traits
- `unwrap()` is fine in tests and examples

## See Also

- [[Code/Languages/Rust/Pattern Matching]] — Matching on Option and Result
- [[Rust]]
