---
type: pattern
pattern: Linked List
---

# Linked List

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Linked List")'
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
