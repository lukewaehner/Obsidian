# Overhead Application

The process of assigning indirect manufacturing costs to products using predetermined rates.

## The Core Problem

**Manufacturing overhead** (MOH) includes all indirect production costs:
- Factory rent and utilities
- Equipment depreciation
- Indirect materials (glue, supplies)
- Indirect labor (supervisors, maintenance)
- Factory insurance and property taxes

**Challenge**: These costs cannot be easily traced to individual products, yet must be included in product costs for:
- Inventory valuation
- Cost of goods sold calculation
- Pricing decisions
- Profitability analysis

## Two Approaches to Applying Overhead

### 1. Actual Overhead (After the Fact)

**Wait until period ends**, then allocate actual overhead incurred.

**Problems**:
- **Timing delay**: Can't know product costs until period ends
- **Fluctuations**: Overhead per unit varies month-to-month
- **Decision delays**: Pricing and planning can't wait for actual data

### 2. Predetermined Overhead Rate (Estimated)

**Calculate rate at beginning of period**, apply throughout year.

**Benefits**:
- **Timely information**: Product costs available immediately
- **Smooth costs**: Same rate all year regardless of monthly fluctuations
- **Better planning**: Managers can make decisions without waiting

**Trade-off**: Less accurate but more timely

## Predetermined Overhead Rate (POHR)

### Formula

```
POHR = Estimated Overhead for Period / Estimated Allocation Base for Period
```

**Common Allocation Bases**:
- Direct labor hours
- Machine hours
- Direct labor cost
- Units produced
- Direct materials cost

### Example: Annual Salary Allocation

**Given**:
- Supervisor annual salary: $36,000
- Estimated annual production: 18,000 units

**Calculate POHR**:
```
POHR = $36,000 / 18,000 units = $2.00 per unit
```

**Application**: Allocate $2.00 to each unit produced every month, regardless of when salary is actually paid.

### Why This Works

**Salary paid once per month**: $3,000
- Without POHR: All January units get $3,000 overhead, February units get $3,000, etc.
- With POHR: Every unit throughout year gets $2.00 (fair allocation)

**Result**: Smooth, consistent product costs year-round.

## Applying Overhead to Production

### Journal Entry When Overhead is Applied

```
Dr. Work in Process                      XXX
    Cr. Manufacturing Overhead Applied       XXX
```

**Example**: 1,000 units produced, POHR = $2.00 per unit
```
Dr. Work in Process                    2,000
    Cr. Manufacturing Overhead Applied     2,000
```

### Actual Overhead Incurred

As actual overhead costs occur, record them:

```
Dr. Manufacturing Overhead Control     XXX
    Cr. Various Accounts (Cash, Payables, etc.)  XXX
```

**Example**: Pay supervisor $3,000
```
Dr. Manufacturing Overhead Control     3,000
    Cr. Salaries Payable                   3,000
```

## Manufacturing Overhead: A Clearing Account

**Manufacturing Overhead has two sides**:

**Debit Side (Control)**:
- Actual overhead costs incurred
- Various debits throughout period

**Credit Side (Applied)**:
- Estimated overhead applied to WIP
- Based on POHR and actual activity

**At Period End**:
- Compare debit total (actual) with credit total (applied)
- Rarely perfectly equal
- Difference = under-applied or over-applied overhead

```
Manufacturing Overhead Account:

Debit (Actual)          |  Credit (Applied)
─────────────────────────────────────────────
Rent         5,000     |  Applied    15,000
Utilities    3,000     |
Depreciation 4,000     |
Supplies     2,500     |
Labor        1,000     |
─────────────────────────────────────────────
Total       15,500     |  Total      15,000
─────────────────────────────────────────────
Balance: $500 Debit (Under-applied)
```

## Under-Applied vs Over-Applied Overhead

### Under-Applied Overhead

**Definition**: Actual overhead > Applied overhead

