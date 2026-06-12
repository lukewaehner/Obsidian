# Matching Algorithm

*`orderbook/src/lib.rs` — `OrderBook::submit_limit`*

---

## Overview

Price-time priority (a.k.a. FIFO matching). When a new order arrives:
1. Try to match it against the **opposite side** of the book at the best available price.
2. If fully filled, done — return trades.
3. If partially filled or not filled at all, **rest** the remainder in the book.

---

## `submit_limit` — Step by Step

```rust
pub fn submit_limit(&mut self, mut taker: Order) -> Vec<Trade>
```

The `taker` is passed by value and mutated (qty decrements with each fill). Returns a `Vec<Trade>` — empty means the order rested without any immediate fill.

### Bid path (buyer is the taker)

```
while taker.qty > 0:
    best_ask = asks.best_price()   → None → break (no sellers)
    if taker.px_ticks < best_ask → break (bid too low, no cross)

    maker = asks.pop_best()        → removes best ask from book
    fill = min(taker.qty, maker.qty)
    taker.qty -= fill
    maker.qty -= fill
    emit Trade { px = best_ask, qty = fill }  ← trade at MAKER'S price

    if maker.qty > 0:
        asks.push_front(maker)     ← partial maker goes back to front

if taker.qty > 0:
    bids.push(taker)               ← remainder rests
```

### Ask path (seller is the taker)

Mirror image: checks `bids.best_price()`, breaks if `taker.px_ticks > best_bid`, pops bids, and rests remainder on ask side.

---

## Crossing Condition

| Taker side | Crosses when |
|---|---|
| Bid (buy) | `taker.px_ticks >= best_ask` |
| Ask (sell) | `taker.px_ticks <= best_bid` |

If no cross exists at entry, the order goes straight to rest. If the book is empty on the opposite side, same result.

---

## Partial Fill Handling

Say there's a resting ask for 50 shares and the incoming bid wants 70:
1. `fill = min(70, 50) = 50` → emit trade for 50
2. `maker.qty = 0` → don't push back
3. `taker.qty = 20` → loop again, find next best ask
4. Next ask has 40 shares → `fill = min(20, 40) = 20` → emit trade for 20
5. `maker.qty = 20` → `asks.push_front(maker)` — the maker retains queue position
6. `taker.qty = 0` → loop exits, nothing rests

Result: 2 trades generated, partial maker still live.

---

## Why Maker's Price?

Standard exchange rule: the **resting** order set the terms first. The incoming taker is *taking* what's available. If a maker posted at 100 and a bid arrives at 105, the trade executes at 100 — the maker gets filled at their limit, the taker gets a better price than they asked for.

---

## What This Doesn't Do (Yet)

- No **market orders** — `OrderKind::Market` exists in the enum but there's no `submit_market` method. Market orders would skip the price-crossing check.
- No **IOC/FOK** — `TimeInForce` variants exist but the matching loop doesn't enforce them. IOC would cancel the remainder instead of resting; FOK would cancel the whole order if not fully filled immediately.
- No **cancel-on-fill** — currently if a maker partially fills, it re-rests automatically.
- No **self-trade prevention** — two orders from the same counterparty can match each other.

---
*See also: [[02 - Order Book Engine]], [[04 - Exchange Service]]*
