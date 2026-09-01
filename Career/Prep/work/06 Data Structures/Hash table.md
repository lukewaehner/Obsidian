---
tags:
  - career
  - interview-prep
  - work
type: work
topic: "[[Career/Prep/topics/06 Data Structures/Hash table|Hash table]]"
parent: "[[Career/Prep/work/06 Data Structures|06 Data Structures]]"
---

# Hash table — Work

Reference: [[Career/Prep/topics/06 Data Structures/Hash table|Hash table]] · Index: [[Career/Prep/work/06 Data Structures|06 Data Structures]] · Master: [[Career/Prep/Prep|Prep]]

## Checklist

- [x] Hash functions and what makes one good — [[Hashtable|Hashtable]] § Hash Function
- [x] Collision handling by chaining — [[Hashtable|Hashtable]]
- [x] Collision handling by open addressing / linear probing — [[Hashtable|Hashtable]]
- [x] Load factor, table doubling, and rehashing — [[Hashtable|Hashtable]]
- [x] Implement with an array using linear probing: `hash(k, m)`, `add`, `exists`,
      `get`, `remove` — [[Hashtable|Hashtable]] § `HashMap`
- [x] Implement a hash set — [[Hashtable|Hashtable]] § `HashTable`
- [x] Average vs. worst-case complexity, and what causes the worst case — [[Hashtable|Hashtable]]
- [ ] Fix tombstone deletion in [[Hashtable|Hashtable]] (see callout)
- [ ] Distributed hash tables
- [ ] Advanced: universal hashing, perfect hashing

> [!warning] Open defect in [[Hashtable|Hashtable]]
> Both `remove` methods blank the slot to `None` rather than writing a tombstone,
> which breaks the probe sequence for any key that collided past it — the exact
> failure the note itself lists as pitfall #5. Fix before studying from the code.
>
> The "(Chaining)" heading mislabel is corrected: both implementations in that
> note use open addressing with linear probing.

## Notes

<!-- working notes, code, and gotchas go here -->
