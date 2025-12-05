
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
