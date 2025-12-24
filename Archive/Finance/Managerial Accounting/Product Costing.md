# Product Costing

The process of accumulating and assigning costs to products or services.

## Why Product Costing Matters

**Managers need to know product costs for**:
1. **Pricing decisions**: Cost-plus pricing strategies
2. **Profitability analysis**: Which products are profitable
3. **Inventory valuation**: Balance sheet reporting
4. **Cost control**: Identifying cost reduction opportunities
5. **Make vs buy**: Should we make or outsource?
6. **Product mix**: Which products to emphasize

## The Formula

```
Total Product Cost = Direct Materials + Direct Labor + Manufacturing Overhead Applied

Product Cost per Unit = Total Product Cost / Units Produced
```

## The Three Components

### 1. Direct Materials (DM)

**Definition**: Raw materials that can be directly traced to the product.

**Characteristics**:
- Physically part of the finished product
- Cost is easily measurable per unit
- Primary substance of the product

**Examples**:
- Wood in furniture
- Flour in bread
- Steel in cars
- Fabric in clothing

**Calculation**:
```
DM Cost = Quantity of Material Used × Cost per Unit of Material

Example:
  Chair uses 10 board-feet of wood at $2/bf
  DM Cost = 10 × $2 = $20 per chair
```

### 2. Direct Labor (DL)

**Definition**: Wages of workers who directly manufacture the product.

**Characteristics**:
- Workers who physically transform materials
- Time spent can be traced to specific products
- Hands-on production work

**Examples**:
- Assembly line workers
- Machine operators
- Welders, carpenters, bakers
- Direct fabrication labor

**Calculation**:
```
DL Cost = Labor Hours × Wage Rate

Example:
  Chair requires 2 hours at $15/hour
  DL Cost = 2 × $15 = $30 per chair
```

**Not Direct Labor**:
- Supervisors
- Janitors
- Quality inspectors
- Maintenance workers
These are **indirect labor** (part of manufacturing overhead).

### 3. Manufacturing Overhead (MOH)

**Definition**: All indirect manufacturing costs that cannot be easily traced to specific products.

**Characteristics**:
- Necessary for production
- Shared across all products
- Requires allocation to products
- Cannot be directly traced cost-effectively

**Categories of MOH**:

**Indirect Materials**:
- Glue, screws, nails
- Sandpaper, cleaning supplies
- Lubricants, small tools

**Indirect Labor**:
- Factory supervisors
- Maintenance workers
- Quality control staff
- Material handlers
- Factory janitors

**Other Manufacturing Costs**:
- Factory rent
- Factory utilities (electricity, heat)
- Equipment depreciation
- Factory insurance
- Property taxes on factory

**Calculation**: See [[Overhead Application]] for detailed methods.

```
MOH per Unit = Predetermined Overhead Rate × Allocation Base per Unit

Example:
  POHR = $10 per direct labor hour
  Chair requires 2 hours
  MOH = $10 × 2 = $20 per chair
```

## Complete Product Cost Example

**Acme Chair Manufacturing**

**Production**: 100 chairs

**Cost Data**:
- Wood: 10 board-feet per chair at $2/bf
- Assembly labor: 2 hours per chair at $15/hour
- POHR: $10 per direct labor hour

**Calculate Total Product Cost**:

```
Direct Materials:
  100 chairs × 10 bf × $2 = $20,000

Direct Labor:
  100 chairs × 2 hours × $15 = $30,000

Manufacturing Overhead:
  100 chairs × 2 hours × $10 = $20,000
───────────────────────────────────
Total Product Cost: $70,000

Cost per Unit: $70,000 / 100 = $700 per chair
```

**Breakdown per Chair**:
```
Direct Materials:       $200
Direct Labor:           $300
Manufacturing Overhead: $200
─────────────────────────────
Total:                  $700
```

## Cost Flows Through Accounts

### Detailed Journal Entry Example

**Using the chair example above:**

**1. Purchase raw materials ($25,000)**:
```
Dr. Raw Materials Inventory    25,000
    Cr. Accounts Payable/Cash         25,000
```

**2. Issue materials to production ($20,000)**:
```
Dr. Work in Process            20,000
    Cr. Raw Materials Inventory       20,000
```

**3. Incur direct labor ($30,000)**:
```
Dr. Work in Process            30,000
    Cr. Salaries Payable              30,000
```

**4. Apply overhead ($20,000)**:
```
Dr. Work in Process            20,000
    Cr. Manufacturing Overhead        20,000
```

**5. Complete production (all 100 chairs)**:
```
Dr. Finished Goods             70,000
    Cr. Work in Process               70,000
```

**6. Sell 80 chairs ($56,000 cost)**:
```
Dr. Cost of Goods Sold         56,000
    Cr. Finished Goods                56,000
```

