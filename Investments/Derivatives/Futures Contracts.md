# Futures Contracts

A **futures contract** is an agreement made today regarding the terms of a trade that will take place at a specified future date. Unlike options, futures contracts create an **obligation** to execute the trade.

## Definition

**Futures Contract**: An agreement to buy or sell an asset at a predetermined price on a specific future date.

### Key Characteristics
- **Obligation**: Both parties must execute (unlike options)
- **Standardized**: Exchange-traded with standard terms
- **No upfront payment**: No premium paid today
- **Expiration date**: When delivery must occur
- **Delivery**: Physical or cash settlement

## Types of Futures

### Financial Futures
Contracts on financial instruments:
- **Stock index futures**: S&P 500, NASDAQ 100, Dow Jones
- **Treasury futures**: T-bonds, T-notes, T-bills
- **Currency futures**: EUR/USD, JPY/USD, GBP/USD
- **Interest rate futures**: Eurodollar, SOFR

### Commodity Futures
Contracts on physical goods:
- **Energy**: Crude oil, natural gas, gasoline
- **Agriculture**: Wheat, corn, soybeans, cattle
- **Metals**: Gold, silver, copper
- **Other**: Coffee, cotton, lumber

## How Futures Work

### Basic Example

**Scenario**: Today is January, crude oil trades at $80/barrel

```
Buyer enters futures contract:
- Agrees to BUY 1,000 barrels
- At $85/barrel
- For delivery in March

Seller enters futures contract:
- Agrees to SELL 1,000 barrels
- At $85/barrel
- For delivery in March
```

### Outcome at Expiration (March)

**If market price is $90/barrel:**
- Buyer gains: ($90 - $85) × 1,000 = $5,000 profit
- Seller loses: ($85 - $90) × 1,000 = $5,000 loss
- Buyer can take delivery at $85, immediately worth $90

**If market price is $75/barrel:**
- Buyer loses: ($75 - $85) × 1,000 = $10,000 loss
- Seller gains: ($85 - $75) × 1,000 = $10,000 profit
- Buyer must take delivery at $85, only worth $75

**Critical**: Both parties MUST execute, regardless of outcome!

## Real-World Example: 2020 Oil Futures Crisis

### What Happened

In April 2020, crude oil futures prices went **negative** for the first time in history:
- Contract price: **-$37.63 per barrel**
- Buyers were paying others to take oil

### Why?

1. **COVID-19 pandemic**: Demand collapsed (no travel, no manufacturing)
2. **Storage full**: No place to store physical oil
3. **Futures obligation**: Contract holders HAD to take delivery
4. **Desperate sellers**: Paid others to accept the oil

### The Lesson

This illustrates the **critical difference** between futures and options:
- Futures = **Obligation** (must execute, even if catastrophic)
- Options = **Right** (can walk away, losing only premium)

## Futures vs Options

| Feature | Futures | [[Options/Options\|Options]] |
|---------|---------|---------|
| **Nature** | Obligation to buy/sell | Right to buy/sell |
| **Upfront cost** | None (margin required) | Premium paid |
| **Buyer risk** | Unlimited losses | Loss limited to premium |
| **Seller risk** | Unlimited losses | Varies by option type |
| **Flexibility** | Locked in | Can choose not to execute |
| **Settlement** | Both parties must perform | Only if buyer chooses |

## Uses of Futures

### 1. Hedging

**Airline Example**:
```
Problem: Fuel costs are 30% of operating expenses, oil price volatility is risk

Solution: Buy oil futures
- Lock in fuel price for next 6 months
- If oil rises → futures profit offsets higher fuel costs
- If oil falls → lose on futures, but benefit from cheaper fuel
- Result: Predictable, stable costs
```

**Exporter Example**:
```
Problem: US company will receive €1M in 3 months, EUR/USD could change

Solution: Sell EUR futures at current rate (e.g., 1.10)
- Lock in $1.1M regardless of future exchange rate
- Eliminates currency risk
```

