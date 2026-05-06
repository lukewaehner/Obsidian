A comprehensive reference for key terms and concepts used in options trading. Understanding this terminology is essential for navigating options markets.

## Contract Fundamentals

### Option Contract
An agreement giving the owner the right (not obligation) to buy or sell an asset at a specified price within a set time period.

### Underlying Asset
The security on which the option is based:
- **Stocks**: AAPL, NVDA, MSFT, etc.
- **Indices**: S&P 500, NASDAQ 100
- **ETFs**: SPY, QQQ
- **Commodities**: Gold, oil
- **Currencies**: EUR/USD

### Strike Price (Exercise Price)
The specified price at which the option holder can buy ([[Call Options|call]]) or sell ([[Put Options|put]]) the underlying asset.

```
Example:
NVDA call option, strike $185
→ Right to BUY NVDA at $185 per share

NVDA put option, strike $185
→ Right to SELL NVDA at $185 per share
```

### Option Premium
The price paid to purchase an option contract:
- Paid by **buyer** to **seller**
- Non-refundable (like insurance premium)
- Quoted per share
- Total cost = Premium × 100 × Contracts

```
Example:
Premium quoted: $3.40 per share
Buy 5 contracts: $3.40 × 100 × 5 = $1,700
```

### Expiration Date
The last day the option can be exercised:
- After this date, option becomes worthless
- Options lose value as expiration approaches (time decay)

```
Example formats:
- Jan 31, 2026
- 2026-01-31
- Jan26 (shorthand)
```

### Contract Size
Standard quantity per contract:
- **Stock options**: 100 shares per contract
- Always remember: 1 contract ≠ 1 share!

```
Common mistake:
Premium = $5
Think: I'll pay $5 ✗
Reality: I'll pay $500 ✓ ($5 × 100)
```

## Option Types

### Call Option
The right to **BUY** the underlying asset at the strike price.

**Buyer**: Bullish, wants stock to rise
**Seller**: Neutral to bearish, willing to sell stock

See: [[Call Options]]

### Put Option
The right to **SELL** the underlying asset at the strike price.

**Buyer**: Bearish, wants stock to fall
**Seller**: Neutral to bullish, willing to buy stock

See: [[Put Options]]

### American Option
Can be exercised **anytime** up to and including expiration date.
- Most US stock options are American
- More flexibility for holder

### European Option
Can only be exercised **on** the expiration date, not before.
- Common for index options
- Some cash-settled options

## Market Participants

### Option Buyer (Holder/Owner)
- Pays premium
- Has the **right** to exercise
- Risk limited to premium paid
- Makes the exercise decision

Also called: Long position, Holder

### Option Seller (Writer/Underwriter)
- Receives premium
- Has the **obligation** to perform if exercised
- Risk can be substantial
- No control over exercise

Also called: Short position, Writer

### Covered vs Naked

**Covered Writer**: Owns the underlying asset
```
Covered call: Own 100 shares, sell 1 call
- If called away, deliver owned shares
- Lower risk
```

**Naked Writer**: Doesn't own underlying
```
Naked call: Sell call without owning stock
- If called away, must buy stock at market
- Unlimited risk ⚠
```

## Exercise and Settlement

### Exercise
Using the option's right to buy (call) or sell (put) at the strike price.

```
Call exercise:
- Buyer exercises → Buy shares at strike
- Seller must deliver shares

Put exercise:
- Buyer exercises → Sell shares at strike
- Seller must buy shares
```

### Assignment
When an option seller is obligated to fulfill the contract because the buyer exercised.

```
You sold 10 calls, strike $100
Stock rises to $120
Buyer exercises
→ You are "assigned"
→ Must sell 1,000 shares at $100
```

### Physical Settlement
Actual shares change hands upon exercise.
- Stock options typically settle physically
- Receive/deliver actual shares

