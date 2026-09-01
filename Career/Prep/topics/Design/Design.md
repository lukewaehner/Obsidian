---
type: group
group: Design
---

# Design

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Design"'
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
