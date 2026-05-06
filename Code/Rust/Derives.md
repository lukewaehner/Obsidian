---
tags:
  - rust
  - traits
type: note
related:
  - '[[Rust]]'
  - '[[Structs]]'
  - '[[Copying]]'
---
# Derives

Auto-implementing common traits with the `#[derive]` attribute.

## Overview

Derives let the compiler generate trait implementations automatically. This reduces boilerplate for common functionality like debugging, comparison, and copying.

## Common Derives

| Derive | Purpose | Example Usage |
|--------|---------|---------------|
| `Debug` | Enables `{:?}` formatting | `println!("{:?}", val)` |
| `Clone` | Explicit duplication with `.clone()` | `let copy = val.clone()` |
| `Copy` | Implicit bitwise copying | `let y = x; // x still valid` |
| `PartialEq` | `==` and `!=` comparison | `if a == b { }` |
| `Eq` | Marker for total equality | Required for `HashMap` keys |
| `Hash` | Hashing for collections | `HashMap<K, V>`, `HashSet<T>` |
| `Default` | Default value | `MyStruct::default()` |
| `PartialOrd` | `<`, `>`, `<=`, `>=` comparison | `if a < b { }` |
| `Ord` | Total ordering | Required for `BTreeMap` keys |

## Basic Usage

```rust
#[derive(Debug, Clone, PartialEq)]
struct Point {
    x: f64,
    y: f64,
}

let p1 = Point { x: 1.0, y: 2.0 };
let p2 = p1.clone();
println!("{:?}", p1);      // Debug
assert_eq!(p1, p2);        // PartialEq
```

## Debug

Enables debug printing:

```rust
#[derive(Debug)]
struct Order {
    id: u64,
    symbol: String,
}

let order = Order { id: 1, symbol: "AAPL".into() };
println!("{:?}", order);   // Compact: Order { id: 1, symbol: "AAPL" }
println!("{:#?}", order);  // Pretty-printed with newlines
```

## Clone and Copy

```rust
// Copy: implicit, bitwise (only for simple types)
#[derive(Copy, Clone)]
struct Point { x: i32, y: i32 }

// Clone only (has heap data)
#[derive(Clone)]
struct Person { name: String }
```

> **Rule**: `Copy` requires all fields to also be `Copy`.

## Equality and Hashing

```rust
#[derive(PartialEq, Eq, Hash)]
struct UserId(u64);

use std::collections::HashMap;
let mut users: HashMap<UserId, String> = HashMap::new();
users.insert(UserId(1), "Alice".into());
```

`Eq` and `Hash` together enable use as `HashMap`/`HashSet` keys.

## Ordering

```rust
#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Version {
    major: u32,
    minor: u32,
    patch: u32,
}

let v1 = Version { major: 1, minor: 0, patch: 0 };
let v2 = Version { major: 2, minor: 0, patch: 0 };
assert!(v1 < v2);

// Ord enables BTreeMap keys and sorting
let mut versions = vec![v2, v1];
versions.sort();
```

## Default

```rust
#[derive(Default)]
struct Config {
    timeout: u64,      // defaults to 0
    retries: u32,      // defaults to 0
    enabled: bool,     // defaults to false
}

let config = Config::default();
let custom = Config { timeout: 30, ..Default::default() };
```

## Combining Derives

Common combinations:

```rust
// Value type (like an ID)
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct OrderId(pub u64);

// Data struct with heap data
#[derive(Debug, Clone, PartialEq)]
pub struct Order {
    pub id: OrderId,
    pub symbol: String,
    pub qty: i64,
}

// Enum
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Side { Bid, Ask }
```

## Tips

- Always derive `Debug` for easier development
- Derive `Copy` for small, stack-only types (integers, simple enums)
- `Eq` requires `PartialEq`, `Ord` requires `PartialOrd`
- `Hash` requires `Eq` for correctness
- Order of derives doesn't matter
- Some derives require all fields to also implement the trait

## See Also

- [[Structs]] — Defining custom types
- [[Copying]] — Copy vs Clone in depth
- [[Rust]]