**Ending Balances**:
```
Raw Materials:      $5,000 (materials on hand)
Work in Process:    $0 (all completed)
Finished Goods:     $14,000 (20 chairs at $700)
COGS:               $56,000 (80 chairs sold)
```

## Prime Costs vs Conversion Costs

### Prime Costs

**Definition**: Direct materials + Direct labor

```
Prime Costs = DM + DL
```

**Represents**: The "prime" (main) traceable costs of production.

**Example**:
```
DM: $200
DL: $300
─────────
Prime: $500
```

### Conversion Costs

**Definition**: Direct labor + Manufacturing overhead

```
Conversion Costs = DL + MOH
```

**Represents**: Costs to "convert" raw materials into finished products.

**Example**:
```
DL:  $300
MOH: $200
─────────
Conversion: $500
```

**Note**: Direct labor appears in both prime and conversion costs.

## Cost-Plus Pricing

**Common business practice**: Set price based on cost plus desired profit margin.

### Basic Cost-Plus Formula

```
Selling Price = Total Product Cost + Markup

Or:

Selling Price = Total Product Cost × (1 + Markup %)
```

**Example**:
```
Product cost: $700
Desired markup: 40%

Selling Price = $700 × 1.40 = $980
```

### Alternative Approaches

**Markup on Variable Costs**:
```
Price = Variable Costs + Fixed Costs + Profit Margin
```

**Target Return Pricing**:
```
Price = Cost + (Desired ROI × Invested Capital) / Units
```

**Considerations**:
- Market price (what will customers pay?)
- Competition
- Demand elasticity
- Strategic positioning

See: [[Cost-Volume-Profit Analysis]] for pricing strategy details.

## Job Order vs Process Costing

### Job Order Costing

**Used when**: Products are unique or customized.

**Characteristics**:
- Track costs by specific job/order
- Each job gets its own cost sheet
- Different costs for different jobs

**Examples**:
- Custom furniture
- Construction projects
- Printing jobs
- Consulting engagements

### Process Costing

**Used when**: Products are homogeneous and mass-produced.

**Characteristics**:
- Track costs by process/department
- Average costs across all units
- Units are identical

**Examples**:
- Oil refining
- Beverage production
- Paper manufacturing
- Chemical processing

**This course focuses on job order costing concepts.**

## Common Issues in Product Costing

### 1. Overhead Allocation Accuracy

**Challenge**: Choosing appropriate allocation base.

**Solutions**:
- [[Activity-Based Costing]] for complex environments
- Multiple overhead rates by department
- More sophisticated cost drivers

### 2. Mixed Costs

**Challenge**: Some costs have both fixed and variable components.

**Solution**: Separate using high-low method or regression.

### 3. Joint Costs

**Challenge**: One process produces multiple products.

**Solution**: Allocate based on relative sales value or physical quantities.

### 4. Changing Cost Structures

**Challenge**: Automation increases overhead, decreases labor.

**Solution**: Update allocation methods to reflect reality.

## Product Costing for Services

**Service companies also need product costing**:

**Service "Product"**: Client engagement, project, or service delivered

**Cost Components**:
- **Direct Labor**: Consultant hours, attorney time
- **Direct Costs**: Travel, materials for client
- **Overhead**: Office rent, support staff, technology

**Example: Consulting Firm**
```
Project for Client X:
  Consultant hours: 100 hrs at $150/hr = $15,000
  Travel and expenses:                  = $2,000
  Overhead (150% of labor):             = $22,500
  ───────────────────────────────────────────────
  Total Project Cost:                   = $39,500
  
  Markup: 25%                           = $9,875
  ───────────────────────────────────────────────
  Price to Client:                      = $49,375
```

## Relationship to Financial Statements

### Balance Sheet

**Product costs appear as**:
- Raw Materials Inventory (DM waiting to use)
- Work in Process (DM + DL + MOH in production)
- Finished Goods (DM + DL + MOH completed)

### Income Statement

**Product costs appear as**:
- Cost of Goods Sold (when products sold)

**Remember**: Product costs are **assets** until sold, then become **expenses**.

## Related Topics

- [[Product vs Period Costs]] - What gets included in product cost
- [[Cost Flows]] - How product costs move through accounts
- [[Overhead Application]] - Applying MOH to products
- [[Activity-Based Costing]] - More accurate overhead allocation
- [[Direct vs Indirect Costs]] - Understanding the three components
- [[Archive/Finance/Managerial Accounting/Types of Inventory]] - Where product costs accumulate

---

**Key Principle**: Product costing accumulates direct materials, direct labor, and manufacturing overhead to determine the full cost of production, which is essential for pricing, profitability analysis, and inventory valuation.