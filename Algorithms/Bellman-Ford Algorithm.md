

## Overview

**Bellman-Ford Algorithm** solves the **single-source shortest path problem** for graphs that may contain **negative edge weights**.

- **Input**: Weighted graph G = (V, E) with weight function w: E → ℝ, and source vertex s
- **Output**: Shortest path distances from s to all vertices, OR detection of negative cycle
- **Advantage**: Works with **negative edge weights**
- **Limitation**: Slower than Dijkstra, but more general

## Problem Definition

### Single-Source Shortest Path with Negative Weights

Given:
- A weighted directed graph G = (V, E)
- A weight function w: E → ℝ (can be negative!)
- A source vertex s

Find:
- Shortest path distances δ(s, v) for all v ∈ V
- Detect if a negative cycle is reachable from s

### Negative Cycles

A **negative cycle** is a cycle whose total weight is negative.

**Critical property**: If a negative cycle is reachable from s, then shortest paths are **undefined** (can keep going around the cycle to get arbitrarily negative distances).

Bellman-Ford detects this condition.

## Algorithm Intuition

Bellman-Ford uses **dynamic programming**:

1. Shortest paths have at most n - 1 edges (in a graph with n vertices)
2. Repeatedly relax **all edges** n - 1 times
3. Each iteration finds shortest paths using up to k edges
4. After n - 1 iterations, all shortest paths are found
5. One more iteration checks for negative cycles

### Key Insight

After k iterations of relaxing all edges:
- d[v] ≤ shortest path from s to v using at most k edges

After n - 1 iterations:
- d[v] = δ(s, v) for all v (if no negative cycles)

## Algorithm

```python
def BellmanFord(G, w, s):
    # Initialize
    for v in V:
        d[v] = ∞              # Distance estimate
        parent[v] = NULL      # Parent in shortest path tree
    
    d[s] = 0                  # Distance to source is 0
    
    # Relax all edges n-1 times
    for i = 1 to |V| - 1:
        for each edge (u, v) ∈ E:
            if d[v] > d[u] + w(u, v):
                d[v] = d[u] + w(u, v)
                parent[v] = u
    
    # Check for negative cycles
    for each edge (u, v) ∈ E:
        if d[v] > d[u] + w(u, v):
            return "Negative cycle detected"
    
    return d, parent
```

## Relaxation

Same as in Dijkstra:

```python
def Relax(u, v, w):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)
        parent[v] = u
```

**Intuition**: If path through u to v is shorter than current estimate, update it.

## Time Complexity

**O(nm)** where n = |V| and m = |E|

### Analysis
- **Outer loop**: n - 1 iterations
- **Inner loop**: Relax all m edges
- **Negative cycle check**: Check all m edges once more
- **Total**: O(nm)

### Comparison
- **Dijkstra**: O(n² or (n+m)log n) but requires non-negative weights
- **Bellman-Ford**: O(nm) but handles negative weights

For sparse graphs (m ≈ n): Bellman-Ford is O(n²)
For dense graphs (m ≈ n²): Bellman-Ford is O(n³)

## Correctness

### Loop Invariant

**After k iterations of the outer loop**:
- For all vertices v: d[v] ≤ weight of shortest path from s to v using at most k edges

### Proof Sketch

**Base case** (k=0): d[s] = 0, all others = ∞. Correct.

**Inductive step**: Assume true for k-1 iterations.
- Consider any shortest path s → v using k edges: s → ... → u → v
- By induction, after k-1 iterations: d[u] ≤ δ_k-1(s, u)
- In iteration k, we relax edge (u, v)
- So d[v] ≤ d[u] + w(u, v) ≤ δ_k(s, v)

**After n-1 iterations**: Any shortest path has at most n-1 edges (no repeated vertices in an optimal path, except in negative cycles).

### Negative Cycle Detection

If we can still improve any distance in the nth iteration:
- There exists a path of length n with strictly decreasing distances
- By pigeonhole principle, some vertex is repeated
- That repeated vertex forms a cycle with negative total weight

## Example Walkthrough

```
Graph with negative edge:
    s --2--> a
    |        |
    4       -3    (negative!)
    |        |
    v        v
    b --1--> c

Weights: w(s,a)=2, w(s,b)=4, w(a,c)=-3, w(b,c)=1
```

| Iteration | d[s] | d[a] | d[b] | d[c] | Edges Relaxed |
|-----------|------|------|------|------|---------------|
| Init | 0 | ∞ | ∞ | ∞ | - |
| 1 | 0 | 2 | 4 | -1 | (s,a), (s,b), (a,c) |
| 2 | 0 | 2 | 4 | -1 | (b,c) tries but doesn't improve |
| Check | 0 | 2 | 4 | -1 | No improvements → No negative cycle |

