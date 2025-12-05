
---

## Primary Keys

Minimal subset of attributes that uniquely identifies each tuple.

---

## Properties

- Unique: No two tuples can have the same key value
- Minimal: No subset of the key is also unique
- Not NULL: Key attributes cannot be NULL

---

## Syntax

Column-level:

```sql
CREATE TABLE Company (
  cname CHAR(20) PRIMARY KEY,
  country CHAR(20)
);
```

Table-level (for composite keys):

```sql
CREATE TABLE Enrollment (
  sid INT,
  cid INT,
  grade CHAR(1),
  PRIMARY KEY (sid, cid)
);
```

---

## Key Constraint

If two tuples agree on key values, they must be the same tuple.

Attempting to insert a duplicate key causes an error.
