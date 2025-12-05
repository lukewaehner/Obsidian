
---

## Inner Joins

Returns only rows that have matching values in both tables.

---

## Implicit Join (Comma Syntax)

```sql
SELECT pName, price
FROM Product, Company
WHERE manufacturer = cName
  AND country = 'Japan'
  AND price <= 200
```

---

## Explicit JOIN Syntax

```sql
SELECT LastName, E.DepartmentID, DepartmentName
FROM Employee E
JOIN Department D ON E.DepartmentID = D.DepartmentID
```

---

## Equi-Join

Join condition based on equality between columns.

Common columns may appear redundantly in result.

---

## Cross Join

Returns Cartesian product (every combination).

```sql
SELECT E.LastName, D.DepartmentName
FROM Employee E, Department D
-- No WHERE clause = cross join
```

Not recommended without a join condition.
