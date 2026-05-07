---
tags:
  - sql
  - performance
type: note
related:
  - "[[Indexes]]"
  - "[[EXPLAIN]]"
  - "[[Databases]]"
---
# Query Performance

Finding and fixing slow queries in production.

## Finding Slow Queries

### pg_stat_statements (PostgreSQL)

The most useful extension for identifying what to optimize:

```sql
-- Enable (add to postgresql.conf or run once)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Top 10 slowest queries by total time
SELECT
  round(total_exec_time::numeric, 2) AS total_ms,
  calls,
  round(mean_exec_time::numeric, 2)  AS avg_ms,
  round((100 * total_exec_time / sum(total_exec_time) OVER())::numeric, 2) AS pct,
  query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;

-- Queries with worst average time (slow per-call)
SELECT query, calls, round(mean_exec_time::numeric, 2) AS avg_ms
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Reset stats
SELECT pg_stat_statements_reset();
```

### Slow query log

```sql
-- Log queries taking longer than 1 second
-- In postgresql.conf:
-- log_min_duration_statement = 1000  (milliseconds)
-- Or set for current session:
SET log_min_duration_statement = 500;
```

## Table and Index Health

```sql
-- Table sizes
SELECT
  tablename,
  pg_size_pretty(pg_total_relation_size(tablename::text)) AS total,
  pg_size_pretty(pg_relation_size(tablename::text)) AS table_only,
  pg_size_pretty(pg_indexes_size(tablename::text)) AS indexes
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(tablename::text) DESC;

-- Sequential scans on large tables (should usually be index scans)
SELECT schemaname, relname, seq_scan, idx_scan,
       n_live_tup AS rows
FROM pg_stat_user_tables
WHERE seq_scan > 0
ORDER BY seq_scan DESC;

-- Unused indexes (wasting space and slowing writes)
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;
```

## The N+1 Problem

The most common ORM-related performance problem. Instead of one query, you run N+1 queries.

```python
# N+1: runs 1 query to get orders, then 1 query per order to get the user
orders = db.query("SELECT * FROM orders LIMIT 100")
for order in orders:
    user = db.query("SELECT * FROM users WHERE id = ?", order.user_id)
    print(f"{user.name}: {order.total}")
# 101 queries total
```

Fix: join or load the related data in one query:

```sql
-- Single query with JOIN
SELECT orders.id, orders.total, users.name
FROM orders
JOIN users ON orders.user_id = users.id
LIMIT 100;
```

Or use your ORM's eager loading:

```python
# Rails
orders = Order.includes(:user).limit(100)

# Python SQLAlchemy
orders = session.query(Order).options(joinedload(Order.user)).limit(100)
```

## Missing Index Indicators

| Symptom | Likely cause |
|---------|-------------|
| Seq scan on large table | Missing index on filter/join column |
| High `seq_scan` in pg_stat | Same — add index |
| Query time spikes as table grows | Missing index, currently fine on small data |
| `ORDER BY` causing sort node in EXPLAIN | No index on sort column |
| Slow JOIN | No index on foreign key column |

## Query Optimization Techniques

### Push filters down — filter early

```sql
-- Slow: join everything, then filter
SELECT * FROM orders
JOIN users ON orders.user_id = users.id
WHERE users.country = 'US';

-- Better: filter in a subquery first (planner usually does this, but not always)
SELECT * FROM orders
JOIN (SELECT id FROM users WHERE country = 'US') u ON orders.user_id = u.id;
```

### Avoid functions on indexed columns

```sql
-- Won't use index on email
WHERE LOWER(email) = 'alice@example.com'

-- Fix 1: expression index
CREATE INDEX idx_users_lower_email ON users(LOWER(email));

-- Fix 2: store lowercase in the column
```

### Use EXISTS instead of COUNT for existence checks

```sql
-- Slow: counts all matching rows
SELECT * FROM users WHERE (SELECT COUNT(*) FROM orders WHERE user_id = users.id) > 0;

-- Fast: stops at first match
SELECT * FROM users WHERE EXISTS (SELECT 1 FROM orders WHERE user_id = users.id);
```

### Avoid SELECT * in production queries

`SELECT *` fetches all columns including large ones (TEXT, JSONB, bytea). Select only what you need.

## Vacuuming and Statistics

PostgreSQL needs regular maintenance:

```sql
-- Update statistics (helps planner make better decisions)
ANALYZE tablename;
ANALYZE;  -- all tables

-- Reclaim dead rows (normally automatic)
VACUUM tablename;
VACUUM ANALYZE tablename;

-- Check autovacuum is running
SELECT relname, last_autovacuum, last_autoanalyze, n_dead_tup
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```

If `n_dead_tup` is very high, autovacuum isn't keeping up — the table is bloated.

## See Also

- [[Indexes]] — Adding indexes to fix slow queries
- [[EXPLAIN]] — Reading query plans
- [[Databases]]
