### Asymptotic
Ratio / limit test
$$\lim_{n\to\infty} \frac{f(n)}{g(n)} = 0 \implies f(n) = O(g(n))$$
$$
\lim_{n \to \infty} \frac{f(n)}{g(n)} = c,\ 0 < c < \infty \implies f(n) = \Theta(g(n))
$$
$$
\lim_{n \to \infty} \frac{f(n)}{g(n)} = c,\ 0 < c \le \infty \implies f(n) = \Omega(g(n))
$$
Generally:
$$
1 \ll \log\log n \ll (\log n)^b \ll n^\epsilon \ll n^a \ll n^a (\log n)^b 

\ll n^{\log n} \ll a^n \ll n! \ll n^n
$$
---
### Master Theorem:
- $n^{\log_B{A}}$ = Outside = $O(n\log{n})$
- < Outside = Outside
- > Outside = Recurrence
---
### Median of Medians:
Divide into $\lceil {n/5}\rceil$ groups (5 elements max per group)
Sort each group (O(n))
Select medians, recurse until have MOM. Order inputs < or > MOM.
Partition the original around MOM, check if the pivot is middle point, if not, restart algorithm with higher or lower half depending

---
### D&C to call on

| Algo                   | Use                                   | Time               |
| ---------------------- | ------------------------------------- | ------------------ |
| Merge                  | Sort array                            | $\Theta(n\log{n})$ |
| BinarySearch           | Finds index of a key                  | $\Theta(\log{n})$  |
| Median-of-Medians      | Above                                 | $\Theta(n)$        |
| Merge                  | Merge two sorted lists (still sorted) | $\Theta(n)$        |
| MaxSubarray            | Find the maximum subarray in an arrat | $\Theta(n\log{n})$ |
| Closest Pair of Points | Finds which two points are closest    |                    |
**Max Subarray**

```python
def MaxSumSubarray(A):
	if |A| = 1 then
		return max(0, A[1])
m = floor(n/2)
l = MaxSumSubarray(A[1..m])
r = MaxSumSubarray(A[m+1..n])
cl = max(from A[1..m]) # max from left
cr = max(from A[m+1..n]) # max from right
s = max(l, r, cl + cr)
return s
```

**Closest Pair of Points**

```python
def ClosestPair(S):
	if |S| = 1 then
		return (), dis = inf
	if |S| = 2 then
		return (p1, p2), dis = |p1 - p2|
	Let m be the median of S, # O(n)
	Sl are points < m. Sr > m
	(l1, l2), dis1 = ClosestPair(Sl)
	(r1, r2), dis2 = ClosestPair(Sr)
	(l3, r3), dis3 = last in Sl, first in Sr.
	
	return pair, dis = min(dis1, dis2, dis3)
```
---
### Dynamic Programming

Max / Min Path

```python
def PathSum(A):
	S <- [n+1][m+1] * 0
	for i = 1..n
		for j = 1..m
			S[i,j] = A[i,j] + max{S(i-1,j), S(i,j-1)} # or min
	return S[n,m] # return bottom
```
O(nm) runtime

```python
LIS(A[1..n]):
  d[1..n] ← +∞
  len ← 0
  for x in A:
    k ← lower_bound(d, x)
    d[k] ← x
    len ← max(len, k)
  return len
```
O(n log n)

```python
WIS(jobs sorted by finish):
  OPT[0] ← 0
  for i=1..n:
    OPT[i] ← max{ OPT[i-1], w[i] + OPT[p[i]] }   
    # p[i] via binary search on finishes
  return OPT[n]
```

### Greedy
