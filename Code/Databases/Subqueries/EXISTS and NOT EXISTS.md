
---

## EXISTS and NOT EXISTS

Test whether a subquery returns any rows.

---

## EXISTS

True if subquery returns at least one row.

```sql
SELECT DISTINCT S.sname
FROM Sailor S
WHERE EXISTS (
  SELECT R.sid
  FROM Reserves R
  WHERE R.sid = S.sid
    AND EXISTS (
      SELECT B.bid
      FROM Boat B
      WHERE B.bid = R.bid
        AND B.color = 'red'
    )
)
```

Finds sailors who reserved a red boat.

---

## NOT EXISTS

True if subquery returns zero rows.

```sql
SELECT DISTINCT S.sname
FROM Sailor S
WHERE NOT EXISTS (
  SELECT R.sid
  FROM Reserves R
  WHERE R.sid = S.sid
    AND EXISTS (
      SELECT B.bid
      FROM Boat B
      WHERE B.bid = R.bid
        AND B.color = 'red'
    )
)
```

Finds sailors who have NOT reserved a red boat.

---

## Double Negation Pattern

"Find X that satisfies ALL Y" = "Find X where NOT EXISTS Y that X doesn't satisfy"

```sql
-- Sailors who reserved ONLY red boats
SELECT DISTINCT S.sname
FROM Sailor S
WHERE NOT EXISTS (
  SELECT *
  FROM Reserves R, Boat B
  WHERE R.sid = S.sid
    AND R.bid = B.bid
    AND B.color != 'red'
)
```
