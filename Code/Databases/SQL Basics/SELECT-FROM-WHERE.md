
---

## SELECT-FROM-WHERE

The basic SQL query structure (SFW query).

```sql
SELECT <attributes>
FROM <one or more relations>
WHERE <conditions>
```

---

## Example

Given Product table:

| PName | Price | Category | Manufacturer |
| --- | --- | --- | --- |
| Gizmo | $19.99 | Gadgets | GizmoWorks |
| Powergizmo | $29.99 | Gadgets | GizmoWorks |
| SingleTouch | $149.99 | Photography | Canon |
| MultiTouch | $203.99 | Household | Hitachi |

**Select all gadgets:**

```sql
SELECT *
FROM Product
WHERE category = 'Gadgets'
```

Returns Gizmo and Powergizmo rows.

**Select expensive products:**

```sql
SELECT pName, price
FROM Product
WHERE price > 100
```

Returns SingleTouch and MultiTouch with their prices.

---

## Conceptual Evaluation Order

1. **FROM** - Get tables
2. **WHERE** - Filter rows
3. **SELECT** - Choose columns
4. **DISTINCT** - Remove duplicates (if specified)
