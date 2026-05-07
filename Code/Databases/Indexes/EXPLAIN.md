---
tags:
  - sql
  - performance
type: note
related:
  - "[[Indexes]]"
  - "[[Query Performance]]"
  - "[[Databases]]"
---
# EXPLAIN

Reading query execution plans to understand and fix slow queries.

## Basic Usage

```sql
-- Show the plan without running the query
EXPLAIN SELECT * FROM orders WHERE user_id = 5;

-- Run the query AND show actual timing + row counts
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 5;

-- Full output with buffers (I/O stats)
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) SELECT * FROM orders WHERE user_id = 5;
```

Always use `EXPLAIN ANALYZE` in development — `EXPLAIN` alone shows estimates, `ANALYZE` shows what actually happened.

## Reading the Output

```
Seq Scan on orders  (cost=0.00..4234.00 rows=150 width=64) (actual time=0.012..18.4 rows=147 loops=1)
  Filter: (user_id = 5)
  Rows Removed by Filter: 99853
```

| Field | Meaning |
|-------|---------|
| **cost=0.00..4234.00** | Estimated startup cost .. total cost (arbitrary units) |
| **rows=150** | Estimated number of rows returned |
| **actual time=0.012..18.4** | Actual startup ms .. total ms |
| **rows=147** | Actual rows returned |
| **loops=1** | How many times this node ran |

The **indented tree structure** shows nested operations — inner nodes execute first.

## Scan Types

### Seq Scan — bad for large tables

Reads every row. Fine for small tables or when fetching a large fraction of rows.

```
Seq Scan on orders (cost=0.00..4234.00 rows=150 width=64)
  Filter: (user_id = 5)
  Rows Removed by Filter: 99853    ← read 100k rows, kept 147
```

99,853 rows thrown away — this needs an index.

### Index Scan — good

Uses an index to find matching rows, then fetches them from the table.

```
Index Scan using idx_orders_user_id on orders (cost=0.29..8.32 rows=147 width=64)
  Index Cond: (user_id = 5)
```

### Index Only Scan — best

All needed columns are in the index — no table access required.

```
Index Only Scan using idx_orders_cover on orders
  Index Cond: (user_id = 5)
  Heap Fetches: 0    ← never touched the table
```

### Bitmap Index Scan

Used when many rows match — fetches a bitmap of pages, then reads those pages.

```
Bitmap Heap Scan on orders
  Recheck Cond: (status = 'pending')
  ->  Bitmap Index Scan on idx_orders_status
```

## Join Types

```
Hash Join  (cost=...) 
  Hash Cond: (orders.user_id = users.id)
  ->  Seq Scan on orders
  ->  Hash
        ->  Seq Scan on users
```

| Join type | When used |
|-----------|-----------|
| **Hash Join** | Large tables, equality join. Builds hash table of smaller side. |
| **Nested Loop** | Small tables or when inner side is indexed. For each outer row, probe inner. |
| **Merge Join** | Both sides already sorted. Efficient but requires sorted input. |

## Diagnosing Problems

### High "Rows Removed by Filter"

A seq scan that throws away most rows — add an index on the filter column.

### Estimated vs Actual rows wildly different

```
(cost=... rows=1000 ...) (actual ... rows=1 ...)
```

The planner had bad statistics. Run `ANALYZE tablename` to update stats.

### Sort appears in plan

```
Sort  (cost=... rows=...)
  Sort Key: created_at
```

If this is slow, an index on `created_at` may avoid the sort entirely (index already sorted).

### Nested Loop with many loops

```
Nested Loop (... loops=50000)
```

50,000 iterations — the inner side should be an index scan. If it's a seq scan, add an index.

## Common Fixes

| Symptom | Fix |
|---------|-----|
| Seq scan on large table | Add index on filter/join column |
| Bad row estimates | `ANALYZE tablename` |
| Sort on large result | Index on ORDER BY column |
| Hash join on huge tables | Check if a composite index could help |
| Index scan but still slow | Check if a covering index would eliminate table fetches |

## Interpreting Cost Numbers

Cost numbers are relative (not milliseconds). High cost ≠ always slow — it's the planner's estimate. `EXPLAIN ANALYZE` gives real times.

A useful heuristic: if `actual time` on a node is high and `Rows Removed by Filter` is large, that node needs an index.

## See Also

- [[Indexes]] — Creating and choosing indexes
- [[Query Performance]] — Slow query logging and monitoring
- [[Databases]]
