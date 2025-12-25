
---

## HAVING

Filters groups after GROUP BY (can use aggregates).

---

## Evaluation Order

```sql
SELECT S
FROM R1, ..., Rn
WHERE C1
GROUP BY a1, ..., ak
HAVING C2
ORDER BY S2
```

1. **FROM** - Get tables
2. **WHERE** - Filter rows (condition C1)
3. **GROUP BY** - Group by attributes
4. **HAVING** - Filter groups (condition C2, may use aggregates)
5. **SELECT** - Compute aggregates, return result
6. **ORDER BY** - Sort rows

---

## WHERE vs HAVING

**WHERE** filters rows before grouping.

**HAVING** filters groups after grouping.

```sql
-- Using WHERE
SELECT Product, SUM(SaleAmount) AS TotalSales
FROM Sales
WHERE Product IN ('iPhone', 'Speakers')
GROUP BY Product
```

```sql
-- Using HAVING
SELECT Product, SUM(SaleAmount) AS TotalSales
FROM Sales
GROUP BY Product
HAVING Product IN ('iPhone', 'Speakers')
```

Both work here, but HAVING can use aggregates:

```sql
SELECT cName
FROM Product P, Company C
WHERE manufacturer = cName AND country = 'USA'
GROUP BY cName
HAVING count(*) >= 2
```
