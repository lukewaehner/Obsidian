# Wire Formats

*`exchange-service/src/types.rs`*

---

## Serialization Formats

| Channel | Format | Reason |
|---|---|---|
| REST endpoints | JSON | Universal client compatibility |
| Trade stream WS | JSON | Easy to consume in browser |
| Depth stream WS | JSON | Same |
| Latency stream WS | JSON | Same |
| **Order stream WS** | **MessagePack (binary)** | Lower serialization overhead at high tick rates |

Only the order-submission WebSocket is binary. The comment in `websocket.rs` is explicit: *"This is the ONLY binary (MessagePack) WebSocket on the service."*

---

## Tagged Enums (Polymorphic Messages)

Rust's `#[serde(tag = "type")]` produces a `type` discriminator field in JSON:

### `WebSocketMessage` (JSON, all read-only streams)
```json
{ "type": "trade",   "symbol": "AAPL", "trade": { ... }, "timestamp": 1234 }
{ "type": "depth",   "symbol": "AAPL", "best_bid": 100, "best_ask": 101, ... }
{ "type": "latency", "latency_ns": 840, "filled": true, "ts_ms": 1234 }
{ "type": "error",   "message": "..." }
{ "type": "ping",    "timestamp": 1234 }
{ "type": "pong",    "timestamp": 1234 }
```

### `OrderStreamMessage` (MessagePack, order-submission WS)
Same shape but binary-encoded:
```
{ "type": "batch",  "seq": 42, "orders": [...] }   ← client → server
{ "type": "result", "seq": 42, "results": [...], "engine_ns": 1200 }  ← server → client
{ "type": "error",  "seq": 42, "message": "..." }
{ "type": "ping",   "timestamp": 1234 }
{ "type": "pong",   "timestamp": 1234 }
```

---

## Sequence Numbers (`seq`)

The `seq` field in `OrderStreamRequest` / `OrderStreamResponse` is client-assigned. The server echoes it back. This lets the client correlate responses to the specific tick that generated them without maintaining any server-side session state. Sequence numbers are not validated or deduplicated — purely for client-side bookkeeping.

---

## Latency Measurement Semantics

`BatchOrderResult.latency_ns` = time inside `submit_limit` for that single order only (wall clock using `Instant`). This excludes:
- Network time
- Deserialization
- Lock acquisition wait time
- Trade broadcast time

`BatchSubmitResponse.engine_ns` = total wall time inside the handler for the full batch (lock acquisition through broadcast). Covers everything the server did for that HTTP request.

`LatencySample.latency_ns` (from bot driver) = same per-order `submit_limit` timing, but here it can approach true "tick-to-trade" latency because there's no HTTP layer at all.

---

## Price Representation in Wire Formats

All prices on the wire are `i64` integer ticks — the same unit used inside the engine. There is no conversion layer. Clients must know the tick size to display human-readable prices (not currently defined in the API — convention is 1 tick = $0.01 for display purposes based on the seed price of 18,750 ticks ≈ $187.50).

---
*See also: [[05 - API and WebSocket Layer]], [[08 - Key Workflows]]*
