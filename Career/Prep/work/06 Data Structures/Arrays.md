---
tags:
  - career
  - interview-prep
  - work
type: work
topic: "[[Career/Prep/topics/06 Data Structures/Arrays|Arrays]]"
parent: "[[Career/Prep/work/06 Data Structures|06 Data Structures]]"
---

# Arrays — Work

Reference: [[Career/Prep/topics/06 Data Structures/Arrays|Arrays]] · Index: [[Career/Prep/work/06 Data Structures|06 Data Structures]] · Master: [[Career/Prep/Prep|Prep]]

## Checklist

- [x] Time and space costs of arrays — [[Career/Prep/work/DSA|DSA]]
- [x] Array vs. linked list tradeoffs — [[Career/Prep/work/Linked List|Linked List]] § Array vs Linked List
- [ ] Dynamic arrays: how resizing actually works (growth factor, shrink at 1/4)
- [ ] Implement a vector with automatic resizing: `size`, `capacity`, `is_empty`,
      `at`, `push`, `insert`, `prepend`, `pop`, `delete`, `remove`, `find`, `resize`
- [ ] Jagged / multi-dimensional arrays

Vector:
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
## Notes

<!-- working notes, code, and gotchas go here -->
