Bond pricing is based on the **present value** of all future cash flows. A bond's price is the sum of the present value of its coupon payments and the present value of its par value at maturity.

## Core Principle

**A bond is worth the present value of its future cash flows**, discounted at the appropriate interest rate.

```
Bond Value = PV(Coupons) + PV(Par Value)
```

## The Bond Pricing Formula

### Annual Coupon Convention:

```
Bond Value = Σ(t=1 to T) [Coupon / (1+r)^t] + [Par Value / (1+r)^T]

Where:
- Coupon = Annual coupon payment ($)
- r = Discount rate (required yield)
- T = Years to maturity
- t = Time period
```

### Semi-Annual Coupon Convention (Most Common):

```
Bond Value = Σ(t=1 to 2T) [C/2 / (1+r/2)^t] + [Par / (1+r/2)^2T]

Where:
- C = Annual coupon payment
- r = Annual discount rate (YTM)
- T = Years to maturity
- Payments occur twice per year
```

## Step-by-Step Bond Pricing

### Example: Price a 3-Year Bond

**Given**:
- Par value: $1,000
- Coupon rate: 6% (annual)
- Payments: Semi-annual
- Required yield (YTM): 8%
- Time to maturity: 3 years

**Step 1**: Calculate semi-annual coupon
```
Annual coupon = $1,000 × 6% = $60
Semi-annual coupon = $60 / 2 = $30
```

**Step 2**: Identify variables
```
Number of periods = 3 years × 2 = 6 periods
Discount rate per period = 8% / 2 = 4% = 0.04
```

**Step 3**: Calculate PV of coupons
```
PV(Coupons) = $30/(1.04)^1 + $30/(1.04)^2 + $30/(1.04)^3 
            + $30/(1.04)^4 + $30/(1.04)^5 + $30/(1.04)^6

PV(Coupons) = $28.85 + $27.74 + $26.67 + $25.64 + $24.65 + $23.70
             = $157.25
```

**Step 4**: Calculate PV of par value
```
PV(Par) = $1,000 / (1.04)^6
        = $1,000 / 1.2653
        = $790.31
```

**Step 5**: Sum to get bond price
```
Bond Price = $157.25 + $790.31 = $947.56
```

**Interpretation**: This bond sells at a **discount** (price < par) because the coupon rate (6%) is less than the required yield (8%).

## Using Financial Calculator

Most bond pricing uses financial calculators or Excel:

### Calculator Inputs:
```
N = 6 (number of periods)
I/Y = 4 (yield per period, in %)
PMT = 30 (coupon payment per period)
FV = 1000 (par value)
Compute PV = -947.56
```

Note: PV is negative (cash outflow to buy bond)

### Excel Formula:
```
=PV(rate, nper, pmt, fv, type)
=PV(0.04, 6, 30, 1000, 0)
= -$947.56
```

## The Discount Rate (r)

**What is the discount rate?**
- The required rate of return
- Reflects the riskiness of the bond
- Determined by the market
- Also called the yield or YTM (when solving for price)

**Factors affecting the discount rate**:
1. **Risk-free rate**: Base rate (Treasury yield)
2. **Credit risk**: Higher risk → higher rate
3. **Liquidity**: Less liquid → higher rate
4. **Maturity**: Longer maturity → typically higher rate
5. **Call risk**: Callable bonds → higher rate

```
Required Yield = Risk-Free Rate + Risk Premiums

Example:
10-year Treasury yield: 3%
Credit spread: 2%
Required yield: 5%
```

## Price Sensitivity to Rates

Bond prices move **inversely** with interest rates:

### Example: 10-Year Bond, 8% Coupon, $1,000 Par

| Interest Rate | Bond Price | % of Par |
|---------------|------------|----------|
| 6% | $1,148.77 | 114.9% |
| 7% | $1,071.06 | 107.1% |
| 8% | $1,000.00 | 100.0% |
| 9% | $935.82 | 93.6% |
| 10% | $877.11 | 87.7% |

**Key insight**: Rate ↑ 1% → Price ↓ ; Rate ↓ 1% → Price ↑

See: [[Bond Price and Interest Rate Relationship]]

## Premium, Par, and Discount Pricing

### Price = Par (Trading at 100)
```
When: Coupon Rate = Required Yield

Example:
Coupon rate = 8%, YTM = 8%
Price = $1,000 (exactly par)
```

### Price > Par (Trading at Premium)
```
When: Coupon Rate > Required Yield

Example:
Coupon rate = 10%, YTM = 8%
Price > $1,000 (premium)
Investor pays extra for higher coupons
```

