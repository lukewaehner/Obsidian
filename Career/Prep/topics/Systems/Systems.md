---
type: group
group: Systems
---

# Systems

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Systems"'
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
