---
tags:
  - rust
  - organization
type: note
related:
  - '[[Rust]]'
  - '[[Structs]]'
  - '[[Testing]]'
---
# Modules

Code organization and visibility in Rust.

## Overview

Rust's module system organizes code into namespaces with controlled visibility. Modules can be defined inline or in separate files.

## Defining Modules

### Inline Modules

```rust
mod math {
    pub fn add(a: i32, b: i32) -> i32 {
        a + b
    }
    
    fn helper() { }  // Private
}

fn main() {
    let sum = math::add(1, 2);
}
```

### File-Based Modules

```
src/
├── lib.rs       # Crate root
├── engine.rs    # mod engine
└── types/
    ├── mod.rs   # mod types
    └── order.rs # types::order
```

```rust
// lib.rs
pub mod engine;
pub mod types;
```

```rust
// engine.rs
pub fn start() { }
```

```rust
// types/mod.rs
pub mod order;
pub use order::Order;  // Re-export
```

## Visibility

```rust
pub mod api {
    pub fn public() { }           // Accessible everywhere
    pub(crate) fn crate_only() { } // Accessible within crate
    pub(super) fn parent_only() { } // Accessible in parent module
    fn private() { }              // Accessible only in this module
}
```

### Visibility Rules

| Keyword | Visibility |
|---------|------------|
| (none) | Private to module |
| `pub` | Public everywhere |
| `pub(crate)` | Public within crate |
| `pub(super)` | Public to parent module |
| `pub(in path)` | Public to specific path |

## Importing with `use`

```rust
// Single item
use std::collections::HashMap;

// Multiple items
use std::collections::{HashMap, HashSet, BTreeMap};

// All public items (use sparingly)
use std::io::*;

// Renaming
use std::io::Result as IoResult;

// Self for the module itself
use std::io::{self, Read, Write};
```

## Re-exporting with `pub use`

Simplify external access:

```rust
// lib.rs
mod types;
mod engine;

// Internal paths
// types::order::Order
// engine::order_book::OrderBook

// Re-export for cleaner external API
pub use types::Order;
pub use engine::OrderBook;

// Now users can do:
// use mycrate::Order;
// Instead of:
// use mycrate::types::order::Order;
```

## Path Types

```rust
// Absolute path (from crate root)
use crate::types::Order;

// Relative path (from current module)
use self::helper::process;
use super::parent_fn;

// External crate
use std::collections::HashMap;
use serde::Serialize;
```

## Module Organization Patterns

### Prelude Pattern

Common re-exports for convenient importing:

```rust
// prelude.rs
pub use crate::Order;
pub use crate::OrderBook;
pub use crate::Side;
pub use crate::Error;
```

```rust
// In user code
use mycrate::prelude::*;
```

### Separating Types and Implementation

```rust
// types.rs - Data structures
pub struct Order { ... }
pub struct Trade { ... }
pub enum Side { Bid, Ask }

// engine.rs - Logic
use crate::types::{Order, Trade, Side};
pub struct OrderBook { ... }
impl OrderBook { ... }
```

## Common Patterns

### Declaring Submodules

```rust
// lib.rs
pub mod types;      // Looks for types.rs or types/mod.rs
mod internal;       // Private module

pub use types::{Order, Trade};  // Re-export
```

### Conditional Compilation

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn it_works() { }
}
```

## Tips

- Use `crate::` for absolute paths within your crate
- Re-export (`pub use`) to create a clean public API
- Keep modules focused—one responsibility per module
- Use `pub(crate)` for internal-but-shared items
- Prefer explicit imports over glob imports (`*`)
- Tests go in a `#[cfg(test)]` submodule

## See Also

- [[Structs]] — Types to organize
- [[Testing]] — Test modules
- [[Rust]]
