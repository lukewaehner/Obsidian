---
type: group
group: Trees
---

# Trees

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Trees"'
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
