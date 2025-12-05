# Types of Inventory

The three inventory accounts in a manufacturing company's Balance Sheet.

## Overview

Manufacturing companies track inventory in **three distinct accounts** representing different stages of production:

1. **Raw Materials Inventory**
2. **Work in Process Inventory (WIP)**
3. **Finished Goods Inventory**

## Raw Materials Inventory

**Definition**: Materials waiting to be processed into products for sale.

**Characteristics**:
- Materials purchased but not yet used in production
- Stored in **storeroom** or warehouse
- Still in original form (unprocessed)
- Balance Sheet account (asset)

**Examples**:
- Lumber for furniture manufacturing
- Flour for bakery
- Steel sheets for car manufacturing
- Electronic components for phones

**Account Activity**:
- **Increases**: When materials are purchased
- **Decreases**: When materials are issued to production

### Equation
```
Beginning Raw Materials
+ Purchases
- Materials Used in Production
─────────────────────────────────
= Ending Raw Materials
```

## Work in Process Inventory (WIP)

**Definition**: Partially completed products that have had some materials, labor, or overhead added.

**Characteristics**:
- Products in the middle of production process
- Located in **factory** or production area
- Has partial costs attached
- Balance Sheet account (asset)

**Examples**:
- Chair with legs attached but no seat
- Half-baked bread dough
- Car frame with engine but no doors
- Phone circuit board without casing

**Account Activity**:
- **Increases**: When materials, labor, or overhead are added
- **Decreases**: When products are completed

### Equation
```
Beginning WIP
+ Direct Materials Used
+ Direct Labor
+ Manufacturing Overhead Applied
- Cost of Goods Manufactured (completed units)
────────────────────────────────────────────
= Ending WIP
```

### Key Insight
WIP is the "**factory account**" - it accumulates all production costs while work is in progress.

## Finished Goods Inventory

**Definition**: Completed products awaiting sale to customers.

**Characteristics**:
- Manufacturing is complete
- Stored in **warehouse**
- Ready for shipment/sale
- Balance Sheet account (asset)

**Examples**:
- Completed chairs in warehouse
- Boxed bread ready for stores
- Cars on dealer lot
- Phones in retail packaging

**Account Activity**:
- **Increases**: When products are completed (from WIP)
- **Decreases**: When products are sold (becomes COGS)

### Equation
```
Beginning Finished Goods
+ Cost of Goods Manufactured
- Cost of Goods Sold
────────────────────────────
= Ending Finished Goods
```

## Physical Flow Through Facility

```
STOREROOM          →    FACTORY           →    WAREHOUSE
Raw Materials           Work in Process         Finished Goods
(waiting to use)        (being made)           (ready to sell)
```

## Cost Flow Summary

```
Raw Materials Inventory
        ↓ (materials issued to production)
Work in Process Inventory
    + Materials
    + Labor
    + Overhead
        ↓ (products completed)
Finished Goods Inventory
        ↓ (products sold)
Cost of Goods Sold (Income Statement)
```

## Journal Entry Flow

### 1. Purchase Raw Materials
```
Dr. Raw Materials Inventory
    Cr. Accounts Payable/Cash
```

### 2. Use Materials in Production
```
Dr. Work in Process
    Cr. Raw Materials Inventory
```

### 3. Add Direct Labor
```
Dr. Work in Process
    Cr. Salaries Payable
```

### 4. Apply Overhead
```
Dr. Work in Process
    Cr. Manufacturing Overhead (or specific accounts)
```

### 5. Complete Production
```
Dr. Finished Goods
    Cr. Work in Process
```

### 6. Sell Products
```
Dr. Cost of Goods Sold
    Cr. Finished Goods
```

## Key Differences

| Inventory Type | Location | Status | Costs Included |
|---------------|----------|--------|----------------|
| Raw Materials | Storeroom | Unprocessed | Purchase cost only |
| WIP | Factory | Partially complete | Materials + Labor + Overhead (partial) |
| Finished Goods | Warehouse | Complete | All product costs (DM + DL + MOH) |

## Balance Sheet Presentation

```
ASSETS
Current Assets:
  Cash                           $XXX
  Accounts Receivable            $XXX
  Inventories:
    Raw Materials      $XXX
    Work in Process    $XXX
    Finished Goods     $XXX
  Total Inventories              $XXX
```

All three inventory accounts are **current assets** on the Balance Sheet.

## Cost of Goods Manufactured vs Cost of Goods Sold

**Cost of Goods Manufactured (COGM)**:
- Transfer from WIP → Finished Goods
- Completion of production
- Not yet an expense

**Cost of Goods Sold (COGS)**:
- Transfer from Finished Goods → Income Statement
- Point of sale to customer
- Becomes an expense

```
COGM = Beginning WIP + Manufacturing Costs - Ending WIP
COGS = Beginning FG + COGM - Ending FG
```

## Example: Manufacturing Timeline

**Day 1**: Buy $1,000 of wood
- Raw Materials: +$1,000

**Day 2**: Issue $800 to production, add $500 labor, $300 overhead
- Raw Materials: -$800
- WIP: +$1,600

**Day 3**: Complete 50 chairs (assume all WIP)
- WIP: -$1,600
- Finished Goods: +$1,600

**Day 4**: Sell 30 chairs ($960 of cost)
- Finished Goods: -$960
- COGS: +$960 (Income Statement)

## Related Topics

- [[Cost Flows]] - How costs move through these accounts
- [[Product vs Period Costs]] - What gets capitalized in inventory
- [[Product Costing]] - Calculating costs in WIP
- [[Work in Process Tracking]] - Managing the WIP account
- [[Cost of Goods Manufactured]] - Computing completed production

---

**Key Principle**: Three inventory accounts represent three production stages - before, during, and after manufacturing.