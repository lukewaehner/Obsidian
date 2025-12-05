# Performance Evaluation

Systems for measuring and analyzing actual results against budgeted expectations using variance analysis.

## Standard Cost Systems

**Standard**: The amount a price, cost, or quantity **should be** under normal conditions.

**Purpose of Standards**:
- **Encourage efficiency**: Targets motivate performance
- **Facilitate planning**: Basis for budgets
- **Enable control**: Benchmark for judging performance
- **Simplify recordkeeping**: Use standard costs in accounts

**Management by Exception**: Focus attention on significant deviations from standards.

## Three Types of Budgets

### 1. Master Budget (Static Budget / Operating Budget)

**Definition**: Budget based on planned volume level.

**Formula**:
```
Master Budget = Standard Quantity × Standard Price × Standard Volume
Master Budget = SQ × SP × SV
```

**Characteristics**:
- Created at beginning of period
- Based on expected sales/production volume
- Does not adjust for actual volume
- Single set of numbers

**Example**:
```
Planned production: 10,000 units
Standard materials: 2 lbs per unit at $5/lb
Master budget for materials: 10,000 × 2 × $5 = $100,000
```

### 2. Flexible Budget

**Definition**: Budget adjusted to actual volume level, keeping standard prices and quantities.

**Formula**:
```
Flexible Budget = Standard Quantity × Standard Price × Actual Volume
Flexible Budget = SQ × SP × AV
```

**Purpose**: 
- Show what costs **should have been** at actual volume
- Remove volume effects from performance evaluation
- Fair comparison basis

**Example**:
```
Actual production: 12,000 units
Standard materials: 2 lbs per unit at $5/lb
Flexible budget for materials: 12,000 × 2 × $5 = $120,000
```

**Key Insight**: Flexible budget asks "What should costs be for the actual volume we produced?"

### 3. Actual Results

**Definition**: What actually occurred.

**Formula**:
```
Actual Results = Actual Quantity × Actual Price × Actual Volume
Actual Results = AQ × AP × AV
```

**Example**:
```
Actual production: 12,000 units
Actual materials used: 25,000 lbs at $4.80/lb
Actual results: 25,000 × $4.80 = $120,000
```

## Variance Analysis Framework

### Three Key Comparisons

```
Master Budget ←→ Flexible Budget ←→ Actual Results
(SQ×SP×SV)       (SQ×SP×AV)          (AQ×AP×AV)
     ↓                 ↓                  ↓
 Volume          Flexible Budget     
 Variance            Variance
```

### Total Budget Variance

**Definition**: Overall difference between master budget and actual results.

```
Budget Variance = Master Budget - Actual Results
Budget Variance = (SQ × SP × SV) - (AQ × AP × AV)
```

**Components**:
```
Budget Variance = Volume Variance + Flexible Budget Variance
```

## Volume Variance

**Definition**: Impact from producing more or fewer units than planned.

```
Volume Variance = Master Budget - Flexible Budget
Volume Variance = (SQ × SP × SV) - (SQ × SP × AV)
Volume Variance = SQ × SP × (SV - AV)
```

**Interpretation**:
- Shows effect of volume difference only
- Holds price and quantity standards constant
- **Favorable**: Produced more than planned (AV > SV)
- **Unfavorable**: Produced less than planned (AV < SV)

**Example**:
```
Master budget (10,000 units): $100,000
Flexible budget (12,000 units): $120,000
Volume variance: $100,000 - $120,000 = $(20,000) unfavorable

Wait - produced MORE but unfavorable?
  - For revenues: More volume = favorable
  - For costs: More volume = unfavorable (higher costs)
```

**Revenue vs Cost Treatment**:
- **Revenue**: Higher volume = Favorable variance
- **Costs**: Higher volume = Unfavorable variance

## Flexible Budget Variance

**Definition**: Difference between what costs should have been (flexible budget) and what they actually were.

```
Flexible Budget Variance = Flexible Budget - Actual Results
Flexible Budget Variance = (SQ × SP × AV) - (AQ × AP × AV)
```

**Can be broken into two components**:

### 1. Price Variance

**Definition**: Impact of paying different price than standard.

```
Price Variance = (SP - AP) × AQ × AV
Price Variance = (Standard Price - Actual Price) × Actual Quantity
```

**Interpretation**:
- Shows effect of price difference
- **Favorable**: Paid less than standard (AP < SP)
- **Unfavorable**: Paid more than standard (AP > SP)

**Example**:
```
Standard price: $5.00/lb
Actual price: $4.80/lb
Actual quantity: 25,000 lbs

Price variance = ($5.00 - $4.80) × 25,000 = $5,000 Favorable
```

**Responsibility**: Usually purchasing department

### 2. Quantity/Efficiency Variance

**Definition**: Impact of using different quantity than standard.

```
Quantity Variance = (SQ - AQ) × SP × AV
Quantity Variance = (Standard Quantity - Actual Quantity) × Standard Price
```

