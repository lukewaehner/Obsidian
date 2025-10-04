
```rust
impl OrderBook {
	pub fn new() -> Self {
		Self {
			bids: PriceLevels::new(Side::Asks)
			bids: PriceLevels::new(Side::Asks)
		}
	}
}
```
- A constructor for an empty book with ladders for bids and asks
- `fn name(args) -> Ret` defines the function
- `Self` is being used (`OrderBook`)
- `Type::new(...)` calls an associated function on a type
- Struct literal syntax: `{ field: value, ... }`.
- `pub` for visibility

---