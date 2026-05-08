---
tags: [algorithms, graphs, hub]
---

# Graphs

Graphs are fundamental data structures for modeling relationships between objects. This collection covers graph theory basics, representations, and algorithms.

## Core Concepts

### Fundamentals
- [[Graph Basics]] - Definition, components, and real-world examples
- [[Graph Terminology]] - Neighbors, degree, paths, cycles, and connectedness
- [[Graph Types]] - Directed, undirected, weighted, acyclic, and special graphs
- [[Basic Graph Facts]] - Degree sums, edge bounds, and key properties

### Representations
- [[Graph Representations]] - Adjacency matrices and adjacency lists

## Special Graph Structures

### Trees
- [[Trees and Rooted Trees]] - Tree properties, rooted trees, and terminology
- [[Code/Topics/Algorithms/Graphs/Binary Search Trees]] - BST invariant, operations, balancing, and applications

## Graph Algorithms

### Traversal
- [[Code/Topics/Algorithms/Graphs/Depth First Search]] - DFS algorithm, edge classification, and applications

### Ordering
- [[DAGs and Topological Ordering]] - Directed acyclic graphs and topological sort algorithms

## Key Patterns

### When to Use Graphs
- Modeling relationships: social networks, dependencies, hierarchies
- Path problems: routing, navigation, reachability
- Scheduling: task ordering, resource allocation
- Data structures: trees, tries, state machines

### Common Graph Types in Practice
- **Trees**: Hierarchical data, file systems, organizational charts
- **DAGs**: Task scheduling, course prerequisites, build dependencies
- **Weighted graphs**: Shortest paths, minimum spanning trees, network flow
- **Bipartite graphs**: Matching problems, recommendation systems

## Complexity Reference

| Structure/Algorithm | Space | Key Operations |
|---------------------|-------|----------------|
| Adjacency Matrix | $O(n^2)$ | Test edge: $O(1)$, List neighbors: $O(n)$ |
| Adjacency List | $O(m)$ | Test edge: $O(\deg)$, List neighbors: $O(\deg)$ |
| BST (balanced) | $O(n)$ | Search/Insert/Delete: $O(\log n)$ |
| DFS | $O(n)$ | Traversal: $O(n + m)$ |
| Topological Sort | $O(n)$ | Sorting: $O(n + m)$ |

## Related Topics
- [[Dynamic Programming]] - Often uses graphs for state spaces
- [[Greedy]] - Many greedy algorithms work on graphs
- [[Divide and Conquer]] - Can be applied to tree structures

```folder-overview
id: c2abf9c9-b5a7-4fef-b9a3-957f8e1b5e88
folderPath: Code/Algorithms/Graphs
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="c2abf9c9-b5a7-4fef-b9a3-957f8e1b5e88"></span>
- [[Code/Algorithms/Graphs/Basic Graph Facts.md|Basic Graph Facts]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Graphs/Binary Search Trees.md|Binary Search Trees]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Graphs/DAGs and Topological Ordering.md|DAGs and Topological Ordering]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Graphs/Depth First Search.md|Depth First Search]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Graphs/Graph Basics.md|Graph Basics]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Graphs/Graph Representations.md|Graph Representations]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Graphs/Graph Terminology.md|Graph Terminology]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Graphs/Graph Types.md|Graph Types]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Graphs/Trees and Rooted Trees.md|Trees and Rooted Trees]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="c2abf9c9-b5a7-4fef-b9a3-957f8e1b5e88"></span>
