---
tags:
  - rust
  - project
  - trading
  - hft
type: moc
---
# HFTX

High-frequency trading exchange implementation in Rust.

## Overview

A limit order book exchange demonstrating Rust's performance and safety for low-latency financial systems.

## Architecture

```
CLI (reqwest) → Exchange Service (axum) → OrderBook Engine
                      ↓
              WebSocket Streams
```

### Components

- **CLI**: HTTP client for order submission and market queries
- **Exchange Service**: Concurrent order book management with REST + WebSocket APIs
- **OrderBook**: Price-time priority matching engine

## Core Data Structures

### Order Book

```rust
pub struct OrderBook {
    pub bids: PriceLevels,  // Buy orders
    pub asks: PriceLevels,  // Sell orders
}
```

Uses [[Collections|BTreeMap + VecDeque]] for O(log n) price levels with O(1) FIFO within each level.

### Price Levels

```rust
pub struct PriceLevels {
    side: Side,
    levels: BTreeMap<i64, VecDeque<Order>>,
}
```

- **BTreeMap**: Sorted prices, O(log n) best price lookup
- **VecDeque**: FIFO queue per price level, O(1) push/pop

### Domain Types

```rust
pub type OrderId = u64;
pub type Ticks = i64;

#[derive(Copy, Clone, Debug, Eq, PartialEq, Hash)]
pub enum Side { Bid, Ask }

pub struct Order {
    pub id: OrderId,
    pub side: Side,
    pub symbol: String,
    pub px_ticks: Ticks,
    pub qty: i64,
    pub ts_ns: i128,
}
```

## Key Concepts Applied

| Concept | Application |
|---------|-------------|
| [[Borrowing]] | `&self` for queries, `&mut self` for mutations |
| [[Pattern Matching]] | `let-else` for optional best price extraction |
| [[Result & Option]] | `Option<i64>` for empty book, `Result` for validation |
| [[Collections]] | BTreeMap for sorted prices, VecDeque for FIFO |
| [[Derives]] | Copy/Clone/Debug/Eq/Hash on value types |

## Matching Engine

```rust
pub fn submit_limit(&mut self, mut taker: Order) -> Vec<Trade> {
    let mut trades = Vec::new();
    
    match taker.side {
        Side::Bid => {
            while taker.qty > 0 {
                let Some(best_ask) = self.asks.best_price() else {
                    break;
                };
                if taker.px_ticks < best_ask {
                    break;
                }
                // Match against makers...
            }
        }
        Side::Ask => { /* Mirror logic */ }
    }
    
    // Rest remaining quantity
    if taker.qty > 0 {
        self.add(taker);
    }
    
    trades
}
```

## Concurrency

- **DashMap**: Lock-free concurrent HashMap for symbol → OrderBook mapping
- **RwLock**: Per-symbol locking (many readers, exclusive writer)

```rust
type Books = DashMap<String, RwLock<OrderBook>>;
```

## Performance Characteristics

| Operation | Complexity |
|-----------|------------|
| Best price lookup | O(log n) |
| Add order | O(log n) |
| Match order | O(k log n) where k = fills |
| Cancel order | O(1) with index |

## Invariants

```rust
debug_assert!(order.qty > 0);
debug_assert!(order.px_ticks >= 0);
debug_assert!(!order.symbol.is_empty());
```

## Deep Dives

- [[Domain Types]] — `OrderId`, `Ticks`, `Side`, `Order` field-by-field
- [[PriceLevels]] — `BTreeMap` + `VecDeque` choice rationale
- [[Matching Engine]] — `submit_limit` walkthrough with borrow/lifetime notes
- [[Invariants]] — `debug_assert!` checks and protected state
- [[Explanation]] — CLI architecture, async stack, request flow

## Related Notes

### Rust Concepts
- [[Borrowing]] — Ownership in method receivers
- [[Pattern Matching]] — Match expressions and let-else
- [[Result & Option]] — Error handling
- [[Collections]] — BTreeMap, VecDeque, HashMap
- [[Code/Languages/Rust/Modules|Modules]] — Code organization

### External APIs
- [[Rest API]] — HTTP endpoints
- [[WebSockets]] — Real-time streaming

## See Also

- [[Rust]] — Language reference

```folder-overview
id: f080c48c-aada-47ec-bc74-e0413e0cf1fe
folderPath: Code/Rust/HFTX
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="f080c48c-aada-47ec-bc74-e0413e0cf1fe"></span>
- [[Code/Rust/HFTX/Domain Types.md|Domain Types]] <span class="fv-link-list-item"></span>
- [[Code/Rust/HFTX/Explanation.md|Explanation]] <span class="fv-link-list-item"></span>
- [[Code/Rust/HFTX/Invariants.md|Invariants]] <span class="fv-link-list-item"></span>
- [[Code/Rust/HFTX/Matching Engine.md|Matching Engine]] <span class="fv-link-list-item"></span>
- [[Code/Rust/HFTX/PriceLevels.md|PriceLevels]] <span class="fv-link-list-item"></span>
- [[Code/Rust/HFTX/Rest API.md|Rest API]] <span class="fv-link-list-item"></span>
- [[Code/Rust/HFTX/WebSockets.md|WebSockets]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="f080c48c-aada-47ec-bc74-e0413e0cf1fe"></span>
