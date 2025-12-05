
---

## Window Function Basics

Aggregates that return a value for each row without collapsing rows.

---

## Syntax

```sql
aggregate_function() OVER (window_specification)
```

---

## Example Without Window Function

Find price difference from minimum price:

```sql
WITH X AS (
  SELECT min(price) AS minp
  FROM Purchase
)
SELECT P.*, price - minp AS delta
FROM Purchase P, X
```

---

## Example With Window Function

```sql
SELECT *, 
       price - min(price) OVER() AS delta
FROM Purchase
```

The `OVER()` clause considers the entire table.

---

## Key Difference from GROUP BY

- GROUP BY reduces rows (one per group)
- Window functions keep all rows, adding computed values

```sql
-- GROUP BY: Returns one row per product
SELECT product, sum(quantity) AS sum_prod
FROM Purchase
GROUP BY product

-- Window function: Returns all rows with sum added
SELECT *, sum(quantity) OVER(PARTITION BY product) AS sum_prod
FROM Purchase
```
