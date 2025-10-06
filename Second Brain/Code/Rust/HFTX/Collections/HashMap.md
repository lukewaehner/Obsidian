- hash table, O(1) average insert / lookup
    
- optional support for cancels or modifications by `OrderId`
    
- map from order id → (price, position)
```rust
use std::collections::HashMap;
let mut index: HashMap<u64, i64> = HashMap::new();
index.insert(42, 101);
if let Some(p) = index.get(&42) {
    println!("order at price {}", p);
}
```