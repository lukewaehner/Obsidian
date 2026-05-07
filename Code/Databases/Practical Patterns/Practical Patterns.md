---
tags:
  - sql
  - patterns
type: note
related:
  - "[[Databases]]"
  - "[[Transactions]]"
  - "[[Data Modification]]"
---
# Practical Patterns

Common schema and query patterns used in real applications.

## Soft Deletes

Mark rows as deleted instead of physically removing them. Preserves history and allows recovery.

```sql
ALTER TABLE users ADD COLUMN deleted_at TIMESTAMPTZ;

-- Soft delete
UPDATE users SET deleted_at = NOW() WHERE id = 1;

-- Query active users
SELECT * FROM users WHERE deleted_at IS NULL;

-- Include deleted
SELECT * FROM users; -- or WHERE deleted_at IS NOT NULL for deleted only
```

### Partial index for performance

```sql
-- Index only active users — smaller, faster
CREATE INDEX idx_users_active ON users(email) WHERE deleted_at IS NULL;
```

### Views for convenience

```sql
CREATE VIEW active_users AS
  SELECT * FROM users WHERE deleted_at IS NULL;
```

### Downsides

- Every query needs `WHERE deleted_at IS NULL` — easy to forget
- Unique constraints break: can't have two users with the same email if one is deleted
- Tables grow unbounded

For unique constraints on soft-deleted tables:

```sql
-- Unique only among active rows
CREATE UNIQUE INDEX idx_users_email_active
  ON users(email) WHERE deleted_at IS NULL;
```

## Audit Logs

Track who changed what and when.

### Approach 1: Audit columns on the table

```sql
ALTER TABLE orders ADD COLUMN created_by INT REFERENCES users(id);
ALTER TABLE orders ADD COLUMN updated_by INT REFERENCES users(id);
ALTER TABLE orders ADD COLUMN created_at TIMESTAMPTZ DEFAULT NOW();
ALTER TABLE orders ADD COLUMN updated_at TIMESTAMPTZ DEFAULT NOW();
```

Simple but only tracks latest state.

### Approach 2: Separate audit table

```sql
CREATE TABLE orders_audit (
  id          BIGSERIAL PRIMARY KEY,
  order_id    INT NOT NULL,
  action      TEXT NOT NULL,   -- 'INSERT', 'UPDATE', 'DELETE'
  old_values  JSONB,
  new_values  JSONB,
  changed_by  INT,
  changed_at  TIMESTAMPTZ DEFAULT NOW()
);

-- Trigger to populate it automatically
CREATE OR REPLACE FUNCTION audit_orders() RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO orders_audit (order_id, action, old_values, new_values)
  VALUES (
    COALESCE(NEW.id, OLD.id),
    TG_OP,
    CASE WHEN TG_OP != 'INSERT' THEN row_to_json(OLD) ELSE NULL END,
    CASE WHEN TG_OP != 'DELETE' THEN row_to_json(NEW) ELSE NULL END
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER orders_audit_trigger
  AFTER INSERT OR UPDATE OR DELETE ON orders
  FOR EACH ROW EXECUTE FUNCTION audit_orders();
```

## Optimistic Locking

Prevent lost updates without holding locks. Each row has a version number; update only succeeds if the version matches.

```sql
ALTER TABLE products ADD COLUMN version INT DEFAULT 1;

-- Read the row (and its version)
SELECT id, price, version FROM products WHERE id = 1;
-- Returns: id=1, price=100, version=3

-- Update only if version hasn't changed
UPDATE products
SET price = 110, version = version + 1
WHERE id = 1 AND version = 3;  -- optimistic lock check

-- Check rows affected in application code
-- If 0 rows updated: someone else changed it — retry or show conflict error
```

Use when conflicts are rare and you want to avoid lock contention. Common in APIs.

## Polymorphic Associations

One table that references multiple different parent tables:

```sql
-- Comments that can belong to posts, videos, or products
CREATE TABLE comments (
  id           BIGSERIAL PRIMARY KEY,
  commentable_type TEXT NOT NULL,  -- 'post', 'video', 'product'
  commentable_id   BIGINT NOT NULL,
  body         TEXT,
  user_id      INT REFERENCES users(id)
);

CREATE INDEX idx_comments_polymorphic ON comments(commentable_type, commentable_id);
```

Query:

```sql
SELECT * FROM comments
WHERE commentable_type = 'post' AND commentable_id = 42;
```

Downside: no foreign key constraint possible. Consider separate join tables if referential integrity matters.

## Hierarchical Data

Storing trees in a relational database.

### Adjacency list (simple, but hard to query)

```sql
CREATE TABLE categories (
  id        SERIAL PRIMARY KEY,
  name      TEXT,
  parent_id INT REFERENCES categories(id)  -- null for root
);
```

To get full tree: requires recursive CTE (see [[Recursion in SQL]]).

### Materialized path (fast reads)

```sql
CREATE TABLE categories (
  id   SERIAL PRIMARY KEY,
  name TEXT,
  path TEXT   -- e.g. '1.4.12.' — IDs from root to this node
);

-- All descendants of node 4
SELECT * FROM categories WHERE path LIKE '1.4.%';

-- Ancestors of node 12
SELECT * FROM categories WHERE '1.4.12.' LIKE path || '%';
```

## Conditional Aggregation

Aggregate filtered subsets without multiple queries:

```sql
-- Orders by status in one query
SELECT
  COUNT(*) FILTER (WHERE status = 'pending')   AS pending,
  COUNT(*) FILTER (WHERE status = 'shipped')   AS shipped,
  COUNT(*) FILTER (WHERE status = 'delivered') AS delivered,
  SUM(total) FILTER (WHERE status = 'delivered') AS delivered_revenue
FROM orders
WHERE user_id = 5;

-- Equivalent with CASE WHEN
SELECT
  COUNT(CASE WHEN status = 'pending' THEN 1 END) AS pending,
  SUM(CASE WHEN status = 'delivered' THEN total ELSE 0 END) AS revenue
FROM orders;
```

## Idempotent Operations

Operations that are safe to repeat. Essential for retry logic:

```sql
-- Safe to run multiple times — only inserts if not exists
INSERT INTO feature_flags (name, enabled)
VALUES ('dark_mode', false)
ON CONFLICT (name) DO NOTHING;

-- Idempotent migration: add column only if it doesn't exist
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM information_schema.columns
    WHERE table_name = 'users' AND column_name = 'last_login'
  ) THEN
    ALTER TABLE users ADD COLUMN last_login TIMESTAMPTZ;
  END IF;
END $$;
```

## See Also

- [[Pagination]] — Fetching large result sets in pages
- [[Migrations]] — Safely changing schema in production
- [[Transactions]] — Atomic multi-step operations
- [[Data Modification]] — INSERT ON CONFLICT, RETURNING
- [[Databases]]
