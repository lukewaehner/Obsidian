---
type: topic
group: Systems
tier: extra
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Compression

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Lossless compression squeezes out redundancy so a message needs fewer bits
to represent without losing information — see
[[Information Theory and Entropy]] for why there's a hard floor on how far
this can go.

## How it works

Huffman coding assigns shorter bit-codes to more frequent symbols, building
an optimal prefix-free code as a binary tree. LZ77-family methods instead
exploit repeated substrings, replacing a repeat with a back-reference to its
earlier occurrence.

## Implementation

## Complexity

## When to use it

## Gotchas

Compression can't beat entropy on average across all inputs (that's the
theoretical floor) — a compressor that "always shrinks the file" is a
contradiction for sufficiently random input.

## Resources

- [Compression (Computerphile, video)](https://www.youtube.com/watch?v=Lto-ajuqW3w)
- [Entropy in Compression (Computerphile, video)](https://www.youtube.com/watch?v=M5c_RFKVkko)
- [Upside Down Trees - Huffman Trees (Computerphile, video)](https://www.youtube.com/watch?v=umTbivyJoiI)
- [EXTRA BITS/TRITS - Huffman Trees (Computerphile, video)](https://www.youtube.com/watch?v=DV8efuB3h2g)
- [Elegant Compression in Text - The LZ 77 Method (Computerphile, video)](https://www.youtube.com/watch?v=goOa3DGezUA)
- [Text Compression Meets Probabilities (Computerphile, video)](https://www.youtube.com/watch?v=cCDCfoHTsaU)
- [Compressor Head (video playlist)](https://www.youtube.com/playlist?list=PLOU2XLYxmsIJGErt5rrCqaSGTMyyqNt2H)
- [Google Developers Live: GZIP is not enough! (video)](https://www.youtube.com/watch?v=whGwm0Lky2s)

## Problems

_None yet._
