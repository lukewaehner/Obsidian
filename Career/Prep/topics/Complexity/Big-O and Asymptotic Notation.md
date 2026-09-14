---
type: topic
group: Complexity
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-13
---

# Big-O and Asymptotic Notation

← [[Career/Prep/topics/Complexity/Complexity|Complexity]]

> [!abstract]- Coverage — 3/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Why asymptotics at all: resource use has to be measured machine-independently, so constant factors are dropped and only growth as `n → ∞` is kept, on the worst case because it is the one bound every input respects — [[Code/Algorithms/Times/Times|Times]] § Empirical Measuring, § Core Ideas.

## How it works

The five relations — `O`, `Ω`, `Θ`, `o`, `ω` — as a table of intuitions, plus the formal `∃k>0, ∃n₀, ∀n>n₀ : |f(n)| ≤ k·g(n)` definition of big-O — [[Code/Algorithms/Times/Times|Times]] § Five Types of Relationships. The growth hierarchy `1 < log n < n < n log n < n² < n³ < 2ⁿ < n! < nⁿ` — [[Code/Algorithms/Recurrences|Recurrences]] § Common Growth Rate Hierarchy.

## Implementation

## Complexity

## When to use it

One note per growth class, each with the exercise that produces it (word count → linear, guessing game → log n, pairwise plagiarism check → n², pattern lock → n!) — [[Code/Algorithms/Times/Constant Time|Constant Time]], [[Code/Algorithms/Times/Logarithmic Time|Logarithmic Time]], [[Code/Algorithms/Times/Linear Time|Linear Time]], [[Code/Algorithms/Times/Loglinear Time|Loglinear Time]], [[Code/Algorithms/Times/Quadratic Time|Quadratic Time]], [[Code/Algorithms/Times/Polynomial Time|Polynomial Time]], [[Code/Algorithms/Times/Exponential Times|Exponential Times]], [[Code/Algorithms/Times/Factorial Time|Factorial Time]].

## Gotchas

## Resources

- When you go through *Cracking the Coding Interview*, its Big-O chapter ends with a runtime-identification quiz — a good review and test.
- [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=V6mKVRU1evU)
- [Big O Notation (and Omega and Theta) - best mathematical explanation (video)](https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [Skiena (video)](https://www.youtube.com/watch?v=z1mkCe3kVUA)
- [UC Berkeley Big O (video)](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
- [Cheat sheet](http://bigocheatsheet.com/)
- [[Review] Analyzing Algorithms (playlist) in 18 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZMxejjIyFHWa-4nKg6sdoIv)

## Problems

- [[Career/Prep/problems/Binary Search/704 · Binary Search|704 · Binary Search]] · Easy · Binary Search
- [[Career/Prep/problems/Binary Search/875 · Koko Eating Bananas|875 · Koko Eating Bananas]] · Medium · Binary Search
