# Cost-Volume-Profit Analysis

A method for analyzing how changes in costs, volume, and price affect profit.

## Core Concept

CVP analysis examines the relationship between:
- **Cost** (fixed and variable)
- **Volume** (units sold/produced)
- **Price** (selling price per unit)
- **Profit** (resulting income)

## Fundamental CVP Equation

```
Revenue - Variable Costs - Fixed Costs = Profit

Or:

(Price × Quantity) - (Variable Cost per Unit × Quantity) - Fixed Costs = Profit
P × Q - VC × Q - FC = Profit
```

## Contribution Margin

**Definition**: The amount remaining from sales revenue after variable costs are deducted.

### Contribution Margin Income Statement Format

```
Sales Revenue
- Variable Costs
─────────────────────
Contribution Margin
- Fixed Costs
─────────────────────
Operating Income
```

### Three Ways to Express Contribution Margin

**1. Total Contribution Margin**:
```
CM = Total Revenue - Total Variable Costs
CM = (P - VC) × Q
```

**2. Contribution Margin per Unit**:
```
CM per unit = Price per Unit - Variable Cost per Unit
CM per unit = P - VC
```

**3. Contribution Margin Ratio (CM%)**:
```
CM Ratio = Contribution Margin / Sales Revenue
CM Ratio = (P - VC) / P

Or:

CM Ratio = CM per unit / Price per unit
```

### Example Calculation

**Given**:
- Selling price: $80 per unit
- Variable cost: $30 per unit
- Fixed costs: $280,000
- Sales: 10,000 units

**Contribution Margin Analysis**:
```
Total Sales:          10,000 × $80 = $800,000
Total Variable Costs: 10,000 × $30 = $300,000
─────────────────────────────────────────────
Contribution Margin:              $500,000
Fixed Costs:                      $280,000
─────────────────────────────────────────────
Operating Income:                 $220,000

CM per unit: $80 - $30 = $50
CM Ratio: $50 / $80 = 62.5%
```

## Break-Even Analysis

**Break-Even Point**: The level of sales where total revenues equal total costs (profit = $0).

### Break-Even in Units

```
Break-Even Units = Fixed Costs / CM per Unit

BEQ = FC / (P - VC)
```

**Example**:
```
Fixed Costs: $280,000
CM per Unit: $50

BEQ = $280,000 / $50 = 5,600 units
```

### Break-Even in Dollars

```
Break-Even Sales $ = Fixed Costs / CM Ratio

BES = FC / (CM / Sales)
```

**Example**:
```
Fixed Costs: $280,000
CM Ratio: 62.5%

BES = $280,000 / 0.625 = $448,000
```

**Verification**: 5,600 units × $80 = $448,000 ✓

## Target Profit Analysis

To achieve a specific profit target, use modified break-even formulas:

### Units for Target Profit

```
Required Units = (Fixed Costs + Target Profit) / CM per Unit

Q = (FC + Target Profit) / (P - VC)
```

**Example**: What sales needed for $300,000 profit?
```
Q = ($280,000 + $300,000) / $50
Q = $580,000 / $50 = 11,600 units
```

### Sales Dollars for Target Profit

```
Required Sales $ = (Fixed Costs + Target Profit) / CM Ratio
```

**Example**:
```
Sales $ = ($280,000 + $300,000) / 0.625
Sales $ = $580,000 / 0.625 = $928,000
```

## Margin of Safety

**Definition**: The cushion between budgeted (actual) sales and break-even sales.

### Margin of Safety Formulas

**In Units**:
```
Margin of Safety (units) = Budgeted Sales - Break-Even Sales
```

**In Dollars**:
```
Margin of Safety ($) = Budgeted Sales $ - Break-Even Sales $
```

**As Percentage**:
```
Margin of Safety % = (Budgeted Sales - Break-Even Sales) / Budgeted Sales
```

### Example

