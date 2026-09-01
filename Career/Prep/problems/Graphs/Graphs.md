---
type: pattern
pattern: Graphs
---

# Graphs

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Graphs")'
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
