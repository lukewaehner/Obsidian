---
tags: [algorithms, graphs, trees]
---

# Trees and Rooted Trees

## Trees (Undirected)
A **tree** is an undirected graph that satisfies 2 out of 3 properties:
1. Connected, acyclic, undirected graph
2. Unique path between any two vertices
3. Connected graph with $n-1$ edges

### Additional Properties
- Adding any edge makes it cyclic
- Removing any edge disconnects it

### Important Equivalence
$(Min \space degree \space 2 \implies cycles) \iff (Trees \implies \exists v \in V, deg(v) = 1)$

## Rooted Trees
A tree with a designated **root** vertex and oriented edges.

### Terminology

#### Node Relationships
- **Root**: Top node, has no parent
- **Parent**: Only one per node
- **Children**: Direct descendants (connected by downward edges)
- **Leaves**: Nodes with no children
- **Siblings**: Nodes sharing a common parent
- **Ancestors**: Parent, grandparent, great-grandparent, etc.
- **Descendants**: Children, grandchildren, etc.

#### Tree Measurements
- **Subtree**: All descendants of a node
- **Height of node**: 
  - 0 if node is a leaf
  - $1 + \max(\text{height(children)})$ otherwise
  - Max distance to any leaf in its subtree
- **Depth of node**:
  - 0 if node is root
  - $1 + \text{depth(parent)}$ otherwise
  - Distance from root to the node
- **Height of tree**: $\max \space \text{depth of any node}$ = depth of deepest node

#### Tree Arity
- **k-ary tree**: Every node has $\leq k$ children (we use smallest possible k)
- **Binary tree**: $k = 2$ (most common)

### Levels
Nodes can be organized by levels:
- **Level 0**: Root node
- **Level 1**: Children of root
- **Level 2**: Children of level 1 nodes
- And so on...

Depth of nodes at level $i$ is $i$.

## Related Topics
- [[Graph Terminology]]
- [[Graph Types]]
- [[Code/Topics/Algorithms/Graphs/Binary Search Trees]]
