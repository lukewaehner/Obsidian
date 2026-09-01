---
type: topic
group: Systems
tier: extra
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Endianness

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Byte order for multi-byte values: big-endian stores the most significant
byte first, little-endian stores the least significant byte first. Neither
is "correct" — it's a hardware/protocol convention that has to match on both
ends of any raw byte exchange.

## How it works

## Implementation

## Complexity

## When to use it

## Gotchas

Network protocols conventionally use big-endian ("network byte order")
regardless of the host's native endianness — reading raw bytes off the wire
or from a binary file format without accounting for this is a classic
silent-corruption bug.

## Resources

- [Big And Little Endian](https://web.archive.org/web/20180107141940/http://www.cs.umd.edu:80/class/sum2003/cmsc311/Notes/Data/endian.html)
- [Big Endian Vs Little Endian (video)](https://www.youtube.com/watch?v=JrNF0KRAlyo)
- [Big And Little Endian Inside/Out (video)](https://www.youtube.com/watch?v=oBSuXP-1Tc0) — technical talk for kernel devs; the first half is enough

## Problems

_None yet._
