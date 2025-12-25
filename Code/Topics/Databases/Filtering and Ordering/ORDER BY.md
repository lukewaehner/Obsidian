
---

## ORDER BY

Sort results by one or more columns.

---

## Basic Syntax

```sql
SELECT pName, price, manufacturer
FROM Product
WHERE category = 'Gadgets' AND price > 10
ORDER BY price, pName
```

Sorts by price first, then breaks ties by pName.

---

## ASC and DESC

```sql
ORDER BY price DESC, pName ASC
```

- **ASC** - Ascending (default)
- **DESC** - Descending

---

## Important Note

Cannot ORDER BY a column not in SELECT when using DISTINCT:

```sql
-- ERROR: Cannot order by pName when selecting distinct categories
SELECT DISTINCT category
FROM Product
ORDER BY pName
```
