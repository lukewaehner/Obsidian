
---

## Outer Joins

Preserve rows that don't have matches.

---

## LEFT JOIN

Returns all rows from left table, with matching rows from right (NULL if no match).

```sql
SELECT *
FROM English
LEFT JOIN French ON eid = fid
```

---

## RIGHT JOIN

Returns all rows from right table, with matching rows from left (NULL if no match).

```sql
SELECT *
FROM English
RIGHT JOIN French ON eid = fid
```

---

## FULL OUTER JOIN

Returns all rows from both tables (NULL where no match).

```sql
SELECT *
FROM English
FULL JOIN French ON eid = fid
```

---

## Example

English table: eid 1-6
French table: fid 2, 5, 7, 8

**INNER JOIN**: Returns eid/fid 2, 5 only

**LEFT JOIN**: Returns all English (1-6), with French data where available

**RIGHT JOIN**: Returns all French (2, 5, 7, 8), with English data where available

**FULL JOIN**: Returns all from both tables
