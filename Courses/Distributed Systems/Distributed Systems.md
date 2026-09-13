---
tags:
  - distributed-systems
  - northeastern
  - cs4730
  - hub
type: moc
semester_start: 2026-09-07
---
# Distributed Systems

**CS 4730 — Distributed Systems** · Fall 2026 · Northeastern (Khoury) · Section 01

**Course Focus**: An introduction to distributed systems — the fundamental concepts (time and
event ordering, consensus, replication, fault tolerance) and how they get applied when building
reliable distributed systems and services. The back half of the course reads real systems
(Dynamo, Cassandra, GFS, BigTable, Spanner, DNS) against those concepts.

> [!info] Source
> Canvas for CS 4730 is empty — no assignments, no modules, no files, no syllabus body. The real
> course lives at **[4730.network](https://4730.network/)**. Everything below is from
> [the syllabus](https://4730.network/docs/syllabus/) and [schedule](https://4730.network/docs/schedule/),
> retrieved 2026-09-10.

## Logistics

|  |  |
| --- | --- |
| **Instructor** | Prof Alden Jackson — a.jackson@northeastern.edu |
| **Time** | Tuesday 11:45 AM–1:25 PM · Thursday 2:50 PM–4:30 PM |
| **Room** | Shillman Hall 105 |
| **Office Hours** | By appointment — [book via Outlook](https://outlook.office.com/book/KhouryCS4730@northeastern.onmicrosoft.com/?ismsaljsauthenabled) |
| **TAs** | Palak Gupta · Karthik Kasaraneni |
| **TA Office Hours** | In person, TBD (starting week of 9/8) |

In-person attendance is expected and there are **no regular recordings**.

## Links

- [Course site](https://4730.network/) — syllabus, schedule, project specs
- [Piazza](https://piazza.com/northeastern/fall2026/cs473013196202710/home) — the class forum
- [Gradescope](https://www.gradescope.com/courses/1388933) — all submissions
- [Canvas](https://northeastern.instructure.com/courses/260754) — grades and SSO only
- Canvas also exposes Poll Everywhere, Panopto, Qwickly Attendance, and Zoom tabs

## Materials

- **Textbook** — Coulouris, Dollimore, Kindberg, and Blair, *Distributed Systems: Concepts and Design*, 5th ed.
- **Week 1 reading** — [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/) and "Why are Distributed Systems so Hard?"
- **Languages** — projects may be in any language, but must compile and run on **Ubuntu Linux** via Gradescope.

## Grading

| Weight | Component |
| --- | --- |
| 60% | Homeworks and quizzes — 8 total, equally weighted |
| 40% | Projects — 6 total, weighted by difficulty |

**No final exam in Fall 2026.**

| Grade | Range | Grade | Range |
| --- | --- | --- | --- |
| A | [93 - 100] | C | [73 - 76] |
| A- | [90 - 92] | C- | [70 - 72] |
| B+ | [87 - 89] | D+ | [67 - 69] |
| B | [83 - 86] | D | [63 - 66] |
| B- | [80 - 82] | D- | [60 - 62] |
| C+ | [77 - 79] | F | [0 - 60] |

### Slip Days

**Six per semester**, usable on Projects 1-4 and Homeworks 1-8 — **not** on the final project or
final homework. Once slip days are gone:

```
Original_Grade * (1 - ceiling(Seconds_Late / 86400) * 0.2)
```

### Collaboration and AI

Discussing with peers is fine. **Sharing code is prohibited** except with your assigned partner.
Online code must be cited with a link, and copying large blocks is not allowed. Unless a
specific assignment says otherwise, **using LLMs, chatbots, or AI agents to complete homework or
projects is prohibited**.

## Deliverables

| Due | Deliverable |
| --- | --- |
| Tue 2026-09-15 | [[Docker Tutorial]] |
| TBD | [[Project 1 - HELLO-ACK Protocol]] |
| TBD | [[Project 2 - Time Agreement Protocol]] |
| TBD | [[Project 3 - Chandy-Lamport]] |
| TBD | [[Project 4 - Randomized Consensus Protocol]] |
| TBD | [[Project 5 - Distributed Key-Value Database (Part 1)]] |
| TBD | [[Project 6 - Distributed Key-Value Database (Part 2)]] |

> [!todo] Not yet scaffolded
> The syllabus counts **8 homeworks and quizzes together**, without naming or dating them, so
> there are no homework notes yet — creating a file named `Homework 1` under `assignments/` will
> scaffold itself from the course template. Project due dates aren't published either; the
> project pages on the course site are index stubs so far.

## Map of These Notes

**[[CS4730 Assignments.base|CS4730 Assignments]]** is the tracker — Upcoming, All assignments,
No due date, and Topics views.

```
assignments/  projects, homeworks, quizzes
topics/       one note per week, following the course site's own week structure
```

> [!warning] Meeting dates are derived
> The course site's schedule is week-based with no calendar dates. The Tue/Thu dates in the week
> notes are computed from the first class (Thu 2026-09-10, per Prof Jackson's welcome
> announcement). Week 12 is listed as "November Break" — confirm whether either day meets.

### Weeks

- [[Week 01 - Introduction and Networking]]
- [[Week 02 - Networking Primer]]
- [[Week 03 - Time, Global States, and Failure Detectors]]
- [[Week 04 - Consensus Algorithms]]
- [[Week 05 - Process Groups, Leader Election, and Multicast]]
- [[Week 06 - Distributed Commit]]
- [[Week 07 - Quorums and Paxos]]
- [[Week 08 - Viewstamped Replication and BFT]]
- [[Week 09 - P2P Overlays, Gossip, and DHTs]]
- [[Week 10 - Real Systems I - Dynamo and Cassandra]]
- [[Week 11 - Real Systems II - GFS, BigTable, Spanner]]
- [[Week 12 - November Break]]
- [[Week 13 - ACMS and DNS]]
- [[Week 14 - Class Summary]]
- [[Week 15 - Finals Week]]

---

**Course Number**: CS 4730
**Semester**: Fall 2026
**Topics**: Networking, Event Ordering, Logical Clocks, Global States, Failure Detectors, Consensus, Leader Election, Multicast, Two- and Three-Phase Commit, Quorums, Paxos, Viewstamped Replication, Byzantine Fault Tolerance, P2P Overlays, Gossip Protocols, DHTs, Dynamo, Cassandra, GFS, BigTable, Spanner, DNS

%% Begin Waypoint %%
- **assignments**
	- [[Docker Tutorial]]
	- [[Project 1 - HELLO-ACK Protocol]]
	- [[Project 2 - Time Agreement Protocol]]
	- [[Project 3 - Chandy-Lamport]]
	- [[Project 4 - Randomized Consensus Protocol]]
	- [[Project 5 - Distributed Key-Value Database (Part 1)]]
	- [[Project 6 - Distributed Key-Value Database (Part 2)]]
- **topics**
	- [[Week 01 - Introduction and Networking]]
	- [[Week 02 - Networking Primer]]
	- [[Week 03 - Time, Global States, and Failure Detectors]]
	- [[Week 04 - Consensus Algorithms]]
	- [[Week 05 - Process Groups, Leader Election, and Multicast]]
	- [[Week 06 - Distributed Commit]]
	- [[Week 07 - Quorums and Paxos]]
	- [[Week 08 - Viewstamped Replication and BFT]]
	- [[Week 09 - P2P Overlays, Gossip, and DHTs]]
	- [[Week 10 - Real Systems I - Dynamo and Cassandra]]
	- [[Week 11 - Real Systems II - GFS, BigTable, Spanner]]
	- [[Week 12 - November Break]]
	- [[Week 13 - ACMS and DNS]]
	- [[Week 14 - Class Summary]]
	- [[Week 15 - Finals Week]]
- [[CS4730 Assignments.base|CS4730 Assignments]]
- [[Distributed Systems]]

%% End Waypoint %%
