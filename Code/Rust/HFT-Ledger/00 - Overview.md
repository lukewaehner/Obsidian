# HFT-Ledger: Project Overview

## What It Is

A simulated high-frequency trading exchange written in Rust. It models a real exchange matching engine — not a toy — using production-grade patterns: price-time priority, lazy cancellation, nanosecond timestamps, and sub-microsecond order matching.

## Workspace Layout

```
hftx/
├── orderbook/          # Core matching engine (pure library, no I/O)
│   ├── src/types.rs        → Order, Trade, Side, OrderId
│   ├── src/price_levels.rs → PriceLevels (the internal data structure)
│   ├── src/lib.rs          → OrderBook (the public API)
│   └── benches/            → Criterion benchmarks
│
├── exchange-service/   # HTTP + WebSocket server wrapping the engine
│   ├── src/exchange.rs     → Exchange (multi-symbol manager)
│   ├── src/websocket.rs    → WS handlers (trade/depth/order/latency streams)
│   ├── src/bot_driver.rs   → Server-side market simulator
│   ├── src/types.rs        → Wire types (request/response structs)
│   └── src/main.rs         → Axum router, AppState
│
└── cli/                # Thin CLI wrapper (unused in main flows)
```

## Dependency Chain

```
orderbook (no deps)
    ↑
exchange-service (axum, dashmap, tokio, rmp-serde, uuid)
```

The `orderbook` crate has zero async or I/O dependencies — it is a pure synchronous data structure library. All async, networking, and concurrency lives in `exchange-service`.

## Key Design Choices

| Decision                    | What                                                        | Why                                                        |
| --------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| Integer ticks               | Prices are `i64`, not `f64`                                 | Eliminates floating-point rounding in financial math       |
| Nanosecond timestamps       | `ts_ns: u128`                                               | True time-priority ordering within a price level           |
| Lazy cancellation           | Canceled orders are marked, removed on next `pop_best`      | O(1) cancel cost, deferred cleanup                         |
| DashMap + RwLock            | Symbol map is lock-free; each book has its own async RwLock | Parallel cross-symbol order flow                           |
| MessagePack on order stream | Binary frames for order submission WS                       | Lower serialization overhead at high tick rates            |
| XorShift RNG                | Custom PRNG in bot_driver                                   | No external dependency, deterministic seed from wall clock |

## Port

The exchange service binds on `0.0.0.0:8080`.

---
*See also: [[01 - Data Structures]], [[02 - Order Book Engine]], [[03 - Matching Algorithm]], [[04 - Exchange Service]], [[05 - API and WebSocket Layer]], [[06 - Bot Driver]], [[07 - Wire Formats]], [[08 - Key Workflows]]*
