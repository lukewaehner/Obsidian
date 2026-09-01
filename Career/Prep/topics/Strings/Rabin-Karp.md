---
type: topic
group: Strings
tier: core
confidence:
---

# Rabin-Karp

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Hash the pattern once, then hash every window of the text and compare hashes
instead of characters — a rolling hash makes each window's hash O(1) to
compute from the previous one — [[String Manipulation]].

## How it works

A rolling hash (e.g. treat the window as a base-b number and use modular
arithmetic) lets you drop the leaving character and add the entering one in
constant time, rather than rehashing the whole window. A hash match is a
candidate; verify it character-by-character before accepting it, since hash
collisions can produce false positives.

## Implementation

## Complexity

Average case O(n + m) with a good rolling hash and modulus. Worst case
O(nm) if collisions are frequent (adversarial input or a weak hash) and every
candidate needs full verification.

## When to use it

Multiple-pattern search (hash all patterns, scan the text once) and
plagiarism/duplicate detection, where a fast probabilistic first pass pays
off.

## Gotchas

Choosing a modulus and base that avoid frequent collisions matters — a lazy
choice degrades this to the O(nm) naive bound with extra hashing overhead on
top. Always verify a hash match against the actual characters.

## Resources

- [Rabin-Karp's Algorithm (video)](https://www.coursera.org/lecture/data-structures/rabin-karps-algorithm-c0Qkw)
- [Precomputing (video)](https://www.coursera.org/learn/data-structures/lecture/nYrc8/optimization-precomputation)
- [Optimization: Implementation and Analysis (video)](https://www.coursera.org/learn/data-structures/lecture/h4ZLc/optimization-implementation-and-analysis)
- [Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=9)
- [Rolling Hashes, Amortized Analysis (video)](https://www.youtube.com/watch?v=w6nuXg0BISo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=32)
- [Sedgewick - Rabin-Karp (video)](https://www.coursera.org/lecture/algorithms-part2/rabin-karp-3KiqT)

## Problems

_None yet._
