Structure
```rust
use std::collections::{BTreeMap, VecDeque};
pub struct PriceLevels {
  side: Side,
  levels: BTreeMap<i64, VecDeque<Order>>,
}
```

- Why `BTreeMap`
    
    - Sorted keys; asks use `first_key_value`, bids use `last_key_value`
        
- FIFO per level via `VecDeque::push_back / pop_front`
    
- Helpers
```rust
pub fn best_price(&self) -> Option<i64> { /* first/last key depending on side */ }
pub fn pop_best(&mut self) -> Option<Order> { /* pop from best level; prune empty */ }
pub fn add(&mut self, o: Order) { /* push_back at level */ }

```

[[HFTX]]