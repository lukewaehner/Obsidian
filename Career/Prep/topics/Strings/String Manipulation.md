---
type: topic
group: Strings
tier: core
confidence:
---

# String Manipulation

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Substring search is the umbrella problem: find one string inside another.
The naive approach checks every offset; [[Knuth-Morris-Pratt]],
[[Rabin-Karp]], and [[Boyer-Moore]] are the three standard ways to beat it.

## How it works

## Implementation

Still open:

- [ ] Naive substring search and its cost

## Complexity

Naive substring search is O(nm) in the worst case (pattern length m, text
length n) — every offset can fail on its last character. The three named
algorithms all improve on this; see each note's Complexity section.

## When to use it

## Gotchas

## Resources

- [Sedgewick - Substring Search (video series)](https://www.coursera.org/learn/algorithms-part2/home/week/4)
- [Sedgewick - Introduction to Substring Search (video)](https://www.coursera.org/lecture/algorithms-part2/introduction-to-substring-search-n3ZpG)
- [Sedgewick - Brute-Force Substring Search (video)](https://www.coursera.org/learn/algorithms-part2/lecture/2Kn5i/brute-force-substring-search)
- [Search pattern in a text (video)](https://www.coursera.org/learn/data-structures/lecture/tAfHI/search-pattern-in-text)
- [Coursera: Algorithms on Strings](https://www.coursera.org/learn/algorithms-on-strings/home/week/1) — starts off great, but gets more complicated than it needs to be past KMP; has a nice explanation of tries; can be skipped

## Problems

_None yet._
