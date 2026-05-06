
---

## Other Constraints

Additional rules for data integrity.

---

## NOT NULL

Column cannot contain NULL values.

```sql
CREATE TABLE Person (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);
```

---

## UNIQUE

Column(s) must have unique values (like primary key but allows NULL).

```sql
CREATE TABLE Employee (
  id INT PRIMARY KEY,
  email VARCHAR(100) UNIQUE
);
```

---

## CHECK

Custom condition that must be true.

```sql
CREATE TABLE Product (
  id INT PRIMARY KEY,
  price DECIMAL(10, 2) CHECK (price > 0),
  quantity INT CHECK (quantity >= 0)
);
```

---

## DEFAULT

Specifies default value when none provided.

```sql
CREATE TABLE Orders (
  id INT PRIMARY KEY,
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
