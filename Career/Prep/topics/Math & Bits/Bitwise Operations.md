---
type: topic
group: Math & Bits
tier: core
confidence:
---

# Bitwise Operations

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Manipulate integers at the bit level with `& | ^ ~ >> <<` — know the powers
of 2 from 2^1 to 2^16 and 2^32 well enough to not have to compute them.

## How it works

- `&` masks bits (test/clear specific bits), `|` sets bits, `^` toggles bits
  and is its own inverse (useful for swaps and finding a lone unpaired
  value), `~` flips every bit.
- `<<`/`>>` shift; a left shift by k multiplies by 2^k, a right shift on an
  unsigned value divides by 2^k (an arithmetic right shift on a signed value
  preserves the sign bit instead).
- Two's complement represents negative numbers by inverting the bits and
  adding 1, so a single representation of zero and normal addition circuitry
  both work for signed and unsigned values.

## Implementation

## Complexity

O(1) per operation, O(w) per pass over an integer's w bits (e.g. counting
set bits by scanning).

## When to use it

Compact set membership (bitmask as a set over a small universe), toggling
flags, and the classic "counting/XOR trick" family of interview problems.

## Gotchas

Brian Kernighan's bit-counting trick (`n & (n-1)` clears the lowest set bit)
runs in O(popcount) rather than O(w) — worth knowing by name, since it comes
up as its own question. Right-shifting a negative signed integer is
implementation/language-defined territory; don't assume it zero-fills.

## Resources

- [Bits cheat sheet (PDF)](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/bits-cheat-sheet.pdf)
- [Word (computer architecture) (Wikipedia)](https://en.wikipedia.org/wiki/Word_(computer_architecture))
- [Bit Manipulation (video)](https://www.youtube.com/watch?v=7jkIUgLC29I)
- [C Programming Tutorial 2-10: Bitwise Operators (video)](https://www.youtube.com/watch?v=d0AwjSpNXR0)
- [Bit manipulation (Wikipedia)](https://en.wikipedia.org/wiki/Bit_manipulation)
- [Bitwise operation (Wikipedia)](https://en.wikipedia.org/wiki/Bitwise_operation)
- [Bit Hacks (Stanford)](https://graphics.stanford.edu/~seander/bithacks.html)
- [The Bit Twiddler](https://bits.stephan-brumme.com/)
- [The Bit Twiddler Interactive](https://bits.stephan-brumme.com/interactive.html)
- [Bit Hacks (video)](https://www.youtube.com/watch?v=ZusiKXcz_ac)
- [Practice Operations](https://pconrad.github.io/old_pconrad_cs16/topics/bitOps/)
- [Binary: Plusses & Minuses (Why We Use Two's Complement) (video)](https://www.youtube.com/watch?v=lKTsv6iVxV4)
- [Ones' complement (Wikipedia)](https://en.wikipedia.org/wiki/Ones%27_complement)
- [Two's complement (Wikipedia)](https://en.wikipedia.org/wiki/Two%27s_complement)
- [4 ways to count bits in a byte (video)](https://youtu.be/Hzuzo9NJrlc)
- [Count Bits (Stanford)](https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan)
- [How To Count The Number Of Set Bits In a 32 Bit Integer (Stack Overflow)](http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer)
- [Swap (bit trick)](https://bits.stephan-brumme.com/swap.html)
- [Absolute Integer](https://bits.stephan-brumme.com/absInteger.html)

## Problems

_None yet._
