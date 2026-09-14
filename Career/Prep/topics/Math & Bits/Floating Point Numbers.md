---
type: topic
group: Math & Bits
tier: core
confidence:
sections_total: 6
sections_done: 1
coverage: 0.17
status: learning
updated: 2026-09-13
---

# Floating Point Numbers

← [[Career/Prep/topics/Math & Bits/Math & Bits|Math & Bits]]

> [!abstract]- Coverage — 1/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
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

The systems answer is: don't, where you can help it. Prices in the order book are `i64` ticks specifically to keep floating-point rounding out of financial arithmetic — [[Code/Rust/HFT-Ledger/00 - Overview|HFT-Ledger: Project Overview]] § Key Design Choices. Address and offset arithmetic stays integer for the same reason — [[Code/Computer Systems/Number Bases|Number Bases]].

## Gotchas

Most decimal fractions (0.1, for instance) have no exact binary
representation, so equality comparisons on floats are a correctness bug
waiting to happen — compare against an epsilon instead. Precision is not
uniform across the range: it's denser near zero and sparser for large
magnitudes.

## Resources

- [Representation of Floating Point Numbers - 1 (video — note: error in calculations, see video description)](https://www.youtube.com/watch?v=ji3SfClm8TU)

## Problems

- [[Career/Prep/problems/Stack/853 · Car Fleet|853 · Car Fleet]] · Medium · Stack
