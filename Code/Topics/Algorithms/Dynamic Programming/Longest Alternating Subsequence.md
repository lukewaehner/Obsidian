---
tags: [algorithms, dynamic-programming, sequences]
---

# Longest Alternating Subsequence

## Problem Definition
A subsequence of sequence $x = (x_1, x_2, ..., x_n)$ is **alternating** if one of the following holds:

### Option 1: Start High
$$x_{i_1} > x_{i_2} < x_{i_3} > \cdots x_{i_k}$$
where $1 \leq i_1 < i_2 < \cdots < i_k \leq n$

### Option 2: Start Low
$$x_{i_1} < x_{i_2} > x_{i_3} < \cdots x_{i_k}$$
where $1 \leq i_1 < i_2 < \cdots < i_k \leq n$

## Layman's Terms
The subsequence keeps **alternating between increasing and decreasing** after every term.

## Example
For sequence: [5, 1, 8, 3, 9, 2, 7]

Alternating subsequences:
- [5, 1, 8, 3, 9] (high-low-high-low-high)
- [1, 8, 3, 9, 2, 7] (low-high-low-high-low-high)

## Related Topics
- [[Longest Increasing Subsequence]]
- [[Sequences and Subsequences]]
- [[Dynamic Programming]]
