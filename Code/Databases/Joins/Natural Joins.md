
---

## Natural Joins

Automatically joins on columns with the same name.

---

## Syntax

```sql
SELECT *
FROM Employee E
NATURAL JOIN Department D
WHERE E.DepartmentID = 34
```

Equivalent to:

```sql
SELECT *
FROM Employee E, Department D
WHERE E.DepartmentID = D.DepartmentID
  AND E.DepartmentID = 34
```

---

## Difference from Equi-Join

Natural join eliminates duplicate columns in the result.