**Given**:
- Budgeted sales: 10,000 units at $80 = $800,000
- Break-even sales: 5,600 units at $80 = $448,000

**Calculate**:
```
MOS (units) = 10,000 - 5,600 = 4,400 units
MOS ($) = $800,000 - $448,000 = $352,000
MOS (%) = $352,000 / $800,000 = 44%
```

**Interpretation**: Sales can drop by 4,400 units (or 44%) before the company starts losing money.

## Operating Leverage

**Definition**: The degree to which a company uses fixed costs in its cost structure.

```
Operating Leverage = Contribution Margin / Operating Income
```

**Example**:
```
Contribution Margin: $500,000
Operating Income: $220,000

Operating Leverage = $500,000 / $220,000 = 2.27
```

**Interpretation**: A 1% increase in sales will result in a 2.27% increase in operating income.

### High vs Low Operating Leverage

**High Operating Leverage** (high fixed costs, low variable costs):
- Greater profit swings from sales changes
- Higher risk, higher potential reward
- Example: Airlines, hotels, software

**Low Operating Leverage** (low fixed costs, high variable costs):
- More stable profits
- Lower risk, lower potential reward
- Example: Consulting, retail

## CVP Assumptions

CVP analysis relies on several simplifying assumptions:

1. **Costs are linear**: Within relevant range
2. **Costs can be classified**: Either fixed or variable
3. **Selling price is constant**: No price changes
4. **Production equals sales**: No inventory changes (or using variable costing)
5. **Sales mix is constant**: For multi-product companies
6. **Relevant range**: Assumptions hold within range

## Multi-Product CVP Analysis

When selling multiple products, use **weighted-average** contribution margin.

### Sales Mix Example

**Products**:
- Product A: 60% of sales, CM = $30 per unit
- Product B: 40% of sales, CM = $50 per unit

**Weighted Average CM**:
```
Weighted CM = (0.60 × $30) + (0.40 × $50)
Weighted CM = $18 + $20 = $38 per unit
```

Use weighted average CM for break-even calculations.

## Sensitivity Analysis

**What-if scenarios** to see how changes affect profit:

### Change in Selling Price
```
If price increases by $5:
  New CM per unit = $55
  New BEQ = $280,000 / $55 = 5,091 units
```

### Change in Variable Costs
```
If variable costs increase by $10:
  New CM per unit = $40
  New BEQ = $280,000 / $40 = 7,000 units
```

### Change in Fixed Costs
```
If fixed costs increase by $50,000:
  New FC = $330,000
  New BEQ = $330,000 / $50 = 6,600 units
```

## Graphical Representation

**Break-Even Chart**:
```
$
|           Revenue Line (P × Q)
|          /
|         /  Profit
|        /  Region
|       /
|      / ← Break-Even Point
|     /
|    / Loss Region
|   /  Total Cost Line (FC + VC × Q)
|  /
| / Fixed Cost Line
|/___________________________
     Units Sold (Q)
```

## Practical Applications

### Pricing Decisions
- Minimum price = Variable cost per unit (short-term)
- Target price = (VC + Allocated FC + Target Profit) / Units

### Make vs Buy
- Compare incremental cost vs purchase price
- Consider contribution margin impact

### Product Mix
- Maximize total contribution margin
- Consider constrained resources

### Marketing Campaigns
- Cost of campaign = Fixed cost increase
- Need increased sales to cover: Cost / CM per unit

## Related Topics

- [[Cost Behavior Patterns]] - Foundation for CVP analysis
- [[Contribution Margin]] - Key CVP metric
- [[Margin of Safety]] - Risk assessment
- [[Operating Leverage]] - Cost structure impact
- [[Break-Even Analysis]] - Core CVP application
- [[Relevant Costs]] - Decision-making with CVP

---

**Key Principle**: CVP analysis shows how profits respond to changes in price, costs, and volume - essential for planning, pricing, and profitability decisions.