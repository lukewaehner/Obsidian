---
tags:
  - rust
  - debugging
type: note
related:
  - '[[Rust]]'
  - '[[Derives]]'
  - '[[Testing]]'
---
# Logging

Debug output and logging in Rust.

## Overview

Rust offers several approaches to logging: simple `println!` for quick debugging, the `log` crate for structured logging, and `Debug` trait for inspecting values.

## Debug Printing

### println! and eprintln!

```rust
// Standard output
println!("Value: {}", x);
println!("Debug: {:?}", complex_struct);
println!("Pretty: {:#?}", nested_struct);

// Standard error (for logs)
eprintln!("Error occurred: {}", e);
```

### Debug Trait

Derive `Debug` for custom types:

```rust
#[derive(Debug)]
struct Order {
    id: u64,
    symbol: String,
    qty: i64,
}

let order = Order { id: 1, symbol: "AAPL".into(), qty: 100 };
println!("{:?}", order);   // Order { id: 1, symbol: "AAPL", qty: 100 }
println!("{:#?}", order);  // Pretty-printed with newlines
```

### dbg! Macro

Quick debugging with file/line info:

```rust
let x = 5;
dbg!(x);  // [src/main.rs:3] x = 5

// Works with expressions
let y = dbg!(x * 2);  // Prints and returns the value
```

## The log Crate

Structured logging with levels:

```toml
# Cargo.toml
[dependencies]
log = "0.4"
env_logger = "0.10"  # One of many backends
```

```rust
use log::{trace, debug, info, warn, error};

fn main() {
    env_logger::init();  // Initialize logger
    
    trace!("Very detailed info");
    debug!("Debugging info");
    info!("General information");
    warn!("Warning message");
    error!("Error occurred: {}", err);
}
```

Run with log level:
```bash
RUST_LOG=debug cargo run
RUST_LOG=my_crate=trace cargo run
```

### Log Levels

| Level | Use Case |
|-------|----------|
| `error!` | Errors that need attention |
| `warn!` | Unexpected but handled situations |
| `info!` | General operational messages |
| `debug!` | Detailed development info |
| `trace!` | Very verbose, step-by-step |

## Conditional Compilation

Only compile logging in debug builds:

```rust
#[cfg(debug_assertions)]
println!("Debug mode only");

// Or use debug_assert!
debug_assert!(x > 0, "x must be positive");
```

## Common Patterns

### Logging Structured Data

```rust
#[derive(Debug)]
struct Trade { maker: u64, taker: u64, qty: i64 }

let trade = Trade { maker: 1, taker: 2, qty: 100 };
debug!("Trade executed: {:?}", trade);
```

### Pretty-Printing Collections

```rust
let orders = vec![order1, order2, order3];
println!("Orders:\n{:#?}", orders);
```

### Logging in Tests

```rust
#[test]
fn test_something() {
    // Initialize logger for tests
    let _ = env_logger::builder().is_test(true).try_init();
    
    debug!("Test starting...");
    // test code
}
```

### Performance-Conscious Logging

```rust
// Lazy evaluation - format string only if level is enabled
debug!("Expensive: {:?}", expensive_computation());

// Check level first for very expensive operations
if log::log_enabled!(log::Level::Trace) {
    trace!("Data: {:?}", very_expensive_dump());
}
```

## Tips

- Always derive `Debug` on your types for easy inspection
- Use `{:#?}` for pretty-printed debug output
- Use `dbg!()` for quick one-off debugging (remove before commit)
- Set `RUST_LOG` environment variable to control log levels
- Use `eprintln!` for error messages (goes to stderr)
- Consider `tracing` crate for async/concurrent applications

## See Also

- [[Derives]] — Deriving Debug trait
- [[Testing]] — Logging in tests
- [[Rust]]
