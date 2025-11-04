# Put Options

A **put option** gives the owner the **right to SELL** an underlying asset at a specified strike price. Put options are used when you expect the asset price to fall, or to protect against downside risk.

## Definition

**Put Option**: A contract giving the buyer:
- The **right** (not obligation)
- To **SELL** the underlying asset
- At the **strike price**
- Until or on the **expiration date**

## How Put Options Work

### Basic Structure

```
Put Option Seller ←──────────────→ Put Option Buyer
  (Underwriter)      Right to SELL stock      (Owner)
                    ← Premium Payment
```

**Buyer perspective**:
- Pays premium upfront
- Can exercise (sell stock at strike) if profitable
- Can let option expire if unprofitable

**Seller perspective**:
- Receives premium upfront
- Must buy stock at strike price if buyer exercises
- Hopes option expires worthless

## When to Use Put Options

### Bearish on Stock
You believe stock price will fall:

```
Example: Corneria Inc.
Current price: $200
Your view: Will fall below $180

Strategy: Buy put option
- Strike: $200
- Premium: $20
- Can sell at $200 even if price crashes
```

### Portfolio Insurance (Protective Put)
Protect existing stock holdings:

```
Own 1,000 shares at $100/share
Worried about market crash

Buy 10 put contracts:
- Strike: $95
- Premium: $3
- Cost: $3 × 100 × 10 = $3,000

Protection: If stock falls below $95, puts gain value
Insurance cost: $3,000
```

### Speculation on Decline
Profit from falling prices without shorting:

```
Think stock will crash from $150 to $100

Buy put options instead of shorting stock:
- Less capital required
- Limited risk (just premium)
- No risk of unlimited losses from short squeeze
```

## Exercise Decision

### You Exercise When: Market Price < Strike Price

**Example: Corneria Put**
```
Strike price: $200
Premium paid: $20
Current market price: $140

Exercise Decision:
- Can sell at $200 (strike) when market is $140
- Gain per share from exercise: $200 - $140 = $60
- Net profit: $60 - $20 = $40 per share
- Decision: EXERCISE ✓
```

```
Strike price: $200
Premium paid: $20
Current market price: $210

Exercise Decision:
- Would sell at $200 when market is $210? No!
- Better to sell in market at $210
- Decision: LET EXPIRE (lose only $20 premium)
```

## Profit and Loss Analysis

### Put Option Buyer (Owner)

**Payoff at expiration** (before premium):
```
Payoff = max(Strike Price - Market Price, 0) × 100 × Contracts
```

**Net Profit** (after premium):
```
Net Profit = (max(Strike Price - Market Price, 0) - Premium) × 100 × Contracts
```

### Example Calculation: Corneria Put

You buy 10 put option contracts on Corneria:
- Strike price: $200
- Premium: $20 per share
- Initial investment: $20 × 100 × 10 = $20,000

**Scenario A: Corneria at $140 at expiration**
```
Payoff = ($200 - $140) × 100 × 10
       = $60 × 1,000
       = $60,000

Net Profit = $60,000 - $20,000
           = $40,000

Return = $40,000 / $20,000 = 200%
```

**Scenario B: Corneria at $210 at expiration**
```
Payoff = max($200 - $210, 0) × 100 × 10
       = $0

Net Profit = $0 - $20,000
           = -$20,000

Return = -100% (lose entire premium)
```

**Scenario C: Corneria at $180 at expiration**
```
Payoff = ($200 - $180) × 100 × 10
       = $20 × 1,000
       = $20,000

Net Profit = $20,000 - $20,000
           = $0

Breakeven point: Strike - Premium = $200 - $20 = $180
```

**Scenario D: Corneria at $185 at expiration**
```
Payoff = ($200 - $185) × 100 × 10
       = $15 × 1,000
       = $15,000

Net Profit = $15,000 - $20,000
           = -$5,000

Loss but better than letting expire worthless!
Still exercise to recover some premium.
```

## Put Option Buyer: Risk and Reward

