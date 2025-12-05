
---

## Three-Valued Logic

SQL uses TRUE, FALSE, and UNKNOWN.

---

## Truth Values

Think of them as numbers:
- FALSE = 0
- UNKNOWN = 0.5
- TRUE = 1

---

## AND

Returns minimum value.

| AND | FALSE | UNKNOWN | TRUE |
| --- | --- | --- | --- |
| FALSE | FALSE | FALSE | FALSE |
| UNKNOWN | FALSE | UNKNOWN | UNKNOWN |
| TRUE | FALSE | UNKNOWN | TRUE |

---

## OR

Returns maximum value.

| OR | FALSE | UNKNOWN | TRUE |
| --- | --- | --- | --- |
| FALSE | FALSE | UNKNOWN | TRUE |
| UNKNOWN | UNKNOWN | UNKNOWN | TRUE |
| TRUE | TRUE | TRUE | TRUE |

---

## NOT

NOT TRUE = FALSE
NOT FALSE = TRUE
NOT UNKNOWN = UNKNOWN

---

## WHERE Clause

Only rows where condition is TRUE are returned.
UNKNOWN is treated like FALSE.

```sql
-- Does NOT return rows where age is NULL
SELECT * FROM Person
WHERE age < 25 OR age >= 25
```

To include NULL:

```sql
SELECT * FROM Person
WHERE age < 25 OR age >= 25 OR age IS NULL
```
