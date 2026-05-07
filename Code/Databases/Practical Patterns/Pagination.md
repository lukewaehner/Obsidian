---
tags:
  - sql
  - patterns
type: note
related:
  - "[[Indexes]]"
  - "[[Databases]]"
---
# Pagination

Fetching large result sets in pages.

## LIMIT / OFFSET (Simple, but Broken at Scale)

```sql
-- Page 1
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 0;
-- Page 2
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 20;
-- Page N
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET (page - 1) * 20;
```

### Problems with OFFSET

**Performance degrades at depth**: `OFFSET 10000` makes the database read and discard 10,000 rows before returning 20. The query gets slower the deeper you go.

**Missing or duplicate rows**: If rows are inserted or deleted between page fetches, rows shift — you skip some or see duplicates.

Use LIMIT/OFFSET only for small datasets or admin UIs where deep pagination doesn't matter.

## Cursor-Based Pagination (Keyset Pagination)

Instead of skipping N rows, use the last seen value as a cursor. The database uses an index to jump directly to the right place.

```sql
-- First page
SELECT id, title, created_at
FROM posts
ORDER BY created_at DESC, id DESC
LIMIT 20;

-- Next page: pass the created_at and id from the last row
SELECT id, title, created_at
FROM posts
WHERE (created_at, id) < ($last_created_at, $last_id)
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

### Why the composite condition works

`(created_at, id) < (X, Y)` uses PostgreSQL's row comparison — it's equivalent to:

```sql
WHERE created_at < X OR (created_at = X AND id < Y)
```

This correctly handles ties on `created_at`.

### Index for cursor pagination

```sql
-- Create an index matching the ORDER BY
CREATE INDEX idx_posts_pagination ON posts(created_at DESC, id DESC);
```

### Returning a cursor token

In an API, encode the cursor as an opaque token:

```json
{
  "data": [...],
  "next_cursor": "eyJjcmVhdGVkX2F0IjoiMjAyNC0wMS0xNSIsImlkIjo0Mn0="
}
```

Decode server-side to get the WHERE clause values.

### Limitations

- Can only go forward (or backward with reversed comparison)
- Can't jump to page 7 directly — must paginate sequentially
- The cursor column(s) must be part of ORDER BY

## COUNT for Total Pages

Counting total rows is expensive on large tables:

```sql
-- Slow on large tables
SELECT COUNT(*) FROM posts WHERE user_id = 5;
```

Approaches:
- Use approximate count from `pg_class` for rough estimates
- Cache the count and update periodically
- Avoid showing "page X of Y" UI — use "load more" / infinite scroll instead

```sql
-- Approximate row count (very fast)
SELECT reltuples::bigint AS approximate_count
FROM pg_class
WHERE relname = 'posts';
```

## Choosing the Right Approach

| Scenario | Use |
|----------|-----|
| Admin UI, small table, arbitrary page jumps | LIMIT/OFFSET |
| Public API, large table, infinite scroll | Cursor-based |
| Large table, "load more" button | Cursor-based |
| Search results with relevance ordering | LIMIT/OFFSET (usually small result set) |

## See Also

- [[Indexes]] — Indexes for ORDER BY columns
- [[Practical Patterns]] — Other common SQL patterns
- [[Databases]]