### Cash Settlement
Only cash difference is exchanged.
- Index options typically cash settled
- No shares delivered
- Convenient for indices (can't deliver S&P 500)

## Moneyness

### In the Money (ITM)
Option has intrinsic value:

**Calls**: Market Price > Strike Price
```
Stock at $200, call strike $185
In the money by $15
```

**Puts**: Market Price < Strike Price
```
Stock at $140, put strike $200
In the money by $60
```

### At the Money (ATM)
Stock price approximately equal to strike price:

```
Stock at $185, strike $185
No intrinsic value
Only time value remains
```

### Out of the Money (OTM)
Option has no intrinsic value:

**Calls**: Market Price < Strike Price
```
Stock at $180, call strike $185
Out of the money by $5
```

**Puts**: Market Price > Strike Price
```
Stock at $210, put strike $200
Out of the money by $10
```

## Value Components

### Intrinsic Value
The value if exercised immediately:

**Call intrinsic value**:
```
max(Market Price - Strike Price, 0)
```

**Put intrinsic value**:
```
max(Strike Price - Market Price, 0)
```

```
Example:
Stock at $105, call strike $100
Intrinsic value = $105 - $100 = $5
```

### Time Value (Extrinsic Value)
The portion of premium beyond intrinsic value:

```
Time Value = Premium - Intrinsic Value
```

```
Example:
Premium = $8
Intrinsic = $5
Time value = $8 - $5 = $3

This $3 represents:
- Possibility of further gains
- Time until expiration
- Volatility
```

### Time Decay (Theta)
The rate at which option value decreases as expiration approaches:
- All options experience time decay
- Accelerates in final month
- At expiration, only intrinsic value remains

```
90 days out: Time value = $5
60 days out: Time value = $4
30 days out: Time value = $2
7 days out: Time value = $0.50
Expiration: Time value = $0
```

## Pricing Factors

### The Greeks

**Delta (Δ)**: Price sensitivity to stock movement
```
Delta = 0.70
Stock moves $1 → Option moves $0.70
```

**Gamma (Γ)**: Rate of delta change

**Theta (Θ)**: Time decay rate
```
Theta = -$0.05 per day
Each day, option loses $5 in value
```

**Vega (V)**: Sensitivity to volatility changes
```
Vega = $0.15
Volatility ↑ 1% → Option price ↑ $0.15
```

**Rho (ρ)**: Sensitivity to interest rate changes

### Implied Volatility (IV)
Market's expectation of future volatility:
- Higher IV = Higher premiums
- Lower IV = Lower premiums
- Changes based on market conditions

```
Example:
Normal times: IV = 20%
Earnings announcement: IV = 50%
→ Options become more expensive
```

## Trading Terms

### Bid Price
The highest price a buyer is willing to pay:
```
Bid: $3.35
Someone will buy at $3.35
```

### Ask Price
The lowest price a seller is willing to accept:
```
Ask: $3.45
Someone will sell at $3.45
```

### Bid-Ask Spread
Difference between bid and ask:
```
Bid: $3.35
Ask: $3.45
Spread: $0.10

Narrow spread = High liquidity ✓
Wide spread = Low liquidity ✗
```

### Last Price
The price of the most recent trade:
```
Last: $3.40
Previous trade executed at $3.40
```

### Volume
Number of contracts traded today:
```
Volume: 128,595
128,595 contracts traded today
```

### Open Interest
Total number of outstanding contracts:
```
Open Interest: 107,506
107,506 contracts currently open
Not closed or expired
```

High open interest = High liquidity

## Contract Naming Convention

### Format
```
[SYMBOL][YY][MM][DD][C/P][STRIKE PRICE]

Example: NVDA251003C00185000
- NVDA: Stock symbol
- 25: Year (2025)
- 10: Month (October)
- 03: Day (3rd)
- C: Call (P for put)
- 00185000: Strike $185.00
```

### Reading Option Chains

```
Contract Name: NVDA251003C00185000
Strike: 185
Last Price: 3.40
Bid: 3.35
Ask: 3.45
Volume: 44,371
Open Interest: 69,247
Implied Volatility: 43.26%

Interpretation:
- Oct 3, 2025 expiration
- Call option
- Strike $185
- Premium $3.40
- Active trading (high volume)
- Good liquidity (tight spread)
```

## Position Terminology

### Long Position
Bought/own the option:
- **Long call**: Bought call option
- **Long put**: Bought put option

### Short Position
Sold/wrote the option:
- **Short call**: Sold call option
- **Short put**: Sold put option

### Opening Transaction
Creating a new position:
```
Buy to open: Create long position
Sell to open: Create short position
```

### Closing Transaction
Exiting an existing position:
```
Sell to close: Close long position
Buy to close: Close short position
```

## Breakeven Points

### Call Option Breakeven
```
Breakeven = Strike Price + Premium
```

```
Example:
Strike $185, Premium $3.40
Breakeven = $185 + $3.40 = $188.40

Need stock above $188.40 to profit
```

### Put Option Breakeven
```
Breakeven = Strike Price - Premium
```

```
Example:
Strike $200, Premium $20
Breakeven = $200 - $20 = $180

Need stock below $180 to profit
```

## Important Distinctions

### Right vs Obligation
- **Buyer**: Has the right (can choose)
- **Seller**: Has the obligation (must perform)

### Premium vs Payoff
- **Premium**: What you pay to buy option
- **Payoff**: What you receive if exercised
- **Net Profit**: Payoff - Premium

### Intrinsic vs Time Value
- **Intrinsic**: Value if exercised now
- **Time**: Value from possibility of future gains
- **Premium**: Intrinsic + Time

### American vs European
- **American**: Exercise anytime
- **European**: Exercise only at expiration

## Quick Reference Table

| Term | Definition | Example |
|------|------------|---------|
| **Strike** | Exercise price | $185 |
| **Premium** | Option price | $3.40 |
| **Contract** | 100 shares | 1 contract = 100 shares |
| **ITM** | Has intrinsic value | Call: Stock > Strike |
| **OTM** | No intrinsic value | Call: Stock < Strike |
| **Breakeven** | No profit/loss point | Strike ± Premium |
| **Assignment** | Seller must perform | Buyer exercises |
| **Time decay** | Value loss over time | Theta |

## Related Concepts

- [[Options|Options Overview]] - Main options hub
- [[Call Options]] - Right to buy
- [[Put Options]] - Right to sell
- [[Option Payoff Calculations]] - Profit/loss formulas

---

*Master these terms to navigate options markets confidently*