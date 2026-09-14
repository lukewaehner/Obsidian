---
type: topic
group: Systems
tier: extra
confidence:
sections_total: 6
sections_done: 1
coverage: 0.17
status: learning
updated: 2026-09-13
---

# Unicode

← [[Career/Prep/topics/Systems/Systems|Systems]]

> [!abstract]- Coverage — 1/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Unicode separates "what character is this" (a code point) from "how is it
stored as bytes" (an encoding, e.g. UTF-8) — conflating the two is the root
of most text-handling bugs.

## How it works

UTF-8 is variable-width (1-4 bytes per code point) and backward-compatible
with ASCII for the first 128 code points; UTF-16 and UTF-32 are the other
common encodings, each with different tradeoffs for space and fixed- vs
variable-width indexing.

## Implementation

UTF-8 in a language that refuses to paper over it: byte length vs character count, why `s[i]` does not compile, and iterating `.chars()` versus `.bytes()` — [[Code/Rust/Strings|Strings]].

## Complexity

## When to use it

## Gotchas

String length in code points is not string length in bytes, and neither is
necessarily the number of user-perceived "characters" (a combining accent
or emoji can span multiple code points) — a naive byte-indexed string
operation can slice a multi-byte character in half.

## Resources

- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](http://www.joelonsoftware.com/articles/Unicode.html)
- [What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text](http://kunststube.net/encoding/)

## Problems

_None yet._
