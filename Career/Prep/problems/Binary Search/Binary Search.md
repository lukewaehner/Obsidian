---
type: pattern
pattern: Binary Search
---

# Binary Search

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Binary Search")'
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
