---
tags:
  - assignment
  - distributed-systems
  - northeastern
  - cs4730
  - raft
type: assignment
course: "[[Distributed Systems]]"
due:
date: 2026-09-10
status: raw
---

# Project 6 — Distributed Key-Value Database (Part 2)

> [!danger] Due date not yet published for Fall 2026 · **hard deadline, no slip days** · Gradescope

Assignment for [[Distributed Systems]]. The spec is shared with Part 1 —
see [[Project 5 - Distributed Key-Value Database (Part 1)]] for the full protocol, message format,
simulator, and config reference. [Spec page](https://4730.network/docs/projects/raft/), retrieved 2026-09-13.

> [!bug] The spec page is stale — do not trust its numbering or dates
> The page body describes **Projects 3, 4, and 5** with **Nov 25 2025 / Dec 5 2025 / Dec 10 2025**
> deadlines — last year's calendar. Three body milestones map onto the two Fall 2026 slots in this
> vault, and the mapping is not stated anywhere. **Confirm on Piazza.**

- [ ] Project 6 — Distributed Key-Value Database (Part 2)

## What Changes From Part 1

Same program, same `4730kvstore` interface — the bar rises:

| Milestone (spec's numbering) | Must pass | Evaluated on |
| --- | --- | --- |
| "Project 3" | `simple-1`, `simple-2`, `crash-1` | Correctness only |
| "Project 4" | Every test except `advanced-*` | Correctness + style |
| "Project 5" (final) | **All** tests including `advanced-*` | Correctness + **performance** |

Each milestone regression-tests the earlier cases, so nothing you already pass may break.

The final milestone is where **performance** counts: total inter-replica messages, failures and
unanswered requests, duplicate responses, and median client latency — all lower-is-better, each
scored Bonus / Passed / Needs Improvement / Failed against the config's `benchmarks` thresholds.
Weight is skewed toward the harder test configurations.

The features that matter most for the `advanced-*` tests:

- [ ] Batched `AppendEntries` — multiple outstanding log entries per RPC
- [ ] Retry of failed commits under packet loss
- [ ] §5.4.1 election restrictions, and the §5.4.2 commit restriction
- [ ] Correct behavior across `part_easy` / `part_hard` / `part_end` partition events
- [ ] Minimized multicast (`dst: "FFFF"`) — it's expensive and inflates `total_msgs`

## Grading

| Item | "P3" | "P4" | "P5" |
| --- | --- | --- | --- |
| Program correctness | 25 | 85 | 70 |
| Performance | — | — | 20 |
| Style and documentation | — | 15 | 15 |

## Implementation Log

## Testing

```bash
./run all      # equivalent to the grading run
```

## Submission Checklist

- [ ] `4730kvstore` + `Makefile`
- [ ] Thoroughly documented source
- [ ] `README.md` — **plain text, no Word or PDF** — high-level approach, challenges faced,
      properties/features of the design you think are good, and how you tested
- [ ] **Teammate named in the Gradescope submission**
- [ ] Submitted

> [!danger] Hard deadline
> The final milestone accepts **no slip days and no late submissions**. Every project in the
> sequence must be turned in by that date.

## Related

- [[Project 5 - Distributed Key-Value Database (Part 1)]]
- [[Distributed Systems]]
- [[Week 07 - Quorums and Paxos]]
- [[Week 08 - Viewstamped Replication and BFT]]
