---
tags: [algorithms, dynamic-programming, strings, sequences, similarity]
---

# Edit Distance and Sequence Alignment

## Motivation

### String Similarity
- [[Longest Common Subsequence|LCS]] tells us the longest subsequence common to two sequences
- But what if we want to know how "close" two sequences are?

### Applications
- Autocorrect
- OCR (Optical Character Recognition)
- DNA similarity (and RNA, proteins, etc.)

### Example Problem
Strings "ocurrance" and "occurrence" seem similar, but exactly how similar?

```
o c u r r a n c e ·
o c c u r r e n c e
```

Without careful definitions, they're mismatched in 7 out of 10 letters!

## Edit Distance Definition
Given two strings $x \in \Sigma^n$, $y \in \Sigma^m$, the **edit distance** is the minimum number of **insertions**, **deletions**, and **substitutions/swaps** required to turn $x$ into $y$.

## Sequence Alignments
Given an alignment between two strings $x$ and $y$, the **cost** of such an alignment is the number of **mismatched positions**.

### Optimal Alignment Example
Best alignment of "ocurrance" and "occurrence" (cost 2):
```
o c · u r r a n c e
o c c u r r e n c e
```

**Key insight**: Edit distance can also be defined as the **cost of the minimum cost alignment**.

## DP Algorithm

### Possible Last Column Cases
In an alignment, the last column can be in one of these cases:

1. $(x_i, \cdot)$ - Character from $x$ present, none from $y$ → **delete from** $x$
2. $(\cdot, y_j)$ - Character from $x$ absent, character from $y$ present → **insert into** $x$
3. $(x_i, y_j)$ - Same character for both $x$ and $y$ → **matching characters**
4. $(x_i, y_j)$ - Two different characters → **mismatch**

### DP Approach
Try each case, recurse on rest of the input, pick best.

## Recurrence Relation
Define $OPT(i, j)$ as the edit distance of strings $x_1...x_i$ and $y_1...y_j$:

$$
OPT(i, j) = 
\begin{cases}
i & j = 0 \\
j & i = 0 \\
\min \begin{cases}
1 + OPT(i-1, j) & \text{(delete)} \\
1 + OPT(i, j-1) & \text{(insert)} \\
\mathbb{1}[x_i \neq y_j] + OPT(i-1, j-1) & \text{(match/mismatch)}
\end{cases} & \text{otherwise}
\end{cases}
$$

Where $\mathbb{1}[x_i \neq y_j]$ is an **indicator function**:
- 1 if $x_i \neq y_j$
- 0 if $x_i = y_j$

## Example: "SALT" vs "SMALL"

### DP Table

|   | ε | S | M | A | L | L |
|---|---|---|---|---|---|---|
| ε | 0 | 1 | 2 | 3 | 4 | 5 |
| S | 1 | 0 | 1 | 2 | 3 | 4 |
| A | 2 | 1 | 1 | 1 | 2 | 3 |
| L | 3 | 2 | 2 | 2 | 1 | 2 |
| T | 4 | 3 | 3 | 3 | 2 | 2 |

**Edit distance**: 2

### Backtracking for Optimal Alignment
Following the arrows from bottom-right to top-left:

```
S · A L T
S M A L L
```

**Operations**:
1. Match S with S
2. Insert M
3. Match A with A
4. Match L with L
5. Mismatch T → L

## Generalized Edit Distance

### Variable Costs
Different edits can have different costs:
- $c_{ins}(z)$: Cost for inserting letter $z$
- $c_{del}(z)$: Cost for deleting letter $z$
- $c_{sub}(z_1, z_2)$: Cost of swapping $z_1$ with $z_2$, where $c_{sub}(z, z) = 0$

### Modified Recurrence
$$
OPT(i, j) = 
\begin{cases}
\sum_{k=1}^i c_{del}(x_i) & j = 0 \\
\sum_{k=1}^j c_{ins}(y_j) & i = 0 \\
\min \begin{cases}
c_{del}(x_i) + OPT(i-1, j) \\
c_{ins}(y_j) + OPT(i, j-1) \\
c_{sub}(x_i, y_j) + OPT(i-1, j-1)
\end{cases} & \text{otherwise}
\end{cases}
$$

## Relations to Other Problems

### LCS via Edit Distance
[[Longest Common Subsequence|LCS]] only allows insertions and deletions.

Set costs:
- $c_{sub}(z, z) = 0$ (matching is free)
- $c_{sub}(z_1, z_2) = \infty$ (no substitutions allowed)
- $c_{ins}(z) = c_{del}(z) = 1$

### Edit Distance with Transpositions
Exchange adjacent letters (e.g., "teh" → "the")

Add extra case to recurrence:
$$c_{tra}(x_{i-1}, x_i, y_{j-1}, y_j) + OPT(i-2, j-2)$$

### LIS via LCS
[[Longest Increasing Subsequence|LIS]] of $x$ can be solved using LCS:
- Use $x$ and $sorted(x)$ as inputs to LCS

## Related Topics
- [[Sequences and Subsequences]]
- [[Longest Increasing Subsequence]]
- [[Dynamic Programming]]
