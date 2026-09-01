---
type: pattern
pattern: Tries
---

# Tries

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Tries")'
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
