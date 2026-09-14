---
type: topic
group: Strings
tier: core
confidence:
sections_total: 6
sections_done: 1
coverage: 0.17
status: learning
updated: 2026-09-13
---

# String Manipulation

← [[Career/Prep/topics/Strings/Strings|Strings]]

> [!abstract]- Coverage — 1/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [x] [[#Gotchas]]

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

Strings are UTF-8, not arrays of characters: byte index ≠ character index, and slicing mid-codepoint is a bug — the Rust notes make this explicit because the language refuses to hide it — [[Code/Rust/Strings|Strings]]. The owned/borrowed split (`String` vs `&str`) is the same distinction every language has, just named.

## Resources

- [Sedgewick - Substring Search (video series)](https://www.coursera.org/learn/algorithms-part2/home/week/4)
- [Sedgewick - Introduction to Substring Search (video)](https://www.coursera.org/lecture/algorithms-part2/introduction-to-substring-search-n3ZpG)
- [Sedgewick - Brute-Force Substring Search (video)](https://www.coursera.org/learn/algorithms-part2/lecture/2Kn5i/brute-force-substring-search)
- [Search pattern in a text (video)](https://www.coursera.org/learn/data-structures/lecture/tAfHI/search-pattern-in-text)
- [Coursera: Algorithms on Strings](https://www.coursera.org/learn/algorithms-on-strings/home/week/1) — starts off great, but gets more complicated than it needs to be past KMP; has a nice explanation of tries; can be skipped

## Problems

- [[Career/Prep/problems/Arrays & Hashing/242 · Valid Anagram|242 · Valid Anagram]] · Easy · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/271 · Encode and Decode Strings|271 · Encode and Decode Strings]] · Medium · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/49 · Group Anagrams|49 · Group Anagrams]] · Medium · Arrays & Hashing
- [[Career/Prep/problems/Sliding Window/3 · Longest Substring Without Repeating Characters|3 · Longest Substring Without Repeating Characters]] · Medium · Sliding Window
- [[Career/Prep/problems/Stack/20 · Valid Parentheses|20 · Valid Parentheses]] · Easy · Stack
- [[Career/Prep/problems/Two Pointers/125 · Valid Palindrome|125 · Valid Palindrome]] · Easy · Two Pointers
