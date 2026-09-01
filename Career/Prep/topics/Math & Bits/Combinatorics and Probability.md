---
type: topic
group: Math & Bits
tier: core
confidence:
---

# Combinatorics and Probability

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Counting (permutations, combinations, n choose k) and basic probability
underpin a recurring family of interview questions — expected value,
independence, and simple Markov chains.

## How it works

- Permutations count arrangements where order matters (n! for n distinct
  items); combinations (n choose k) count selections where it doesn't.
- Basic probability: independence, conditional probability, expected value
  as a linear (additive) quantity even when the underlying events aren't
  independent.
- Markov chains model a sequence where the next state depends only on the
  current one, not the full history — the basis of simple text-generation
  exercises.

## Implementation

## Complexity

## When to use it

Estimation questions ("how many ways can...") and probability-of-collision
style questions (e.g. birthday-paradox reasoning for hash function design).

## Gotchas

Expected value is linear regardless of independence — a common shortcut
that avoids having to reason about a joint distribution.

## Resources

- [Math Skills: How to find Factorial, Permutation, and Combination (Choose) (video)](https://www.youtube.com/watch?v=8RRo6Ti9d0U)
- [Make School: Probability (video)](https://www.youtube.com/watch?v=sZkAAk9Wwa4)
- [Make School: More Probability and Markov Chains (video)](https://www.youtube.com/watch?v=dNaJg-mLobQ)
- [Khan Academy: Basic Theoretical Probability](https://www.khanacademy.org/math/probability/probability-and-combinatorics-topic)
- [Probability Explained (video playlist, 41 videos)](https://www.youtube.com/watch?v=uzkc-qNVoOk&list=PLC58778F28211FA19)

## Problems

_None yet._
