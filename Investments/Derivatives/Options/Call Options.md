# Call Options

A **call option** gives the owner the **right to BUY** an underlying asset at a specified strike price. Call options are used when you expect the asset price to rise.

## Definition

**Call Option**: A contract giving the buyer:
- The **right** (not obligation)
- To **BUY** the underlying asset
- At the **strike price**
- Until or on the **expiration date**

## How Call Options Work

### Basic Structure

```
Call Option Seller ←──────────────→ Call Option Buyer
  (Underwriter)      Right to BUY stock      (Owner)
                    ← Premium Payment
```

**Buyer perspective**:
- Pays premium upfront
- Can exercise (buy stock at strike) if profitable
- Can let option expire if unprofitable

**Seller perspective**:
- Receives premium upfront
- Must sell stock at strike price if buyer exercises
- Hopes option expires worthless

## When to Use Call Options

### Bullish on Stock
You believe stock price will rise:

```
Example: Microsoft (MSFT)
Current price: $101.51
Your view: Will rise to $110+

Strategy: Buy call option
- Strike: $100
- Premium: $3.81
- Expiration: Feb 8, 2019
```

### Instead of Buying Stock
Control more shares with same capital:

```
$10,000 to invest:

Option 1: Buy stock directly
- 200 shares at $50/share = $10,000

Option 2: Buy call options
- Premium: $4/share = $400/contract
- $10,000 / $400 = 25 contracts
- Control: 25 × 100 = 2,500 shares

Result: 12.5x more exposure with options!
```

## Exercise Decision

### You Exercise When: Market Price > Strike Price

**Example: Rann Corporation Call**
```
Strike price: $50
Premium paid: $4
Expiration: 3 months

Scenario 1: Stock at $55 at expiration
- Exercise: Buy at $50, immediately worth $55
- Gain per share: $5
- Net profit: $5 - $4 = $1 per share
- Decision: EXERCISE ✓

Scenario 2: Stock at $45 at expiration
- Exercise: Buy at $50, only worth $45? No!
- Would lose an extra $5 per share
- Decision: LET EXPIRE (lose only $4 premium)
```

## Profit and Loss Analysis

### Call Option Buyer (Owner)

**Payoff at expiration** (before premium):
```
Payoff = max(Market Price - Strike Price, 0) × 100 × Contracts
```

**Net Profit** (after premium):
```
Net Profit = (max(Market Price - Strike Price, 0) - Premium) × 100 × Contracts
```

### Example Calculation: NVDA Call

You buy 10 call option contracts on NVDA:
- Strike price: $185
- Premium: $3.40 per share
- Initial investment: $3.40 × 100 × 10 = $3,400

**Scenario A: NVDA at $200 at expiration**
```
Payoff = ($200 - $185) × 100 × 10
       = $15 × 1,000
       = $15,000

Net Profit = $15,000 - $3,400
           = $11,600

Return = $11,600 / $3,400 = 341%
```

**Scenario B: NVDA at $180 at expiration**
```
Payoff = max($180 - $185, 0) × 100 × 10
       = $0

Net Profit = $0 - $3,400
           = -$3,400

Return = -100% (lose entire premium)
```

**Scenario C: NVDA at $188.40 at expiration**
```
Payoff = ($188.40 - $185) × 100 × 10
       = $3.40 × 1,000
       = $3,400

Net Profit = $3,400 - $3,400
           = $0

Breakeven point: Strike + Premium = $185 + $3.40 = $188.40
```

## Call Option Buyer: Risk and Reward

### Limited Losses ✓
```
Maximum Loss = Premium × 100 × Contracts

Example:
Premium = $3.40
Contracts = 10
Max Loss = $3.40 × 100 × 10 = $3,400

Even if stock goes to $0, you lose only $3,400!
```

**Why limited?**
- You have the **right**, not obligation
- Can choose NOT to exercise
- Walk away losing only the premium

### Unlimited Gains ✓
```
Gains = (Market Price - Strike Price - Premium) × 100 × Contracts

As Market Price → ∞, Gains → ∞

Example scenarios:
Stock at $200: Gain $11,600
Stock at $250: Gain $61,600
Stock at $300: Gain $111,600
No ceiling!
```

**Why unlimited?**
- Stock price has no theoretical ceiling
- Your strike price is fixed
- The higher the stock goes, the more you gain

## Call Option Seller (Writer): Risk and Reward

### Limited Gains
```
Maximum Gain = Premium × 100 × Contracts

Example:
Premium received = $3.40
Contracts = 10
Max Gain = $3.40 × 100 × 10 = $3,400

Best case: Option expires worthless, keep entire premium
```

### Unlimited Losses ⚠️
```
Loss = (Market Price - Strike Price - Premium) × 100 × Contracts

As Market Price → ∞, Loss → ∞

Example: Sold 10 calls, strike $185, premium $3.40
Stock at $200: Loss = ($200 - $185 - $3.40) × 1,000 = -$11,600
Stock at $250: Loss = ($250 - $185 - $3.40) × 1,000 = -$61,600
Stock at $300: Loss = ($300 - $185 - $3.40) × 1,000 = -$111,600
```

