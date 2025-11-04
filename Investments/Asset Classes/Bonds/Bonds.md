# Bonds

**Bonds** are fixed-income securities representing debt obligations. When you buy a bond, you're lending money to the issuer in exchange for periodic interest payments and the return of principal at maturity.

## What is a Bond?

A **straight bond** is an IOU that obligates the issuer to pay the bondholder:
1. A **fixed sum of money** (principal, par value, or face value) at maturity
2. **Constant, periodic interest payments** (coupons) during the bond's life

Bonds are one of the three major asset classes, alongside equities and derivatives.

## Core Bond Concepts

### [[Bond Basics]]
Understanding the fundamental structure:
- Face value (par value)
- Coupon payments
- Maturity date
- Bond issuers (government, corporate, municipal)

### [[Bond Terminology]]
Essential terms for bond investing:
- Coupon rate vs current yield vs YTM
- Clean price vs dirty price
- Investment grade vs junk bonds
- Call provisions and conversion features

## Bond Valuation

### [[Bond Pricing]]
How to value bonds:
- Present value of future cash flows
- PV of coupons + PV of par value
- Discount rate determines price
- Semi-annual coupon conventions

**Key formula**:
```
Bond Value = Σ(Coupon/(1+r)^t) + Par Value/(1+r)^T
```

### [[Yield to Maturity (YTM)]]
The internal rate of return of a bond:
- Discount rate that equates price to PV of cash flows
- Most important yield measure
- Inverse relationship with price

### [[Premium, Par, and Discount Bonds]]
Understanding bond pricing relationships:
- **Premium**: Price > Par, Coupon > YTM
- **Par**: Price = Par, Coupon = YTM  
- **Discount**: Price < Par, Coupon < YTM

## Price-Yield Dynamics

### [[Bond Price and Interest Rate Relationship]]
The fundamental inverse relationship:
- Interest rates ↑ → Bond prices ↓
- Interest rates ↓ → Bond prices ↑
- Longer maturity = greater price sensitivity
- Primary source of bond market risk

```
Key Insight: A 30-year bond is much more sensitive to 
interest rate changes than a 1-year bond
```

### [[Accrued Interest]]
Trading between coupon dates:
- Buyer compensates seller for earned interest
- Invoice price = Flat price + Accrued interest
- Quoted prices are "clean" (exclude accrued interest)

## Special Bond Types

### [[Callable Bonds]]
Bonds the issuer can repurchase:
- Call price and call protection period
- Yield to Call (YTC) instead of YTM
- Premium bonds more likely to be called
- Common when interest rates fall (refinancing)

### [[Convertible Bonds]]
Bonds exchangeable for stock:
- Specified number of shares
- Combines debt and equity features
- Valuable conversion option

### [[Inflation-Protected Bonds (TIPS)]]
Bonds adjusted for inflation:
- Par value increases with CPI
- Real return protection
- Coupon payment grows with par value

### [[Zero-Coupon Bonds]]
Bonds with no periodic coupons:
- Sell at deep discount
- Single payment at maturity
- Higher price volatility

## Bond Risks

### [[Interest Rate Risk]]
Risk from changing interest rates:
- Affects all bonds
- Longer maturity = higher risk
- Can't avoid unless holding to maturity

### [[Default Risk and Credit Ratings]]
Risk that issuer won't pay:
- Credit ratings: AAA to D
- Investment grade vs junk bonds
- Higher default risk = higher yield required
- Yield spreads reflect credit quality

## Types of Bonds by Issuer

### Government Bonds
**U.S. Treasury Securities**:
- T-Bills: < 1 year maturity
- T-Notes: 1-10 year maturity
- T-Bonds: > 10 year maturity
- Considered risk-free (no default risk)
- Benchmark for other bonds

**Municipal Bonds**:
- Issued by state/local governments
- Often tax-exempt
- Lower yields due to tax advantage

