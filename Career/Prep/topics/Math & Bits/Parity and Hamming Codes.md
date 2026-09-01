---
type: topic
group: Math & Bits
tier: extra
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Parity and Hamming Codes

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Error detection and correction by adding redundant bits: a parity bit
detects a single flipped bit; a Hamming code adds enough parity bits to
also identify (and correct) which one flipped.

## How it works

A parity bit is the XOR of a set of data bits — it flips if an odd number
of those bits flip, catching (but not locating) a single-bit error. Hamming
codes use multiple overlapping parity bits, each covering a different
subset of positions, so the pattern of which parities fail encodes the index
of the flipped bit.

## Implementation

## Complexity

## When to use it

Memory (ECC RAM) and low-level network/storage protocols where undetected
bit flips are unacceptable and full retransmission is expensive.

## Gotchas

Parity alone only detects an odd number of flipped bits — an even number of
flips (e.g. exactly two) cancels out and passes undetected.

## Resources

- [Intro (video)](https://www.youtube.com/watch?v=q-3BctoUpHE)
- [Parity (video)](https://www.youtube.com/watch?v=DdMcAUlxh1M)
- [Hamming Code: Error detection (video)](https://www.youtube.com/watch?v=1A_NcXxdoCc)
- [Hamming Code: Error correction (video)](https://www.youtube.com/watch?v=JAMLuxdHH8o)
- [Error Checking (video)](https://www.youtube.com/watch?v=wbH2VxzmoZk)

## Problems

_None yet._
