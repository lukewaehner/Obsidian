# Dijkstra's Algorithm

## Overview

**Dijkstra's Algorithm** solves the **single-source shortest path problem** for graphs with **non-negative edge weights**.

- **Input**: Weighted graph G = (V, E) with weight function w: E → ℝ≥0, and source vertex s
- **Output**: Shortest path distances from s to all other vertices
- **Constraint**: All edge weights must be **non-negative** (w(e) ≥ 0 for all e ∈ E)

## Problem Definition

### Single-Source Shortest Path (SSSP)

Given:
- A weighted directed graph G = (V, E)
- A weight function w: E → ℝ (assigns weight to each edge)
- A source vertex s

Find:
- δ(s, v) = shortest path distance from s to every vertex v ∈ V
- The actual shortest paths (can be reconstructed using parent pointers)

### Shortest Path Properties

**Path weight**: w(p) = sum of all edge weights on path p

**Shortest path distance**: δ(s, v) = min{w(p) : p is a path from s to v}
- If no path exists: δ(s, v) = ∞

## Algorithm Intuition

Dijkstra's algorithm uses a **greedy approach**:

1. Maintain a set S of vertices whose shortest path distances are **finalized**
2. Repeatedly select the **unfinalized vertex with minimum distance estimate**
3. **Relax** all edges leaving that vertex
4. Add vertex to finalized set

### Key Insight

With non-negative weights, once we select the closest unfinalized vertex, we've found its true shortest path. Why? Any other path would have to go through a farther vertex first, making it longer.

## Algorithm

```python
def Dijkstra(G, w, s):
    # Initialize
    for v in V:
        d[v] = ∞              # Distance estimate
        parent[v] = NULL      # Parent in shortest path tree
    
    d[s] = 0                  # Distance to source is 0
    S = ∅                     # Set of finalized vertices
    Q = V                     # Priority queue of unfinalized vertices
    
    while Q is not empty:
        u = ExtractMin(Q)     # Get vertex with minimum d[u]
        S = S ∪ {u}          # Finalize u
        
        # Relax all edges leaving u
        for each edge (u, v) ∈ E:
            if d[v] > d[u] + w(u, v):
                d[v] = d[u] + w(u, v)    # Update distance
                parent[v] = u             # Update parent
                DecreaseKey(Q, v)         # Update priority in Q
    
    return d, parent
```

## Relaxation

**Relaxation** is the process of improving shortest path estimates:

```python
def Relax(u, v, w):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)
        parent[v] = u
```

**Intuition**: If going through u provides a shorter path to v, update v's distance.

## Time Complexity

The complexity depends on the **priority queue implementation**:

| Implementation | ExtractMin | DecreaseKey | Total Time |
|----------------|------------|-------------|------------|
| **Array** | O(n) | O(1) | **O(n² + m)** = **O(n²)** |
| **Binary Heap** | O(log n) | O(log n) | **O((n + m) log n)** |
| **Fibonacci Heap** | O(log n) | O(1) amortized | **O(n log n + m)** |

### Analysis Details

- **ExtractMin**: Called n times (once per vertex)
- **DecreaseKey**: Called at most m times (once per edge relaxation)

**For sparse graphs** (m ≈ n): Binary heap gives O(n log n)
**For dense graphs** (m ≈ n²): Array implementation gives O(n²), same as binary heap

## Correctness

### Loop Invariant

**At the start of each iteration**:
- For all v ∈ S: d[v] = δ(s, v) (finalized vertices have correct distances)
- For all v ∉ S: d[v] = shortest path using only vertices in S as intermediates

### Why Non-Negative Weights Matter

Dijkstra's greedy choice works because:
1. When we select vertex u with minimum d[u]
2. Any path to u through an unfinalized vertex v would have distance ≥ d[v] ≥ d[u]
3. Since all weights are non-negative, extending that path can only make it longer
4. Therefore, d[u] is the true shortest path distance

**With negative weights**, this breaks: a path through a farther vertex might become shorter after adding a negative edge.

## Example Walkthrough

```
Graph:
    s --2--> a
    |        |
    4        1
    |        |
    v        v
    b --3--> c

Weights: w(s,a)=2, w(s,b)=4, w(a,c)=1, w(b,c)=3
```

| Step | u | S | d[s] | d[a] | d[b] | d[c] |
|------|---|---|------|------|------|------|
| Init | - | ∅ | 0 | ∞ | ∞ | ∞ |
| 1 | s | {s} | 0 | 2 | 4 | ∞ |
| 2 | a | {s,a} | 0 | 2 | 4 | 3 |
| 3 | c | {s,a,c} | 0 | 2 | 4 | 3 |
| 4 | b | {s,a,c,b} | 0 | 2 | 4 | 3 |

Final shortest paths:
- s to a: 2 (via s→a)
- s to b: 4 (via s→b)
- s to c: 3 (via s→a→c)

## Reconstructing Shortest Paths

Use parent pointers to trace back from target to source:

```python
def GetPath(target, parent):
    path = []
    current = target
    while current != NULL:
        path.prepend(current)
        current = parent[current]
    return path
```

## Variants and Extensions

### All-Pairs Shortest Path
Run Dijkstra from each vertex: O(n³) with array, O(n²log n + nm) with binary heap

### Single-Target Shortest Path
Run Dijkstra from target on reverse graph

### Bidirectional Dijkstra
Run from source and target simultaneously, stop when they meet

## Limitations

**Cannot handle**:
- ❌ Negative edge weights (use [[Bellman-Ford Algorithm]] instead)
- ❌ Negative cycles (no shortest path exists)

**Can handle**:
- ✓ Directed or undirected graphs
- ✓ Disconnected graphs (unreachable vertices stay at ∞)
- ✓ Zero-weight edges

## Practical Considerations

### Implementation Tips
1. Use adjacency list representation
2. Binary heap is usually best in practice
3. Can terminate early if only interested in distance to specific target
4. For road networks, use A* (Dijkstra + heuristic) for better performance

### Common Mistakes
- Forgetting to initialize distances to ∞
- Using Dijkstra with negative weights (gives wrong answers)
- Not updating priority queue after DecreaseKey
- Inefficient priority queue implementation

## Applications

1. **GPS Navigation**: Finding shortest routes
2. **Network Routing**: OSPF protocol uses Dijkstra
3. **Social Networks**: Finding degrees of separation
4. **Game AI**: Pathfinding for NPCs
5. **Operations Research**: Resource allocation, scheduling

## Comparison with Other Algorithms

| Algorithm | Weights | Time | Use When |
|-----------|---------|------|----------|
| **Dijkstra** | Non-negative | O(n² or (n+m)log n) | General SSSP |
| **BFS** | Unweighted (all 1) | O(n + m) | Unweighted graphs |
| **Bellman-Ford** | Any (even negative) | O(nm) | Negative weights possible |
| **Floyd-Warshall** | Any | O(n³) | All-pairs shortest paths |

## Related Topics

- [[Bellman-Ford Algorithm]] - Handles negative weights
- [[Breadth First Search]] - Special case for unweighted graphs
- [[Priority Queue]] - Key data structure for efficient implementation
- [[Shortest Path Problem]] - General problem category
- [[Graph Representations]] - Adjacency list vs matrix

---

**Topics**: Dijkstra's Algorithm, Shortest Paths, Greedy Algorithms, Priority Queues