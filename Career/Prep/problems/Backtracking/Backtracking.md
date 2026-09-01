---
type: pattern
pattern: Backtracking
---

# Backtracking

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Backtracking")'
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
