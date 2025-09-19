## Class: Algorithms
---
## Topic: Analyzing Algorithms
---
## Notes:
## Empirical Measuring
- Algorithms should not take up too much time or space.
- How do we measure time or space that an algorithm needs
- Needs to be machine independent
- Constant factors doesn't matter as much as change due to input size
	- If machine A is twice as fast, it will run the algorithm twice as fast on the same data size
- Only care about change due to input size
- How does resource reuirement grow as $n \rightarrow \infty$ (asymptotic behavior)
- Most algorithms might do well for small input. We care about scalability.  
-  We want to characterize which algorithms work well on large inputs.  
- Finally, we focus on worst case behavior:  
	1. Different algorithms may work better/worse on certain inputs.  
	2. Worst case provides a uniform bound to compare against.  
	3. Also, we don’t need any consensus on what is meant by the “average” input.  
- Asymptotic notation formalizes all this intuition in a mathematically rigorous way

## Core Ideas
- Assume that $f(n),g(n) \gt 0 \text{ for large }n$
- We want to be able to say $f(n) ~ g(n)$
	- which means $f(n)$ basically/for our purposes/essentially behaviors like $g(n)$
- In this case, this means
	- Ignore constants: $f(n) ~ g(n) \implies a \cdot g(n)$ for any positive $a$. (this is for machine independence, focus on growth)
- Only large $n$: the $~$ relation is basically $\approx$ for large enough n.
- The large values idea is formalized as:
	- there exists some $n_0$ such that for all $n \geq n_0$  {blah blah blah} holds

## Simple Exercises
- Count occurrences of the word 'foo' in a file $n =$ length of file. 
	- Linear
- Brute force crack a pass code made using ${0,1,...,9}. n =$ length of code.
	- $10^n$
- Check for plagiarism by comparing each pari of submissions
	- (Technically $\binom{n}{2}$) $\approx n^2$
- Playing a guessing game with **Yes/No** questions
	- Each answer reduces solutions by half
	- $\log{n}$
- Brute force crack a pattern code on $n$ points
	- A pattern code is a specific ordering through (potentially) all $n$ points
	- $n!$

## Five Types of Relationships

| Notation        | Description        | Intuition                     |
| --------------- | ------------------ | ----------------------------- |
| $O(\cdot)$      | not worse than     | it wont take longer than      |
| $\Omega(\cdot)$ | not better than    | it takes at least so much     |
| $\Theta(\cdot)$ | Exact analysis     | this is how long it takes     |
| $o(\cdot)$      | Strict upper bound | it takes *strictly* less than |
| $\omega(\cdot)$ | Strict lower bound | it takes *strictly* more than |

## Big-O Notation f(n) = O(g(n)) - $f$ bounded above by $g$ (asymptotically)
- There is some positive factor $k$ and a threshold value $n_0$ such that for any $n$ beyond this threshold, the value of $f(n)$ is upper bounded by $k \cdot g(n)$
- $\exists{k} \gt 0, \exists{n_0}, \forall{n} \gt n_0$  such that: $|\,f(n)\,| \leq k \cdot g(n)$
---
## Links to Other Topics:
- [[Logarithmic Time]]
- [[Linear Time]]
- [[Constant Time]]
- [[Quadratic Time]]
- [[Loglinear Time]]
- [[Polynomial Time]]
- [[Exponential Times]]
- [[Factorial Time]]
---
## Summary:
- 