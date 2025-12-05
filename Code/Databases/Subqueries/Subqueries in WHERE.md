
---

## Subqueries in WHERE

Use query results in WHERE conditions.

---

## IN Operator

```sql
SELECT C.country
FROM Company C
WHERE C.cname IN (
  SELECT P.manufacturer
  FROM Purchase PU, Product P
  WHERE P.pname = PU.pname
    AND PU.buyer = 'Joe B'
)
```

---

## Comparison with Subquery

```sql
SELECT DISTINCT P2.product, P2.price AS mp
FROM Purchase P2
WHERE P2.price = (
  SELECT max(price)
  FROM Purchase
)
```

---

## ANY / SOME

True if comparison is true for at least one value.

```sql
SELECT DISTINCT C.cname
FROM Company C
WHERE 25 > ANY (
  SELECT price
  FROM Product P
  WHERE P.cid = C.cid
)
```

---

## ALL

True if comparison is true for all values.

```sql
SELECT DISTINCT C.cname
FROM Company C
WHERE 25 > ALL (
  SELECT P.price
  FROM Product P
  WHERE C.cid = P.cid
)
```

Finds companies where ALL products cost less than 25.