**Why unlimited?**
- Seller has **obligation** to sell at strike price
- If buyer exercises, seller MUST deliver stock
- If seller doesn't own stock (naked call), must buy at market price
- No ceiling on stock price = no ceiling on loss

## Profit Diagrams

### Call Buyer Profit Profile

```
Profit
  ^
  |          /
  |         /
  |        /
  |-------/------------ Breakeven (Strike + Premium)
  |      /|
  |     / |
  |    /  |
  |___/___|____________> Stock Price
      ^   ^
   Strike Premium
      |
   Max Loss
```

**Key points**:
- Breakeven: Strike + Premium
- Max loss: Premium (horizontal line below)
- Unlimited upside (diagonal line)

### Call Seller Profit Profile

```
Profit
  ^
  |________
  |        \
  |         \
  |          \--------- Breakeven (Strike + Premium)
  |           \
  |            \
  |             \
  |______________\____> Stock Price
      ^
   Strike
      |
   Max Gain
```

**Key points**:
- Max gain: Premium (horizontal line above)
- Breakeven: Strike + Premium
- Unlimited downside (diagonal line)

## Real Example: Microsoft Call Option

From the lecture slides (January 2, 2019):

```
Microsoft Stock: $101.51

Call Option Details:
- Expiration: February 8, 2019
- Strike: $95
- Premium: $9.50

Analysis:
Current price ($101.51) > Strike ($95)
This is "in the money" by $6.51

Intrinsic Value = $101.51 - $95 = $6.51
Time Value = $9.50 - $6.51 = $2.99

Total Premium = Intrinsic Value + Time Value
```

**If held to expiration and MSFT at $105**:
```
Payoff = ($105 - $95) × 100 = $1,000
Cost = $9.50 × 100 = $950
Net Profit = $1,000 - $950 = $50
Return = $50 / $950 = 5.3%
```

## Strategies Using Call Options

### Long Call (Basic)
- Buy call option
- Profit if stock rises above strike + premium
- Limited risk, unlimited reward

### Covered Call
- Own 100 shares of stock
- Sell 1 call option against it
- Collect premium income
- Willing to sell stock if called away

### Call Spread
- Buy call at lower strike
- Sell call at higher strike
- Reduce cost, limit both risk and reward

## Factors Affecting Call Option Prices

### 1. Stock Price
Higher stock price → Higher call premium
```
Stock at $100 vs $110
Call with strike $105 worth more when stock is $110
```

### 2. Strike Price
Lower strike → Higher call premium
```
Stock at $100:
Call strike $90 > Call strike $100 > Call strike $110
```

### 3. Time to Expiration
More time → Higher call premium
```
Same strike, stock price:
6 months to expiration > 3 months > 1 month
```

### 4. Volatility
Higher volatility → Higher call premium
```
Stable stock: Lower premiums
Volatile stock: Higher premiums
```

### 5. Interest Rates
Higher rates → Slightly higher call premium

### 6. Dividends
Higher dividends → Lower call premium

## Moneyness

### In the Money (ITM)
```
Market Price > Strike Price

Example:
Stock at $200, Strike $185
In the money by $15
Has intrinsic value
```

### At the Money (ATM)
```
Market Price ≈ Strike Price

Example:
Stock at $185, Strike $185
No intrinsic value, only time value
```

### Out of the Money (OTM)
```
Market Price < Strike Price

Example:
Stock at $180, Strike $185
Out of the money
No intrinsic value, only time value
```

## When Call Options Expire Worthless

Option expires worthless when:
```
Market Price ≤ Strike Price at expiration
```

**Example**:
```
Call option:
Strike: $50
Premium: $4

At expiration, stock at $48
- Would you pay $50 for something worth $48? No!
- Option expires worthless
- Buyer loses $4 premium
- Seller keeps $4 premium
```

## Common Mistakes

### 1. Confusing Right with Obligation
❌ "I must exercise my call option"
✓ "I can choose to exercise if profitable"

### 2. Forgetting Contract Size
❌ "Premium is $3.40, so I pay $3.40"
✓ "Premium is $3.40/share, I pay $340 per contract"

### 3. Exercising Early (Usually Wrong)
❌ Exercising American call before expiration
✓ Selling the option retains time value

### 4. Ignoring Breakeven
❌ "Stock above strike, I profit!"
✓ "Stock must be above strike + premium to profit"

## Related Concepts

- [[Options|Options Overview]] - General option concepts
- [[Put Options]] - Right to sell (opposite of calls)
- [[Option Terminology]] - Key terms and definitions
- [[Option Payoff Calculations]] - Formulas and examples

---

*The right to buy - limited risk for buyers, unlimited potential, but unlimited risk for sellers*