# Activity-Based Costing

A more accurate method for allocating overhead costs based on activities that drive costs, rather than a single volume-based allocation.

## The Problem with Traditional Costing

**Traditional Cost Systems**:
- Developed when manufacturing was **labor-intensive**
- Use single company-wide overhead rate
- Typically based on **direct labor hours** or **direct labor cost**
- Worked well when overhead was small relative to direct costs

**Modern Manufacturing**:
- Highly **automated** processes
- Overhead costs are **much larger** (utilities, depreciation)
- Direct labor is **much smaller**
- Using labor to allocate overhead creates **distortion**

### Example of Distortion

**Traditional approach**: Allocate all overhead based on labor hours

**Problem**: 
- Product A: Labor-intensive, low machine use
- Product B: Automated, high machine use
- Both get overhead based on labor hours
- Product A over-costed, Product B under-costed

## What is Activity-Based Costing (ABC)?

**ABC Definition**: A two-stage allocation process that:
1. Traces costs to **activities** (cost pools)
2. Allocates costs to products based on **consumption of activities** (cost drivers)

**Key Insight**: Products consume activities, activities consume resources.

```
Resources → Activities → Products
(overhead)  (cost pools) (cost objects)
```

## The Activity Hierarchy

ABC organizes activities into four levels:

### 1. Unit-Level Activities

**Performed for each individual unit** produced.

**Characteristics**:
- Increases proportionally with units
- Most like traditional variable costs

**Examples**:
- Direct materials usage
- Power to run machines per unit
- Quality inspection per unit
- Packaging each unit

**Cost Driver**: Number of units produced

### 2. Batch-Level Activities

**Performed for each batch**, regardless of batch size.

**Characteristics**:
- Cost is per batch, not per unit
- Larger batches = lower cost per unit

**Examples**:
- Machine setups
- Purchase orders
- Material movements
- Quality testing per batch

**Cost Driver**: Number of batches, setups, orders

**Example**: Cookie baking
- Mixing ingredients = Batch-level (one mix for whole batch)
- Baking each cookie = Unit-level (apply heat to each)

### 3. Product-Level Activities

**Support a specific product line**, regardless of production volume.

**Characteristics**:
- Costs exist even if only one unit made
- Same cost whether making 10 or 10,000 units

**Examples**:
- Product design and engineering
- Product advertising campaigns
- Maintaining product specifications
- Product-specific training
- Patents for specific products

**Cost Driver**: Number of products/product lines

### 4. Facility-Level Activities

**Support entire facility**, necessary to operate as a whole.

**Characteristics**:
- Cannot trace to specific products
- Support overall operations
- Often remain as period costs

**Examples**:
- Factory building depreciation
- Plant security
- Property taxes
- Plant manager salary
- General factory maintenance

**Cost Driver**: Often not allocated, or allocated arbitrarily (e.g., square footage)

## ABC Two-Stage Process

### Stage 1: Trace Costs to Activity Cost Pools

**Identify activities** and create cost pool for each:
```
Activity: Machine Setups
Costs in Pool:
  - Setup labor:        $50,000
  - Setup supplies:     $10,000
  - Machine downtime:   $40,000
  ────────────────────────────────
Total Setup Pool:      $100,000
```

### Stage 2: Allocate Costs to Products

**Calculate activity rate**:
```
Activity Rate = Total Cost in Pool / Total Activity Driver

Setup Rate = $100,000 / 500 setups = $200 per setup
```

**Allocate to products**:
```
Product A: 100 setups × $200 = $20,000
Product B: 400 setups × $200 = $80,000
```

## Example: Circuit Board Manufacturing

**Company makes two products**:
- **Simple boards**: High volume, few components
- **Complex boards**: Low volume, many components

**Traditional costing**: $80 overhead rate per direct labor hour

**ABC approach**: Identify activities and drivers

### Activity Analysis

| Activity | Cost Pool | Driver | Total Driver | Rate |
|----------|-----------|--------|--------------|------|
| Machine setups | $200,000 | Setups | 400 setups | $500/setup |
| Material handling | $150,000 | Moves | 1,000 moves | $150/move |
| Quality inspection | $100,000 | Inspections | 2,000 inspections | $50/inspection |
| Machine operations | $250,000 | Machine hours | 25,000 hours | $10/hour |

### Product Comparison

