# Logarithmic Time - O(log n)

We don't even need to look at the whole data. Time is proportional to $C\log{n} = C'\log{n} = C''\log{n}$ (change of base property).

**Question:** Can we find the maximum in an unsorted list in logarithmic time?  
**Answer:** No. Because $\log{n} < n$ implies some input is unseen - what if that is the maximum?

**Examples:**
- [[Algorithms/Binary Search/Binary Search]] in a sorted array
- [[Drone Drop Durability#Infinite Drones]] example
