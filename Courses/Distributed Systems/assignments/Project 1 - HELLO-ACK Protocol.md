---
tags:
  - assignment
  - distributed-systems
  - northeastern
  - cs4730
type: assignment
course: "[[Distributed Systems]]"
due:
date: 2026-09-10
status: raw
---

# Project 1 — HELLO-ACK Protocol

> [!danger] Due date not yet published · submitted via Gradescope by 11:59:59pm ET

Assignment for [[Distributed Systems]]. [Full spec](https://4730.network/docs/projects/hello-ack/), retrieved 2026-09-13.

> [!info] Projects are 40% of the grade in total, weighted by difficulty. Six slip days for Projects 1-4 and Homeworks 1-8; none on the final project or homework. Late penalty: `Original_Grade * (1 - ceiling(Seconds_Late / 86400) * 0.2)`. Code sharing is prohibited except with your assigned partner. Any language, but it must compile and run on Ubuntu Linux via Gradescope.

- [ ] Project 1 — HELLO-ACK Protocol

## The Spec

Write an **asynchronous** program implementing a Hello-Ack protocol of your own design. Every
peer discovers that it has heard from and acknowledged every other peer that was launched, then
terminates.

### Output contract

Exactly **one** line, and nothing else — extra debug output loses points.

- Every peer except one prints `DONE: number of rounds`
- The peer with the **lowest IP address** prints
  `DONE: number of rounds` followed by a comma-separated list of `(domain name, IP address)` for
  the source of every `ACK` it received. That list must cover **every process started**.

Use `--verbose` for debugging output instead of bare prints.

The run must be **deterministic**: it always reaches the correct result and no peer crashes.

### Command line

```
$ ./proj1 [-h] --peers PEERS [PEERS ...] [--port PORT] [--timeout TIMEOUT] [--verbose]
```

`--peers` is required. `--port`, `--timeout`, and `--verbose` must all be **implemented** but are
optional on the command line.

### Running it

A `Dockerfile` and `proj1-compose.yml` ship with the starter code. Both may be modified, but
**evaluation uses the supplied compose file**.

```bash
docker compose -f proj1-compose.yml up --build   # build and run
docker compose -f proj1-compose.yml up           # run after building
```

### Starter code

Template repo on the Khoury GitHub server — a peer that opens a UDP socket, sends `HELLO` to its
peers, and prints everything it receives. Optional basis for the project.

## Design

> [!warning] Design review is 30% of the grade
> You must review your protocol with a TA **no less than five (5) weekdays before submitting**.
> Scheduling system will be posted on Piazza. Book this early.

The review must address, at minimum:

- [ ] UDP is used — state the port number
- [ ] Specification of every message: contents, format, and field values (hint: use JSON)
- [ ] The protocol that determines all launched nodes have been heard from and acknowledged
- [ ] The condition that **deterministically** ends the run — how does each peer know to stop?
- [ ] How the round count per peer is captured

## Protocol Notes

Suggested style is **event-driven and single-threaded**: `select()` or `poll()` on the datagram
socket (the starter code shows this). A thread-per-socket model is allowed but is substantially
harder to debug.

## Implementation Log


## Testing

### Runtime analysis (required, 10% of grade)

For **5-, 11-, 21-, and 51-node** systems, find the average number of rounds to reach consensus
and exit. Each `n` runs `ceil(log_1.5(n^2))` times; document the run count in the write-up.

| Nodes in system | Number of runs | Average rounds |
| --- | --- | --- |
| 5 |  |  |
| 11 |  |  |
| 21 |  |  |
| 51 |  |  |

Written analysis: explain the variation between individual runs at each `n`, and what that says
about the complexity of starting and managing distributed systems with large node counts. Table
plus analysis go in **`table.pdf`**.

## Cited Sources

Online code must be cited with a link; large blocks may not be copied. LLMs, chatbots, and AI
agents are prohibited on this project.

## Submission Checklist

All of the following in the **root** of a `.zip`, uploaded to Gradescope. A missing required file
scores 0.

- [ ] `Dockerfile`
- [ ] `proj1-compose.yml`
- [ ] Source code
- [ ] `table.pdf`
- [ ] Submitted

**No autograder** — evaluated by hand.

## Grading

| Item | Percentage |
| --- | --- |
| Design review | 30% |
| Program correctness | 40% |
| Runtime table | 10% |
| Style and documentation | 20% |

## Related

- [[Distributed Systems]]
- [[Docker Tutorial]]
- [[Week 01 - Introduction and Networking]]
- [[Week 02 - Networking Primer]]
