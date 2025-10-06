- Use `Option` for “not found / empty book”
    
- Use `Result<T, EngineErr>` for input validation & invariants
```rust
pub enum EngineErr { NonPositiveQty, NegativePrice, SymbolEmpty }
pub fn submit_limit(&mut self, taker: Order) -> Result<Vec<Trade>, EngineErr> { /* … */ }
```
- The `?` operator to early-return on errors
    
- Converting: `Option<T>.ok_or(EngineErr::…)`