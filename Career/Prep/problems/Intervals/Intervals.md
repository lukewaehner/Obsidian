---
type: pattern
pattern: Intervals
---

# Intervals

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Intervals")'
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
