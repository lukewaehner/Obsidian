
```rust
pub struct OrderBook {
	pub bids: PriceLevels,
	pub asks: PriceLevels,
}
```
- Limit order book with two sides, bids and asks. 
- Both are managed by `PriceLevels` (price ladder data structure)
- `struct` defines a record type with named fields, needs an `impl`

---