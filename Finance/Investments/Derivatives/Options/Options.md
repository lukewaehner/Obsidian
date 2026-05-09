**Options** are derivative contracts that give the owner the **right, but not the obligation**, to buy or sell an underlying asset at a specified price within a set time period. This flexibility distinguishes options from [[Futures Contracts|futures contracts]].

## Core Definition

**Option Contract**: An agreement that gives the owner:
- **The right** (not obligation)
- To **buy or sell**
- A **specific asset**
- At a **specified price** (strike price)
- For a **set period of time** (until expiration)

## The Insurance Analogy

Options work like insurance policies:

### Medical Insurance
```
Insurance Company ←──────────────→ Policy Owner
                 Right to make claim
                 ← Premium Payment
```

### Auto Insurance
```
Insurance Company ←──────────────→ Policy Owner
                 Right to fix car
                 ← Premium Payment
```

### Stock Options
```
Option Seller ←──────────────→ Option Buyer
(Underwriter)    Right to buy/sell stock    (Owner)
              ← Premium Payment
```

**Key similarity**: You pay a premium upfront for the **right** to make a claim/exercise, but you're not **obligated** to do so.

## Types of Options

### [[Call Options]]
**The right to BUY** the underlying asset
```
Example: NVDA Call Option
- Strike price: $185
- Premium: $3.40
- Expiration: October 3, 2025
- Right: Buy NVDA at $185 per share
```

### [[Put Options]]
**The right to SELL** the underlying asset
```
Example: Corneria Put Option
- Strike price: $200
- Premium: $20
- Right: Sell Corneria at $200 per share
```

## Key Terminology

### Strike Price (Exercise Price)
The specified price at which you can buy (call) or sell (put) the underlying asset.

### Option Premium
The price paid today to buy the option contract:
- This is the cost of the "right"
- Paid by buyer to seller
- Non-refundable (like insurance premium)

### Expiration Date
When the option contract ends:
- **American options**: Can exercise anytime up to and including expiration
- **European options**: Can only exercise on expiration date

Most stock options in US are American-style.

### Underlying Asset
The asset the option is based on:
- Individual stocks (AAPL, NVDA, MSFT)
- Stock indices (S&P 500, NASDAQ)
- Commodities, currencies, bonds

### Contract Size
Options are standardized:
- **1 contract = 100 shares** of stock
- Premium quoted per share
- Payment is premium × 100

```
Example: Option premium = $3.40
To buy 1 contract: $3.40 × 100 = $340
To buy 10 contracts: $3.40 × 100 × 10 = $3,400
```

## Buyer vs Seller Dynamics

### Option Buyer (Owner/Holder)
```
Pays: Premium (upfront cost)
Gets: Right to exercise
Risk: Limited to premium paid
Decision: Can choose whether to exercise
```

### Option Seller (Writer/Underwriter)
```
Receives: Premium (upfront payment)
Obligation: Must perform if buyer exercises
Risk: Varies (can be substantial)
Decision: No control once sold
```

**Critical asymmetry**: Buyer has flexibility; seller has obligation!

## When to Exercise?

### You will ONLY exercise when it's profitable:

**Call Option** (right to buy):
- Exercise when: Market price > Strike price
- Don't exercise when: Market price < Strike price

**Put Option** (right to sell):
- Exercise when: Market price < Strike price
- Don't exercise when: Market price > Strike price

### Example: NVDA Call
```
You own: Call option, Strike = $215, expires Jan 31, 2026

Scenario 1: NVDA trading at $250
- Exercise! Buy at $215, immediately worth $250
- Gain from exercise: $35 per share

Scenario 2: NVDA trading at $200
- Don't exercise! Buying at $215 makes no sense
- Let option expire worthless
- Loss: Only the premium you paid
```

## Options vs Futures

| Feature | Options | [[Futures Contracts\|Futures]] |
|---------|---------|---------|
| **Obligation** | Right, not obligation | Must execute |
| **Upfront payment** | Pay premium | No payment (margin required) |
| **Buyer risk** | Limited to premium | Unlimited |
| **Flexibility** | Can choose not to exercise | Locked in |
| **Cost** | Premium is certain cost | Profit/loss uncertain |

## Why Use Options?

