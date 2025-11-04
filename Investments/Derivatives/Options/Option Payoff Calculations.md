# Option Payoff Calculations

Formulas and step-by-step examples for calculating option profits and losses. Understanding these calculations is essential for evaluating option strategies.

## Key Principles

### 1. Buyer Pays Premium, Seller Receives Premium
```
At purchase:
Buyer: -$Premium × 100 × Contracts
Seller: +$Premium × 100 × Contracts
```

### 2. Buyer Has Right, Seller Has Obligation
```
Buyer: Can choose whether to exercise
Seller: Must perform if buyer exercises
```

### 3. Exercise Only When Profitable
```
Calls: Exercise when Market Price > Strike Price
Puts: Exercise when Market Price < Strike Price
```

### 4. One Contract = 100 Shares
```
Always multiply by 100 for actual cash amounts!
Premium of $5 = $500 per contract
```

## [[Call Options|Call Option]] Formulas

### Call Buyer (Long Call)

**Payoff at Expiration** (before considering premium):
```
Payoff = max(Market Price - Strike Price, 0) × 100 × Contracts
```

**Net Profit** (after premium cost):
```
Net Profit = (max(Market Price - Strike Price, 0) - Premium) × 100 × Contracts
```

**Alternative form**:
```
If Market Price > Strike Price:
    Net Profit = (Market Price - Strike Price - Premium) × 100 × Contracts
    
If Market Price ≤ Strike Price:
    Net Profit = -Premium × 100 × Contracts
```

**Percentage Return**:
```
Return = Net Profit / Initial Investment × 100%

Initial Investment = Premium × 100 × Contracts
```

**Breakeven**:
```
Breakeven Price = Strike Price + Premium
```

### Call Seller (Short Call)

