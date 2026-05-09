---
tags:
  - sql
type: note
related:
  - "[[Databases]]"
  - "[[Transactions]]"
---
# Data Modification

INSERT, UPDATE, DELETE — and how to use them effectively in practice.

## INSERT

```sql
-- Single row
INSERT INTO users (email, name, created_at)
VALUES ('alice@example.com', 'Alice', NOW());

-- Multiple rows (much faster than individual inserts)
INSERT INTO users (email, name) VALUES
  ('alice@example.com', 'Alice'),
  ('bob@example.com',   'Bob'),
  ('carol@example.com', 'Carol');

-- From a query
INSERT INTO archive_orders (SELECT * FROM orders WHERE created_at < '2023-01-01');
```

### RETURNING — get back what was inserted

```sql
-- Get the generated ID
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice')
RETURNING id, created_at;

-- Get multiple columns
INSERT INTO orders (user_id, total)
VALUES (1, 99.99)
RETURNING id, created_at, status;
```

`RETURNING` is PostgreSQL-specific. Eliminates the need for a follow-up `SELECT` to get the new row's ID.

### INSERT ON CONFLICT — Upsert

Insert a row, or do something specific if it already exists:

```sql
-- Insert or do nothing
INSERT INTO user_preferences (user_id, key, value)
VALUES (1, 'theme', 'dark')
ON CONFLICT (user_id, key) DO NOTHING;

-- Insert or update (upsert)
INSERT INTO user_preferences (user_id, key, value)
VALUES (1, 'theme', 'dark')
ON CONFLICT (user_id, key)
DO UPDATE SET
  value = EXCLUDED.value,
  updated_at = NOW();
-- EXCLUDED refers to the row that failed to insert
```

```sql
-- Increment a counter, creating it if it doesn't exist
INSERT INTO page_views (page, views)
VALUES ('home', 1)
ON CONFLICT (page)
DO UPDATE SET views = page_views.views + 1;
```

## UPDATE

```sql
-- Basic
UPDATE users SET name = 'Alice Smith' WHERE id = 1;

-- Multiple columns
UPDATE users
SET name = 'Alice Smith', updated_at = NOW()
WHERE id = 1;

-- Update based on another table (UPDATE FROM)
UPDATE orders
SET status = 'cancelled'
FROM users
WHERE orders.user_id = users.id
  AND users.account_status = 'suspended';
```

### RETURNING from UPDATE

```sql
UPDATE orders
SET status = 'shipped', shipped_at = NOW()
WHERE id = 1
RETURNING id, status, shipped_at;
```

### UPDATE with subquery

```sql
UPDATE products
SET price = price * 1.1
WHERE category_id IN (
  SELECT id FROM categories WHERE name = 'Electronics'
);
```

## DELETE

```sql
-- Delete specific rows
DELETE FROM sessions WHERE expires_at < NOW();

-- Delete with RETURNING
DELETE FROM jobs WHERE status = 'failed'
RETURNING id, error_message;

-- Delete based on another table (DELETE USING)
DELETE FROM order_items
USING orders
WHERE order_items.order_id = orders.id
  AND orders.status = 'cancelled';
```

## TRUNCATE vs DELETE

```sql
DELETE FROM logs;    -- removes all rows, can be rolled back, fires triggers, slow on large tables
TRUNCATE logs;       -- removes all rows instantly, resets sequences, minimal logging
TRUNCATE logs RESTART IDENTITY;  -- also resets auto-increment sequences
```

Use `TRUNCATE` when you want to empty a large table quickly in dev/test. In PostgreSQL it's transactional.

## Bulk Operations

### Batch inserts in application code

Don't loop single inserts — batch them:

```python
# Slow: one insert per row
for user in users:
    db.execute("INSERT INTO users (email) VALUES (?)", [user.email])

# Fast: one statement, many rows
db.execute(
    "INSERT INTO users (email) VALUES " + ",".join(["(?)"] * len(users)),
    [u.email for u in users]
)
```

### COPY — fastest bulk load (PostgreSQL)

```sql
-- Load from CSV
COPY users (email, name, created_at)
FROM '/path/to/users.csv'
WITH (FORMAT CSV, HEADER true);

-- Export to CSV
COPY (SELECT * FROM users WHERE active = true)
TO '/path/to/export.csv'
WITH (FORMAT CSV, HEADER true);
```

`COPY` bypasses many checks and is orders of magnitude faster than INSERT for bulk loads.

## Common Patterns

### Conditional insert/update (upsert pattern)

```sql
INSERT INTO article_reads (user_id, article_id, count, last_read)
VALUES (1, 42, 1, NOW())
ON CONFLICT (user_id, article_id)
DO UPDATE SET
  count = article_reads.count + 1,
  last_read = NOW();
```

### Moving rows between tables

```sql
WITH moved AS (
  DELETE FROM jobs WHERE status = 'completed'
  RETURNING *
)
INSERT INTO completed_jobs SELECT * FROM moved;
```

### Update-or-insert with CTE

```sql
WITH updated AS (
  UPDATE settings SET value = $2
  WHERE user_id = $1 AND key = $2
  RETURNING *
)
INSERT INTO settings (user_id, key, value)
SELECT $1, $2, $3
WHERE NOT EXISTS (SELECT 1 FROM updated);
```

## See Also

- [[Transactions]] — Wrapping modifications in atomic units
- [[Locking]] — Preventing race conditions in updates
- [[Subqueries]] — Using subqueries in WHERE/FROM for updates
- [[Databases]]

%% Begin Waypoint %%


%% End Waypoint %%
