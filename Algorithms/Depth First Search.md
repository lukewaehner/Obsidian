# Depth First Search (DFS)

## Overview

**Depth First Search (DFS)** is a graph traversal algorithm that explores as far as possible along each branch before backtracking.

- **Time Complexity**: Θ(n + m) where n = vertices, m = edges
- **Space Complexity**: Θ(n) for storing parent pointers, discovery times, and finish times

## DFS Algorithm for Directed Graphs

```python
# G = (V, E) is a digraph
for u in V:
    p[u], d[u], f[u] = NULL, -1, -1  # parent, discovery, finish

clock = 1

def DFS(u):
    d[u] = clock                    # Discovery time
    clock = clock + 1
    
    for (u, v) in E:                # Explore all neighbors
        if d[v] == -1:              # If v not discovered
            p[v] = u                # Set parent
            DFS(v)                  # Recurse
    
    f[u] = clock                    # Finish time
    clock = clock + 1
```

### Algorithm Components

- **p[u]**: Parent of vertex u in DFS tree
- **d[u]**: Discovery time (when first visited)
- **f[u]**: Finish time (when finished exploring)
- **clock**: Global counter for timestamps

## Edge Classification in Directed Graphs

DFS classifies every edge into one of four types:

### 1. Tree Edges
- Edges that **discover new nodes**
- Form the DFS tree/forest
- Edge (u, v) where v was undiscovered when explored from u

### 2. Forward Edges
- From **ancestor to descendant** in DFS tree
- Not tree edges, but go "forward" in the tree

### 3. Back Edges
- From **descendant to ancestor** in DFS tree
- **Implies a directed cycle** exists in G
- Critical for cycle detection

### 4. Cross Edges
- Between vertices with **no ancestral relationship**
- Can go between different DFS trees or across subtrees

## Edge Classification Using Discovery/Finish Times

For any directed edge (u, v):

| Time Relationship | Edge Type | Notes |
|-------------------|-----------|-------|
| d[u] < d[v] < f[v] < f[u] | Tree or Forward | u finished after v |
| d[v] < d[u] < f[u] < f[v] | Back | u inside v's discovery interval |
| d[v] < f[v] < d[u] < f[u] | Cross | v completely finished before u started |
| d[u] < d[v] < f[u] < f[v] | **Impossible** | Cannot finish before child |
| d[v] < d[u] < f[v] < f[u] | **Impossible** | DFS always finishes before ancestor |

## DFS in Undirected Graphs

### Key Differences

- **No forward edges possible** in undirected graphs
- **No cross edges possible** in undirected graphs
- Every edge is either:
  - **Tree edge**, or
  - **Back edge**

### Why No Forward/Cross Edges?

When traversing edge (u, v) in an undirected graph:
- If v is undiscovered: (u, v) is a tree edge
- If v is already discovered: (u, v) is a back edge
- No other possibilities exist in undirected graphs

Think: If v was discovered but finished, we would have discovered u from v already (since edges are bidirectional).

## DFS Properties and Characteristics

### Exploration Guarantees

- Every **reachable vertex** is explored exactly once
- Every **edge** is explored exactly once
- Different processing orders lead to different DFS trees and edge classifications
- However, reachability results remain consistent

### Multiple DFS Trees

If the graph is disconnected:
- DFS creates a **DFS forest** (multiple trees)
- Must call DFS from each unvisited vertex

### Practical Considerations

**Space**: Only need to store three arrays of size n:
- Parent pointers: p[]
- Discovery times: d[]
- Finish times: f[]

**Time**: Each vertex is visited once, each edge explored once:
- Visit all vertices: Θ(n)
- Explore all edges: Θ(m)
- Total: Θ(n + m)

## Applications

1. **Cycle Detection**: Check for back edges
2. **Topological Sorting**: Use finish times (for DAGs)
3. **Connected Components**: Count separate DFS trees
4. **Path Finding**: Use parent pointers to reconstruct paths
5. **Strongly Connected Components**: Advanced DFS application

## Related Topics

- [[Breadth First Search]] - Alternative graph traversal
- [[Topological Ordering]] - Uses DFS finish times
- [[Graph Terminology]] - Basic graph concepts
- [[Cycle Detection]] - Using back edges

---

**Source**: CS3000 Lecture 13 (October 24, 2025)
**Topics**: Depth First Search, Edge Classification, Graph Traversal