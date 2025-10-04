- `// lib.rs`
    
    ```rust
    pub mod types; 
    mod engine; 
    pub use engine::OrderBook;
    ```
    
- `use` rules
    
    - `use crate::types::{Order, Side};`
        
    - Re-export to simplify external paths: `pub use types::{Order, OrderId, Side, Trade};`
        
- Visibility
    
    - `pub` (crate-external), `pub(crate)` (crate-wide), `pub(super)` (parent mod)
        
- Path tips
    
    - Prefer absolute (`crate::…`) inside the crate for clarity