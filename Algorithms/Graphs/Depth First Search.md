---
tags: [algorithms, graphs, traversal, dfs]
---

# Depth First Search (DFS)

## Algorithm

DFS explores a graph by going as deep as possible before backtracking.

### Pseudocode
```python
# G = (V, E) is a digraph
for u in V:
    p[u], d[u], f[u] = NULL, -1, -1

clock = 1

def DFS(u):
    d[u] = clock           # Discovery time
    clock = clock + 1
    
    for (u, v) in E:       # Explore neighbors
        if d[v] == -1:     # Not yet discovered
            p[v] = u       # Set parent
            DFS(v)         # Recurse
    
    f[u] = clock           # Finish time
    clock = clock + 1
```

### Data Structures
- `p[u]`: Parent of vertex $u$ in DFS tree
- `d[u]`: Discovery time (when vertex first visited)
- `f[u]`: Finish time (when all descendants explored)

## Edge Classification

DFS classifies edges based on the relationship between vertices:

### For Directed Graphs
1. **Tree edges**: Discover new nodes (edges in DFS tree)
   - Parent to child in DFS tree
   
2. **Forward edges**: Ancestor to descendant (not tree edge)
   - Skip generations in DFS tree
   
3. **Back edges**: Descendant to ancestor
   - **Important**: Indicates a directed cycle in $G$
   
4. **Cross edges**: No ancestral relation
   - Between different branches of DFS tree

### For Undirected Graphs
Only two types possible:
- **Tree edges**: Discover new nodes
- **Back edges**: Connect to ancestor

**Why no forward/cross edges?** 
If $(u, v)$ exists and $u$ is discovered before $v$, then $v$ must be discovered during $u$'s recursive call (making it a tree edge). Otherwise it would have been discovered earlier.

## Determining Edge Types

### Using Discovery/Finish Times
For any directed edge $(u, v)$:

| Condition | Edge Type |
|-----------|-----------|
| $d[u] < d[v] < f[v] < f[u]$ | Tree or Forward |
| $d[v] < d[u] < f[u] < f[v]$ | Back |
| $d[v] < f[v] < d[u] < f[u]$ | Cross |

**Impossible cases**:
- $d[u] < d[v] < f[u] < f[v]$: Cannot finish before child
- $d[v] < d[u] < f[v] < f[u]$: DFS won't allow (always finish before ancestor)

### Visual Pattern
```
Tree/Forward:  [u ... [v ... ] ... ]   (u contains v)
Back:          [v ... [u ... ] ... ]   (v contains u)
Cross:         [v ... ] ... [u ... ]   (disjoint intervals)
```

## Complexity Analysis

### Time Complexity
**$\Theta(n + m)$** where $n = |V|$, $m = |E|$

- Each vertex is visited exactly once
- Each edge is examined exactly once
- For each vertex $u$, we loop through all its neighbors

### Space Complexity
**$\Theta(n)$**

Storage for:
- Parent array: $O(n)$
- Discovery times: $O(n)$
- Finish times: $O(n)$

## Properties

1. **DFS creates a forest**: Multiple trees if graph not connected
2. **Every reachable vertex explored exactly once**
3. **Every reachable edge explored exactly once**
4. **Different processing order** → different trees/classifications
5. **Can reconstruct DFS tree** using parent pointers
6. **Detects cycles**: Back edges indicate cycles

## Applications

### Cycle Detection
- Directed graph has cycle ↔ DFS finds a back edge

### Connected Components
- Run DFS from each unvisited vertex
- Each DFS tree is a connected component

### Topological Sorting
- For DAGs, reverse finish times give topological order
- See [[DAGs and Topological Ordering]]

### Path Finding
- Parent pointers form paths in DFS tree

## Example Walkthrough

For graph with edges: $(a,b), (b,c), (c,d), (d,a), (d,b)$

Starting DFS from $a$:

| Vertex | Parent | Discovery | Finish |
|--------|--------|-----------|--------|
| a | NULL | 1 | 8 |
| b | a | 2 | 7 |
| c | b | 3 | 6 |
| d | c | 4 | 5 |

Edge classifications:
- $(a,b)$: Tree edge
- $(b,c)$: Tree edge
- $(c,d)$: Tree edge
- $(d,a)$: Back edge (cycle!)
- $(d,b)$: Back edge

## Related Topics
- [[Graph Traversal Algorithms]]
- [[DAGs and Topological Ordering]]
- [[Graph Types]]
- [[Breadth First Search]]
