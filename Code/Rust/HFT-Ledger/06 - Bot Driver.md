# Bot Driver (Server-Side Market Simulator)

*`exchange-service/src/bot_driver.rs`*

---

## Purpose

Generates synthetic market activity directly inside the server process — no HTTP roundtrip. Useful when you want the latency histogram to reflect pure engine time (not network + serialize + deserialize).

Bypasses the HTTP layer entirely: calls `exchange.submit_order_batch()` directly on the `Arc<Exchange>`.

---

## `BotDriver` Struct

```rust
pub struct BotDriver {
    exchange:   Arc<Exchange>,
    trade_tx:   broadcast::Sender<TradeEvent>,
    latency_tx: broadcast::Sender<LatencySample>,
    drivers:    Arc<Mutex<HashMap<String, DriverHandle>>>,
}
```

`drivers` is a `HashMap<symbol → DriverHandle>`. Each entry represents one running tokio task for that symbol.

`BotDriver` is `Clone` because `Arc`/`broadcast::Sender` are all cheap to clone. It's passed into `AppState` and cloned per-request.

---

## `DriverHandle`

```rust
struct DriverHandle {
    config:    BotConfig,
    cancel_tx: watch::Sender<bool>,
}
```

`cancel_tx` is a `tokio::sync::watch` channel. The running task holds the receiver side. When `stop()` is called, `cancel_tx.send(true)` signals the task to exit on its next `tokio::select!` iteration.

---

## `BotConfig`

```rust
pub struct BotConfig {
    pub symbol:     String,
    pub makers:     u32,   // maker orders to generate per tick
    pub takers:     u32,   // taker orders to generate per tick
    pub aggression: u32,   // 0–100
    pub tick_ms:    u64,   // interval between order batches
}
```

`aggression` controls two things:
- **Maker spread**: higher aggression → tighter spread (makers post closer to mid)
- **Taker crossing probability**: higher aggression → more takers actually cross the spread

---

## `run_driver` — The Tick Loop

```rust
async fn run_driver(exchange, trade_tx, latency_tx, config, cancel_rx)
```

Every `tick_ms` milliseconds:

### 1. Sample the current market mid-price
```
(best_bid, best_ask) = exchange.get_best_prices(symbol)
reference_mid = (best_bid + best_ask) / 2   (or SEED_MID_TICKS = 18_750 if empty)
```

The mid-price anchors all generated orders — makers post around it, takers target it.

### 2. Generate maker orders
For each of `config.makers`:
- Half-spread = `8.0 - aggression*6.0 + rand*5.0` (decreases with aggression)
- Randomly choose Bid or Ask side
- Price = `mid ± offset` (random offset within the half-spread)
- Qty = 10–90 (random)

Maker orders are designed to **rest in the book** — they're priced away from the opposite best so they don't cross immediately.

### 3. Generate taker orders
For each of `config.takers`:
- `will_cross = rand < 0.35 + aggression * 0.55` (35%–90% chance depending on aggression)
- If crossing: price is set **at or through the opposite best** (bid above best ask, ask below best bid)
- If not crossing: price equals the current best on the same side (joins the queue)
- Qty = 5–55 (random)

### 4. Submit the entire batch
```
exchange.submit_order_batch(symbol, all_orders_this_tick)
```
One write-lock acquisition for the full tick.

### 5. Broadcast results
```
for (trades, latency_ns) in results:
    for trade in trades:
        trade_tx.send(TradeEvent { ... })
    latency_tx.send(LatencySample { latency_ns, filled, ts_ms })
```

---

## `XorShiftRng`

```rust
struct XorShiftRng(u64);
```

A tiny custom PRNG. No external crate needed.

```rust
fn next_u64(&mut self) -> u64 {
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    self.0 = x; x
}
fn next_f64(&mut self) -> f64 {
    (self.next_u64() >> 11) as f64 / (1u64 << 53) as f64  // uniform [0, 1)
}
```

Seeded from `SystemTime::now().as_nanos() XOR 0xDEAD_BEEF_CAFE_BABE`. The XOR ensures the seed is never zero (which would produce all-zero outputs forever from XorShift).

---

## Start / Stop Flow

```
POST /sim/start { symbol, makers, takers, aggression, tick_ms }
    → BotDriver::start(config)
        → if existing driver for symbol: send cancel, remove
        → tokio::spawn(run_driver(...))
        → store DriverHandle in drivers map

POST /sim/stop { symbol }
    → BotDriver::stop(symbol)
        → remove from map, send cancel_tx.send(true)
        → task sees changed watch value, breaks loop
```

`start()` is idempotent — starting while one is already running replaces it cleanly.

---
*See also: [[04 - Exchange Service]], [[05 - API and WebSocket Layer]], [[08 - Key Workflows]]*
