
## Information and Stock Prices

How stock prices incorporate and react to new information.

---

## Price Formation in Semi-Strong Markets

In semi-strong form efficient markets, **stock prices change when traders buy and sell** based on their view of future prospects.

**Process**:
1. Traders constantly evaluate company prospects
2. They form expectations about future performance
3. These expectations determine willingness to pay
4. Trading activity moves prices to fair value

**Key Insight**: Future prospects are influenced by **unexpected news announcements**.

---

## Three Possible Market Reactions

Prices can react to unexpected news in three basic ways:

### 1. Efficient Market Reaction

**Characteristics**:
- **Instant reaction** to new information
- Price jumps immediately to new fair value
- No delay, no drift
- This is what EMH predicts

**Graph Pattern**:
```
Price
  |
  |        ┌─────────
  |        │
  |────────┘
  |
  └────────────────→ Time
           ↑
        News announced
```

**Example**:
```
Company announces earnings beat expectations
  → Stock immediately jumps from $50 to $55
  → Price stabilizes at $55
  → No further price changes related to this news
```

### 2. Delayed Reaction and Slow Price Adjustment

**Characteristics**:
- Price initially under-reacts to news
- Gradual adjustment over time
- Post-announcement drift
- **Suggests market inefficiency**

**Graph Pattern**:
```
Price
  |
  |            ┌─────
  |          ╱
  |        ╱
  |      ╱
  |────────
  |
  └────────────────→ Time
           ↑
        News announced
```

**Example**:
```
Company announces positive news
  → Stock rises from $50 to $52 (partial adjustment)
  → Over next few weeks, continues rising to $55
  → Indicates initial under-reaction
```

**Why This Happens**:
- Investors slow to process information
- Behavioral biases (anchoring, conservatism)
- Limited attention
- Institutional constraints

### 3. Overreaction and Correction

**Characteristics**:
- Price initially over-reacts to news
- Subsequent reversal/correction
- Price overshoots then comes back
- **Suggests market inefficiency**

**Graph Pattern**:
```
Price
  |        ╱╲
  |       ╱  ╲
  |      ╱    └─────
  |     │
  |─────┘
  |
  └────────────────→ Time
           ↑
        News announced
```

**Example**:
```
Company announces positive news
  → Stock jumps from $50 to $58 (overreaction)
  → Over next few days, falls back to $55
  → Initial enthusiasm was excessive
```

**Why This Happens**:
- Investor overconfidence
- Herding behavior
- Momentum trading
- Media hype

---

## Visual Summary

![Market Reaction Patterns](IMG-20251201230052501.png)

The three patterns show:
- **Efficient**: Immediate adjustment to fair value
- **Delayed**: Gradual drift toward fair value (under-reaction)
- **Overreaction**: Overshoot followed by reversal

---

## Implications for Trading

### If Markets React Efficiently
- **No trading opportunities** from public news
- By the time you hear news, it's already in the price
- Cannot profit from buying/selling after announcement
- Supports passive investing

### If Markets Under-React (Delayed)
- **Momentum strategies** can work
- Buy after positive news, ride the drift
- Post-earnings announcement drift (PEAD) is real
- Suggests semi-strong form EMH doesn't hold perfectly

### If Markets Over-React
- **Contrarian strategies** can work
- Sell after excessive positive reaction
- Buy after excessive negative reaction
- Mean reversion opportunities exist

---

## Empirical Evidence

**What Studies Show**:

**Short-term (minutes to hours)**:
- Prices react very quickly to news
- Most adjustment happens within minutes
- Supports market efficiency

**Medium-term (days to months)**:
- Some evidence of post-announcement drift
- Momentum effects exist
- Suggests mild inefficiency

**Long-term (years)**:
- Some evidence of overreaction/reversal
- Value strategies work (buying "cheap" stocks)
- Long-term mean reversion

**Conclusion**:
Markets are **mostly efficient** but not perfectly so:
- Very efficient in short run
- Some exploitable patterns in medium/long run
- Patterns are often small and may not survive trading costs

---

## Speed of Information Incorporation

**Factors Affecting Speed**:

**Faster Incorporation**:
- Liquid markets (high trading volume)
- Many sophisticated investors
- Clear, unambiguous news
- No short-sale constraints
- Low transaction costs

**Slower Incorporation**:
- Illiquid markets (low volume)
- Retail-dominated trading
- Complex, hard-to-interpret news
- Short-sale restrictions
- High transaction costs

---

## Real-World Example

**Earnings Announcement**:

```
Before: Stock trading at $50
Expected earnings: $2.00/share
Actual earnings: $2.50/share (beat by $0.50)

Efficient Market Reaction:
  → Price immediately jumps to $55
  → Stabilizes there

Under-Reaction:
  → Price jumps to $52 on announcement day
  → Drifts to $55 over next 60 days
  → Post-earnings announcement drift

Over-Reaction:
  → Price jumps to $58 on announcement day
  → Falls back to $55 over next week
  → Initial overenthusiasm corrected
```

---

## Testing for Market Efficiency

**Event Study Methodology**:
1. Identify event (earnings announcement, merger, etc.)
2. Measure abnormal returns around event
3. Plot cumulative abnormal returns over time
4. Analyze pattern:
   - Jump and flat → efficient
   - Gradual rise → under-reaction
   - Jump then fall → over-reaction

**Result**:
Most event studies show prices react **very quickly**, supporting semi-strong efficiency, though some drift patterns exist for certain types of news.

---

## Related

- [[EMH Forms]] - Types of efficiency
- [[Market Efficiency Mechanisms]] - Why efficiency occurs
- [[Market Efficiency Implications]] - What this means for investors