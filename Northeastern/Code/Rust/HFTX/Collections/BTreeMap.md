- balanced tree map, sorted keys
    
- O(log n) insert / lookup
    
- lets you quickly find best price (min or max key depending on side)
    
- structure for price ladder: `BTreeMap<i64, VecDeque<Order>>`
```rust
use std::collections::BTreeMap;
let mut book = BTreeMap::new();
book.insert(100, VecDeque::new());
if let Some(q) = book.first_key_value() {
    println!("best price: {}", q.0);
}
```