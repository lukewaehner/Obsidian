---
tags: [algorithms, graphs, terminology]
---

# Graph Terminology

## Neighbors
**Neighbors of vertex $v$**: Any other vertex with an edge with it.
- For vertex $a$ with neighbors $b, c$: $N(a) = \{b, c\}$

## Degree
**Degree of a vertex**: $deg(v) = |N(v)|$
- Number of edges "incident" on it
- **In-degree**: Number of incoming edges (directed graphs)
- **Out-degree**: Number of outgoing edges (directed graphs)

## Paths
**Path**: $(v_1, v_2, v_3, ..., v_k)$ with edges $(v_i, v_{i+1})$
- Sequence of vertices with edges between them
- Example: $(a, b, c, d)$ is a path
- NOT a path: $(a, d, b)$ if there's no direct edge from $a$ to $d$

## Cycles
**Cycle**: $(v_1, v_2, ..., v_k)$ where the path ends at the starting point
- Paths that end at starting point
- Examples:
  - 3-cycle (triangle): $(a, b, c, a)$
  - 4-cycle: $(a, b, c, d, a)$
  - One 2-cycle: $(a, b, a)$ (with two edges between them)

## Acyclic Graph
A graph with no cycles at all.

## Trees
An undirected acyclic graph is called a **TREE**.

### Rooted Trees
When edges are oriented:
- **Root** (top node): Has parent but only one
- **Parent**: Only one parent
- **Children** (direct edges downward)
- **Leaves**: No children
- **Subtree**: All descendants of a node
- **Height** (of nodes): Max distance to a leaf
- **Depth** (of nodes): Distance to root = max depth of any node
- **Ancestors**: Parent, grandparent, etc.
- **Descendants**: Children and their children, etc.
- **Siblings**: Common parent
- **k-ary**: If every node has ≤ k children (we say "smallest possible k")

Most common: **k=2** is binary trees.

### Tree Properties
Trees have the following properties (2 out of 3 define a tree):
1. Connected, acyclic, undirected graph
2. Unique path between any two vertices
3. Connected graph with $n-1$ edges
4. Adding any edge makes it cyclic
5. Removing any edge disconnects it

## Connectedness

### Undirected Graphs
Undirected $G$ is **connected** if there's a path between $u$ and $v$ for every $u, v \in V$.

### Directed Graphs
Directed $G = (V, E)$ is **strongly connected** if for all $u, v \in V$ there's a path from $u$ to $v$ AND from $v$ to $u$.

**Weakly connected**: If the undirected version of $G$ is connected.

## Subgraphs
Given $G = (V, E)$, a subgraph $G' = (V', E')$ where:
- $V' \subseteq V$
- $E' \subseteq E$
- For all $\{u, v\} \in E'$: $u, v \in V'$

Only deletions allowed - no modifications or additions.

## Complete Graphs
$G = (V, E)$ is $K_n$ if $|V| = n$ and for all $u, v$, $\{u, v\} \in E$.

All possible edges exist.

| Graph | Vertices | Edges |
|-------|----------|-------|
| $K_1$ | 1 | 0 |
| $K_2$ | 2 | 1 |
| $K_3$ | 3 | 3 (triangle) |
| $K_4$ | 4 | 6 |
| $K_5$ | 5 | 10 |

## Bipartite Graphs
All edges go from one subset of vertices to another.
- Vertices can be partitioned into two disjoint sets
- No edges within the same partition
- All edges connect vertices from different partitions

Can extend to **k-partite** graphs.

## Related Topics
- [[Graph Basics]]
- [[Graph Types]]
- [[Trees and Rooted Trees]]
