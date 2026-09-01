---
type: topic
group: Systems
tier: extra
confidence:
---

# Unicode

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
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
