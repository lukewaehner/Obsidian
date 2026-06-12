# Order Book Engine

*`orderbook/src/lib.rs` + `orderbook/src/price_levels.rs`*

---

## `OrderBook`

```rust
pub struct OrderBook {
    pub bids: PriceLevels,  // buy side — highest price = best
    pub asks: PriceLevels,  // sell side — lowest price = best
}
```

Simple pair of `PriceLevels`. Each side is self-contained. There is **no symbol field** on `OrderBook` itself — the `Exchange` layer maps symbols to books.

**Not thread-safe.** The comment in the code says: "wrap in RwLock for concurrent access." The `Exchange` does exactly that.

---

## `PriceLevels` — Full API

### Insertion

```rust
fn push(&mut self, order: Order)
```
Appends to the back of the `VecDeque` at `order.px_ticks`. Creates the level if it doesn't exist. Also inserts into the `index`. O(log n) for BTreeMap entry, O(1) for deque push.

```rust
fn push_front(&mut self, order: Order)
```
Used only for **partial fills**: a maker order was partially consumed, so it goes back to the *front* of its price level to keep time priority. Without this, the partially-filled maker would lose its queue position.

---

### Best-Price Reads

```rust
fn best_price(&self) -> Option<i64>
```
- **Asks**: `self.levels.first_key_value()` — BTreeMap is sorted ascending, so the first key is the cheapest ask.
- **Bids**: `self.levels.last_key_value()` — the last key is the highest bid.

O(log n).

```rust
fn peek_best(&self) -> Option<&Order>
```
Returns a reference to the front-of-queue order at the best price, skipping any tombstoned orders. Does not remove anything.

---

### Consuming / Matching

```rust
fn pop_best(&mut self) -> Option<Order>
```
The hot path during matching. Steps:
1. Get `best_price()`.
2. Walk the front of the deque, **skipping canceled orders** (lazy removal happens here).
3. Pop and return the first live order.
4. If the level's deque is now empty, remove the level from the BTreeMap.

This loop in `pop_best` is what makes lazy cancellation work — you mark cancels with O(1), and the actual cleanup happens the next time that price level is hit during matching.

---

### Cancellation

```rust
fn cancel(&mut self, id: OrderId) -> bool
```
Lazy cancel: removes `id` from `index`, adds to `canceled` set. Does **not** touch the `BTreeMap` or `VecDeque`. Returns `false` if the order wasn't in the index (already filled or double-cancel).

```rust
fn remove(&mut self, id: OrderId) -> Option<Order>
```
Eager cancel: actually digs into the `VecDeque` and pulls the order out. Used for order amendments. More expensive — O(n) in queue length at that price — but returns the order for the caller to inspect.

---

### Query Helpers

| Method | Description |
|---|---|
| `best_level_size() -> usize` | Count of live orders at best price |
| `qty_at_price(px) -> i64` | Total quantity (sum) at a specific price, excluding tombstones |
| `total_len() -> usize` | All orders in book minus tombstones |
| `contains(id) -> bool` | True if order is live (in index and not canceled) |
| `iter_levels_best_first()` | Iterator of `(price, total_qty)` from best to worst; used to build market depth snapshots |
| `get_price_levels()` | Raw `&BTreeMap` reference; used by `Exchange` to count levels |

---

## Invariants

1. Every order in `levels` that is not in `canceled` must be in `index`.
2. An order in `canceled` will be absent from `index` (cancel removes from index first).
3. Empty price levels are removed from `levels` — no ghost entries.
4. Partially-filled makers retain their queue position via `push_front`.

---
*See also: [[03 - Matching Algorithm]], [[01 - Data Structures]]*