### Price < Par (Trading at Discount)
```
When: Coupon Rate < Required Yield

Example:
Coupon rate = 6%, YTM = 8%
Price < $1,000 (discount)
Lower coupons require lower purchase price
```

See: [[Premium, Par, and Discount Bonds]]

## Price Behavior Over Time

Assuming interest rates stay constant, bond prices converge to par as maturity approaches:

### Premium Bond:
```
Price starts above $1,000
Price gradually falls toward $1,000
Price = $1,000 at maturity
```

### Discount Bond:
```
Price starts below $1,000
Price gradually rises toward $1,000
Price = $1,000 at maturity
```

### Par Bond:
```
Price stays at $1,000 (assuming no rate changes)
```

## Factors Affecting Bond Prices

### 1. Interest Rates (Primary Factor)
- Rates ↑ → Prices ↓ (inverse relationship)
- Long-term bonds more sensitive than short-term

### 2. Time to Maturity
- Longer maturity → greater price volatility
- Short-term bonds less affected by rate changes

### 3. Coupon Rate
- Higher coupon → less price sensitive
- Zero-coupon bonds most price sensitive

### 4. Credit Quality
- Credit downgrade → price falls
- Credit upgrade → price rises

### 5. Call Provisions
- Callable bonds trade at lower prices (less valuable to investor)
- Call risk increases when rates fall

## Example: Maturity Effect on Price Sensitivity

**Given**: 8% coupon bonds, all trading to yield 8% (at par)

When interest rates rise to 10%:

| Time to Maturity | New Price | % Change |
|------------------|-----------|----------|
| 1 year | $981.41 | -1.9% |
| 10 years | $875.38 | -12.5% |
| 20 years | $828.41 | -17.2% |
| 30 years | $810.71 | -18.9% |

**Key insight**: 30-year bond fell 18.9%, but 1-year bond only fell 1.9%!

## Clean Price vs Dirty Price

### Clean Price (Quoted Price)
- Does NOT include accrued interest
- What you see in price quotes
- Used for comparison purposes

### Dirty Price (Invoice Price)
- Includes accrued interest
- What you actually pay
- Clean price + Accrued interest

```
Example:
Clean price: $1,020
Accrued interest: $15
Dirty price (what you pay): $1,035
```

See: [[Accrued Interest]]

## Bond Pricing Between Coupon Dates

When buying between coupon dates, must account for:

1. **Time until next coupon**: Affects present value calculation
2. **Accrued interest**: Compensate seller for earned interest

**Modified formula**:
```
Price = [PV of remaining cash flows] - [Accrued Interest]
```

This ensures clean price doesn't jump on coupon payment dates.

## Pricing Special Bonds

### Zero-Coupon Bonds
Only one cash flow (par at maturity):
```
Price = Par Value / (1+r)^T

Example:
Par = $1,000, T = 10 years, r = 8%
Price = $1,000 / (1.08)^10 = $463.19
```

### Perpetual Bonds (Consols)
Pay coupons forever, never mature:
```
Price = Annual Coupon / r

Example:
Annual coupon = $60, r = 8%
Price = $60 / 0.08 = $750
```

## Common Pricing Scenarios

### Scenario 1: New Issue at Par
```
Company issues bond:
Coupon rate set to current market rate
Price = Par = $1,000
```

### Scenario 2: Rates Rise After Issuance
```
Bond issued at 6% coupon
Market rates rise to 8%
Bond price falls below par
Investors demand 8% return → pay less than $1,000
```

### Scenario 3: Approaching Maturity
```
Bond initially at $950 (discount)
As maturity nears, price → $1,000
"Pull to par" effect
```

## Relationship Summary

```
Interest Rates ↑  →  Bond Prices ↓
Interest Rates ↓  →  Bond Prices ↑

Longer Maturity  →  Greater Price Sensitivity
Higher Coupon    →  Less Price Sensitivity

Coupon > YTM  →  Premium Bond (Price > Par)
Coupon = YTM  →  Par Bond (Price = Par)
Coupon < YTM  →  Discount Bond (Price < Par)
```

## Related Concepts

- [[Yield to Maturity (YTM)]] - The discount rate when solving for yield
- [[Bond Price and Interest Rate Relationship]] - Why prices and rates move inversely
- [[Premium, Par, and Discount Bonds]] - Price-yield relationships
- [[Accrued Interest]] - Adjusting prices between coupon dates
- [[Interest Rate Risk]] - Risk from price volatility

---

*Bond prices are present values - understanding this is key to fixed-income investing*