Final shortest paths:
- s to a: 2 (via s→a)
- s to b: 4 (via s→b)
- s to c: -1 (via s→a→c)

### Example with Negative Cycle

```
Graph:
    s --1--> a --2--> b
             ^        |
             |       -5  (creates negative cycle: a→b→a = -3)
             +--------+
```

After n-1 iterations, distances are updated.
In the nth iteration (negative cycle check), edge (b,a) can still improve d[a].
→ Negative cycle detected!

## Optimizations

### Early Termination

If no distances change in an iteration, we can stop early:

```python
for i = 1 to |V| - 1:
    changed = False
    for each edge (u, v) ∈ E:
        if d[v] > d[u] + w(u, v):
            d[v] = d[u] + w(u, v)
            parent[v] = u
            changed = True
    if not changed:
        break  # No changes, we're done
```

### Queue-Based Bellman-Ford (SPFA)

Only relax edges from vertices whose distances changed:

```python
def SPFA(G, w, s):
    # Initialize
    for v in V:
        d[v] = ∞
        in_queue[v] = False
    
    d[s] = 0
    Q = Queue([s])
    in_queue[s] = True
    
    while Q is not empty:
        u = Q.dequeue()
        in_queue[u] = False
        
        for each edge (u, v) ∈ E:
            if d[v] > d[u] + w(u, v):
                d[v] = d[u] + w(u, v)
                parent[v] = u
                if not in_queue[v]:
                    Q.enqueue(v)
                    in_queue[v] = True
    
    return d, parent
```

**Average case**: Often much faster in practice, O(km) where k << n
**Worst case**: Still O(nm)

## Finding Vertices Affected by Negative Cycles

```python
# After detecting negative cycle exists
# Run one more round to mark affected vertices

affected = set()
for i = 1 to |V|:
    for each edge (u, v) ∈ E:
        if d[v] > d[u] + w(u, v):
            d[v] = -∞
            affected.add(v)

# All vertices in 'affected' are reachable from negative cycles
```

## Applications

1. **Arbitrage Detection**: Finding profitable cycles in currency exchange
2. **Network Routing**: Protocols that can handle cost adjustments
3. **Scheduling with Penalties**: Problems with negative costs
4. **Constraint Systems**: Difference constraints (system of inequalities)
5. **Game Theory**: Finding equilibria in certain game types

## When to Use Bellman-Ford vs Dijkstra

| Scenario | Use |
|----------|-----|
| All edge weights ≥ 0 | **Dijkstra** (faster) |
| Some negative edges, no negative cycles | **Bellman-Ford** |
| Need to detect negative cycles | **Bellman-Ford** |
| Dense graph, negative weights | **Bellman-Ford** |
| Sparse graph, non-negative weights | **Dijkstra with binary heap** |
| Distributed/parallel setting | **Bellman-Ford** (easier to parallelize) |

## Practical Considerations

### Implementation Tips
1. Use edge list representation (easier for iterating all edges)
2. Consider SPFA optimization for real-world graphs
3. Early termination saves significant time in practice
4. For negative cycle detection, may want to identify which vertices are affected

### Common Mistakes
- Forgetting to check for negative cycles
- Running only n-2 iterations instead of n-1
- Not handling disconnected components properly
- Assuming all vertices affected by negative cycle (only those reachable from it are)

## Relationship to Dynamic Programming

Bellman-Ford is a classic DP algorithm:

**Subproblem**: d_k[v] = shortest path from s to v using at most k edges

**Recurrence**: d_k[v] = min(d_{k-1}[v], min_{(u,v)∈E}(d_{k-1}[u] + w(u,v)))

**Base case**: d_0[s] = 0, d_0[v] = ∞ for v ≠ s

Bellman-Ford uses space optimization (rolling array) to use O(n) space instead of O(n²).

## Variants

### All-Pairs Shortest Paths
- Run Bellman-Ford from each vertex: O(n²m)
- Better: Use [[Floyd-Warshall Algorithm]]: O(n³)

### Longest Path in DAGs
- Negate all weights and run Bellman-Ford
- Or use topological sort + DP: O(n + m)

## Related Topics

- [[Dijkstra's Algorithm]] - Faster but requires non-negative weights
- [[Floyd-Warshall Algorithm]] - All-pairs shortest paths
- [[Dynamic Programming]] - Bellman-Ford is a DP algorithm
- [[Negative Cycles]] - Detection and handling
- [[Shortest Path Problem]] - General problem category

---

**Topics**: Bellman-Ford Algorithm, Shortest Paths, Negative Weights, Negative Cycle Detection