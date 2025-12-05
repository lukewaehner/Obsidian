# Cost Behavior Patterns

How costs change (or don't change) in response to changes in activity levels.

## Overview

Understanding cost behavior is critical for:
- Budgeting and planning
- Cost-volume-profit analysis
- Pricing decisions
- Performance evaluation

## Four Main Cost Behaviors

### 1. Variable Costs

**Definition**: Costs that change in **total** proportionally with activity level, but remain **constant per unit**.

**Characteristics**:
- Total cost increases/decreases with volume
- Per-unit cost stays constant
- Linear relationship with activity

**Formula**:
```
Total Variable Cost = Variable Cost per Unit × Activity Level
```

**Examples**:
- Direct materials (more units = more materials)
- Sales commissions (% of revenue)
- Shipping costs per package
- Direct labor (in many cases)

**Graph**:
```
Total Cost
    |    /
    |   /
    |  /
    | /
    |/_______________
        Activity
```

**Behavior Table**:

| Units | Total Variable Cost | Per Unit Cost |
|-------|---------------------|---------------|
| 100   | $1,000             | $10           |
| 200   | $2,000             | $10           |
| 300   | $3,000             | $10           |

**Key Insight**: Total goes up, per-unit stays constant.

### 2. Fixed Costs

**Definition**: Costs that remain **constant in total** within the relevant range, but **vary per unit** inversely with activity.

**Characteristics**:
- Total cost stays the same regardless of volume
- Per-unit cost decreases as volume increases
- Time-specific or capacity-specific

**Examples**:
- Factory rent ($50,000/month regardless of production)
- Equipment depreciation (straight-line)
- Property taxes
- Salaries of managers
- Insurance premiums

**Graph**:
```
Total Cost
    |_______________
    |
    |
    |
    |_______________
        Activity
```

**Behavior Table**:

| Units | Total Fixed Cost | Per Unit Cost |
|-------|------------------|---------------|
| 100   | $50,000         | $500          |
| 200   | $50,000         | $250          |
| 300   | $50,000         | $167          |

**Key Insight**: Total stays constant, per-unit goes down with more volume.

### 3. Mixed Costs (Semi-Variable)

**Definition**: Costs that contain **both fixed and variable components**.

**Formula**:
```
Total Cost = Fixed Component + (Variable Rate × Activity)
Y = mx + b
```
Where:
- Y = Total cost
- m = Variable cost per unit
- x = Activity level
- b = Fixed cost component

**Examples**:
- Electricity: Base connection fee + metered usage
- Phone bill: Monthly fee + per-minute charges
- Rental with base + overage charges
- Maintenance: Scheduled (fixed) + repairs (variable)

**Graph**:
```
Total Cost
    |    /
    |   /
    |  /
    | /
    |/_____ (starts above zero)
        Activity
```

**Example Breakdown**:
```
Monthly electricity bill:
  Fixed: $500 (connection fee)
  Variable: $0.10 per kWh

If 10,000 kWh used:
  Total = $500 + ($0.10 × 10,000) = $1,500
```

### 4. Step Costs

**Definition**: Costs that are **fixed over a range** but jump to a new level when activity exceeds capacity.

**Characteristics**:
- Fixed within a range
- Jumps (steps up) at certain thresholds
- Often related to capacity constraints

**Examples**:
- **Lawyers per clients**: Each lawyer has salary (fixed) and can handle N clients
  - 0-50 clients: 1 lawyer ($100,000)
  - 51-100 clients: 2 lawyers ($200,000)
  - 101-150 clients: 3 lawyers ($300,000)

- **Supervisors**: One supervisor per 10 workers
- **Delivery trucks**: Buy new truck every 1,000 deliveries/month

**Graph**:
```
Total Cost
    |         ┌─────
    |    ┌────┘
    |    │
    |────┘
    |_______________
        Activity
```

## Relevant Range

**Definition**: The range of activity over which cost behavior assumptions hold true.

**Why It Matters**:
- Fixed costs are only fixed within a specific range
- Variable costs may change rates outside the range
- Step costs remain constant within each step

**Example**:
```
Current capacity: 0-10,000 units
  Rent: $50,000 (fixed)
  Materials: $5/unit (variable)

At 11,000 units:
  Need bigger facility: $75,000 (new fixed cost)
  Materials: $4.50/unit (volume discount)
```

**Critical Insight**: Cost behavior is **not universal** - it's specific to a relevant range.

## Concert Example

**Scenario**: Booking bands for a concert.

### Popular Band Strategy
```
Pay: $50,000 flat fee (Fixed Cost)

If 100,000 people attend:
  Cost per ticket: $50,000 / 100,000 = $0.50

If 2 people attend:
  Cost per ticket: $50,000 / 2 = $25,000

Risk: Low attendance = high per-ticket cost
```

### Unknown Band Strategy
```
Pay: 10% of each ticket sold (Variable Cost)
Ticket price: $50

If 100,000 people attend:
  Total cost: 100,000 × $5 = $500,000
  Cost per ticket: $5

If 2 people attend:
  Total cost: 2 × $5 = $10
  Cost per ticket: $5

Benefit: Low attendance = low total cost
```

**Insight**: Popular bands want variable (% of revenue) to benefit from high attendance. Organizers prefer fixed to control costs.

## Relevant Range Example

### Workers with Overtime

**Regular time**: $10/hour for first 40 hours
**Overtime**: $15/hour for hours beyond 40

```
Within relevant range (0-40 hours):
  Variable cost: $10/hour

Beyond relevant range (>40 hours):
  Variable cost: $15/hour
```

Cost behavior **changes** outside the relevant range.

## Mixed Cost Separation

To analyze mixed costs, separate them into components:

### High-Low Method
1. Identify highest and lowest activity levels
2. Calculate variable rate: (High Cost - Low Cost) / (High Activity - Low Activity)
3. Calculate fixed component: Total Cost - (Variable Rate × Activity)

### Regression Analysis
- More sophisticated statistical method
- Uses all data points, not just high/low

## Impact on Operating Leverage

**Operating Leverage**: The degree to which a company uses fixed costs.

```
Operating Leverage = Contribution Margin / Net Income
```

**High Fixed Costs** (high operating leverage):
- Higher risk
- Profit swings dramatically with volume changes
- More sensitive to sales fluctuations

**High Variable Costs** (low operating leverage):
- Lower risk
- Profit changes proportionally with volume
- More stable, but less upside potential

## Related Topics

- [[Cost-Volume-Profit Analysis]] - Uses cost behavior for break-even analysis
- [[Contribution Margin]] - Separates variable from fixed costs
- [[Relevant Range]] - Context for cost behavior
- [[Mixed Cost Analysis]] - Separating fixed and variable components
- [[Operating Leverage]] - Impact of cost structure

---

**Key Principle**: Cost behavior describes how total costs and per-unit costs respond to changes in activity - understanding this is essential for planning and decision-making.