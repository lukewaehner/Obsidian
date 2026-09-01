---
type: group
group: Design
---

# Design

## Resources

- [The System Design Primer](https://github.com/donnemartin/system-design-primer) — start here
- [MIT 6.824: Distributed Systems, Spring 2020 (20 videos)](https://www.youtube.com/watch?v=cQP8WApzIQQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB)

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