### Limited Losses ✓
```
Maximum Loss = Premium × 100 × Contracts

Example:
Premium = $20
Contracts = 10
Max Loss = $20 × 100 × 10 = $20,000

Even if stock goes to infinity, lose only $20,000!
```

**Why limited?**
- You have the **right**, not obligation
- Can choose NOT to exercise
- Walk away losing only the premium

### Limited Gains (but substantial)
```
Maximum Gain occurs when stock → $0

Max Gain = (Strike Price - $0 - Premium) × 100 × Contracts
         = (Strike - Premium) × 100 × Contracts

Example:
Strike = $200, Premium = $20, Contracts = 10
Max Gain = ($200 - $20) × 100 × 10
         = $180 × 1,000
         = $180,000
```

**Why limited?**
- Stock price cannot go below $0
- Maximum profit when stock becomes worthless
- Cap at (Strike - Premium) per share

## Put Option Seller (Writer): Risk and Reward

### Limited Gains
```
Maximum Gain = Premium × 100 × Contracts

Example:
Premium received = $20
Contracts = 10
Max Gain = $20 × 100 × 10 = $20,000

Best case: Option expires worthless, keep entire premium
```

### Limited Losses (but can be large) ⚠️
```
Maximum Loss occurs when stock → $0

Max Loss = (Strike Price - $0 - Premium) × 100 × Contracts
         = (Strike - Premium) × 100 × Contracts

Example: Sold 10 puts, strike $200, premium $20
If stock → $0:
Loss = ($200 - $0 - $20) × 1,000
     = $180 × 1,000
     = $180,000
```

**Why limited but still dangerous?**
- Seller has **obligation** to buy at strike price
- Worst case: Buy worthless stock at strike price
- Can lose nearly the entire strike price (minus premium)

## Profit Diagrams

### Put Buyer Profit Profile

```
Profit
  ^
  |\
  | \
  |  \
  |   \
  |    \________ Breakeven (Strike - Premium)
  |            
  |             \
  |______________\____> Stock Price
      ^          ^
   Max Gain    Strike
   (at $0)       |
              Max Loss
```

**Key points**:
- Max gain when stock → $0
- Breakeven: Strike - Premium
- Max loss: Premium (right side)

### Put Seller Profit Profile

```
Profit
  ^
  |              /
  |             /
  |            /
  |___________/_______ Breakeven (Strike - Premium)
  |          /
  |         /
  |        /
  |_______/_________> Stock Price
      ^   ^
   Max    Strike
   Loss
```

**Key points**:
- Max gain: Premium (right side)
- Breakeven: Strike - Premium
- Max loss when stock → $0 (left side)

## Comparison: Put Buyer vs Put Seller

| Feature | Put Buyer | Put Seller |
|---------|-----------|------------|
| **Pays/Receives** | Pays premium | Receives premium |
| **Market view** | Bearish | Bullish |
| **Max gain** | Strike - Premium | Premium |
| **Max loss** | Premium | Strike - Premium |
| **Breakeven** | Strike - Premium | Strike - Premium |
| **Risk** | Limited | Large (but capped) |
| **Decision control** | Choose to exercise | No control |

## Real Example: From Lecture

Microsoft Put Option (January 2, 2019):
```
Microsoft Stock: $101.51

Put Option Details:
- Expiration: February 8, 2019
- Strike: $105
- Premium: $6.35

Analysis:
Current price ($101.51) < Strike ($105)
This is "in the money" by $3.49

Intrinsic Value = $105 - $101.51 = $3.49
Time Value = $6.35 - $3.49 = $2.86

If held to expiration and MSFT at $95:
Payoff = ($105 - $95) × 100 = $1,000
Cost = $6.35 × 100 = $635
Net Profit = $1,000 - $635 = $365
Return = $365 / $635 = 57.5%
```

## Strategies Using Put Options

### Long Put (Basic)
- Buy put option
- Profit if stock falls below strike - premium
- Limited risk, substantial reward

### Protective Put (Portfolio Insurance)
- Own 100 shares of stock
- Buy 1 put option
- Protect against downside
- Like buying insurance

### Cash-Secured Put
- Sell put option
- Hold cash equal to strike × 100
- Willing to buy stock at strike
- Collect premium income

