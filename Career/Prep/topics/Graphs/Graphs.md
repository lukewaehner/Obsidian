---
type: group
group: Graphs
---

# Graphs

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Graphs"'
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
