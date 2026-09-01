---
type: group
group: Data Structures
---

# Data Structures

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Data Structures"'
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
