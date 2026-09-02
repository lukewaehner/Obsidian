---
type: topic
group: Data Structures
tier: core
confidence:
sections_total: 7
sections_done: 4
coverage: 0.57
status: learning
updated: 2026-09-01
---

# Hash Tables

> [!abstract]- Coverage — 4/7
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [x] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]
> - [ ] [[#Distributed hash tables]]

## Idea

Hash functions and what makes one good — [[Hashtable]] § Hash Function.

## How it works

Collision handling by chaining, and by open addressing / linear probing.

Load factor, table doubling, and rehashing — [[Hashtable]].

## Implementation

Implemented with an array using linear probing: `hash(k, m)`, `add`, `exists`,
`get`, `remove` — [[Hashtable]] § `HashMap`.

Implemented a hash set — [[Hashtable]] § `HashTable`.

## Complexity

Average vs. worst-case complexity, and what causes the worst case — [[Hashtable]].

## When to use it

## Gotchas

> [!warning] Open defect in [[Hashtable]]
> Both `remove` methods blank the slot to `None` rather than writing a tombstone,
> which breaks the probe sequence for any key that collided past it — the exact
> failure the note itself lists as pitfall #5. Fix before studying from the code.
>
> The "(Chaining)" heading mislabel is corrected: both implementations in that
> note use open addressing with linear probing.

Still open:

- [ ] Advanced: universal hashing, perfect hashing (see Resources)

## Distributed hash tables

## Resources

- [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)
- [Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [Open Addressing, Cryptographic Hashing (video)](https://www.youtube.com/watch?v=rvdJDijO2Ro&index=10&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [PyCon 2010: The Mighty Dictionary (video)](https://www.youtube.com/watch?v=C4Kc8xzcA68)
- [PyCon 2017: The Dictionary Even Mightier (video)](https://www.youtube.com/watch?v=66P5FMkWoVU)
- [(Advanced) Randomization: Universal & Perfect Hashing (video)](https://www.youtube.com/watch?v=z0lJ2k0sl1g&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=11)
- [(Advanced) Perfect hashing (video)](https://www.youtube.com/watch?v=N0COwN14gt0&list=PL2B4EEwhKD-NbwZ4ezj7gyc_3yNrojKM9&index=4)
- [[Review] Hash tables in 4 minutes (video)](https://youtu.be/knV86FlSXJ8)
- [Core Hash Tables (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-hash-tables-m7UuP)
- [Data Structures (video)](https://www.coursera.org/learn/data-structures/home/week/4)
- [Phone Book Problem (video)](https://www.coursera.org/lecture/data-structures/phone-book-problem-NYZZP)
- Distributed hash tables: [Instant Uploads And Storage Optimization In Dropbox (video)](https://www.coursera.org/lecture/data-structures/instant-uploads-and-storage-optimization-in-dropbox-DvaIb), [Distributed Hash Tables (video)](https://www.coursera.org/lecture/data-structures/distributed-hash-tables-tvH8H)

## Problems

- [[Career/Prep/problems/Arrays & Hashing/1 · Two Sum|1 · Two Sum]] · Easy · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/217 · Contains Duplicate|217 · Contains Duplicate]] · Easy · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/242 · Valid Anagram|242 · Valid Anagram]] · Easy · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/347 · Top K Frequent Elements|347 · Top K Frequent Elements]] · Medium · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/36 · Valid Sudoku|36 · Valid Sudoku]] · Medium · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/49 · Group Anagrams|49 · Group Anagrams]] · Medium · Arrays & Hashing