### 2. Speculation

**Bull on crude oil**:
```
Trader thinks oil will rise from $80 to $90

Action: Buy 10 crude oil futures contracts (10,000 barrels)
- Contract price: $80/barrel
- At expiration, oil is $90/barrel
- Profit: ($90 - $80) × 10,000 = $100,000

Risk: If oil falls to $70, loss = $100,000
```

### 3. Arbitrage

Exploiting price differences between markets:
```
If spot price = $80 and futures = $85 (too high):
- Buy oil in spot market at $80
- Sell futures at $85
- Store oil until delivery
- Profit if storage cost < $5/barrel
```

## Contract Specifications

### Example: Crude Oil Futures (NYMEX)

- **Contract size**: 1,000 barrels
- **Price quote**: Dollars per barrel
- **Tick size**: $0.01 per barrel ($10 per contract)
- **Expiration**: Monthly (Jan, Feb, Mar...)
- **Delivery point**: Cushing, Oklahoma
- **Trading hours**: Nearly 24 hours

## Margin Requirements

Unlike options (pay premium upfront), futures use **margin**:

### Initial Margin
Deposit required to open position:
```
Example: Crude oil futures
- Contract value: $80,000 (1,000 barrels × $80)
- Initial margin: ~$8,000 (10%)
- You control $80,000 with $8,000
```

### Maintenance Margin
Minimum balance required:
```
If losses reduce account below maintenance margin:
- Receive margin call
- Must deposit more funds
- Or position is closed
```

### Mark-to-Market
Daily settlement of gains/losses:
```
Day 1: Enter long at $80, margin account = $8,000
Day 2: Price drops to $78
- Loss: ($80 - $78) × 1,000 = $2,000
- New margin: $8,000 - $2,000 = $6,000
- If below maintenance margin → margin call
```

## Risks of Futures

### Unlimited Losses
No cap on potential losses:
```
Long crude oil at $80:
- If price falls to $60 → $20,000 loss per contract
- If price falls to $40 → $40,000 loss per contract
- If price goes negative → catastrophic losses (2020)
```

### Leverage Risk
Small price moves = large P&L:
```
Control $80,000 contract with $8,000 margin
- 10% price drop = 100% loss of margin
- Leverage magnifies both gains and losses
```

### Liquidity Risk
May be difficult to exit position:
- Especially in thinly traded contracts
- Or during market stress (like 2020 oil)

### Delivery Risk
Physical delivery can be problematic:
- Storage costs
- Transportation
- Quality specifications
- As seen in 2020 oil crisis

## Closing a Futures Position

### Before Expiration

**Offsetting transaction**:
```
Originally: Bought 10 March oil futures at $80
To close: Sell 10 March oil futures at current price

If current price is $85:
- Profit: ($85 - $80) × 10,000 = $50,000
- No physical delivery needed
```

### At Expiration

Two options:
1. **Physical delivery**: Actually receive/deliver the commodity
2. **Cash settlement**: Pay/receive cash difference

Most traders close positions before expiration to avoid delivery.

## Futures Markets and Exchanges

### Major Exchanges

- **CME Group** (Chicago): Financial futures, currencies, stock indices
- **NYMEX** (New York): Energy futures (oil, gas)
- **CBOT** (Chicago): Agricultural futures (corn, wheat)
- **ICE** (Atlanta): Energy and agricultural commodities

### Clearinghouse Role

Acts as intermediary:
- Buyer and seller don't transact directly
- Clearinghouse guarantees both sides
- Eliminates counterparty risk
- Requires margin from both parties

## Related Concepts

- [[Options/Options|Options]] - Alternative derivative with no obligation
- [[Options/Call Options|Call Options]] - Right to buy (vs obligation in futures)
- [[Options/Put Options|Put Options]] - Right to sell (vs obligation in futures)
- [[Derivatives|Derivatives Overview]] - Broader category

---

*Contractual obligations to buy or sell at future dates - powerful but risky tools that require careful management*