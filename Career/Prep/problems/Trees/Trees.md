---
type: pattern
pattern: Trees
---

# Trees

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Trees")'
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