**For materials**: Quantity variance (usage)
**For labor**: Efficiency variance (hours)

**Interpretation**:
- Shows effect of quantity/efficiency difference
- **Favorable**: Used less than standard (AQ < SQ)
- **Unfavorable**: Used more than standard (AQ > SQ)

**Example**:
```
Standard quantity: 2 lbs/unit × 12,000 units = 24,000 lbs
Actual quantity: 25,000 lbs
Standard price: $5.00/lb

Quantity variance = (24,000 - 25,000) × $5.00 = $(5,000) Unfavorable
```

**Responsibility**: Usually production department

## Complete Variance Analysis Example

**Given Standards**:
- Production: 10,000 units planned
- Materials: 2 lbs per unit at $5.00/lb

**Actual Results**:
- Production: 12,000 units
- Materials: 25,000 lbs at $4.80/lb

### Calculate All Variances

**Master Budget**:
```
10,000 units × 2 lbs × $5.00 = $100,000
```

**Flexible Budget**:
```
12,000 units × 2 lbs × $5.00 = $120,000
```

**Actual Results**:
```
25,000 lbs × $4.80 = $120,000
```

**Volume Variance**:
```
$100,000 - $120,000 = $(20,000) U
(Produced 2,000 more units → higher costs)
```

**Price Variance**:
```
($5.00 - $4.80) × 25,000 = $5,000 F
(Paid $0.20 less per lb)
```

**Quantity Variance**:
```
(24,000 - 25,000) × $5.00 = $(5,000) U
(Used 1,000 lbs more than standard)
```

**Flexible Budget Variance**:
```
$120,000 - $120,000 = $0
(Price variance $5,000 F offset by quantity variance $5,000 U)
```

**Total Budget Variance**:
```
$100,000 - $120,000 = $(20,000) U
(Equals volume variance + flexible budget variance)
$(20,000) U = $(20,000) U + $0
```

## Variance Analysis Diagram

```
Master Budget          Flexible Budget       Actual Results
(SQ × SP × SV)         (SQ × SP × AV)        (AQ × AP × AV)
$100,000               $120,000              $120,000
    |                      |                      |
    |←―――Volume――――――――→|←――Flexible Budget―――→|
    |    Variance         |     Variance          |
    |   $(20,000) U       |        $0             |
    |                     |                       |
    |←――――――――――Total Budget Variance―――――――――――→|
    |                $(20,000) U                  |
                          
                    Flexible Budget Variance breakdown:
                    
                    Price Variance:      $5,000 F
                    Quantity Variance:   $(5,000) U
                    ─────────────────────────────────
                    Total:               $0
```

## Favorable vs Unfavorable Notation

**Favorable (F)**:
- Actual revenue > Budget
- Actual costs < Budget
- Good for company

**Unfavorable (U)**:
- Actual revenue < Budget
- Actual costs > Budget
- Bad for company

**Common notation**:
- Positive numbers often indicate favorable
- Negative numbers (in parentheses) indicate unfavorable
- Or explicitly mark with F or U

## Management by Exception

**Principle**: Focus management attention on significant variances.

**Process**:
1. Calculate all variances
2. Identify **significant** variances (materiality threshold)
3. Investigate causes of significant variances
4. Take corrective action when needed

**Materiality Guidelines**:
- Dollar amount (> $10,000)
- Percentage (> 5% of budget)
- Combination (> $5,000 AND > 10%)

**Investigation Questions**:
- Is variance controllable?
- Is it recurring or one-time?
- What caused it?
- Can we fix it going forward?

## Variance Interpretations

### Price Variances

**Favorable Price Variance Might Mean**:
- Good negotiation by purchasing
- Quantity discounts obtained
- Market prices decreased

**Or Could Mean** (caution):
- Lower quality materials purchased
- Will cause problems in production

**Unfavorable Price Variance Might Mean**:
- Poor negotiation
- Market prices increased
- Rush orders (premium pricing)

### Quantity/Efficiency Variances

**Favorable Quantity Variance Might Mean**:
- Efficient production
- Less waste/scrap
- Better trained workers

**Unfavorable Quantity Variance Might Mean**:
- Inefficient production
- More waste/scrap
- Poor quality materials (links to favorable price variance)
- Inadequate training

## Interrelated Variances

**Example**: Favorable price variance, unfavorable quantity variance
```
Purchased cheaper materials (F price variance)
  ↓
Materials were lower quality
  ↓
More waste in production (U quantity variance)
  ↓
Net effect: $5,000 F - $5,000 U = $0
```

**Key Insight**: Must evaluate variances together, not in isolation.

## Related Topics

- [[Budgeting]] - Creating the master budget
- [[Standard Costing]] - Setting standards
- [[Responsibility Accounting]] - Who's accountable for variances
- [[Flexible Budgets]] - Adjusting for volume
- [[Management by Exception]] - Using variances for control

---

**Key Principle**: Variance analysis separates performance into controllable components (price, efficiency) and volume effects, enabling targeted management action.