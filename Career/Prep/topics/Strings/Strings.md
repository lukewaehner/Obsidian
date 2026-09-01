---
type: group
group: Strings
---

# Strings

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Strings"'
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
