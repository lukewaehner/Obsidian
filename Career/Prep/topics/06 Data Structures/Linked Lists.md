---
tags:
  - career
  - interview-prep
type: note
parent: "[[Career/Prep/topics/06 Data Structures/06 Data Structures|06 Data Structures]]"
source: coding-interview-university
---

# Linked Lists

- [ ] Description:
	- [ ] [Linked Lists CS50 Harvard University](https://www.youtube.com/watch?v=2T-A_GFuoTo&t=650s) - this builds the intuition.
	- [ ] [Singly Linked Lists (video)](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
	- [ ] [CS 61B - Linked Lists 1 (video)](https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0)
	- [ ] [CS 61B - Linked Lists 2 (video)](https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w)
	- [ ] [[Review] Linked lists in 4 minutes (video)](https://youtu.be/F8AbOfQwl1c)
- [ ] [C Code (video)](https://www.youtube.com/watch?v=QN6FPiD0Gzo)
		- not the whole video, just portions about Node struct and memory allocation
- [ ] Linked List vs Arrays:
	- [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9)
	- [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/in-the-real-world-lists-vs-arrays-QUaUd)
- [ ] [Why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)
- [ ] Gotcha: you need pointer to pointer knowledge:
	(for when you pass a pointer to a function that may change the address where that pointer points)
	This page is just to get a grasp on ptr to ptr. I don't recommend this list traversal style. Readability and maintainability suffer due to cleverness.
	- [Pointers to Pointers](https://www.eskimo.com/~scs/cclass/int/sx8.html)
- [ ] Implement (I did with tail pointer & without):
	- [ ] size() - returns the number of data elements in the list
	- [ ] empty() - bool returns true if empty
	- [ ] value_at(index) - returns the value of the nth item (starting at 0 for first)
	- [ ] push_front(value) - adds an item to the front of the list
	- [ ] pop_front() - remove the front item and return its value
	- [ ] push_back(value) - adds an item at the end
	- [ ] pop_back() - removes end item and returns its value
	- [ ] front() - get the value of the front item
	- [ ] back() - get the value of the end item
	- [ ] insert(index, value) - insert value at index, so the current item at that index is pointed to by the new item at the index
	- [ ] erase(index) - removes node at given index
	- [ ] value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
	- [ ] reverse() - reverses the list
	- [ ] remove_value(value) - removes the first item in the list with this value
- [ ] Doubly-linked List
	- [Description (video)](https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpGKD)
	- No need to implement

---

**Work here → [[Career/Prep/work/06 Data Structures/Linked Lists|Linked Lists]]** · [[Career/Prep/topics/06 Data Structures/06 Data Structures|06 Data Structures]] · [[Career/Prep/Prep|Prep]]
