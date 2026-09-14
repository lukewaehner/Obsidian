---
type: topic
group: Systems
tier: core
confidence:
sections_total: 6
sections_done: 5
coverage: 0.83
status: learning
updated: 2026-09-13
---

# How a Program Runs

← [[Career/Prep/topics/Systems/Systems|Systems]]

> [!abstract]- Coverage — 5/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

From source to execution: a program is compiled/assembled into instructions,
loaded into memory, and stepped through by the CPU one fetch-decode-execute
cycle at a time.

## How it works

The CPU fetches an instruction from memory, decodes what it says to do, and
executes it (often via the ALU for arithmetic/logic), then advances to the
next instruction — registers and RAM hold the state this cycle reads and
writes.

The build side of the same story: `hello.c → preprocessor → .i → compiler → .s → assembler → .o → linker → executable`, and where bytecode VMs (JVM, CPython) diverge from it — [[Code/Computer Systems/Assembly/Assembly & Compilation Pipeline|Assembly & Compilation Pipeline]]. The ISA is the contract between the two halves — [[Code/Computer Systems/CPU Basics|CPU Basics]].

## Implementation

[[Code/Computer Systems/CPU Basics|CPU Basics]],
[[Code/Computer Systems/Data & Registers|Data & Registers]], and
[[Code/Computer Systems/Kernels/OS Boot Process|OS Boot Process]] cover this
in more depth from the coursework side.

Also: the stack frame built on call and torn down on return via `%rsp`/`%rbp` ([[Code/Computer Systems/Stack & Functions|Stack & Functions]]), the instruction set itself ([[Code/Computer Systems/Assembly/Assembly Instructions|Assembly Instructions]], [[Code/Computer Systems/Assembly/x86_64 Architecture|x86_64 Architecture]]), and the user→kernel crossing ([[Code/Computer Systems/Kernels/System Calls|System Calls]]).

## Complexity

## When to use it

One layer down: how the machine gets to the point of running anything at all — POST → BIOS → MBR → bootloader → kernel, traced through xv6 — [[Code/Computer Systems/Kernels/OS Boot Process|OS Boot Process]], [[Code/Computer Systems/Kernels/XV6 Boot Sequence|XV6 Boot Sequence]], [[Code/Computer Systems/Kernels/Kernel Architecture|Kernel Architecture]].

## Gotchas

The stack grows down and the heap grows up; they are the same address space approaching each other — [[Code/Computer Systems/Stack & Functions|Stack & Functions]] § The Stack vs Heap.

## Resources

- [How CPU executes a program (video)](https://www.youtube.com/watch?v=XM4lGflQFvA)
- [How computers calculate - ALU (video)](https://youtu.be/1I5ZMmrOfnA)
- [Registers and RAM (video)](https://youtu.be/fpnE6UAfbtU)
- [The Central Processing Unit (CPU) (video)](https://youtu.be/FZGugFqdr60)
- [Instructions and Programs (video)](https://youtu.be/zltgXvg6r3k)
- [NAND to Tetris: Build a Modern Computer from First Principles](https://www.coursera.org/learn/build-a-computer)

## Problems

_None yet._
