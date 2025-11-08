# Topological Ordering

## Definition

A **topological ordering** (or topological sort) of a directed acyclic graph (DAG) is a linear ordering of vertices such that for every directed edge (u, v), vertex u comes before vertex v in the ordering.

**Key requirement**: The graph must be a **DAG** (Directed Acyclic Graph) - no cycles allowed.

## Intuition

- Imagine arranging all vertices in a line from left to right
- Since the DAG is acyclic, there exists some ordering where **all edges point left to right**
- Any such valid ordering is a topological ordering

### Example: Course Prerequisites

```
Discrete → Algo → ToC
    ↓       ↘
Fundies I → Fundies II → OOD → Databases → Graduation
```

Valid topological ordering:
`Discrete, Fundies I, Algo, Fundies II, OOD, Databases, ToC, Graduation`

## Algorithm I: In-Degree Method

### Intuition
- The first node in any topological ordering must have **no incoming edges** (in-degree = 0)
- After placing a node, we can "remove" it and find the next node with in-degree 0

### Algorithm

```python
# Initialize
Z = empty queue  # Queue of zero in-degree nodes
i = 1            # Position in ordering

# Find all nodes with no incoming edges
for u in V:
    in_degree[u] = count incoming edges to u
    if in_degree[u] == 0:
        Z.append(u)

# Process nodes with zero in-degree
while Z is not empty:
    u = Z.remove_first()
    position[u] = i              # Assign position in ordering
    i = i + 1
    
    for (u, v) in E:             # For each outgoing edge
        in_degree[v] -= 1        # Decrement in-degree
        if in_degree[v] == 0:
            Z.append(v)          # Add to queue if now zero
```

### Time Complexity
**Θ(n + m)** if carefully implemented:
- Computing all in-degrees: Θ(n + m)
- Processing all vertices: Θ(n)
- Processing all edges: Θ(m)

### Implementation Notes
- Use an adjacency list representation for the graph
- Maintain in-degree counts in an array
- Use a queue (or any collection) for zero in-degree nodes

## Algorithm II: DFS Finish Time Method

### Key Insight
**Ordering vertices by decreasing DFS finish time produces a valid topological ordering.**

### Algorithm

```python
def DFS(u):
    d[u] = clock
    clock = clock + 1
    
    for (u, v) in E:
        if d[v] == -1:           # If v not discovered
            p[v] = u
            DFS(v)
    
    f[u] = clock
    clock = clock + 1
    prepend u to TopOrder        # Add to front of ordering
```

### Why This Works: Proof

**Claim**: Ordering by decreasing finish time is a valid topological ordering.

**Proof by contradiction**:
1. A DAG has **no back edges** (back edges create cycles)
2. Suppose the decreasing f[u] ordering is NOT a valid topological ordering
3. Then there exists an edge (u, v) where f[u] < f[v]
   - This means v finishes after u
   - But u has an edge to v
4. If we follow edge (u, v) during DFS:
   - If v is undiscovered: we visit v, so f[v] < f[u] ✓
   - If v is discovered but unfinished: (u, v) is a back edge ✗
   - If v is finished: (u, v) is a cross/forward edge, so f[v] < f[u] ✓
5. The only way f[u] < f[v] is if (u, v) is a back edge
6. But DAGs cannot have back edges
7. **Contradiction** → our assumption was wrong
8. Therefore, decreasing finish time is a valid topological ordering ∎

### Time Complexity
**Θ(n + m)** - same as DFS:
- Run DFS on the graph: Θ(n + m)
- Prepending to list can be O(1) with linked list

### Advantages
- Simple to implement (just DFS + prepend)
- No need to compute in-degrees
- Can detect if graph has cycle (back edge found)

## Comparing the Two Algorithms

| Aspect | In-Degree Method | DFS Method |
|--------|------------------|------------|
| **Time** | Θ(n + m) | Θ(n + m) |
| **Space** | Θ(n) for in-degrees | Θ(n) for DFS arrays |
| **Intuition** | Iteratively remove sources | Reverse post-order |
| **Implementation** | Requires queue | Uses recursion/stack |
| **Cycle Detection** | Can detect (nodes remain) | Can detect (back edge) |

Both algorithms are equally efficient - choose based on:
- What data structures you already have
- Whether you're already using DFS
- Personal preference for iterative vs recursive

## Properties of Topological Orderings

### Non-Uniqueness
- A DAG can have **multiple valid** topological orderings
- The number depends on the structure of the graph

### Existence
- A directed graph has a topological ordering **if and only if** it is a DAG
- If the graph has a cycle, no topological ordering exists

### Applications
1. **Task Scheduling**: Dependencies between tasks
2. **Build Systems**: Compile order for dependencies
3. **Course Prerequisites**: Valid course taking order
4. **Spreadsheet Formulas**: Evaluation order
5. **Package Management**: Installation order

## Related Topics

- [[Depth First Search]] - Used in Algorithm II
- [[Directed Acyclic Graphs]] - Required for topological ordering
- [[Cycle Detection]] - Related to existence of topological ordering
- [[Graph Terminology]] - In-degree, out-degree concepts

---

**Source**: CS3000 Lecture 13 (October 24, 2025)
**Topics**: Topological Ordering, DAGs, DFS Applications