**Net Profit** (seller's perspective is opposite of buyer):
```
Net Profit = -(max(Market Price - Strike Price, 0) - Premium) × 100 × Contracts
```

**Simplified**:
```
If Market Price > Strike Price:
    Net Profit = (Premium - (Market Price - Strike Price)) × 100 × Contracts
    
If Market Price ≤ Strike Price:
    Net Profit = Premium × 100 × Contracts
```

**Maximum Gain**:
```
Max Gain = Premium × 100 × Contracts
```

**Maximum Loss**:
```
Max Loss = Unlimited (as stock price can rise indefinitely)
```

## [[Put Options|Put Option]] Formulas

### Put Buyer (Long Put)

**Payoff at Expiration** (before premium):
```
Payoff = max(Strike Price - Market Price, 0) × 100 × Contracts
```

**Net Profit** (after premium cost):
```
Net Profit = (max(Strike Price - Market Price, 0) - Premium) × 100 × Contracts
```

**Alternative form**:
```
If Market Price < Strike Price:
    Net Profit = (Strike Price - Market Price - Premium) × 100 × Contracts
    
If Market Price ≥ Strike Price:
    Net Profit = -Premium × 100 × Contracts
```

**Percentage Return**:
```
Return = Net Profit / Initial Investment × 100%

Initial Investment = Premium × 100 × Contracts
```

**Breakeven**:
```
Breakeven Price = Strike Price - Premium
```

**Maximum Gain**:
```
Max Gain = (Strike Price - $0 - Premium) × 100 × Contracts
         = (Strike Price - Premium) × 100 × Contracts
```

### Put Seller (Short Put)

**Net Profit** (seller's perspective):
```
Net Profit = -(max(Strike Price - Market Price, 0) - Premium) × 100 × Contracts
```

**Simplified**:
```
If Market Price < Strike Price:
    Net Profit = (Premium - (Strike Price - Market Price)) × 100 × Contracts
    
If Market Price ≥ Strike Price:
    Net Profit = Premium × 100 × Contracts
```

**Maximum Gain**:
```
Max Gain = Premium × 100 × Contracts
```

**Maximum Loss**:
```
Max Loss = (Strike Price - $0 - Premium) × 100 × Contracts
         = (Strike Price - Premium) × 100 × Contracts
```

## Worked Examples

### Example 1: Call Option - Rann Corporation

**Setup**:
```
You have $10,000 to invest
Rann stock: $50/share
Call option: Strike $50, Premium $4, 3 months to expiration

How many contracts can you buy?
Cost per contract = $4 × 100 = $400
Number of contracts = $10,000 / $400 = 25 contracts
Shares controlled = 25 × 100 = 2,500 shares
```

**Scenario A: Stock at $55 at expiration**
```
Payoff = ($55 - $50) × 100 × 25
       = $5 × 2,500
       = $12,500

Net Profit = $12,500 - $10,000
           = $2,500

Return = $2,500 / $10,000 = 25%
```

**Scenario B: Stock at $45 at expiration**
```
Payoff = max($45 - $50, 0) × 100 × 25
       = $0

Net Profit = $0 - $10,000
           = -$10,000

Return = -100% (total loss)
```

**Scenario C: Stock at $54 (break even)**
```
Breakeven = $50 + $4 = $54

Payoff = ($54 - $50) × 100 × 25
       = $4 × 2,500
       = $10,000

Net Profit = $10,000 - $10,000 = $0
```

**Comparison to buying stock directly**:
```
Stock purchase: $10,000 / $50 = 200 shares

At $55:
Stock profit = ($55 - $50) × 200 = $1,000
Option profit = $2,500
Option wins! 2.5x better

At $45:
Stock loss = ($45 - $50) × 200 = -$1,000
Option loss = -$10,000
Stock better (smaller loss)
```

### Example 2: Put Option - Corneria Inc.

**Setup**:
```
Purchased 10 put option contracts
Strike price: $200
Premium: $20 per share
Initial investment = $20 × 100 × 10 = $20,000
```

**Scenario A: Stock at $140 at expiration**
```
Payoff = ($200 - $140) × 100 × 10
       = $60 × 1,000
       = $60,000

Net Profit = $60,000 - $20,000
           = $40,000

Return = $40,000 / $20,000 = 200%
```

**Scenario B: Stock at $210 at expiration**
```
Payoff = max($200 - $210, 0) × 100 × 10
       = $0

Net Profit = $0 - $20,000
           = -$20,000

Return = -100%
```

**Scenario C: Stock at $185 at expiration**
```
Payoff = ($200 - $185) × 100 × 10
       = $15 × 1,000
       = $15,000

Net Profit = $15,000 - $20,000
           = -$5,000

Return = -$5,000 / $20,000 = -25%

Note: Still exercise! Recovers $15,000 of the $20,000 premium.
```

**Breakeven**:
```
Breakeven = $200 - $20 = $180

At $180:
Payoff = ($200 - $180) × 1,000 = $20,000
Net Profit = $20,000 - $20,000 = $0
```

### Example 3: NVDA Call Option (From Lecture)

**Setup**:
```
NVDA trading at $187.24
Buy 10 call contracts
Strike: $185
Premium: $3.40
Expiration: October 3, 2025

Initial investment = $3.40 × 100 × 10 = $3,400
```

**Scenario A: NVDA at $200**
```
Payoff = ($200 - $185) × 100 × 10
       = $15 × 1,000
       = $15,000

Net Profit = $15,000 - $3,400
           = $11,600

Return = $11,600 / $3,400 = 341%
```

**Scenario B: NVDA at $180**
```
Payoff = max($180 - $185, 0) × 100 × 10
       = $0

Net Profit = $0 - $3,400
           = -$3,400

Return = -100%
```

**Scenario C: NVDA at $188.40 (breakeven)**
```
Breakeven = $185 + $3.40 = $188.40

Payoff = ($188.40 - $185) × 100 × 10
       = $3.40 × 1,000
       = $3,400

Net Profit = $3,400 - $3,400 = $0
```

**Scenario D: NVDA at $195**
```
Payoff = ($195 - $185) × 100 × 10
       = $10 × 1,000
       = $10,000

Net Profit = $10,000 - $3,400
           = $6,600

Return = $6,600 / $3,400 = 194%
```

### Example 4: Microsoft Options (From Lecture)

**Data from January 2, 2019**:
```
Microsoft stock: $101.51
```

**Call Option**:
```
Expiration: February 8, 2019
Strike: $95
Premium: $9.50

Currently in the money by: $101.51 - $95 = $6.51

If held to expiration and MSFT at $105:
Payoff = ($105 - $95) × 100 = $1,000
Cost = $9.50 × 100 = $950
Net Profit = $1,000 - $950 = $50
Return = $50 / $950 = 5.3%
```

**Put Option**:
```
Expiration: February 8, 2019
Strike: $100
Premium: $2.20

Currently out of the money (stock > strike)

If held to expiration and MSFT at $95:
Payoff = ($100 - $95) × 100 = $500
Cost = $2.20 × 100 = $220
Net Profit = $500 - $220 = $280
Return = $280 / $220 = 127%
```

## Profit/Loss Tables

### Call Buyer (Long Call)

```
Strike: $100, Premium: $5

Stock Price | Payoff | Net Profit | Return
------------|--------|------------|-------
    $90     |   $0   |  -$500     | -100%
    $95     |   $0   |  -$500     | -100%
   $100     |   $0   |  -$500     | -100%
   $105     |  $500  |    $0      |    0%  ← Breakeven
   $110     | $1,000 |  +$500     |  +100%
   $120     | $2,000 | +$1,500    |  +300%
   $130     | $3,000 | +$2,500    |  +500%
```

### Put Buyer (Long Put)

```
Strike: $100, Premium: $5

Stock Price | Payoff | Net Profit | Return
------------|--------|------------|-------
    $70     | $3,000 | +$2,500    | +500%
    $80     | $2,000 | +$1,500    | +300%
    $90     | $1,000 |  +$500     | +100%
    $95     |  $500  |    $0      |    0%  ← Breakeven
   $100     |   $0   |  -$500     | -100%
   $105     |   $0   |  -$500     | -100%
   $110     |   $0   |  -$500     | -100%
```

## Quick Calculation Checklist

When calculating option P&L, always:

### 1. Identify Your Position
```
□ Long call (bought call)
□ Short call (sold call)
□ Long put (bought put)
□ Short put (sold put)
```

### 2. Determine Exercise Decision
```
Calls: Exercise if Market Price > Strike
Puts: Exercise if Market Price < Strike
```

### 3. Calculate Payoff
```
Use max() function:
Calls: max(Market - Strike, 0)
Puts: max(Strike - Market, 0)
```

### 4. Calculate Net Profit
```
Buyer: Payoff - Premium paid
Seller: Premium received - Payoff
```

### 5. Multiply by Contract Size
```
× 100 shares per contract
× Number of contracts
```

### 6. Calculate Return
```
Return = Net Profit / Initial Investment
```

## Common Calculation Mistakes

### Mistake 1: Forgetting to Multiply by 100
```
❌ Premium $5, 1 contract = $5
✓ Premium $5, 1 contract = $500
```

### Mistake 2: Not Using max() Function
```
❌ Call at expiration: Market $90, Strike $100
    Payoff = $90 - $100 = -$10 ✗
    
✓ Payoff = max($90 - $100, 0) = $0
   (You don't exercise, just lose premium)
```

### Mistake 3: Confusing Payoff with Net Profit
```
❌ "Payoff is $1,000, so I made $1,000!"
✓ "Payoff is $1,000, I paid $500 premium,
    so net profit is $500"
```

### Mistake 4: Wrong Breakeven
```
❌ Call breakeven = Strike price
✓ Call breakeven = Strike + Premium

❌ Put breakeven = Strike price
✓ Put breakeven = Strike - Premium
```

### Mistake 5: Forgetting Premium in Max Gain/Loss
```
Put buyer max gain:
❌ Strike price
✓ Strike price - Premium

Call seller max gain:
❌ $0
✓ Premium received
```

## Summary Formulas

### Quick Reference

| Position | Payoff Formula | Net Profit Formula |
|----------|----------------|-------------------|
| **Long Call** | max(S - K, 0) | max(S - K, 0) - P |
| **Short Call** | -max(S - K, 0) | P - max(S - K, 0) |
| **Long Put** | max(K - S, 0) | max(K - S, 0) - P |
| **Short Put** | -max(K - S, 0) | P - max(K - S, 0) |

Where:
- S = Market (Stock) Price
- K = Strike Price  
- P = Premium

Always multiply by: **100 × Number of Contracts**

## Related Concepts

- [[Options|Options Overview]] - Main options hub
- [[Call Options]] - Call option details
- [[Put Options]] - Put option details
- [[Option Terminology]] - Key terms reference

---

*Master these formulas to calculate option profits and losses accurately*