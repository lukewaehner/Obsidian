
---

## Comparison Predicates

Operators for filtering in WHERE clauses.

---

## Numeric and String Comparisons

| Operator | Meaning |
| --- | --- |
| `=` | Equal to |
| `<` | Less than |
| `<=` | Less than or equal |
| `>` | Greater than |
| `>=` | Greater than or equal |
| `<>` or `!=` | Not equal |

---

## Range and Set Membership

| Predicate | Example |
| --- | --- |
| `BETWEEN x AND y` | `price BETWEEN 10 AND 100` |
| `IN (list)` | `category IN ('Gadgets', 'Electronics')` |
| `NOT IN (list)` | `category NOT IN ('Household')` |