### Put Spread
- Buy put at higher strike
- Sell put at lower strike
- Reduce cost, limit both risk and reward

## Protective Put: Portfolio Insurance

### Example

You own 1,000 shares of NVDA at $187:
```
Current value: $187,000

Buy 10 put contracts:
- Strike: $175
- Premium: $5
- Cost: $5 × 100 × 10 = $5,000

Scenarios at expiration:

Stock at $150 (crash):
- Stock loss: ($187 - $150) × 1,000 = -$37,000
- Put gain: ($175 - $150) × 1,000 = +$25,000
- Premium: -$5,000
- Net loss: -$17,000
- Without puts: -$37,000 ✗

Stock at $200 (rise):
- Stock gain: ($200 - $187) × 1,000 = +$13,000
- Put loss: -$5,000
- Net gain: +$8,000
- Without puts: +$13,000 (better, but protected downside)
```

**Trade-off**: Pay premium (insurance cost) for downside protection

## Moneyness for Puts

### In the Money (ITM)
```
Market Price < Strike Price

Example:
Stock at $140, Strike $200
In the money by $60
Has intrinsic value
```

### At the Money (ATM)
```
Market Price ≈ Strike Price

Example:
Stock at $200, Strike $200
No intrinsic value, only time value
```

### Out of the Money (OTM)
```
Market Price > Strike Price

Example:
Stock at $210, Strike $200
Out of the money
No intrinsic value, only time value
```

## When Put Options Expire Worthless

Put expires worthless when:
```
Market Price ≥ Strike Price at expiration
```

**Example**:
```
Put option:
Strike: $200
Premium: $20

At expiration, stock at $210
- Would you sell at $200 something worth $210? No!
- Option expires worthless
- Buyer loses $20 premium
- Seller keeps $20 premium
```

## Factors Affecting Put Option Prices

### 1. Stock Price
Lower stock price → Higher put premium
```
Stock at $90 vs $100
Put with strike $95 worth more when stock is $90
```

### 2. Strike Price
Higher strike → Higher put premium
```
Stock at $100:
Put strike $110 > Put strike $100 > Put strike $90
```

### 3. Time to Expiration
More time → Higher put premium
```
Same strike, stock price:
6 months to expiration > 3 months > 1 month
```

### 4. Volatility
Higher volatility → Higher put premium
```
Stable stock: Lower premiums
Volatile stock: Higher premiums
```

### 5. Interest Rates
Higher rates → Slightly lower put premium

### 6. Dividends
Higher dividends → Higher put premium

## Puts vs Short Selling

### Buying Puts vs Shorting Stock

| Feature | Buy Put | Short Stock |
|---------|---------|-------------|
| **Capital required** | Premium only | Full stock value (margin) |
| **Max loss** | Premium | Unlimited |
| **Max gain** | Strike - Premium | Full stock value |
| **Time limit** | Yes (expiration) | No |
| **Margin calls** | No | Yes |
| **Borrowing required** | No | Yes (borrow shares) |

**Put advantages**:
- Limited loss (just premium)
- No margin calls
- No short squeeze risk
- Less capital required

**Short advantages**:
- No time decay
- No expiration
- Can hold indefinitely

## Common Mistakes

### 1. Confusing Calls and Puts
❌ "I think stock will fall, so I'll buy calls"
✓ "I think stock will fall, so I'll buy puts"

### 2. Not Exercising Profitable Puts
❌ Put is in the money, but let it expire
✓ Exercise or sell the put to capture value

### 3. Forgetting Breakeven
❌ "Stock below strike, I profit!"
✓ "Stock must be below strike - premium to profit"

### 4. Selling Naked Puts Without Cash
❌ Sell puts without ability to buy stock
✓ Cash-secured puts: Have cash to buy if assigned

## Related Concepts

- [[Options|Options Overview]] - General option concepts
- [[Call Options]] - Right to buy (opposite of puts)
- [[Option Terminology]] - Key terms and definitions
- [[Option Payoff Calculations]] - Formulas and examples

---

*The right to sell - protection against falling prices, or speculation on declines with limited risk*