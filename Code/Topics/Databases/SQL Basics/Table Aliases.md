
---

## Table Aliases (Tuple Variables)

Rename tables for clarity or self-joins.

---

## Syntax

```sql
SELECT X.pName, Y.address
FROM Person AS X, University AS Y
WHERE X.works_for = Y.uName
```

The `AS` keyword is optional:

```sql
FROM Person X, University Y
```

---

## Self-Joins

When you need to reference the same table twice.

**Find US companies that manufacture at least two different products:**

```sql
SELECT DISTINCT cName
FROM Product P1, Product P2, Company
WHERE country = 'USA'
  AND P1.manufacturer = cName
  AND P2.manufacturer = cName
  AND P1.pName != P2.pName
```

P1 and P2 are aliases for the same Product table.
