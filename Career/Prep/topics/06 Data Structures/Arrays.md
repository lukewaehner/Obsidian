---
tags:
  - career
  - interview-prep
type: note
parent: "[[Career/Prep/topics/06 Data Structures/06 Data Structures|06 Data Structures]]"
source: coding-interview-university
---

# Arrays

- [x] About Arrays: ✅ 2026-08-31
	- [Arrays CS50 Harvard University](https://www.youtube.com/watch?v=tI_tIZFyKBw&t=3009s)
	- [Arrays (video)](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)
	- [UC Berkeley CS61B - Linear and Multi-Dim Arrays (video)](https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE) (Start watching from 15m 32s)
	- [Dynamic Arrays (video)](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
	- [Jagged Arrays (video)](https://www.youtube.com/watch?v=1jtrQqYpt7g)
- [ ] Implement a vector (mutable array with automatic resizing):
	- [ ] Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
	- [ ] New raw data array with allocated memory
		- can allocate int array under the hood, just not use its features
		- start with 16, or if the starting number is greater, use power of 2 - 16, 32, 64, 128
	- [x] size() - number of items ✅ 2026-08-31
	- [x] capacity() - number of items it can hold ✅ 2026-08-31
	- [x] is_empty() ✅ 2026-08-31
	- [x] at(index) - returns the item at a given index, blows up if index out of bounds ✅ 2026-08-31
	- [x] push(item) ✅ 2026-08-31
	- [x] insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right ✅ 2026-08-31
	- [x] prepend(item) - can use insert above at index 0 ✅ 2026-08-31
	- [x] pop() - remove from end, return value ✅ 2026-08-31
	- [x] delete(index) - delete item at index, shifting all trailing elements left ✅ 2026-08-31
	- [x] remove(item) - looks for value and removes index holding it (even if in multiple places) ✅ 2026-08-31
	- [x] find(item) - looks for value and returns first index with that value, -1 if not found ✅ 2026-08-31
	- [x] resize(new_capacity) // private function ✅ 2026-08-31
		- when you reach capacity, resize to double the size
		- when popping an item, if the size is 1/4 of capacity, resize to half
- [ ] Time
	- O(1) to add/remove at end (amortized for allocations for more space), index, or update
	- O(n) to insert/remove elsewhere
- [ ] Space
	- contiguous in memory, so proximity helps performance
	- space needed = (array capacity, which is >= n) * size of item, but even if 2n, still O(n)

---

**Work here → [[Career/Prep/work/06 Data Structures/Arrays|Arrays]]** · [[Career/Prep/topics/06 Data Structures/06 Data Structures|06 Data Structures]] · [[Career/Prep/Prep|Prep]]
