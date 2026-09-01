---
type: pattern
pattern: Advanced Graphs
---

# Advanced Graphs

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Advanced Graphs")'
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
