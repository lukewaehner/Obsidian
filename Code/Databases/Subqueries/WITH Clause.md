
---

## WITH Clause (Common Table Expressions)

Define temporary named relations for use in a query.

---

## Basic Syntax

```sql
WITH X AS (
  SELECT product, SUM(quantity) AS TQ
  FROM Purchase
  GROUP BY product
)
SELECT MAX(TQ) AS MTQ
FROM X
```

---

## Multiple CTEs

```sql
WITH 
  X AS (SELECT ...),
  Y AS (SELECT ...)
SELECT ...
FROM X, Y
WHERE ...
```

---

## Reusing CTEs

```sql
WITH X AS (
  SELECT product, sum(quantity) AS sales
  FROM Purchase
  GROUP BY product
)
SELECT product, sales
FROM X
WHERE sales = (SELECT max(sales) FROM X)
```

The CTE X is referenced twice.

---

## Benefits

- Improves readability
- Allows reuse of subquery results
- Can be more efficient than repeated subqueries
