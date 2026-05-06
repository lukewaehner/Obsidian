---
tags: [algorithms, graphs, data-structures, representation]
---

# Graph Representations

## Adjacency Matrix

### Structure
- $n \times n$ matrix $A$
- $A_{ij} = \begin{cases} 1 & \text{if } \{i,j\} \in E \\ 0 & \text{otherwise} \end{cases}$

### Properties
- **Undirected graph**: $A_{ij} = A_{ji}$ (symmetric matrix)
- **Directed graph**: $A_{ij}$ indicates edge from $i$ to $j$

### Complexity
- **Space**: $O(n^2)$
- **Time to test edge**: $O(1)$
- **Time to list neighbors**: $O(n)$

### Example
For graph with vertices $\{a, b, c, d\}$ and edges $\{a,b\}, \{a,c\}, \{a,d\}, \{b,d\}, \{c,d\}$:

|   | a | b | c | d |
|---|---|---|---|---|
| a | 0 | 1 | 1 | 1 |
| b | 1 | 0 | 0 | 1 |
| c | 1 | 0 | 0 | 1 |
| d | 1 | 1 | 1 | 0 |

## Adjacency List

### Structure (Undirected)
For each vertex $v$, store a list of its neighbors.

```
a: [b, c, d]
b: [a, d]
c: [a, d]
d: [a, b, c]
```

### Structure (Directed)
Can store:
- **Outgoing edges only**: `a: [b, c]` (most common)
- **Incoming and outgoing separately**: 
  ```
  a: in[d], out[b, c]
  ```

### Complexity
- **Space**: $O(m)$ where $m = |E|$
  - Better than adjacency matrix when graph is sparse
  - For a tree: $O(m) = O(n)$ since $m = n-1$
- **Time to test edge $\{u,v\}$**: $O(n)$ (not too tight, actually $O(\max(\deg(u), \deg(v)))$)
- **Time to list neighbors of $u$**: $O(\deg(u))$

### When to Use
Adjacency lists are better than adjacency matrix when:
1. The graph doesn't have too many edges
2. Example: For a tree, $O(m) = O(n)$ vs $O(n^2)$ for matrix

## Comparison

| Operation | Adjacency Matrix | Adjacency List |
|-----------|------------------|----------------|
| Space | $O(n^2)$ | $O(m)$ |
| Test edge | $O(1)$ | $O(n)$ (better: $O(\deg)$) |
| List neighbors | $O(n)$ | $O(\deg(u))$ |

## Related Topics
- [[Graph Basics]]
- [[Graph Terminology]]
