
---

## COALESCE

Returns the first non-NULL value from a list.

---

## Syntax

```sql
COALESCE(value1, value2, ...)
```

---

## Examples

```sql
SELECT COALESCE(1, NULL)      -- 1
SELECT COALESCE(NULL, 3)      -- 3
SELECT COALESCE(1, 2)         -- 1
SELECT COALESCE(NULL, NULL)   -- NULL
```

---

## Use Case: Full Outer Join

```sql
SELECT M.a, N.a, COALESCE(M.a, N.a) AS combined
FROM M
FULL JOIN N ON M.a = N.a
```

| M.a | N.a | combined |
| --- | --- | --- |
| 1 | NULL | 1 |
| 2 | 2 | 2 |
| NULL | 3 | 3 |
