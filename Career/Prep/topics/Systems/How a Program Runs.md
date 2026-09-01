---
type: topic
group: Systems
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# How a Program Runs

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

From source to execution: a program is compiled/assembled into instructions,
loaded into memory, and stepped through by the CPU one fetch-decode-execute
cycle at a time.

## How it works

The CPU fetches an instruction from memory, decodes what it says to do, and
executes it (often via the ALU for arithmetic/logic), then advances to the
next instruction — registers and RAM hold the state this cycle reads and
writes.

## Implementation

[[Code/Computer Systems/CPU Basics|CPU Basics]],
[[Code/Computer Systems/Data & Registers|Data & Registers]], and
[[Code/Computer Systems/Kernels/OS Boot Process|OS Boot Process]] cover this
in more depth from the coursework side.

## Complexity

## When to use it

## Gotchas

## Resources

- [How CPU executes a program (video)](https://www.youtube.com/watch?v=XM4lGflQFvA)
- [How computers calculate - ALU (video)](https://youtu.be/1I5ZMmrOfnA)
- [Registers and RAM (video)](https://youtu.be/fpnE6UAfbtU)
- [The Central Processing Unit (CPU) (video)](https://youtu.be/FZGugFqdr60)
- [Instructions and Programs (video)](https://youtu.be/zltgXvg6r3k)
- [NAND to Tetris: Build a Modern Computer from First Principles](https://www.coursera.org/learn/build-a-computer)

## Problems

_None yet._
