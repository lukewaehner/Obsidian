---
tags:
  - sql
  - performance
type: note
related:
  - "[[Databases]]"
  - "[[EXPLAIN]]"
  - "[[Query Performance]]"
---
# Indexes

Indexes are separate data structures the database maintains to find rows without scanning every row in the table. They're the single biggest lever for query performance.

## How They Work

Without an index, a query like `WHERE email = 'alice@example.com'` reads every row in the table — a **sequential scan** (seq scan). With an index on `email`, the database jumps directly to the matching rows in O(log n) time via a **B-tree**.

Indexes cost: they use disk space and slow down writes (INSERT/UPDATE/DELETE must update the index too). Add them deliberately.

## Creating Indexes

```sql
-- Basic index
CREATE INDEX idx_users_email ON users(email);

-- Unique index (also enforces uniqueness constraint)
CREATE UNIQUE INDEX idx_users_email ON users(email);

-- Composite index (column order matters — see below)
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Partial index — only index rows matching a condition
CREATE INDEX idx_orders_pending ON orders(created_at)
  WHERE status = 'pending';

-- Expression index
CREATE INDEX idx_users_lower_email ON users(lower(email));

-- Drop an index
DROP INDEX idx_users_email;
```

In PostgreSQL, `CREATE INDEX CONCURRENTLY` builds without locking the table — use this in production:

```sql
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
```

## Composite Indexes and Column Order

A composite index on `(a, b, c)` can be used for:
- `WHERE a = ?`
- `WHERE a = ? AND b = ?`
- `WHERE a = ? AND b = ? AND c = ?`
- `ORDER BY a`, `ORDER BY a, b`

It **cannot** be used efficiently for:
- `WHERE b = ?` alone — leftmost column must be present
- `WHERE c = ?` alone

```sql
-- Index on (user_id, created_at)
SELECT * FROM orders WHERE user_id = 5;                     -- uses index
SELECT * FROM orders WHERE user_id = 5 AND created_at > X; -- uses index, efficient
SELECT * FROM orders WHERE created_at > X;                  -- cannot use index
```

Rule: put the most selective column (most unique values) first, or the column used in equality filters first.

## Covering Indexes

If an index contains all the columns a query needs, the database never touches the table — **index-only scan**. Much faster.

```sql
-- Query only needs user_id and status
SELECT user_id, status FROM orders WHERE user_id = 5;

-- Covering index for this query
CREATE INDEX idx_orders_cover ON orders(user_id) INCLUDE (status);
-- PostgreSQL syntax — INCLUDE adds non-key columns
```

## Partial Indexes

Index only a subset of rows. Smaller, faster, and the planner uses them when the WHERE clause matches:

```sql
-- Only index unprocessed jobs — table might have millions of processed ones
CREATE INDEX idx_jobs_pending ON jobs(created_at)
  WHERE processed = false;

-- Only this query benefits (matches the partial index condition)
SELECT * FROM jobs WHERE processed = false ORDER BY created_at;
```

## When the Index Is NOT Used

The planner won't use an index when:

```sql
-- Function wrapping the column prevents index use
WHERE lower(email) = 'alice@x.com'   -- won't use index on email
-- Fix: create an expression index on lower(email)

-- Implicit type cast
WHERE user_id = '5'                  -- user_id is int, '5' is string
-- Fix: use the right type

-- Leading wildcard
WHERE name LIKE '%alice%'            -- can't use B-tree index
-- Fix: use full-text search

-- NOT on indexed column
WHERE status != 'active'             -- often not worth using index
```

## Index Types (PostgreSQL)

| Type | Use case |
|------|----------|
| **B-tree** | Default. Equality, ranges, sorting |
| **Hash** | Equality only — rarely needed |
| **GIN** | Arrays, JSONB, full-text search |
| **GiST** | Geometric types, full-text search |
| **BRIN** | Very large tables with natural ordering (timestamps, IDs) |

```sql
-- GIN index for JSONB queries
CREATE INDEX idx_events_data ON events USING GIN (data);

-- GIN index for full-text search
CREATE INDEX idx_posts_search ON posts USING GIN (to_tsvector('english', body));
```

## What to Index

Index columns that:
- Appear in `WHERE` clauses frequently
- Are used in `JOIN` conditions (foreign keys)
- Are used in `ORDER BY` / `GROUP BY`
- Have high cardinality (many distinct values) — low-cardinality columns like `status` with 3 values often not worth it

Don't index:
- Small tables (seq scan is faster)
- Columns rarely used in queries
- Tables with very high write rates and rare reads

## Checking Existing Indexes

```sql
-- PostgreSQL: list indexes on a table
\d users

-- Or query directly
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'users';

-- Index usage stats (are your indexes being used?)
SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read
FROM pg_stat_user_indexes
WHERE tablename = 'users';
```

If `idx_scan` is 0, the index isn't being used — consider dropping it.

## See Also

- [[EXPLAIN]] — Reading query plans to verify index use
- [[Query Performance]] — Identifying slow queries
- [[Databases]]

%% Begin Waypoint %%
- [[EXPLAIN]]
- [[Query Performance]]

%% End Waypoint %%
