# Key Workflows

End-to-end traces through the system for the most important operations.

---

## 1. Single Order Submission (REST)

```
Client: POST /symbols/AAPL/orders
        { "side": "Bid", "price": 18750, "quantity": 100 }

main.rs:submit_order
  → generate OrderId from uuid v4
  → build Order { id, symbol, side, px_ticks, qty, ts_ns=now_ns }
  → exchange.submit_order("AAPL", order)
      → dashmap.get("AAPL")        ← O(1) lock-free
      → orderbook.write().await    ← exclusive write lock
      → OrderBook::submit_limit(order)
          → match against asks (if bid) or bids (if ask)
          → return Vec<Trade>
  → for each trade: trade_broadcaster.send(TradeEvent)
  → return SubmitOrderResponse { order_id, status, trades }
```

Status is `"rested"` if no trades, `"filled"` if any trades occurred.

---

## 2. Batch Order Submission (REST)

```
Client: POST /symbols/AAPL/orders/batch
        { "orders": [ {side, price, qty}, ... ] }

main.rs:submit_order_batch
  → assign uuid OrderId to each order
  → build Vec<Order>
  → t0 = Instant::now()
  → exchange.submit_order_batch("AAPL", orders)
      → ONE write lock for the whole batch
      → for each order:
            sub_t0 = Instant::now()
            trades = orderbook.submit_limit(order)
            latency_ns = sub_t0.elapsed()
            push (trades, latency_ns)
  → engine_ns = t0.elapsed()
  → broadcast all trades
  → return BatchSubmitResponse { results[], engine_ns }
```

Each `BatchOrderResult` has its own `latency_ns` — the time for just that single order's matching pass.

---

## 3. WebSocket Order Stream (Binary, low-latency path)

```
Client: WS connect → /symbols/AAPL/orders/stream

Client sends MessagePack frame:
    { type: "batch", seq: 1, orders: [...] }

websocket.rs:handle_order_stream
  → rmp_serde::from_slice::<OrderStreamMessage>
  → process_batch("AAPL", state, req)
      → assign OrderIds
      → exchange.submit_order_batch("AAPL", orders)
      → broadcast trades
      → build OrderStreamResponse { seq: 1, results[], engine_ns }
  → rmp_serde::to_vec_named(OrderStreamMessage::Result(...))
  → send binary frame back
```

Client matches response to request via `seq`. Multiple batches can be in-flight; the server processes them sequentially (one per `receiver.next()` iteration).

---

## 4. Server-Side Bot Simulation

```
Client: POST /sim/start
        { symbol: "AAPL", makers: 5, takers: 3, aggression: 60, tick_ms: 50 }

main.rs:sim_start
  → BotDriver::start(config)
      → spawn tokio task: run_driver(...)

[Every 50ms inside the spawned task:]
run_driver tick:
  → exchange.get_best_prices("AAPL")    ← read lock, fast
  → compute reference_mid
  → generate 5 maker orders (priced around mid, won't cross)
  → generate 3 taker orders (some will cross)
  → exchange.submit_order_batch("AAPL", all 8 orders)
  → for each (trades, latency_ns):
        trade_tx.send(TradeEvent)       → trade stream subscribers see it
        latency_tx.send(LatencySample)  → latency stream subscribers see it

Client: WS connect → /sim/latency/stream
  → receives { type: "latency", latency_ns: 840, filled: true, ts_ms: ... }
  → frontend plots in histogram
```

---

## 5. Market Depth Query

```
Client: GET /symbols/AAPL/depth?levels=5

main.rs:get_depth
  → exchange.get_market_depth("AAPL", 5)
      → read lock
      → asks.iter_levels_best_first().take(5)   ← BTreeMap ascending
      → bids.iter_levels_best_first().take(5)   ← BTreeMap descending
      → for each (price, qty): build PriceLevel
  → return MarketDepth { symbol, bids[5], asks[5], timestamp }
```

---

## 6. Order Cancellation

```
Client: DELETE /symbols/AAPL/orders/123456789...

main.rs:cancel_order
  → parse order_id as u128
  → exchange.cancel_order("AAPL", OrderId(id))
      → write lock
      → bids.cancel(order_id)    ← O(1): remove from index, add to canceled set
      → asks.cancel(order_id)    ← same
      → return true if either side found it
```

The order is not immediately removed from the `VecDeque`. It's tombstoned and will be skipped the next time `pop_best` reaches it during matching.

---

## Data Flow Diagram

```
                    ┌─────────────────────────────────────────┐
                    │           exchange-service               │
                    │                                          │
  REST/WS ──────►  │  Axum Router                            │
                    │     ↓                                   │
                    │  AppState                               │
                    │   ├── Arc<Exchange>                     │
                    │   │     └── DashMap<sym, RwLock<OB>>   │
                    │   │                ↓                    │
                    │   │          OrderBook::submit_limit    │
                    │   │                ↓                    │
                    │   │          Vec<Trade>                 │
                    │   │                                     │
                    │   ├── broadcast::Sender<TradeEvent>     │──► WS trade stream
                    │   ├── broadcast::Sender<LatencySample>  │──► WS latency stream
                    │   └── BotDriver                         │
                    │         └── tokio tasks per symbol      │
                    │               (bypasses HTTP)           │
                    └─────────────────────────────────────────┘
```

---
*See also: [[03 - Matching Algorithm]], [[04 - Exchange Service]], [[06 - Bot Driver]]*
