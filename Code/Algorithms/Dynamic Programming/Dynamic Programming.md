---
tags: [algorithms, dynamic-programming, hub]
---

# Dynamic Programming

Dynamic Programming is an algorithmic technique for solving optimization problems by breaking them down into overlapping subproblems and storing solutions to avoid redundant computation.

## Core Concepts
- [[DP Introduction]] - Memoization, optimal substructure, and the general approach

## Classic Problems

### Scheduling and Optimization
- [[Weighted Interval Scheduling]] - Maximum weight subset of non-overlapping jobs
- [[Knapsack Problem]] - Maximizing value within weight constraints
- [[Maximum Grid Path Sum]] - Finding optimal paths through grids

### Sequence Problems
- [[Sequences and Subsequences]] - Fundamental definitions and concepts
- [[Longest Increasing Subsequence]] - Finding longest increasing subsequences
- [[Longest Alternating Subsequence]] - Subsequences that alternate up and down
- [[Edit Distance and Sequence Alignment]] - Measuring string similarity and transformations

## Advanced Topics
- [[Space Optimization in DP]] - Reducing space complexity in DP solutions

## Key Techniques
1. **Identify subproblem structure**
2. **Derive Bellman Optimality Equation**
3. **Choose implementation approach**:
   - Top-down with memoization (recursive)
   - Bottom-up with tabulation (iterative)
4. **Analyze time and space complexity**
5. **Implement backtracking** (if solution path needed)

## Common Patterns
- **Sequential**: Process elements one at a time (WIS, LIS)
- **Two-sequence**: Compare/align two sequences (Edit Distance, LCS)
- **Grid/Matrix**: Navigate 2D structures (Grid Path)
- **Bounded resource**: Optimize with constraints (Knapsack)

## Related Topics
- [[Divide and Conquer]] - Similar optimal substructure, but without overlapping subproblems
- [[Greedy]] - Sometimes works, but DP needed when greedy fails
- [[Recurrences]] - Understanding time complexity of recursive solutions

```folder-overview
id: e94656a0-805c-4376-b750-4470c7f10aa5
folderPath: Code/Algorithms/Dynamic Programming
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
<span class="fv-link-list-start" id="e94656a0-805c-4376-b750-4470c7f10aa5"></span>
- [[Code/Algorithms/Dynamic Programming/DP Introduction.md|DP Introduction]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dynamic Programming/Edit Distance and Sequence Alignment.md|Edit Distance and Sequence Alignment]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dynamic Programming/Knapsack Problem.md|Knapsack Problem]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dynamic Programming/Longest Alternating Subsequence.md|Longest Alternating Subsequence]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dynamic Programming/Longest Increasing Subsequence.md|Longest Increasing Subsequence]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dynamic Programming/Maximum Grid Path Sum.md|Maximum Grid Path Sum]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dynamic Programming/Sequences and Subsequences.md|Sequences and Subsequences]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dynamic Programming/Space Optimization in DP.md|Space Optimization in DP]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Dynamic Programming/Weighted Interval Scheduling.md|Weighted Interval Scheduling]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="e94656a0-805c-4376-b750-4470c7f10aa5"></span>
