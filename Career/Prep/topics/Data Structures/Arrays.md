---
type: topic
group: Data Structures
tier: core
confidence:
sections_total: 7
sections_done: 7
coverage: 1.00
status: solid
updated: 2026-09-01
---

# Arrays

> [!abstract]- Coverage — 7/7
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]
> - [x] [[#Implement a vector]]

## Idea

Reviewed what arrays are and how dynamic arrays grow — see Resources for the video set.

## How it works

Arrays are data structures that occupy continuous space in memory, a N size array containing M byte datatypes takes up a padded M * N - holding some metadata along sided, this is where we can do pointer arithmetic to move. Arrays only hold the same type in memory. 

## Implementation
No need

## Complexity

Time and space costs of arrays — [[DSA]].

- O(1) to add/remove at end (amortized for allocations for more space), index, or update.
- O(n) to insert/remove elsewhere.
- Space is contiguous in memory, so proximity helps performance; space needed is
  (array capacity, which is >= n) * size of item, but even at 2n, still O(n).

## When to use it

Array vs. linked list tradeoffs — [[Code/Algorithms/Linked List|Linked List]] § Array vs Linked List.

## Gotchas

OOBs, 

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
> This is just a vector
- [ ] Jagged / multi-dimensional arrays
> An array of arrays that do not make up a MxN matrix. Like a mountain

## Resources

- [Arrays CS50 Harvard University](https://www.youtube.com/watch?v=tI_tIZFyKBw&t=3009s)
- [Arrays (video)](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)
- [UC Berkeley CS61B - Linear and Multi-Dim Arrays (video)](https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE) (Start watching from 15m 32s)
- [Dynamic Arrays (video)](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
- [Jagged Arrays (video)](https://www.youtube.com/watch?v=1jtrQqYpt7g)

## Problems

- [[Career/Prep/problems/Arrays & Hashing/1 · Two Sum|1 · Two Sum]] · Easy · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/217 · Contains Duplicate|217 · Contains Duplicate]] · Easy · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/238 · Product of Array Except Self|238 · Product of Array Except Self]] · Medium · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/271 · Encode and Decode Strings|271 · Encode and Decode Strings]] · Medium · Arrays & Hashing
- [[Career/Prep/problems/Arrays & Hashing/36 · Valid Sudoku|36 · Valid Sudoku]] · Medium · Arrays & Hashing
- [[Career/Prep/problems/Two Pointers/167 · Two Sum II - Input Array Is Sorted|167 · Two Sum II - Input Array Is Sorted]] · Medium · Two Pointers