**Simple Board** (10,000 units):
```
Traditional: 1 DLH × $80 = $80 overhead per unit

ABC:
  Setups:      50 × $500 / 10,000 =    $2.50
  Moves:       100 × $150 / 10,000 =   $1.50
  Inspections: 200 × $50 / 10,000 =    $1.00
  Machine hrs: 5,000 × $10 / 10,000 =  $5.00
  ────────────────────────────────────────────
  Total ABC overhead per unit:         $10.00
```

**Complex Board** (2,000 units):
```
Traditional: 5 DLH × $80 = $400 overhead per unit

ABC:
  Setups:      350 × $500 / 2,000 =    $87.50
  Moves:       900 × $150 / 2,000 =    $67.50
  Inspections: 1,800 × $50 / 2,000 =   $45.00
  Machine hrs: 20,000 × $10 / 2,000 =  $100.00
  ──────────────────────────────────────────────
  Total ABC overhead per unit:         $300.00
```

**Analysis**:
- Simple board: Traditional over-costed ($80 vs $10)
- Complex board: Traditional under-costed ($400 vs $300)
- ABC reveals true cost of complexity

## Benefits of ABC

### 1. Improved Cost Traceability
- More accurate product costs
- Better links between costs and activities
- Identifies cost drivers

### 2. Reduced Product Cost Distortion
- Low-volume, complex products not under-costed
- High-volume, simple products not over-costed
- Better pricing decisions

### 3. Better Management Information
- Identifies non-value-added activities
- Highlights improvement opportunities
- Supports process improvement

### 4. Strategic Insights
- Understand profitability by product/customer
- Make better product mix decisions
- Identify areas for cost reduction

## Costs of ABC

### 1. Information System Requirements
- Need to capture activity data
- Track multiple cost drivers
- More complex software needed

### 2. Implementation Costs
- Identify activities and drivers
- Train employees
- Redesign accounting system

### 3. Ongoing Maintenance
- Update activity rates
- Monitor driver accuracy
- More complex reporting

### 4. Resistance to Change
- More complex than traditional
- Requires cross-functional teams
- May reveal uncomfortable truths

## When to Use ABC

**ABC is Most Beneficial When**:
- Products are diverse (different volumes, complexity)
- Overhead is large relative to direct costs
- Production is automated (labor is small cost)
- Products consume resources differently
- Competition requires accurate costs

**Traditional Costing Sufficient When**:
- Products are similar
- Overhead is small
- Labor-intensive operations
- Simple cost structure
- Cost-benefit doesn't justify ABC

## ABC vs Traditional Costing

| Aspect | Traditional | ABC |
|--------|-------------|-----|
| **Cost pools** | One or few | Many (by activity) |
| **Allocation bases** | Volume-based (labor, units) | Activity-based (diverse drivers) |
| **Accuracy** | Less accurate for diverse products | More accurate |
| **Complexity** | Simple | Complex |
| **Cost** | Low | High |
| **Best for** | Homogeneous products | Diverse products |

## Common ABC Mistakes

### 1. Too Many Activities
- Overwhelms system
- Excessive complexity
- Diminishing returns

**Solution**: Focus on significant activities

### 2. Wrong Cost Drivers
- Weak correlation with cost
- Poor allocation results

**Solution**: Analyze actual cost behavior

### 3. Facility-Level Costs
- Trying to allocate what shouldn't be allocated
- Creates distortion

**Solution**: Keep some costs unallocated

### 4. Static System
- Not updating rates regularly
- Stale activity analysis

**Solution**: Regular review and updates

## ABC Beyond Manufacturing

**ABC principles apply to service industries**:

**Healthcare**: 
- Activity: Patient admission
- Driver: Number of admissions

**Banking**:
- Activity: Processing loan applications  
- Driver: Number of applications

**Hotels**:
- Activity: Room cleaning
- Driver: Number of room-nights

## Related Topics

- [[Overhead Application]] - Traditional approach to overhead
- [[Cost Drivers]] - Choosing appropriate drivers
- [[Product Costing]] - Why accurate costs matter
- [[Direct vs Indirect Costs]] - What gets allocated
- [[Cost Pools]] - Grouping costs by activity

---

**Key Principle**: ABC recognizes that products consume activities in different proportions, and activities drive costs - resulting in more accurate product costs than traditional volume-based allocation.