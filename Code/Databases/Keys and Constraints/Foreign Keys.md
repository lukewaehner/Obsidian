
---

## Foreign Keys

Attribute that references a primary key in another table.

---

## Purpose

Enforces referential integrity - ensures relationships between tables are valid.

---

## Syntax

```sql
CREATE TABLE Product (
  pname CHAR(20) PRIMARY KEY,
  manufacturer CHAR(20),
  FOREIGN KEY (manufacturer) REFERENCES Company(cname)
);
```

---

## Referential Integrity

**Violations prevented:**

1. Cannot insert a product with manufacturer that doesn't exist in Company:

```sql
-- ERROR if 'NewCom' not in Company
INSERT INTO Product VALUES ('Gadget', 99.99, 'Electronics', 'NewCom');
```

2. Cannot delete a company that has products:

```sql
-- ERROR if Canon has products
DELETE FROM Company WHERE cname = 'Canon';
```

---

## NULL Foreign Keys

By default, NULL is allowed:

```sql
INSERT INTO Product VALUES ('Widget', 49.99, 'Tools', NULL);
-- OK: NULL manufacturer
```

Use NOT NULL to prevent:

```sql
manufacturer CHAR(20) NOT NULL
```
