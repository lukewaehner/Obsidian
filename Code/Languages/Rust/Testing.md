---
tags:
  - rust
  - testing
type: note
related:
  - '[[Rust]]'
  - '[[Modules]]'
  - '[[Result & Option]]'
---
# Testing

Unit tests and assertions in Rust.

## Overview

Rust has built-in testing support. Tests are functions annotated with `#[test]` that panic on failure. They live alongside your code in `#[cfg(test)]` modules.

## Basic Test

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
```

Run tests with:
```bash
cargo test
cargo test test_name      # Run specific test
cargo test -- --nocapture # Show println! output
```

## Assertions

```rust
#[test]
fn test_assertions() {
    // Equality
    assert_eq!(actual, expected);
    assert_ne!(a, b);
    
    // Boolean
    assert!(condition);
    assert!(!condition);
    
    // With custom message
    assert!(x > 0, "x should be positive, got {}", x);
    assert_eq!(a, b, "values should match");
}
```

## Testing for Panics

```rust
#[test]
#[should_panic]
fn test_panic() {
    panic!("This test should panic");
}

#[test]
#[should_panic(expected = "out of bounds")]
fn test_specific_panic() {
    let v = vec![1, 2, 3];
    v[99];  // Panics with "out of bounds"
}
```

## Testing Results

```rust
#[test]
fn test_result() -> Result<(), String> {
    let result = do_something()?;
    assert_eq!(result, expected);
    Ok(())
}
```

## Test Organization

### Unit Tests (Same File)

```rust
// src/lib.rs
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }
    
    #[test]
    fn test_add_negative() {
        assert_eq!(add(-1, 1), 0);
    }
}
```

### Integration Tests (tests/ directory)

```
project/
├── src/
│   └── lib.rs
└── tests/
    └── integration_test.rs
```

```rust
// tests/integration_test.rs
use my_crate::add;

#[test]
fn test_add_integration() {
    assert_eq!(add(2, 2), 4);
}
```

## Debug Assertions

Only run in debug builds:

```rust
fn process(order: &Order) {
    debug_assert!(order.qty > 0);
    debug_assert!(matches!(order.side, Side::Bid | Side::Ask));
    // ...
}
```

## Test Helpers

### Setup and Teardown

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    fn setup() -> TestContext {
        TestContext::new()
    }
    
    #[test]
    fn test_with_setup() {
        let ctx = setup();
        // use ctx...
    }
}
```

### Test Fixtures

```rust
fn sample_order() -> Order {
    Order {
        id: 1,
        symbol: "AAPL".into(),
        side: Side::Bid,
        qty: 100,
        price: 150,
    }
}

#[test]
fn test_order_processing() {
    let order = sample_order();
    // test with order...
}
```

## Common Patterns

### Testing Private Functions

Unit tests in the same file can access private items:

```rust
fn private_helper(x: i32) -> i32 {
    x * 2
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_private() {
        assert_eq!(private_helper(5), 10);  // Works!
    }
}
```

### Property-Based Testing Ideas

```rust
#[test]
fn test_order_conservation() {
    // Total filled quantity <= submitted quantity
    let mut book = OrderBook::new();
    let order = sample_order();
    let initial_qty = order.qty;
    
    let trades = book.submit(order);
    let filled: i64 = trades.iter().map(|t| t.qty).sum();
    
    assert!(filled <= initial_qty);
}

#[test]
fn test_price_time_priority() {
    // Earlier maker fills first at same price
    // ...
}
```

### Ignoring Tests

```rust
#[test]
#[ignore]
fn expensive_test() {
    // Run with: cargo test -- --ignored
}
```

## Tips

- Use `assert_eq!` over `assert!(a == b)` for better error messages
- Keep tests focused—one assertion per test when possible
- Use descriptive test names: `test_bid_crosses_ask_produces_trade`
- Put `#[cfg(test)]` on the module, not individual functions
- Use `debug_assert!` for invariants that should hold but are expensive to check
- Run `cargo test -- --test-threads=1` for sequential execution

## See Also

- [[Modules]] — Test module organization
- [[Result & Option]] — Testing error cases
- [[Rust]]
