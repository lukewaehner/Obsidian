---
tags: [algorithms, graphs, classification]
---

# Graph Types

## Directed vs Undirected
- **Directed**: Edges have a direction $(u, v)$ (ordered pair)
- **Undirected**: Edges have no direction $\{u, v\}$ (unordered set)

## Simple Graphs
We will only look at **simple graphs**:
- No self-loops
- No multi-edges (multiple edges between same pair of vertices)

## Cyclic vs Acyclic
- **Cyclic**: Contains cycles
- **Acyclic**: No cycles present

## Weighted vs Unweighted
- **Weighted**: Edges (sometimes vertices) have weights
- **Unweighted**: No weights assigned

## Special Graph Types

### Trees
- Undirected
- Acyclic
- Connected

See [[Trees and Rooted Trees]] for details.

### DAGs (Directed Acyclic Graphs)
- Directed
- Acyclic

Important for:
- Topological ordering
- Dependency resolution
- Task scheduling

See [[DAGs and Topological Ordering]] for details.

### Bipartite Graphs
- Vertices split into two sets
- All edges connect vertices from different sets
- No edges within the same set

### Complete Graphs ($K_n$)
- Every possible edge exists
- For $n$ vertices: $\binom{n}{2} = \frac{n(n-1)}{2}$ edges

## Related Topics
- [[Graph Basics]]
- [[Graph Terminology]]
- [[Trees and Rooted Trees]]
- [[DAGs and Topological Ordering]]