**Means**: We under-estimated overhead, didn't apply enough to products

**Balance**: Debit balance in Manufacturing Overhead account

**Example**:
```
Actual overhead incurred:    $15,500
Applied overhead (POHR):     $15,000
─────────────────────────────────────
Under-applied:               $500
```

**Interpretation**: Product costs were understated by $500.

### Over-Applied Overhead

**Definition**: Applied overhead > Actual overhead

**Means**: We over-estimated overhead, applied too much to products

**Balance**: Credit balance in Manufacturing Overhead account

**Example**:
```
Actual overhead incurred:    $14,500
Applied overhead (POHR):     $15,000
─────────────────────────────────────
Over-applied:                $500
```

**Interpretation**: Product costs were overstated by $500.

## Disposing of Over/Under-Applied Overhead

At year-end, must close out the Manufacturing Overhead account. Two approaches:

### 1. COGS Approach (Simpler)

**Close entire balance to Cost of Goods Sold.**

**For Under-Applied** (debit balance):
```
Dr. Cost of Goods Sold              500
    Cr. Manufacturing Overhead          500
```
Effect: Increases COGS (we under-costed products)

**For Over-Applied** (credit balance):
```
Dr. Manufacturing Overhead          500
    Cr. Cost of Goods Sold              500
```
Effect: Decreases COGS (we over-costed products)

### 2. Allocation Approach (More Accurate)

**Allocate proportionally** to all accounts containing applied overhead:
- Work in Process
- Finished Goods
- Cost of Goods Sold

**Example**: $500 under-applied overhead

**Account balances with applied overhead**:
- WIP: $2,000 (10%)
- Finished Goods: $3,000 (15%)
- COGS: $15,000 (75%)
- Total: $20,000 (100%)

**Allocation**:
```
WIP increase:   $500 × 10% = $50
FG increase:    $500 × 15% = $75
COGS increase:  $500 × 75% = $375
                              ────
Total:                        $500
```

**Journal Entry**:
```
Dr. Work in Process                  50
Dr. Finished Goods                   75
Dr. Cost of Goods Sold              375
    Cr. Manufacturing Overhead          500
```

### Which Approach to Use?

**COGS Approach**:
- Simpler, faster
- Assumes most production was sold
- Good when under/over-applied is small

**Allocation Approach**:
- More accurate
- Better matches costs to inventory still on hand
- Required when under/over-applied is material

## Summary Table

| Situation | Balance Type | COGS Approach | Allocation Approach |
|-----------|--------------|---------------|---------------------|
| Under-Applied | Debit | Increase COGS | Increase WIP, FG, COGS |
| Over-Applied | Credit | Decrease COGS | Decrease WIP, FG, COGS |

## Why Under/Over-Applied Occurs

**Common Reasons**:

1. **Estimation errors**: 
   - Actual production differs from estimated
   - Actual overhead differs from estimated

2. **Seasonal variations**: 
   - Utility costs higher in summer/winter
   - Production volume fluctuates

3. **Changes during year**: 
   - Unexpected cost increases
   - Equipment failures
   - New regulations

4. **Allocation base mismatch**:
   - Used direct labor hours, but overhead driven by machine hours
   - Poor choice of allocation base

## Multiple Overhead Rates

Instead of single company-wide rate, can use:
- **Departmental rates**: Different POHR for each department
- **Activity-based rates**: Different POHR for different activities
- See: [[Activity-Based Costing]]

## Related Topics

- [[Product Costing]] - Why we need to apply overhead
- [[Cost Drivers]] - Choosing allocation bases
- [[Activity-Based Costing]] - More sophisticated overhead allocation
- [[Direct vs Indirect Costs]] - What overhead includes
- [[Actual vs Estimated Costs]] - Trade-off between accuracy and timeliness

---

**Key Principle**: Predetermined overhead rates sacrifice some accuracy for timely information, with year-end adjustments to correct for estimation errors.