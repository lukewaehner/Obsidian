## Matching engine
```rust
pub fn submit_limit(&mut self, mut taker: Order) -> Vec<Trade> {
```
- Entry point for posting a limit order. It may match against the opposite side, making a trade. The remaining quantity will rest on the book.
- `&mut self` takes a mutable borrow of OrderBook
- `mut taker: Order` makes the parameter variable itself mutable
- Returns `Vec<Trade>` a growable array of trades
```rust
let mut trades = Vec::new();
let ts_ns = taker.ts_ns
```
- `let` binds variables
- `mut` allows reassignment
- `Vec::new()` makes an empty vector

---
```rust
match taker.side {
	Side::Bid => {
```
- Branch to the other side, try to match against asks for a bid order.
- `match` compares a value against patterns

```rust
while taker.qty > 0 {
	let Some(best_ask_px) = self.asks.best_price() else {
		break;
	};
```
- Gets the best price, if there is no ask, it breaks out
- `let Some(x) = expr else { ... }` this is the let-else pattern. Extract `x` if the expression is `Some` otherwise runs the else block
```rust
if taker.px_ticks < best_ask_px {
	break;
}
```
- A bid can only trade if its price $\geq$ best ask.
```rust
let mut maker = match self.asks.pop_best() {
	Some(o) => o,
	None => break,
}
```
- Pulls the front (price-time first) maker order at the best ask level.
```rust
let fill = taker.qty.min(maker.qty);
taker.qty -= fill;
maker.qty -= fill;
```
- Either the taker wants more than the maker has, and needs to go to another maker, or a partial fill, or the taker wants less than the maker has, and the taker gets full fill, maker has some left over.
```rust
trades.push(Trade {
	maker: maker.id,
	taker: taker.id,
	symbol: taker.symbol.clone(),
	px_ticks: best_ask_px,
	qty: fill,
	ts_ns
});
```
- Records a trade at the maker's price.
- `vec.push(value)` appends
- `Type { field: value, ... }` constructs a struct
- `.clone()` duplicates owned data

---
[[HFTX]]