
---

## Data Types

Common SQL data types.

---

## Character Types

| Type | Description |
| --- | --- |
| `VARCHAR(n)` | Variable-length string (max n) |
| `CHAR(n)` | Fixed-length string (blank-padded) |
| `TEXT` | Unlimited variable-length string |

Note: CHAR may be faster for index lookups but requires length handling.

---

## Numeric Types

| Type | Description |
| --- | --- |
| `INT` / `INTEGER` | Whole numbers |
| `DECIMAL(p, s)` | Exact decimal (p total digits, s after decimal) |
| `FLOAT` | Floating-point number |
| `REAL` | Single-precision floating-point |

---

## Date/Time Types

| Type | Description |
| --- | --- |
| `DATE` | Date (year, month, day) |
| `TIME` | Time of day |
| `TIMESTAMP` | Date and time |

---

## Boolean

`BOOLEAN` - TRUE, FALSE, or NULL (in some databases)
