---
type: group
group: Complexity
---

# Complexity

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Complexity"'
views:
  - type: table
    name: Progress
    order:
      - file.name
      - tier
      - status
      - coverage
      - confidence
      - updated
    groupBy:
      property: tier
      direction: ASC
```

← [[Prep]]
