
---

## LIKE and Pattern Matching

Pattern matching for string comparisons.

---

## % Operator (Multi-Character)

Matches zero or more characters.

```sql
SELECT pName
FROM Product
WHERE pName LIKE '%izmo'
```

Returns: Gizmo, Powergizmo

---

## _ Operator (Single Character)

Matches exactly one character.

```sql
SELECT pName
FROM Product
WHERE pName LIKE '_izmo'
```

Returns: Gizmo (5 characters starting with any single char before "izmo")

---

## Common Patterns

| Pattern | Meaning |
| --- | --- |
| `'S%'` | Starts with S |
| `'%S'` | Ends with S |
| `'%S%'` | Contains S |
| `'S_S'` | S at both ends with one char in middle |

---

## Beyond LIKE

- **SIMILAR TO** - Extended pattern matching
- **POSIX regex** - substring(), regex_replace()
