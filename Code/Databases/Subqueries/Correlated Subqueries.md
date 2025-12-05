
---

## Correlated Subqueries

Inner query references columns from outer query.

---

## Example

For each company, find the most expensive product:

```sql
SELECT C2.cname, P2.pname, P2.price
FROM Company C2, Product P2
WHERE C2.cid = P2.cid
  AND P2.price = (
    SELECT max(P1.price)
    FROM Product P1
    WHERE P1.cid = C2.cid
  )
```

The inner query references `C2.cid` from the outer query.

---

## Evaluation

For each row in outer query:
1. Evaluate inner query using outer row's values
2. Check if outer row satisfies condition

---

## Performance Note

Correlated subqueries can be slow because inner query runs once per outer row.
