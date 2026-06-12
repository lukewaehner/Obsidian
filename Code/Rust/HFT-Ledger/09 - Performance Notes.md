# Performance Notes

---

## Benchmarks (Criterion)

Benchmarks live in `orderbook/benches/orderbook_bench.rs`. Run with `cargo bench` from the `orderbook` directory.

### Benchmark groups

| Group | What it measures |
|---|---|
| `order_submission` | `submit_limit` on 100/1000/10000 non-crossing orders |
| `order_matching` | Crossing order that sweeps 10/100/1000 resting levels |
| `market_data` | `best_bid()` and `best_ask()` on a 1000-order book |
| `price_levels` | `best_price`, `total_len`, `qty_at_price`, `peek_best` |
| `cancellation` | Lazy cancel vs eager `remove` on 100/1000 orders |
| `hft_scenario` | 100 iterations of: post 5 makers, post 5 takers, sweep, query |

---

## Key Performance Properties

### Lock-free symbol routing
DashMap shards internally — looking up a symbol (e.g., "AAPL") to get its `RwLock` doesn't block any other symbol's reads or writes.

### Per-symbol read/write lock
`tokio::sync::RwLock` allows unlimited concurrent readers. Market data queries (depth, best prices, orderbook state) all take read locks and run in parallel. Only order submission and cancellation need write locks.

### Batch amortization
One write-lock acquisition per batch, not per order. At 50ms tick intervals with 8 orders/tick, that's one lock per 50ms covering 8 matching passes — versus 8 separate lock acquisitions if submitted individually.

### Lazy cancellation
`cancel()` is O(1): just a `HashMap::remove` and a `HashSet::insert`. No `VecDeque` traversal. The deferred cleanup in `pop_best` only happens when that price level is actually matched against — so canceled orders in deep-out-of-money levels essentially have zero ongoing cost.

### Integer tick prices
`i64` comparison is a single CPU instruction. No floating-point rounding. `BTreeMap<i64, ...>` ordering is exact.

### `XorShift` RNG in bot driver
~3 instructions per random number, no syscall, no heap allocation. Suitable for generating hundreds of orders per second without the RNG becoming a bottleneck.

### `Instant::now()` latency measurement
Uses `Instant` (monotonic clock) not `SystemTime` for per-order timing. `SystemTime` can go backward (NTP); `Instant` cannot. Per-order timing wraps only `submit_limit`, not lock acquisition — so it measures pure matching engine performance.

---

## Known Bottlenecks / Limitations

1. **No market orders** — all orders go through `submit_limit`, which checks price crossing. Market orders would need to bypass the price check entirely.
2. **String symbol cloning** — every `Order` contains a `String` for symbol. In a production system, this would be an interned integer or a small fixed-size byte array.
3. **`Vec<Trade>` allocation per order** — each `submit_limit` allocates a new `Vec`. For non-crossing orders (common case), this is immediately empty and cheap, but it's still an allocation. Could use a pre-allocated buffer or smallvec.
4. **Broadcast channel lag** — `broadcast::Sender` with capacity 4096 for latency samples. Slow WebSocket consumers can lag and miss samples (caught with `RecvError::Lagged`). No backpressure.
5. **`total_len()` is O(levels)** — it iterates all price levels to sum queue lengths. For deep books, this is expensive. Called on every depth stream tick (10 Hz) for volume reporting.

---
*See also: [[02 - Order Book Engine]], [[04 - Exchange Service]]*
