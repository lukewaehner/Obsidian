---
tags:
  - lecture
  - distributed-systems
  - northeastern
  - cs4730
  - time-global-states-failure-detectors
type: lecture
course: "[[Distributed Systems]]"
module: 3
week: 3
date: 2026-09-10
status: raw
---

# Week 03 — Time, Global States, and Failure Detectors

Lecture for [[Distributed Systems]].

> [!info] Time in distributed systems; Global states; Failure detectors. Meeting dates are derived — the course site's schedule is week-based with no calendar dates. Tue/Thu pattern anchored on the first class, Thu 2026-09-10.

## Meetings

- **Tue Sep 22**
- **Thu Sep 24**
- **Tue Sep 29** — spillover from the one-meeting slip

> [!note] Running one meeting behind
> The Tue Sep 15 lecture was cancelled (see [[Week 02 - Networking Primer]]), so from Week 03 on
> each topic lands one meeting later than the course site's week grid. Dates below include that slip.

## Assigned Material

- [ ] Slides: [Event Ordering](https://4730.network/slides/cs4730_ds_time_awj.pptx) (pptx)

## Notes

Challenge 1: Global State
No host has global knowledge
Need to use network to exchange state information
- Network capacity is limited, it can't send everything
Information may be incorrect, out of date, etc
- New information takes time to propagate
- Other changes may happen in the meantime
Key issue: how can you detect and address inconsistencies?

Challenge 2: Time
Time cannot be measured perfectly
- Hosts have different clocks, skew
- Network can delay / duplicate messages
How do we determine what happened first?
- Who shot first in a game
- Who bought the last seat on a plane?
Need a more nuanced abstraction to represent time

Ordering events:
Message based:
- Send & receive
Time is essential for ordering events:
- Physical Time
	- Global time
	- Local time
- Logical time
	- Lamport clock
	- Vector clock


## Key Takeaways

- 

## Open Questions

- 

## Related

- [[Distributed Systems]]
