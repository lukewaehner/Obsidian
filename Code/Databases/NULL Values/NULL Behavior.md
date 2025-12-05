
---

## NULL Behavior

How NULL affects different operations.

---

## Arithmetic

Any arithmetic with NULL produces NULL.

```sql
SELECT 5 + NULL  -- NULL
SELECT NULL * 10 -- NULL
```

---

## Comparisons

Comparisons with NULL produce UNKNOWN (not TRUE or FALSE).

```sql
SELECT NULL = NULL   -- UNKNOWN (not TRUE!)
SELECT NULL < 5      -- UNKNOWN
SELECT 5 = NULL      -- UNKNOWN
```

---

## Testing for NULL

Use IS NULL or IS NOT NULL:

```sql
SELECT *
FROM Person
WHERE age IS NULL
```

Cannot use `= NULL`:

```sql
-- WRONG: This doesn't work!
SELECT * FROM Person WHERE age = NULL
```

---

## Aggregates and NULL

- `COUNT(*)` counts all rows including NULL
- `COUNT(column)` counts non-NULL values only
- `SUM`, `AVG`, `MIN`, `MAX` ignore NULL values

| v |
| --- |
| 1 |
| 2 |
| NULL |

- `COUNT(*)` = 3
- `COUNT(v)` = 2
- `SUM(v)` = 3
- `AVG(v)` = 1.5
