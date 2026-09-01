---
type: topic
group: Data Structures
tier: core
confidence:
sections_total: 7
sections_done: 3
coverage: 0.43
status: learning
updated: 2026-09-01
---

# Arrays

> [!abstract]- Coverage — 3/7
> - [x] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [ ] [[#Gotchas]]
> - [ ] [[#Implement a vector]]

## Idea

Reviewed what arrays are and how dynamic arrays grow — see Resources for the video set.

## How it works

## Implementation

## Complexity

Time and space costs of arrays — [[DSA]].

- O(1) to add/remove at end (amortized for allocations for more space), index, or update.
- O(n) to insert/remove elsewhere.
- Space is contiguous in memory, so proximity helps performance; space needed is
  (array capacity, which is >= n) * size of item, but even at 2n, still O(n).

## When to use it

Array vs. linked list tradeoffs — [[Code/Algorithms/Linked List|Linked List]] § Array vs Linked List.

## Gotchas

## Implement a vector

```python
class Vector:
	def __init__(self):
		self.data = [None] * 8
		self.capacity = 8
		self.size = 0
	
	def size(self) -> int:
		return self.size
	
	def capacity(self) -> int:
		return self.capacity
	
	def is_empty(self) -> bool:
		return self.size == 0
	
	def at(self, idx):
		if idx >= self.size:
			raise IndexError("oob")
		return self.data[idx]
	
	def push(self, item):
		if self.size == self.capacity:
			resize(self.capacity * 2)
		self.data[self.size] = item
		self.size += 1
		
	def insert(self, item, index):
		if index < 0 or index > size:
			raise IndexError("oob")
		if self.size == self.capacity:
			resize(self.capacity * 2)
		for i in range(self.size, index, -1):
			self.data[i] = self.data[i-1]
		self.data[index] = item
		self.size += 1
	
	def prepend(self, item):
		self.insert(item, 0)
	
	def pop(self)
		item = self.data[self.size-1]
		self.data[self.size-1] = None
		self.size -= 1
		return item
	
	def delete(self, idx):
		if idx < 0 or idx >= self.size:
			raise IndexError("oob")
		for i in range(idx, self.size-1):
			self.data[i] = self.data[i+1]
		self.data[self.size - 1] = None
		self.size -= 1
	
	def remove(self, item):
	    write = 0
	    for read in range(self.size):
	        if self.data[read] != item:
	            self.data[write] = self.data[read]
	            write += 1
	
	    for i in range(write, self.size):
	        self.data[i] = None
	
	    removed = self.size - write
	    self.size = write
	    return removed
		
	def find(self, item):
		for i in self.size - 1:
			if data[i] == item
				return i
		return None
		
	def resize(self, new):
		old = self.data
		self.capacity = new
		self.data = [None] * new
		for i in range(len(old)):
			self.data[i] = old[i]
	
```

Still open:

- [ ] Dynamic arrays: how resizing actually works (growth factor, shrink at 1/4)
- [ ] Jagged / multi-dimensional arrays

## Resources

- [Arrays CS50 Harvard University](https://www.youtube.com/watch?v=tI_tIZFyKBw&t=3009s)
- [Arrays (video)](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)
- [UC Berkeley CS61B - Linear and Multi-Dim Arrays (video)](https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE) (Start watching from 15m 32s)
- [Dynamic Arrays (video)](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
- [Jagged Arrays (video)](https://www.youtube.com/watch?v=1jtrQqYpt7g)

## Problems

_None yet._
