---
type: topic
group: Sorting & Searching
tier: core
confidence:
---

# Counting and Radix Sort

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Non-comparison sorts: counting sort tallies exact key frequencies; radix sort
applies counting sort digit-by-digit (or character-by-character for
strings), least- or most-significant first.

## How it works

## Implementation

## Complexity

O(n + k) for counting sort, where k is the key range. O(d·(n + k)) for radix
sort over d digits — linear in n when k and d are bounded, beating the
Ω(n log n) comparison-sort floor because these aren't comparison sorts.

## When to use it

Keys are small integers, or fixed-width strings, where the range or digit
count is bounded independent of n.

## Gotchas

Space cost scales with the key range k, not just n — a wide range with few
actual values wastes memory.

## Resources

- [UC Berkeley 2014-04-21: Radix Sort (video)](https://archive.org/details/ucberkeley_webcast_pvbBMd-3NoI)
- [Sedgewick - Radix Sorts (6 videos)](https://www.coursera.org/learn/algorithms-part2/home/week/3)
    - [1. Strings in Java](https://www.coursera.org/learn/algorithms-part2/lecture/vGHvb/strings-in-java)
    - [2. Key Indexed Counting](https://www.coursera.org/lecture/algorithms-part2/key-indexed-counting-2pi1Z)
    - [3. Least Significant Digit First String Radix Sort](https://www.coursera.org/learn/algorithms-part2/lecture/c1U7L/lsd-radix-sort)
    - [4. Most Significant Digit First String Radix Sort](https://www.coursera.org/learn/algorithms-part2/lecture/gFxwG/msd-radix-sort)
    - [5. 3 Way Radix Quicksort](https://www.coursera.org/lecture/algorithms-part2/3-way-radix-quicksort-crkd5)
- [Radix Sort (Yale notes)](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#radixSort)
- [Radix Sort (video)](https://www.youtube.com/watch?v=xhr26ia4k38)
- [Radix Sort, Counting Sort (linear time given constraints) (video)](https://www.youtube.com/watch?v=Nz1KZXbghj8&index=7&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [Sorting in Linear Time (video)](https://www.youtube.com/watch?v=pOKy3RZbSws&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf&index=14)
- General sorting review (from "Additional Detail on Some Subjects"):
    - [Stanford Lecture 15 | Programming Abstractions (video)](https://www.youtube.com/watch?v=ENp00xylP7c&index=15&list=PLFE6E58F856038C69)
    - [Stanford Lecture 16 | Programming Abstractions (video)](https://www.youtube.com/watch?v=y4M9IVgrVKo&index=16&list=PLFE6E58F856038C69)
    - [Simonson: Algorithms - Sorting - Lecture 2 (video)](https://www.youtube.com/watch?v=odNJmw5TOEE&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=2)
    - [Simonson: Algorithms - Sorting II - Lecture 3 (video)](https://www.youtube.com/watch?v=hj8YKFTFKEE&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=3)
    - [Skiena: CSE373 2020 - Mergesort/Quicksort (video)](https://www.youtube.com/watch?v=jUf-UQ3a0kg&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=8)
    - [Skiena: CSE373 2020 - Linear Sorting (video)](https://www.youtube.com/watch?v=0ksyQKmre84&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=9)

## Problems

_None yet._
