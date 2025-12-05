
---

## Subqueries in FROM (Derived Tables)

Use query results as a temporary table.

---

## Example

Find the maximum total quantity sold for any product:

```sql
SELECT MAX(TQ) AS MTQ
FROM (
  SELECT product, SUM(quantity) AS TQ
  FROM Purchase
  GROUP BY product
) X
```

The subquery creates a derived table X with product totals.

---

## Filtering Aggregated Results

```sql
SELECT *
FROM (
  SELECT product,
         sum(quantity) AS SumQ,
         max(price) AS MaxP
  FROM Purchase
  GROUP BY product
) X
WHERE SumQ > 50
```

Alternative using HAVING:

```sql
SELECT product, sum(quantity) AS SumQ, max(price) AS MaxP
FROM Purchase
GROUP BY product
HAVING sum(quantity) > 50
```