### 1. Leverage
Control large positions with less capital:
```
Direct stock purchase: $10,000 buys 200 shares at $50
Call options: $10,000 buys options on 2,500 shares
- Premium $4 per share
- $10,000 / $4 = 2,500 shares controlled
- 25x contracts × 100 shares/contract
```

### 2. Limited Risk (for buyers)
Maximum loss is known upfront:
```
Buy call option for $400 (premium)
Worst case: Stock crashes to $0
Your loss: $400 (just the premium)

Compare to stock: Buy 100 shares at $50 = $5,000
Stock crashes: Lose entire $5,000
```

### 3. Hedging
Protect existing positions:
```
Own 1,000 shares of stock, worried about decline
Buy put options to create "insurance"
If stock falls: Put option gains offset stock losses
If stock rises: Lose premium, but stock gains more
```

### 4. Income Generation
Sell options to collect premiums:
```
Own 1,000 shares, willing to sell at higher price
Sell call options, collect premium
If stock doesn't reach strike: Keep premium + stock
If stock rises above strike: Sell stock, keep premium
```

### 5. Speculation
Bet on price movements without owning stock:
```
Think NVDA will surge but don't want to buy stock
Buy call options instead
If correct: Large percentage gains
If wrong: Lose only premium (less than buying stock)
```

## Reading Option Quotes

### Example: NVDA Options (Yahoo Finance)

```
Contract Name: NVDA251003C00185000
Expiration: Oct 3, 2025
Strike: $185
Last Price: $3.40
Bid: $3.35
Ask: $3.45
Volume: 128,595
Open Interest: 107,506
```

**Interpreting**:
- Premium = $3.40 per share = $340 per contract
- To control 100 shares, pay $340
- To control 1,000 shares (10 contracts), pay $3,400

## Option Strategies (Preview)

Options can be combined in sophisticated ways:

### Basic Strategies
- **Long call**: Buy calls (bullish)
- **Long put**: Buy puts (bearish)
- **Covered call**: Own stock + sell calls (income)
- **Protective put**: Own stock + buy puts (insurance)

### Advanced Strategies
- **Spreads**: Buy and sell options at different strikes
- **Straddles**: Buy both call and put (volatility bet)
- **Iron condors**: Multiple options for range-bound markets

See: [[Option Strategies]] (to be created)

## Practical Considerations

### Liquidity
Not all options trade actively:
- Check **volume** and **open interest**
- Wide bid-ask spreads indicate low liquidity
- May be difficult to exit position

### Time Decay
Options lose value as expiration approaches:
- Called "theta decay"
- Accelerates in final month
- Even if stock stays flat, option loses value

### Volatility
Option prices increase with volatility:
- Higher volatility = higher premiums
- **Implied volatility**: Market's expected future volatility
- Important for option pricing

### Early Exercise (American Options)
Usually better to sell option than exercise early:
- Retain time value
- Exception: Deep in-the-money, dividend approaching

## Connections to Other Topics

### Underlying Assets
- [[Stocks]] - Most common underlying
- [[Bonds]] - Bond options exist
- Indices, commodities, currencies

### Risk Management
- [[Portfolio Risk]] - Options for hedging
- Asymmetric risk profiles
- [[Put Options|Protective puts]] as portfolio insurance

### Valuation
- [[Option Payoff Calculations]]
- Black-Scholes formula
- Greeks (Delta, Gamma, Theta, Vega, Rho)

## Summary: Key Differences

### What makes options special:

1. **Right without obligation** - Flexibility to choose
2. **Premium as cost** - Known upfront investment
3. **Limited risk for buyers** - Maximum loss = premium
4. **Leverage** - Control large positions with less capital
5. **Versatility** - Many strategies for different scenarios

### Critical Rules:

1. **As buyer**: You pay premium, you decide whether to exercise
2. **As seller**: You receive premium, you must perform if buyer exercises
3. **1 contract = 100 shares**
4. **Exercise only when profitable** (in-the-money)

---

*The right, but not the obligation - options provide flexibility and leverage in financial markets*

%% Begin Waypoint %%
- [[Call Options]]
- [[Option Payoff Calculations]]
- [[Option Terminology]]
- [[Options]]
- [[Put Options]]

%% End Waypoint %%