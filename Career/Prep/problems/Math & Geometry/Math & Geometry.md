---
type: pattern
pattern: Math & Geometry
---

# Math & Geometry

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Math & Geometry")'
views:
  - type: table
    name: Problems
    order:
      - number
      - file.name
      - difficulty
      - time
      - space
      - aid
      - solved_on
      - revisit
```

← [[Prep]]
