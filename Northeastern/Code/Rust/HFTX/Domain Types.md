`OrderId` and `symbol` types
```rust
pub type OrderId = u64; // fast, Copy
pub type Ticks = i64;   // price in ticks
```

`Side` as enum
```rust
#[derive(Copy, Clone, Debug, Eq, PartialEq, Hash)]
pub enum Side { Bid, Ask }
```

`Order` minimal, heap owns strings only if necessary
```rust
pub struct Order {
  pub id: OrderId,
  pub side: Side,
  pub symbol: String,   // consider Arc<str> if lots of clones
  pub px_ticks: Ticks,
  pub qty: i64,
  pub ts_ns: i128,
}
```
- `Trade` mirrors minimal copyable fields