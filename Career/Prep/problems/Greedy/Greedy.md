---
type: pattern
pattern: Greedy
---

# Greedy

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Greedy")'
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
