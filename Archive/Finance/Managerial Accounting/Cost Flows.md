# Cost Flows

The movement of costs through manufacturing accounts from acquisition to sale.

## Overview

Product costs flow through **three inventory accounts** before becoming an expense:
1. Raw Materials Inventory
2. Work in Process Inventory
3. Finished Goods Inventory

## The Basic Flow Diagram

```
Raw Materials → Work in Process → Finished Goods → Cost of Goods Sold
  (Storage)      (Production)       (Warehouse)    (Income Statement)
     ↓               ↓                   ↓              ↓
Balance Sheet   Balance Sheet      Balance Sheet   Income Statement
```

## Detailed Cost Flows

### Materials Flow

**Raw Materials for Product**:
```
Purchase → Raw Materials Inventory → Work in Process → COGS
          (Balance Sheet)            (Balance Sheet)   (Income Statement)
```

**Office Materials** (Period Cost):
```
Purchase → Expense immediately
          (Income Statement)
```

### Labor Flow

**Production Wages** (Product Cost):
```
Incurred → Work in Process → Finished Goods → COGS
          (Balance Sheet)    (Balance Sheet)   (Income Statement)
```

**Administrative Salaries** (Period Cost):
```
Incurred → Expense immediately
          (Income Statement)
```

### Overhead Flow

**Manufacturing Overhead** (Product Cost):
```
Incurred → Work in Process → Finished Goods → COGS
          (Balance Sheet)    (Balance Sheet)   (Income Statement)
```

## Inventory Equation for Each Account

### General Formula
```
Beginning Inventory + Cost Added - Cost Transferred Out = Ending Inventory
```

### Raw Materials
```
BI + Materials Purchased - Materials Used = EI
```

### Work in Process
```
BI + Materials Used + Labor + Overhead - Cost of Goods Manufactured = EI
```

### Finished Goods
```
BI + Cost of Goods Manufactured - Cost of Goods Sold = EI
```

## Example: JetPack Manufacturing

**Given Information**:
- Raw materials purchased: $2,500
- Raw materials used: $2,000
- Production worker wages: $2,000
- Manufacturing equipment depreciation: $1,500
- Completed: 50 jetpacks
- Sold: 10 jetpacks

**Cost Calculations**:
```
Total Product Cost:
Direct Materials:     $2,000
Direct Labor:         $2,000
Manufacturing OH:     $1,500
─────────────────────────────
Total:               $5,500

Cost per unit: $5,500 / 50 = $110 per jetpack
COGS: 10 units × $110 = $1,100
```

## Journal Entries

### 1. Purchase Raw Materials
```
Dr. Raw Materials Inventory      2,500
    Cr. Accounts Payable/Cash           2,500
```

### 2. Use Materials in Production
```
Dr. Work in Process              2,000
    Cr. Raw Materials Inventory         2,000
```

### 3. Incur Direct Labor
```
Dr. Work in Process              2,000
    Cr. Salaries Payable                2,000
```

### 4. Apply Manufacturing Overhead
```
Dr. Work in Process              1,500
    Cr. Accumulated Depreciation        1,500
```

### 5. Complete Production
```
Dr. Finished Goods               5,500
    Cr. Work in Process                 5,500
```

### 6. Sell Products
```
Dr. Cost of Goods Sold           1,100
    Cr. Finished Goods                  1,100
```

## Transformation of Assets

**Financial Assets** → **Physical Assets** → **Revenue**

```
Cash
  ↓
Purchase materials, pay labor, incur overhead
  ↓
Raw Materials → WIP → Finished Goods
  ↓
Cost of Goods Sold (matched with Revenue)
  ↓
Net Income → Retained Earnings → Cash (cycle continues)
```

## Key Insights

### Work in Process is the "Factory Account"
- All product costs accumulate here during production
- Gets "drained" when products are completed
- Represents partially completed products

### Finished Goods is the "Warehouse Account"
- Holds completed products awaiting sale
- Only decreases when products are sold
- Transfer to COGS triggers expense recognition

### COGS is the Expense Account
- Only appears on Income Statement
- Matches product costs with sales revenue
- Timing: expensed when product sells, not when made

## Related Topics

- [[Product vs Period Costs]] - What flows through these accounts
- [[Archive/Finance/Managerial Accounting/Types of Inventory]] - The three inventory accounts
- [[Product Costing]] - Calculating costs that flow
- [[Work in Process Tracking]] - Detailed WIP management

---

**Key Principle**: Costs flow through Balance Sheet accounts (as assets) until the product is sold, then transfer to Income Statement (as expenses).