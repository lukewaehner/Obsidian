
---

## GROUP BY

Groups rows that have the same values in specified columns.

---

## Syntax

```sql
SELECT product, sum(quantity) AS TQ
FROM Purchase
WHERE price > 1
GROUP BY product
```

Groups purchases by product, then sums quantity for each group.

---

## Rules

- Every column in SELECT must either be:
  - In the GROUP BY clause, OR
  - Inside an aggregate function

```sql
-- ERROR: price not in GROUP BY or aggregate
SELECT product, sum(quantity) AS TQ, price
FROM Purchase
GROUP BY product
```

---

## Example

```sql
SELECT color, avg(numc) AS anc
FROM Shapes
GROUP BY color
```

Groups shapes by color, returns average number of corners per color.