### Corporate Bonds
Issued by companies:
- Higher yields than Treasuries
- Credit risk varies by company
- May have call provisions
- Rated by agencies (S&P, Moody's, Fitch)

### Agency Bonds
Government-sponsored enterprises:
- Fannie Mae, Freddie Mac
- Ginnie Mae (explicitly backed by gov't)
- Federal Home Loan Banks
- Farm Credit agencies

### International Bonds
**Foreign bonds**: Issued in another country's currency
**Eurobonds**: Issued in currency different from market

## Bond Market Innovations

### Asset-Backed Bonds
- Backed by specific assets (mortgages, auto loans)
- Cash flows from underlying assets pay bondholders
- Securitization process

### Catastrophe Bonds
- Higher yields for taking on disaster risk
- If catastrophe occurs, investors lose principal
- Insurance companies transfer risk

## Yield Measures Comparison

| Yield Type | Formula | Use Case |
|------------|---------|----------|
| **Coupon Rate** | Annual Coupon / Par Value | Fixed at issuance |
| **Current Yield** | Annual Coupon / Market Price | Simple income measure |
| **YTM** | IRR of all cash flows | Most comprehensive |
| **YTC** | IRR to call date | For callable bonds |

### Relationships:
```
Premium bonds: Coupon Rate > Current Yield > YTM
Par bonds:     Coupon Rate = Current Yield = YTM
Discount bonds: Coupon Rate < Current Yield < YTM
```

## Reading Bond Quotes

### Treasury Bond Quote Example (Nov 15, 2019):
```
Maturity    Coupon   Bid      Ask      Change   Asked Yield
30-Jun-21   1.125    99.054   99.060   -0.008   1.714

Interpretation:
- Matures June 30, 2021
- 1.125% coupon rate
- Trading below par (discount bond)
- Yield to maturity: 1.714%
```

### Corporate Bond Quote Example:
```
Issuer: Boeing Co
Symbol: BA4866208
Coupon: 3.250%
Maturity: 02/01/2035
Rating: A (S&P)
Price: 104.242
Yield: 2.900%

Interpretation:
- Investment grade bond
- Trading at premium (price > 100)
- Coupon > Yield (premium bond relationship)
```

## Bond Investment Strategies

### Buy and Hold
- Hold until maturity
- Receive all coupons and par value
- No interest rate risk if held to maturity
- Earn the YTM (assuming no default)

### Active Trading
- Buy and sell before maturity
- Profit from price changes
- Subject to interest rate risk
- Requires market timing

### Laddering
- Buy bonds with staggered maturities
- Reduces reinvestment risk
- Provides regular liquidity

### Barbell Strategy
- Concentrate in short and long maturities
- Skip intermediate maturities
- Balance liquidity and yield

## Tax Considerations

### Taxable Bonds
- Corporate bonds
- Most Treasury securities
- Interest taxed as ordinary income

### Tax-Exempt Bonds
- Municipal bonds
- Interest exempt from federal tax
- Often exempt from state tax (if issued in your state)
- Lower yields but higher after-tax returns for high-income investors

```
Tax-Equivalent Yield = Tax-Exempt Yield / (1 - Tax Rate)

Example:
Municipal bond yields 3%
Your tax rate: 30%
Tax-equivalent yield = 3% / (1 - 0.30) = 4.29%
```

## Connections to Other Topics

### Risk and Return
- [[../Risk & Return/Risk|Fixed Income Risk]] - Interest rate and credit risk
- Lower volatility than stocks
- Negative correlation with equities (sometimes)

### Portfolio Construction
- [[../Investment Process/Investment Process|Asset Allocation]] - Role in diversified portfolios
- Income generation
- Capital preservation

### Derivatives
- [[../Derivatives/Derivatives|Bond Derivatives]] - Bond options and futures
- Interest rate swaps
- Credit default swaps (CDS)

### Valuation
- [[../Valuation Metrics/Valuation Metrics|Present Value]] - Discounting future cash flows
- Time value of money
- Risk-adjusted returns

## Key Formulas Reference

### Bond Pricing (Semi-Annual Coupons):
```
Bond Price = Σ(C/2)/(1+r/2)^(2t) + Par/(1+r/2)^(2T)

Where:
C = Annual coupon payment
r = Annual discount rate (YTM)
T = Years to maturity
t = Period number
```

### Current Yield:
```
Current Yield = Annual Coupon / Bond Price
```

### Accrued Interest:
```
AI = (Annual Coupon/2) × (Days Since Last Payment / Days Between Payments)
```

### Invoice Price:
```
Invoice Price = Quoted Price + Accrued Interest
```

## Important Insights

1. **Inverse price-yield relationship** is fundamental to bond investing
2. **Longer maturity = higher interest rate risk** (price sensitivity)
3. **Credit ratings matter** - higher risk requires higher yield
4. **Holding to maturity eliminates price risk** but not default risk
5. **Callable bonds benefit issuer** when rates fall (refinancing opportunity)
6. **TIPS protect against inflation** but have lower nominal yields
7. **Tax treatment affects returns** especially for high-income investors

## Bond Market Size

The bond market is actually **larger** than the stock market:
- U.S. bond market: ~$50 trillion
- U.S. stock market: ~$40 trillion
- Global bond market: ~$130 trillion

Bonds are crucial for:
- Corporate financing
- Government funding
- Pension fund investments
- Insurance company portfolios

---

*Fixed-income securities providing predictable cash flows and lower volatility than equities*