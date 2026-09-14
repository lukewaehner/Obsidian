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

# Project 5 — Distributed Key-Value Database (Part 1)

> [!danger] Due date not yet published for Fall 2026 · submitted via Gradescope by 11:59:59pm ET

Assignment for [[Distributed Systems]]. [Full spec](https://4730.network/docs/projects/raft/), retrieved 2026-09-13.
This page is the **shared spec for Parts 1 and 2** — see [[Project 6 - Distributed Key-Value Database (Part 2)]].

> [!bug] The spec page is stale — do not trust its numbering or dates
> The site's nav calls this "Projects 5 and 6", but the page body describes **Projects 3, 4, and
> 5** and gives deadlines of **Nov 25 2025 / Dec 5 2025 / Dec 10 2025** — last year's calendar.
> It also says "Projects 3, 4, and 5 are group projects." Three body milestones map onto two
> Fall 2026 project slots, and which is which is not stated. **Confirm the numbering and the real
> dates on Piazza before planning around them.**

> [!info] Projects are 40% of the grade in total, weighted by difficulty. No slip days on the final project. Group project — code sharing is allowed with your assigned partner only.

- [ ] Project 5 — Distributed Key-Value Database (Part 1)

## The Spec

Build a distributed, replicated key-value datastore supporting two client calls — `put(key, value)`
and `get(key)` — with **strong consistency**, by implementing a simplified **Raft**. The datastore
runs as multiple parallel replicas that use Raft to stay in consensus. Real-world analogues:
memcached, Redis, DynamoDB.

Graded on both correctness and performance: fewer packets scores higher, and lower query latency
scores higher.

### Your program

One program named **`4730kvstore`**, any language that compiles and runs on Gradescope.

- Compiled language → the executable is named `4730kvstore`
- Interpreted → the script is named `4730kvstore`, has a shebang, and is marked executable
- VM language (Java, C#) → a Bash wrapper named `4730kvstore` that takes the CLI below and launches
  the real program

```
./4730kvstore <UDP port> <your ID> <ID of second replica> [<ID of third replica> ...]
```

Replica IDs are unique four-digit hex numbers (`0AA1`, `F29A`). Clients also get IDs from the
simulator. A `Makefile` must be submitted **even if nothing needs compiling** (an empty one that
exits cleanly is fine).

### Libraries

Anything allowed on Gradescope, **except**:

- Any library implementing a consensus protocol — Raft, Paxos, Replicated View-state, Viewstamped
  Replication, Byzantine consensus, or similar
- Any library or package implementing a replicated key-value datastore (no thin wrappers over
  memcached)

Local storage libraries (SQLite, BerkeleyDB, LevelDB) are permitted for per-replica persistence.
Ask on Piazza if unsure. IDEs are fine during development, but the code must build and run from the
command line with no IDE dependency.

### Starter code

```bash
git clone git@github.khoury.northeastern.edu:cs4730/raft-starter-code.git
```

Python 3.6+; a bare-bones replica that connects to the LAN and broadcasts a no-op once a second.
Recommended only if you're comfortable with Python — port it yourself otherwise.

## Protocol Notes

### Message format

JSON dictionaries over local UDP sockets emulating a LAN. Every message carries at least:

| Key | Meaning |
| --- | --- |
| `src` | ID of the sender |
| `dst` | ID of the destination — `"FFFF"` multicasts to all replicas (expensive, use sparingly) |
| `leader` | ID of the believed leader, or `"FFFF"` if unknown |
| `type` | Message type |

The simulator routes on `src`/`dst` rather than IP, and learns the leader from the `leader` field —
so it must always be present. Custom types and extra keys are allowed and necessary for Raft.

**Required client-facing types** — the `MID` in a response must match the request:

```jsonc
// get
{"src": "<ID>", "dst": "<ID>", "leader": "<ID>", "type": "get", "MID": "<unique>", "key": "<key>"}
// put
{"src": "<ID>", "dst": "<ID>", "leader": "<ID>", "type": "put", "MID": "<unique>", "key": "<key>", "value": "<value>"}
// ok (get) — value included
{"src": "<ID>", "dst": "<ID>", "leader": "<ID>", "type": "ok", "MID": "<unique>", "value": "<value>"}
// ok (put)
{"src": "<ID>", "dst": "<ID>", "leader": "<ID>", "type": "ok", "MID": "<unique>"}
// fail — client retries
{"src": "<ID>", "dst": "<ID>", "leader": "<ID>", "type": "fail", "MID": "<unique>"}
// redirect — sent when a non-leader receives a client request
{"src": "<ID>", "dst": "<ID>", "leader": "<ID>", "type": "redirect", "MID": "<unique>"}
// hello — broadcast on startup so the simulator knows you're alive
{"src": "<ID>", "dst": "FFFF", "leader": "FFFF", "type": "hello", "MID": "<unique>"}
```

A `get()` for a key that was never `put()` returns **`ok` with an empty string value**, not a
failure.

Event-driven and single-threaded via `select()` / `poll()` is strongly encouraged.

### What you do *not* have to implement

- **True persistence** — data and the log can live in memory
- **Garbage collection** of the Raft log
- **Restarts** — replicas crash-fail permanently and never return

### Suggested build order

1. Respond to every `get()`/`put()` with `fail`
2. Raft leader election (§5.2); add `redirect` responses
3. Leader-failure timeout, and confirm the new election proceeds correctly
4. Empty `AppendEntries` RPC as a keepalive to suppress unnecessary elections
5. Transaction log + state machine (§5.3) — leader alone answers correctly, no replication yet
6. Real `AppendEntries` that ships data; commit only on quorum ← **the crux, budget the most time**
7. Retry failed commits; test on lossy networks
8. Election restrictions from §5.4.1; test lossy + failed leaders
9. The commit restriction in §5.4.2
10. Batch multiple outstanding log entries into one `AppendEntries`
11. Test, test, test

Start from the Raft paper — it's written to be readable. More resources on the Raft GitHub.

## Testing

A simulator is provided: it builds the emulated network and sockets, launches copies of your
replica, routes messages, and generates client requests. You don't modify it.

```
$ ./run [-h] [--replica REPLICA] [--silence] [--config_directory CONFIG_DIRECTORY] test
```

- `test` — path to a JSON test config, or `all`
- `--replica, -r` — path to your program (default `./4730kvstore`); **grading does not use this**
- `--silence, -s` — pipe replica stdout/stderr to `/dev/null`
- `--config_directory, -c` — where `all` looks for configs (default `./configs/`)

### Config file keys

| Key | Meaning |
| --- | --- |
| `lifetime` *(req)* | Seconds to run; at least 5 |
| `replicas` *(req)* | Number of replicas; at least 3 |
| `requests` *(req)* | Number of client `get()`/`put()` requests to generate |
| `mix` | Fraction of queries that are `get()`s (default `0.8`) |
| `wait` | Seconds before the first client request (default 2) |
| `end_wait` | Seconds to wait before measuring performance (default 2) |
| `seed` | Random seed, for semi-reproducible runs |
| `drops` | Fraction of inter-replica messages dropped (default 0) |
| `events` | List of `{type, time}` events |
| `tests` *(req)* | Correctness thresholds and `benchmarks` |

Event types: `kill_non_leader`, `kill_leader`, `part_easy` (leader keeps a quorum), `part_hard`
(leader loses its quorum), `part_end` (heal all partitions).

Correctness thresholds under `tests`: `maximum_get_fail_fraction` (0.5),
`maximum_put_fail_fraction` (0.5), `maximum_get_generation_fail_fraction` (0.1),
`maximum_appends_batched_fraction` (0.5).

`benchmarks` sets three thresholds per category, splitting extra credit / full / partial / no
credit: `total_msgs`, `failures`, `duplicates`, `median_latency` — **lower is better** in all four.

```json
{
  "lifetime": 30, "replicas": 5, "requests": 300, "mix": 0.2, "drops": 0.15, "end_wait": 5,
  "events": [{"type": "kill_leader", "time": 8}, {"type": "kill_leader", "time": 16}],
  "tests": { "benchmarks": {
    "total_msgs": [1000, 3000, 4000], "failures": [1, 10, 100],
    "duplicates": [0, 2, 10], "median_latency": [0.00015, 0.005, 0.05] } }
}
```

Performance is only assessed if the correctness checks pass. In `./run all` output, the four
performance tier numbers mean **Bonus (0), Passed (1), Needs Improvement (2), Failed (3)** for
total messages, failures/unanswered, duplicates, and median latency respectively. `all` mode is
what grading uses — if you fail there, you fail the grader.

## Implementation Log

## Submission Checklist

- [ ] `4730kvstore`, correctly named and executable
- [ ] `Makefile` (even if it does nothing)
- [ ] Thoroughly documented source
- [ ] **Teammate named in the Gradescope submission** — they get no credit otherwise
- [ ] Submitted

Per the (stale) spec, the first milestone only needs to pass **`simple-1`, `simple-2`, and
`crash-1`**, and only correctness is evaluated. All student code is run through plagiarism
detection.

## Related

- [[Project 6 - Distributed Key-Value Database (Part 2)]]
- [[Distributed Systems]]
- [[Week 07 - Quorums and Paxos]]
- [[Week 08 - Viewstamped Replication and BFT]]
