
---

## Recursion in SQL

Recursive CTEs for hierarchical or graph queries.

---

## Basic Syntax

```sql
WITH RECURSIVE T(n) AS (
  -- Base case
  VALUES(1)
  UNION ALL
  -- Recursive case
  SELECT n + 1
  FROM T
  WHERE n <= 3
)
SELECT n FROM T
```

Returns: 1, 2, 3, 4

---

## Fibonacci Example

```sql
WITH RECURSIVE Fib AS (
  SELECT 0 AS n, 0 AS fibn, 1 AS fibn1
  UNION ALL
  SELECT n + 1, fibn1, fibn1 + fibn
  FROM Fib
)
SELECT * FROM Fib
LIMIT 10
```

---

## Graph Queries

Find all reachable nodes in a graph:

```sql
WITH RECURSIVE P AS (
  -- Base: direct edges
  SELECT S, T FROM A
  UNION
  -- Recursive: paths through intermediate nodes
  SELECT A.S, P.T
  FROM A, P
  WHERE A.T = P.S
)
SELECT * FROM P
```

Computes transitive closure of the graph.

```folder-overview
id: 35202e7a-eeaa-4d65-8a5a-312401743997
folderPath: Code/Databases/Recursion in SQL
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
<span class="fv-link-list-start" id="35202e7a-eeaa-4d65-8a5a-312401743997"></span>
<span class="fv-link-list-end" id="35202e7a-eeaa-4d65-8a5a-312401743997"></span>
