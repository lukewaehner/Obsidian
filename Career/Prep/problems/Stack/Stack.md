---
type: pattern
pattern: Stack
---

# Stack

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Stack")'
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
