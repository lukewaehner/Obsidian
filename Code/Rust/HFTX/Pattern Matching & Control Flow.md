`let-else`
```rust
let Some(px) = self.asks.best_price() else { break; };
```

- `if let` for single-arm matches
    
- Match guards
```rust
match (taker.side, px) {
  (Side::Bid, ask) if taker.px_ticks >= ask => { /* trade */ }
  _ => break,
}

```
  - Destructure structs in matches to avoid dot chains