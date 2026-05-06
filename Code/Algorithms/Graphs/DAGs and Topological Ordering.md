---
tags: [algorithms, graphs, dag, topological-sort]
---

# DAGs and Topological Ordering

## Directed Acyclic Graphs (DAGs)

### Definition
A **DAG** is a directed graph with no cycles.

### Properties
- No back edges (back edges create cycles)
- Can be ordered topologically
- Represents dependency relationships without circular dependencies

### Common Applications
- Task scheduling
- Course prerequisites
- Build systems (e.g., Makefile dependencies)
- Data processing pipelines

## Topological Ordering

### Definition
A **topological ordering** is a linear ordering of vertices such that:
- For every directed edge $(u, v)$, vertex $u$ comes before vertex $v$ in the ordering

Visually: If vertices are arranged left to right, all edges point left to right.

### Example: Course Prerequisites
```
Discrete → Algo → ToC
    ↓       ↓
Fundies I → Fundies II → OOD → Databases
                                  ↓
                              Graduation
```

Valid topological orderings:
- Discrete, Fundies I, Algo, Fundies II, OOD, Databases, ToC, Graduation
- Fundies I, Discrete, Algo, Fundies II, ToC, OOD, Databases, Graduation
- And many others...

### Existence
A topological ordering exists **if and only if** the graph is a DAG.
- Cycles prevent topological ordering
- DAGs always have at least one topological ordering

## Algorithm I: In-Degree Method

### Intuition
The first node in a topological ordering has no incoming edges!

### Algorithm
```python
# Initialize
Z = empty queue    # Queue of nodes with in-degree 0
i = 1             # Position in ordering

# Find all nodes with in-degree 0
for u in V:
    calculate in-degree of u
    if in-degree == 0:
        append u to Z

# Process nodes
while Z is not empty:
    remove first node u from Z
    assign position i in ordering to u
    
    # Update neighbors
    for (u, v) in E:
        decrement in-degree of v
        if in-degree of v == 0:
            append v to Z
    
    i = i + 1
```

### Complexity
**$\Theta(n + m)$** if carefully implemented

### How It Works
1. Start with nodes that have no dependencies (in-degree 0)
2. Remove each node and its outgoing edges
3. Repeat: find new nodes with in-degree 0
4. Continue until all nodes processed

## Algorithm II: DFS Method

### Key Insight
**Claim**: Ordering vertices by **decreasing DFS finish time** gives a topological ordering.

### Proof
- Suppose decreasing $f[u]$ isn't a topological order
- Then there exists edge $(u, v)$ with $f[u] < f[v]$
- This means $v$ finished after $u$, so $(u, v)$ is a back edge
- But DAGs cannot have back edges (they create cycles)
- Contradiction! Therefore, decreasing finish time is a valid topological order.

### Algorithm
```python
def DFS(u):
    d[u] = clock
    clock = clock + 1
    
    for (u, v) in E:
        if d[v] == -1:
            p[v] = u
            DFS(v)
    
    f[u] = clock
    clock = clock + 1
    prepend u to TopOrder    # Add to front of list
```

### Complexity
**$\Theta(n + m)$** (same as DFS)

### Why It Works
- A node is finished only after all its descendants are finished
- If $(u, v)$ is an edge, $v$ is finished before $u$
- Therefore, $f[u] > f[v]$ for all edges $(u, v)$
- Decreasing finish time respects all edge directions

## Comparison of Algorithms

| Aspect | In-Degree Method | DFS Method |
|--------|------------------|------------|
| Time | $\Theta(n + m)$ | $\Theta(n + m)$ |
| Space | $O(n)$ | $O(n)$ |
| Intuition | Remove nodes with no dependencies | Finish descendants before ancestors |
| Implementation | Iterative with queue | Recursive |

Both methods are equally valid and efficient!

## Multiple Valid Orderings

DAGs typically have **many** valid topological orderings.

### Example
For graph: $A \to B \to D$ and $A \to C \to D$

Valid orderings include:
- $A, B, C, D$
- $A, C, B, D$

But NOT:
- $B, A, C, D$ (violates $A \to B$)
- $A, D, B, C$ (violates $B \to D$ and $C \to D$)

## Detecting Non-DAGs

### In-Degree Method
If algorithm terminates with unprocessed vertices, the graph has a cycle.

### DFS Method
If DFS finds a back edge, the graph has a cycle (not a DAG).

## Related Topics
- [[Code/Topics/Algorithms/Graphs/Depth First Search]]
- [[Graph Types]]
- [[Graph Terminology]]
