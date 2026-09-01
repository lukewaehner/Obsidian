---
type: topic
group: Math & Bits
tier: extra
confidence:
---

# Information Theory and Entropy

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Information theory quantifies how much a message can be compressed —
entropy is the theoretical minimum number of bits needed, on average, to
encode a source given its symbol distribution.

## How it works

Entropy is higher when outcomes are more unpredictable (uniform distribution)
and lower when they're skewed (some symbols much more likely than others) —
skew is exactly what a compressor exploits, assigning shorter codes to more
frequent symbols. Redundancy in a message is the gap between its actual
encoding length and its entropy.

## Implementation

## Complexity

## When to use it

Anywhere lossless compression matters — see [[Compression]] for the
algorithms (Huffman coding, LZ77) that approach the entropy bound in
practice.

## Gotchas

## Resources

- [Khan Academy: Information Theory](https://www.khanacademy.org/computing/computer-science/informationtheory)
- [Information Theory, Claude Shannon, Entropy, Redundancy, Data Compression & Bits (video)](https://youtu.be/JnJq3Py0dyM?t=176)
- [Core Markov Text Generation (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/waxgx/core-markov-text-generation)
- [Core Implementing Markov Text Generation (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/gZhiC/core-implementing-markov-text-generation)
- [Project: Markov Text Generation Walk Through (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/EUjrq/project-markov-text-generation-walk-through)

## Problems

_None yet._
