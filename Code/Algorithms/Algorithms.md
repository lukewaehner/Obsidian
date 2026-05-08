**Course Focus**: Design, analysis, and correctness of algorithms using mathematical foundations and various algorithmic paradigms.

## Core Topics

### Mathematical Foundations
- **Proof Techniques**: Induction, contradiction, correctness proofs
- **Asymptotic Analysis**: Big-O, Θ, Ω notation for runtime analysis
- **[[Recurrences]]**: Solving recurrence relations
- **[[Master Theorem]]**: Analyzing divide-and-conquer algorithms

### Algorithmic Paradigms

#### [[Divide and Conquer]]
Breaking problems into smaller subproblems, solving recursively, and combining results.
- Multiplication algorithms
- [[Sorts|Sorting algorithms]]
- [[Order Statistics]]

#### [[Dynamic Programming]]
Building solutions from optimal subproblem solutions with memoization.
- Compare & contrast with divide-and-conquer and greedy approaches
- Bottom-up vs top-down approaches

#### [[Greedy]]
Making locally optimal choices with the hope of finding global optimum.
- Short-sighted and easy to describe
- Non-trivial to prove correctness

### Data Structures

#### [[Code/Topics/Algorithms/Graphs/Binary Search Trees]]
Self-balancing trees for O(log n) operations.
- BST operations, rotations, balancing
- Applications: sets, dictionaries, priority queues

### Graph Algorithms

#### [[Graphs]]
Modeling pairwise relationships between entities.

**Traversal Algorithms**:
- [[Code/Topics/Algorithms/Depth First Search]] - Explore deeply, edge classification
- Breadth First Search - Level-by-level exploration

**Topological Ordering**:
- [[Topological Ordering]] - Linear ordering of DAGs

**Shortest Path Algorithms**:
- [[Dijkstra's Algorithm]] - Single-source shortest paths (non-negative weights)
- [[Bellman-Ford Algorithm]] - Single-source shortest paths (handles negative weights)

**Advanced Topics**:
- Network flows
- Minimum spanning trees

### Special Topics
- Number-theoretic algorithms
- Linear programming
- Randomization
- Approximation algorithms
- Computational hardness (NP-completeness)

## Course Materials

### Problem Sets & Exams
- [[PS4]] - Problem Set 4
- [[Exam]] - Exam preparation and review

### Practice Problems
- [[Drone Drop Durability]] - Application problem

## Organization by Topic

### Complexity Analysis
- [[Times]] - Runtime analysis notes
- [[Recurrences]] - Solving recurrence relations
- [[Master Theorem]] - D&C complexity analysis

### Algorithmic Techniques
- [[Divide and Conquer]]
- [[Dynamic Programming]]
- [[Greedy]]

### Data Structures & Algorithms
- [[Code/Topics/Algorithms/Binary Search/Binary Search]] - Binary search algorithms
- [[Code/Topics/Algorithms/Graphs/Binary Search Trees]] - Self-balancing trees
- [[Sorts]] - Sorting algorithms
- [[Graphs]] - Graph algorithms and theory

### Shortest Paths
- [[Dijkstra's Algorithm]] - Non-negative weights, O((n+m)log n)
- [[Bellman-Ford Algorithm]] - Negative weights, O(nm)

### Graph Traversal & Ordering
- [[Code/Topics/Algorithms/Depth First Search]] - DFS, edge classification
- [[Topological Ordering]] - Ordering DAGs

## Key Concepts

**Algorithm Design**:
1. Understand the problem
2. Choose appropriate paradigm (D&C, DP, Greedy, etc.)
3. Design algorithm
4. Prove correctness
5. Analyze time & space complexity

**Complexity Classes**:
- O(1) - Constant
- O(log n) - Logarithmic
- O(n) - Linear
- O(n log n) - Linearithmic
- O(n²) - Quadratic
- O(2ⁿ) - Exponential

---

**Course Number**: CS3000
**Topics**: Algorithms, Data Structures, Complexity Analysis, Graph Theory

[[Code/Algorithms/Graphs/Binary Search Trees|Binary Search Trees]]

```folder-overview
id: ca188108-c793-4612-beb1-33ff88fce172
folderPath: Code/Algorithms
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
<span class="fv-link-list-start" id="ca188108-c793-4612-beb1-33ff88fce172"></span>
- [[Code/Algorithms/Bellman-Ford Algorithm.md|Bellman-Ford Algorithm]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Depth First Search.md|Depth First Search]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dijkstra's Algorithm.md|Dijkstra's Algorithm]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Divide and Conquer.md|Divide and Conquer]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Drone Drop Durability.md|Drone Drop Durability]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Master Theorem.md|Master Theorem]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Order Statistics.md|Order Statistics]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Recurrences.md|Recurrences]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Topological Ordering.md|Topological Ordering]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="ca188108-c793-4612-beb1-33ff88fce172"></span>
