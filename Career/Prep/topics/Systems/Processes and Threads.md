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

# Processes and Threads

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

A process is an independent unit of resources (memory, file descriptors);
threads are units of execution within a process that share most of those
resources but each keep their own stack, program counter, and registers.

## How it works

- Process memory: code, static storage, stack, heap, plus file descriptors
  and I/O handles.
- Thread memory: shares everything above except the stack with other
  threads in the same process — each thread gets its own stack, program
  counter, and registers.
- Forking is copy-on-write: the child shares the parent's memory pages
  read-only until either process writes, which triggers a page copy.
- Context switching swaps which process/thread the CPU is running; it's
  triggered by interrupts, timer expiry, or blocking I/O, and its cost is
  paid in cache/TLB state, not just register save/restore.
- Locks, mutexes, semaphores, and monitors coordinate access to shared
  state; deadlock (circular wait) and livelock (threads keep responding to
  each other's state changes without progress) are the two failure modes to
  name.

## Implementation

[[Code/Computer Systems/Processes/Processes|Processes]],
[[Code/Computer Systems/Concurrency/Processes vs Threads|Processes vs Threads]],
[[Code/Computer Systems/Concurrency/Threads|Threads]],
[[Code/Computer Systems/Concurrency/Mutex Locks|Mutex Locks]],
[[Code/Computer Systems/Concurrency/Semaphores|Semaphores]], and
[[Code/Computer Systems/Concurrency/Deadlocks|Deadlocks]] cover this from the
coursework side.

## Complexity

## When to use it

## Gotchas

Python's GIL means threads don't give you real parallelism for CPU-bound
work in CPython — only for I/O-bound work where the GIL is released during
the wait.

## Resources

- [CS 162: Operating Systems and System Programming (video playlist)](https://archive.org/details/ucberkeley-webcast-PL-XXv-cvA_iBDyz-ba4yDskqMDY6A1w_c) — for processes and threads, see videos 1-11
- [What Is The Difference Between A Process And A Thread? (Quora)](https://www.quora.com/What-is-the-difference-between-a-process-and-a-thread)
- [Paging, segmentation, and virtual memory (video)](https://youtu.be/O4nwUqQodAg)
- [Interrupts (video)](https://youtu.be/iKlAWIKEyuw)
- [How context switching is initiated by the operating system and underlying hardware?](https://www.javatpoint.com/what-is-the-context-switching-in-the-operating-system)
- [Threads in C++ (video series, 10 videos)](https://www.youtube.com/playlist?list=PL5jc9xFGsL8E12so1wlMS0r0hTQoJL74M)
- [CS 377: Operating Systems (UMass, video playlist)](https://www.youtube.com/playlist?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)
- [Short series on threads (Python, video playlist)](https://www.youtube.com/playlist?list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1)
- [Python Threads (video)](https://www.youtube.com/watch?v=Bs7vPNbB9JM)
- [Understanding the Python GIL, 2010 (video)](https://www.youtube.com/watch?v=Obt-vMVdM8s) — [reference](http://www.dabeaz.com/GIL)
- [David Beazley - Python Concurrency From the Ground Up LIVE! - PyCon 2015 (video)](https://www.youtube.com/watch?v=MCs5OvhV9S4)
- [Keynote David Beazley - Topics of Interest (Python Asyncio) (video)](https://www.youtube.com/watch?v=ZzfHjytDceU)
- [Mutex in Python (video)](https://www.youtube.com/watch?v=0zaPs8OtyKY)

## Problems

_None yet._
