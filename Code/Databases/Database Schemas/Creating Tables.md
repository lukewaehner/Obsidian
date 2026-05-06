
---

## Creating Tables

DDL statements for defining table structure.

---

## Basic Syntax

```sql
CREATE TABLE Company (
  cname CHAR(20) PRIMARY KEY,
  stockPrice INT,
  country CHAR(20)
);

CREATE TABLE Product (
  pname CHAR(20),
  price DECIMAL(9, 2),
  category CHAR(20),
  manufacturer CHAR(20),
  PRIMARY KEY (pname),
  FOREIGN KEY (manufacturer) REFERENCES Company(cname)
);
```

---

## Column Definitions

Each column has:
- Name
- Data type
- Optional constraints (PRIMARY KEY, NOT NULL, etc.)

---

## Table Constraints

Defined after columns:
- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- CHECK
