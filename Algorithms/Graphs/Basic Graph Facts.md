---
tags: [algorithms, graphs, facts, properties]
---

# Basic Graph Facts

## Degree Sum
**Sum of degrees in an undirected graph must be even and equal to $2m$**.

Why? Each edge $\{u, v\}$ contributes to both $\deg(u)$ and $\deg(v)$, so every edge is counted twice.

$$\sum_{v \in V} \deg(v) = 2|E|$$

This implies there's always an even number of vertices with odd degree (proven by contradiction).

## Maximum Number of Edges

### Undirected Graph
For $|V| = n$, $|E| = m$:

$$m \leq \binom{n}{2} = \frac{n(n-1)}{2} = O(n^2)$$

This maximum is achieved in a **complete graph** $K_n$ - choose any two endpoints.

### Directed Graph
For $|V| = n$:

$$m \leq 2 \cdot \binom{n}{2} = n(n-1) = O(n^2)$$

Each unordered pair can have edges in both directions.

## Practice Problems

### Coloring
Show a planar graph which needs 4 colors (for revision).

### Eulerian Path/Cycle
Visit every edge exactly once (for revision).

### Trees
Key properties (see [[Trees and Rooted Trees]]):
1. Connected, acyclic, undirected
2. Unique path between any two vertices
3. $+1$ edge adds cycle
4. $-1$ edge disconnects

## Related Topics
- [[Graph Basics]]
- [[Graph Terminology]]
- [[Graph Types]]
