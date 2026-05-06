
---

## PARTITION BY

Divides rows into groups for window function calculation.

---

## Syntax

```sql
aggregate_function() OVER(PARTITION BY column)
```

---

## Example

Average salary by department for each employee:

```sql
SELECT *, 
       AVG(Salary) OVER(PARTITION BY Department) AS Avg_Salary
FROM Employee
```

Each row gets the average salary for its department.

---

## Without PARTITION BY

Calculates over entire table:

```sql
SELECT *, 
       AVG(Salary) OVER() AS Overall_Avg
FROM Employee
```

Every row gets the same overall average.

---

## Comparison to GROUP BY

| GROUP BY | PARTITION BY |
| --- | --- |
| Reduces rows | Keeps all rows |
| Returns one row per group | Adds column to each row |
| Can't access individual row data | Can access all row data |
