
---

## Aggregate Functions

Functions that operate on sets of rows.

---

## Common Aggregates

| Function | Description |
| --- | --- |
| `COUNT(*)` | Number of rows |
| `COUNT(column)` | Number of non-NULL values |
| `COUNT(DISTINCT column)` | Number of unique non-NULL values |
| `SUM(column)` | Sum of values |
| `AVG(column)` | Average of values |
| `MIN(column)` | Minimum value |
| `MAX(column)` | Maximum value |

---

## Examples

```sql
SELECT avg(price)
FROM Car
WHERE price > 100
```

```sql
SELECT count(*) as n, max(price)
FROM Car
WHERE price > 100
```

```sql
SELECT sum(price * quantity)
FROM Purchase
WHERE product = 'Apple'
```

---

## Renaming Results

```sql
SELECT count(*) AS total_count
FROM Car
```
