---
type: group
group: Sorting & Searching
---

# Sorting & Searching

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Sorting & Searching"'
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
