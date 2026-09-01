---
type: pattern
pattern: Two Pointers
---

# Two Pointers

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Two Pointers")'
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
