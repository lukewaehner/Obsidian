# Exchange Service

*`exchange-service/src/exchange.rs`*

---

## `Exchange` Struct

```rust
pub struct Exchange {
    orderbooks: DashMap<String, RwLock<OrderBook>>,
}
```

Two layers of concurrency:

| Layer | Type | Purpose |
|---|---|---|
| Outer | `DashMap<String, ...>` | Lock-free concurrent HashMap. Multiple threads can look up different symbols simultaneously without contention. |
| Inner | `RwLock<OrderBook>` | Per-symbol async read/write lock. Many readers (market data queries) can proceed in parallel; order submission takes an exclusive write lock. |

This design means: **two orders for AAPL serialize against each other, but an AAPL order and a TSLA order run in parallel.**

`Exchange` is wrapped in `Arc<Exchange>` before being shared across Axum handlers and the bot driver.

---

## Default Symbols

On startup, five books are pre-created: `AAPL`, `TSLA`, `MSFT`, `NVDA`, `GOOGL`. `add_symbol()` exists to add more at runtime.

---

## Method Reference

### `submit_order(symbol, order) → Option<Vec<Trade>>`
Single-order submission. Takes a write lock on the symbol's book, calls `OrderBook::submit_limit`, returns trades. Returns `None` if symbol doesn't exist.

### `submit_order_batch(symbol, orders) → Option<Vec<(Vec<Trade>, u128)>>`
The performance-critical path. Takes **one write lock** for the whole batch, then loops through all orders calling `submit_limit` individually. Measures `Instant::now()` around each `submit_limit` call to record **per-order engine latency in nanoseconds** (the `u128` in the tuple). This is the number the latency histogram displays.

```
lock acquired once
for each order:
    t0 = Instant::now()
    trades = orderbook.submit_limit(order)
    latency_ns = t0.elapsed().as_nanos()
    push (trades, latency_ns)
lock released
```

Amortizes lock acquisition cost across the whole batch — critical for high-tick-rate scenarios.

### `cancel_order(symbol, order_id) → Option<bool>`
Tries to cancel from bids first, then asks. Returns `true` if found on either side.

### `get_market_depth(symbol, levels) → Option<MarketDepth>`
Read lock. Calls `iter_levels_best_first()` on both sides, takes up to `levels` entries, skips zero-qty levels. Returns the full `MarketDepth` struct.

### `get_best_prices(symbol) → Option<(Option<i64>, Option<i64>)>`
Read lock. Returns `(best_bid, best_ask)` — both are `Option<i64>` because a side can be empty.

### `get_total_volume(symbol) → Option<(i64, i64)>`
Read lock. Returns `(bid_order_count, ask_order_count)` using `total_len()` on each side.

### `get_orderbook_state(symbol) → Option<OrderBookState>`
Read lock. Returns a summary: best prices, number of price levels each side, current timestamp.

---

## Why Not a Single Global Lock?

With a single `Mutex<HashMap<String, OrderBook>>`, every order submission for *any* symbol would block every other symbol. The DashMap + per-symbol RwLock means:
- **Cross-symbol parallelism** is automatic — the DashMap shards internally.
- **Read-heavy workloads** (market data polling, depth queries) don't block each other or order submission on *other* symbols.
- Only same-symbol writes serialize, which is necessary for correctness.

---
*See also: [[03 - Matching Algorithm]], [[05 - API and WebSocket Layer]], [[06 - Bot Driver]]*
