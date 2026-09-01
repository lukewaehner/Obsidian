---
type: topic
group: Math & Bits
tier: extra
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Fast Fourier Transform

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

The Fourier transform decomposes a signal into the frequencies that compose
it; the FFT is a divide-and-conquer algorithm that computes it (or its
discrete/inverse form) fast — [[Career/Prep/topics/Algorithm Design/Divide and Conquer|Divide and Conquer]].

## How it works

Naive discrete Fourier transform is O(n²) (compare every point against every
frequency). The FFT splits the problem into even- and odd-indexed terms
recursively, halving the work at each level.

## Implementation

## Complexity

O(n log n), versus O(n²) for the naive discrete Fourier transform.

## When to use it

Polynomial multiplication, signal processing, and any problem that reduces
to a convolution — large-integer multiplication can be sped up this way too.

## Gotchas

## Resources

- [An Interactive Guide To The Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
- [What is a Fourier transform? What is it used for?](http://www.askamathematician.com/2012/09/q-what-is-a-fourier-transform-what-is-it-used-for/)
- [What is the Fourier Transform? (video)](https://www.youtube.com/watch?v=Xxut2PN-V8Q)
- [Divide & Conquer: FFT (video)](https://www.youtube.com/watch?v=iTMn0Kt18tg&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=4)
- [Understanding The FFT](http://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/)

## Problems

_None yet._
