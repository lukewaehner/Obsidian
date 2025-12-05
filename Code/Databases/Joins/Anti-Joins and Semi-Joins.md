
---

## Anti-Joins and Semi-Joins

Special join patterns for set operations.

---

## Anti-Join

Returns rows from left table that have NO match in right table.

```sql
SELECT eText, eid
FROM English
LEFT JOIN French ON eid = fid
WHERE fid IS NULL
```

Alternative:

```sql
SELECT *
FROM English
WHERE eid NOT IN (SELECT fid FROM French)
```

---

## Semi-Join

Returns rows from left table that HAVE a match in right table (without duplicating).

```sql
SELECT eText, eid
FROM English
LEFT JOIN French ON eid = fid
WHERE fid IS NOT NULL
```

Alternative using EXISTS:

```sql
SELECT *
FROM English
WHERE EXISTS (
  SELECT *
  FROM French
  WHERE eid = fid
)
```

---

## Key Difference

- **Anti-join**: Tuples in A that do NOT appear in B
- **Semi-join**: Tuples in A that DO appear in B (preserves A's columns only)
