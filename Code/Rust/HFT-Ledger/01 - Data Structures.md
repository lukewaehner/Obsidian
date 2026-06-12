# Core Data Structures

*Defined in `orderbook/src/types.rs` and `exchange-service/src/types.rs`*

---

## Primitives (orderbook crate)

### `OrderId`
```rust
pub struct OrderId(pub u128);
```
A newtype wrapping `u128`. In practice filled from `uuid::Uuid::new_v4().as_u128()` — globally unique, 128-bit, no coordination needed.

---

### `Side`
```rust
pub enum Side { Bid, Ask }
```
Bid = buy intent. Ask = sell intent. Controls which side of the book an order rests on and which side it matches against.

---

### `TimeInForce` / `OrderKind`
Defined but currently only `Limit` orders flow through the system. `IOC`, `FOK`, and `Market` are reserved for future use.

---

### `Order`
```rust
pub struct Order {
    pub id:      OrderId,
    pub symbol:  String,
    pub side:    Side,
    pub px_ticks: i64,   // price in integer ticks (not dollars)
    pub qty:     i64,    // shares/lots remaining
    pub ts_ns:   u128,   // nanoseconds since UNIX epoch
}
```
`qty` is **mutable during matching** — it decrements as fills happen. `ts_ns` is set at submission time and never changes; it's the tiebreaker for same-price orders (FIFO).

---

### `Trade`
```rust
pub struct Trade {
    pub maker:    OrderId,  // resting order (was already in book)
    pub taker:    OrderId,  // incoming order (just submitted)
    pub symbol:   String,
    pub px_ticks: i64,      // always the maker's price
    pub qty:      i64,      // shares actually exchanged
    pub ts_ns:    u128,     // timestamp of the execution
}
```
Trade price is **always the maker's price** — standard exchange rule. The taker accepts whatever price the resting order was posted at.

---

## Internal Book Structure (orderbook crate)

### `PriceLevels`
```rust
pub struct PriceLevels {
    side:     Side,
    levels:   BTreeMap<i64, VecDeque<Order>>,  // price → FIFO queue
    index:    HashMap<OrderId, i64>,            // id → price (for O(1) cancel lookup)
    canceled: HashSet<OrderId>,                 // lazy tombstone set
}
```

The workhorse of the matching engine. Three collections working together:

| Collection | Purpose | Complexity |
|---|---|---|
| `BTreeMap` | Price-ordered map; asks iterate low→high, bids high→low | O(log n) insert/lookup |
| `VecDeque<Order>` per level | FIFO queue within a price — time priority | O(1) push/pop front |
| `HashMap<OrderId, i64>` | Maps an order id to its price tick; needed to find an order to cancel without scanning | O(1) lookup |
| `HashSet<OrderId>` | Tombstones for lazily canceled orders | O(1) mark/check |

**Why BTreeMap over HashMap for levels?** The matching engine needs the *best* price every tick (minimum for asks, maximum for bids). BTreeMap's `first_key_value()` and `last_key_value()` give that in O(log n) without any extra bookkeeping.

---

## Wire / API Types (exchange-service crate)

### REST request/response types
- `SubmitOrderRequest` → `{side, price, quantity}`
- `SubmitOrderResponse` → `{order_id, status, trades[]}`
- `BatchSubmitRequest` → `{orders[]}` (array of `SubmitOrderRequest`)
- `BatchSubmitResponse` → `{results[], engine_ns}`
- `BatchOrderResult` → `{order_id, filled, trade_count, latency_ns}`

### WebSocket stream types
- `TradeEvent` — a `Trade` + symbol + wall-clock ms timestamp
- `DepthUpdate` — best bid/ask prices + total volume each side
- `LatencySample` — `{latency_ns, filled, ts_ms}` per order from bot driver

### Market snapshot types
- `OrderBookState` — best bid, best ask, bid/ask level counts
- `MarketDepth` — up to N `PriceLevel` entries per side
- `PriceLevel` — `{price, quantity, orders}` (aggregated view)

---
*See also: [[02 - Order Book Engine]], [[07 - Wire Formats]]*
