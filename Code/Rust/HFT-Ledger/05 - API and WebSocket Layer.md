# API & WebSocket Layer

*`exchange-service/src/main.rs` + `exchange-service/src/websocket.rs`*

---

## `AppState`

```rust
pub struct AppState {
    pub exchange:            Arc<Exchange>,
    pub trade_broadcaster:   broadcast::Sender<TradeEvent>,
    pub bot_driver:          BotDriver,
    pub latency_broadcaster: broadcast::Sender<LatencySample>,
}
```

Cloned cheaply into every Axum handler via `State<AppState>`. The two `broadcast::Sender`s are the pub-sub buses for live event streaming. Capacity:
- `trade_broadcaster`: 1000 messages
- `latency_broadcaster`: 4096 messages (higher because the bot driver can send one sample per order per tick)

---

## HTTP Routes

```
GET  /health                              → status JSON
GET  /symbols                             → list of symbol strings
GET  /symbols/:symbol/orderbook           → OrderBookState
GET  /symbols/:symbol/depth?levels=N      → MarketDepth (default 10 levels)
POST /symbols/:symbol/orders              → SubmitOrderResponse
POST /symbols/:symbol/orders/batch        → BatchSubmitResponse
DEL  /symbols/:symbol/orders/:order_id    → cancel confirm JSON

POST /sim/start                           → 202 Accepted
POST /sim/stop                            → {stopped, symbol}
GET  /sim/status                          → SimStatusResponse
```

---

## WebSocket Routes & Protocols

### `/symbols/:symbol/trades/stream` — JSON
Pushes `TradeEvent` objects as `{"type":"trade", ...}` whenever a trade is broadcast on `trade_broadcaster`. Subscribes with `state.trade_broadcaster.subscribe()` and filters by symbol.

### `/symbols/:symbol/depth/stream` — JSON
Polls `get_best_prices()` at **10 Hz** (100ms interval). Sends `DepthUpdate` only when best bid or best ask has changed since last send. Sends an initial snapshot on connect.

### `/symbols/:symbol/orders/stream` — **MessagePack (binary)**
The only binary WebSocket. Clients send `OrderStreamMessage::Batch` frames (MessagePack-encoded), server replies with `OrderStreamMessage::Result`. Each batch frame carries a `seq` number for client-side request/response matching. Internally calls `submit_order_batch`.

### `/sim/latency/stream` — JSON
Subscribes to `latency_broadcaster`. Pushes `LatencySample` frames as `{"type":"latency", latency_ns, filled, ts_ms}`. Used by the frontend histogram. If the channel lags (slow consumer), `RecvError::Lagged` is caught and processing continues — no disconnect.

---

## WebSocket Connection Pattern

All four handlers follow the same structure:

```
split socket into (sender, receiver)
subscribe to relevant broadcast channel
interval for heartbeat (30s)

loop {
    tokio::select! {
        msg = receiver.next()   → handle ping/close/errors
        event = channel.recv()  → forward event to sender
        _ = ping_interval.tick() → send heartbeat ping
    }
}
```

The `tokio::select!` ensures the handler never blocks on one branch while another has work to do. A `send` error on the socket (client disconnected) breaks the loop.

---

## Error Handling

```rust
enum AppError { SymbolNotFound, OrderNotFound, InvalidOrderId }
```

Each variant maps to an HTTP status code and a JSON error body via `IntoResponse`. All route handlers return `Result<impl IntoResponse, AppError>` — clean separation between logic errors and serialization.

---

## CORS

`CorsLayer::permissive()` is applied globally — the frontend (Next.js dev server on a different port) can talk to the exchange service without CORS blocks.

---
*See also: [[04 - Exchange Service]], [[07 - Wire Formats]], [[08 - Key Workflows]]*
