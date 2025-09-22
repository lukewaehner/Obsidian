Building trades
```rust
let mut trades = Vec::new();
trades.push(Trade { /* … */ });

```

Using `min` for fill
```rust
let fill = taker.qty.min(maker.qty);
```

Retain empty levels
```rust
if dq.is_empty() { self.levels.remove(&px); }
```
- `while taker.qty > 0 { … }` over iterator when matching