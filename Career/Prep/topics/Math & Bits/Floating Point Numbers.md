---
type: topic
group: Math & Bits
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Floating Point Numbers

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Floating point trades exact representation for range: a sign bit, an
exponent, and a mantissa (fraction) encode a number as roughly
`sign * mantissa * 2^exponent`, the same idea as scientific notation but in
binary.

## How it works

## Implementation

## Complexity

## When to use it

## Gotchas

Most decimal fractions (0.1, for instance) have no exact binary
representation, so equality comparisons on floats are a correctness bug
waiting to happen — compare against an epsilon instead. Precision is not
uniform across the range: it's denser near zero and sparser for large
magnitudes.

## Resources

- [Representation of Floating Point Numbers - 1 (video — note: error in calculations, see video description)](https://www.youtube.com/watch?v=ji3SfClm8TU)

## Problems

_None yet._
