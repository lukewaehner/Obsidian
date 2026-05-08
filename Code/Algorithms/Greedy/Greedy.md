# Greedy Algorithms

Greedy algorithms build solutions by making locally optimal choices at each step, never looking back or worrying about future consequences.

## Core Concepts

### What Makes an Algorithm Greedy?
- [[Greedy Algorithm Pattern]] - The general structure and components of greedy algorithms
- [[Greedy vs Dynamic Programming]] - When to use greedy vs DP approaches

### Proof Techniques
- [[Greedy Stays Ahead Proof Technique]] - The primary method for proving greedy correctness

## Classic Problems

### Interval Scheduling
- [[Interval Scheduling Problem]] - The unweighted interval scheduling problem
- [[Earliest Finish Time Rule]] - The optimal greedy solution and its proof

## Key Insights

### Advantages
- **Fastest and simplest** when applicable
- **Sometimes optimal** - produces the best solution
- **Great hints** - even when not optimal, guides toward better solutions  
- **Easy to adapt** - simplicity makes them flexible across domains

### Challenges
- **Proof required** - Must prove the greedy choice is correct
- **Limited applicability** - Only works for specific problem types
- **Easy to get wrong** - Intuitive approaches often fail

### Common Characteristics
- Sorting usually dominates complexity ($O(n \log n)$)
- Single pass through data
- Minimal memory usage
- Local choices must lead to global optimum

## Relationship to Other Paradigms
- [[Dynamic Programming]] - More powerful but slower; greedy is special case
- [[Divide and Conquer]] - Different paradigm with independent subproblems
- [[Sorts]] - Often the bottleneck in greedy algorithms

---

*Part of: [[Algorithms]]*

```folder-overview
id: 85a0aa67-ecc4-4736-9569-3d7784ad3518
folderPath: Code/Algorithms/Greedy
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
<span class="fv-link-list-start" id="85a0aa67-ecc4-4736-9569-3d7784ad3518"></span>
- [[Code/Algorithms/Greedy/Earliest Finish Time Rule.md|Earliest Finish Time Rule]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Greedy/Greedy Algorithm Pattern.md|Greedy Algorithm Pattern]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Greedy/Greedy Stays Ahead Proof Technique.md|Greedy Stays Ahead Proof Technique]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Greedy/Greedy vs Dynamic Programming.md|Greedy vs Dynamic Programming]] <span class="fv-link-list-item"></span>
- [[Code/Algorithms/Greedy/Interval Scheduling Problem.md|Interval Scheduling Problem]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="85a0aa67-ecc4-4736-9569-3d7784ad3518"></span>
