---
type: pattern
pattern: Sliding Window
---

# Sliding Window

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Sliding Window")'
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
