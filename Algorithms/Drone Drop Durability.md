## Class: Algorithms
---
## Topic: What height can a drone fall without breaking apart?
---
## Notes:
- We want height $x\in\{1,2,...,n\}$ such that drones break when falling from height $\geq x$There is a known maximum height $n$ after which the drone definitely breaks
- Test setup: Try dropping a drone from height h, if it breaks $x \leq h$ otherwise $x \gt h$. 
- Assume repeated dropping doesn't harm drone at all.
- What's the minimum drops needed to find $x$ when:
	1. No limit on number of drones. If one breaks, use the next
	2. There is only one test drone, If it breaks, you're done.
	3. There are two test drones. One spare.
	4. Later we consider k drones.

# Infinite Drones
- Drones are free $\Rightarrow$ extract maximum information from each drone.
- Each drop allows ruling out either all floors above or all below
- Ensure as many are ruled out during each drop
- Best if number of floors above and below are equal: $min(k,n-k)$ is maximized when $k = \frac{n}{2}$
- Ensures that at least half are thrown out with each drop
- This is binary search
- Need potentially $log(n)$ drones, but drops also bounded by $log(n)$
 
# One Drone
 - Skipping is a bad idea, as if it skips at floor $i+1$, is $x = i$ or $x = i + 1$
 - Just iterate up
 - Potentially need n drops

# Two drones:
- Single spare
- Binary Search -> Sequential on fail?
- Skip alternating floors and use the last one to test (2, 4, 6 {breaks} -> Check 5)
- Lower fractioned binary search

- Should be skipping, but the skip distance is unknown
- Skip too little, eg. $2, 4, 6, ... \Rightarrow$ first drone doing too much work
- Skip too much, $eg \frac{n}{2}, n \Rightarrow$ second drone doing too much work
- Assume that we are skipping k floors within first drone
	- First drone is at most $\frac{n}{k}$ drops.
	- Second drone is at most $k$ drops.

- Minimizing $\frac{n}{k} + k$ happens when $\frac{n}{k} = k = \sqrt{n}$
- A bracketing / binning approach: First drone tries at multiples of $\sqrt{n}$. Whenever it breaks, we have found a $(i \times \sqrt{n}, (i+1) \times \sqrt{n})$ range for spare drone
- Each drone drops at most $\sqrt{n}$ times for a total of $\leq 2\sqrt{n}$ drops
- if ab is fixed
	- a+b is minimized when a=b
 

$$
\begin{aligned}
\textbf{for } \text{i} = [1,2,...,n]: \\

\end{aligned}
$$

 ---
## Links to Other Topics:
- 
- 
---
## Summary:
- 
