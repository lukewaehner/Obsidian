```rust
pub mod types; 
// A submodule types, include the module, make it public
pub use types::{Order, OrderId, Side, Trade} 
// exports items from types so we can use 
// use crate::Order
```
- Submodules can be used in other files
- Exports can be used to reduce typing needs

---
