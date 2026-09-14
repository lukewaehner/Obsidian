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

# Project 4 — Randomized Consensus Protocol

> [!danger] Due date not yet published · submitted via Gradescope by 11:59:59pm ET

Assignment for [[Distributed Systems]]. [Full spec](https://4730.network/docs/projects/random-consensus/), retrieved 2026-09-13.

> [!info] Projects are 40% of the grade in total, weighted by difficulty. Six slip days for Projects 1-4 and Homeworks 1-8; none on the final project or homework. Late penalty: `Original_Grade * (1 - ceiling(Seconds_Late / 86400) * 0.2)`. Code sharing is prohibited except with your assigned partner. Any language, but it must compile and run on Ubuntu Linux via Gradescope.

> [!warning] The binary is named `proj2`
> The spec's command line says `./proj2`, not `./proj4`, even though this is Project 4. Confirm on
> Piazza before submitting — the page appears to carry over naming from an earlier offering.

- [ ] Project 4 — Randomized Consensus Protocol

## The Spec

Implement **Ben-Or's randomized consensus protocol**. Also on page 85 of the Consensus slide deck
linked from the [schedule](https://4730.network/docs/schedule/).

- `input` — random boolean initial value, `[0,1]`
- `output` — boolean final consensus value
- `n` — number of nodes; `f` — faulty nodes permitted, with **`n/2 > f`**

```
begin
  pref  = input
  round = 1
  while true
    do_Protocol
  end
end

do_Protocol:
  send {"round": round, "pref": pref, "phase": 1, "ratify": 0} to all peers
  wait to receive (n - f) phase-1 messages

  if received more than (n / 2) phase-1 messages with the same pref
    send {"phase": 2, "round": round, "pref": pref, "ratify": 1} to all processes
  else
    send {"phase": 2, "round": round, "pref": -1,   "ratify": 0} to all processes

  wait to receive (n - f) phase-2 messages

  if received 1  {"phase": 2, "round": round, "pref": v, "ratify": 1} message
    pref = v
  if received > f {"phase": 2, "round": round, "pref": v, "ratify": 1} messages
    output = v
    print DONE:output
    exit
  else
    pref  = CoinFlip()
    round = round + 1

def CoinFlip() := random selection of 0 or 1
```

### Output contract

All peers communicate over a **single UDP socket on default port 50000**.

Exactly **one** line:

```
DONE: [output value, 0 or 1]; Round: [round number]
```

No extra debug output — use `--verbose` for that. The result must be deterministic: always the
correct value, no peer crashes, and **no more than `f` peers time out** during any run.

### Command line

```
$ ./proj2 [-h] --peers PEERS [PEERS ...] [--port PORT] [--f number of faulty nodes allowed] [--timeout max runtime in seconds] [--verbose]
```

`--peers`, `--f`, and `--port` are required. `--timeout` (default 300s) and `--verbose` must be
implemented but are optional.

### Running it

Starter code supplies a `Dockerfile` and `proj2-compose-5.yml`, `proj2-compose-11.yml`,
`proj2-compose-21.yml`. `FAULTS` must be exported so `--f` reaches the compose file:

```bash
export FAULTS=[num faults]; docker compose -f proj2-compose-[5,11,21].yml up --build
export FAULTS=[num faults]; docker compose -f proj2-compose-[5,11,21].yml up
```

## Design

## Protocol Notes

Event-driven and single-threaded via `select()` / `poll()` is encouraged; threaded is allowed but
much harder to debug.

## Implementation Log

## Testing

### Runtime analysis (15% of grade)

For 5-, 11-, and 21-node systems, find the **distribution** of rounds to consensus. At least 12
runs per `f` (more is fine); document the count.

| `n` nodes | `f` failures | Number of runs |
| --- | --- | --- |
| 5 | 1 |  |
| 5 | 2 |  |
| 11 | 1 |  |
| 11 | 2 |  |
| 11 | 5 |  |
| 21 | 1 |  |
| 21 | 4 |  |
| 21 | 10 |  |

Plot min, max, and 1st/3rd quartiles as a box-and-whisker chart — **all configurations on one
graph**, x-axis configuration, y-axis rounds to consensus. Written analysis explains the variation
within a system given `f`, and across systems with different `n`.

## Cited Sources

## Submission Checklist

All in the **root** of a `.zip` uploaded to Gradescope; a missing file scores 0.

- [ ] `Dockerfile`
- [ ] `proj2-compose-*.yml`
- [ ] `README.pdf` — high-level approach, challenges, how you tested, the analysis graphic and a
      short explanation (graph ~1/2 page, explanation 1/2 page, max 1 page)
- [ ] Source code (executable if it's a script)
- [ ] Submitted

**No autograder** — evaluated by hand.

## Grading

| Item | Percentage |
| --- | --- |
| Program correctness | 70% |
| Analysis | 15% |
| Style and documentation | 15% |

## Related

- [[Distributed Systems]]
- [[Week 04 - Consensus Algorithms]]
