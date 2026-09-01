---
type: group
group: Math & Bits
---

# Math & Bits

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Math & Bits"'
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
