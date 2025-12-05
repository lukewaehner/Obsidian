
---

## RANK and ROW_NUMBER

Assign rankings to rows within partitions.

---

## RANK()

Assigns rank with gaps for ties.

```sql
SELECT *,
       RANK() OVER(PARTITION BY product ORDER BY price ASC) AS price_rank
FROM Purchase
```

---

## ROW_NUMBER()

Assigns unique sequential numbers (no ties).

```sql
SELECT *,
       ROW_NUMBER() OVER(ORDER BY price DESC) AS row_num
FROM Purchase
```

---

## DENSE_RANK()

Assigns rank without gaps for ties.

---

## Example

| Price | RANK() | DENSE_RANK() | ROW_NUMBER() |
| --- | --- | --- | --- |
| 100 | 1 | 1 | 1 |
| 100 | 1 | 1 | 2 |
| 200 | 3 | 2 | 3 |
| 300 | 4 | 3 | 4 |

- RANK: Same rank for ties, then skips
- DENSE_RANK: Same rank for ties, no skip
- ROW_NUMBER: Always unique
