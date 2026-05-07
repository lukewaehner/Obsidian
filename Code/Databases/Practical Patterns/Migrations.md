---
tags:
  - sql
  - patterns
type: note
related:
  - "[[Databases]]"
  - "[[Transactions]]"
  - "[[Practical Patterns]]"
---
# Migrations

Changing database schema safely in production.

## The Core Problem

Schema changes on live databases must avoid:
- **Locking** the table and blocking reads/writes
- **Breaking** existing app code before the deployment completes
- **Corrupting** data during the change

## Safe vs Unsafe Operations

### Generally safe (no full table lock)

```sql
-- Add a nullable column — fast
ALTER TABLE users ADD COLUMN last_login TIMESTAMPTZ;

-- Add a column with a default (PostgreSQL 11+) — fast
ALTER TABLE users ADD COLUMN score INT DEFAULT 0;

-- Add an index concurrently — no lock
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- Drop a column (marks as invisible, doesn't rewrite) — fast
ALTER TABLE users DROP COLUMN old_field;

-- Rename an index — fast
ALTER INDEX old_name RENAME TO new_name;
```

### Dangerous — can lock the table for minutes on large tables

```sql
-- Adding NOT NULL to existing column with no default
ALTER TABLE users ALTER COLUMN score SET NOT NULL;  -- rewrites entire table

-- Adding a column with a non-constant default (PostgreSQL <11)
ALTER TABLE users ADD COLUMN score INT DEFAULT compute_score(); -- rewrites

-- Adding a CHECK constraint
ALTER TABLE orders ADD CONSTRAINT check_positive CHECK (total > 0); -- scans table

-- Changing a column type
ALTER TABLE users ALTER COLUMN age TYPE BIGINT;  -- rewrites table
```

## Safe Patterns for Common Changes

### Add a NOT NULL column with a default

Wrong — locks the table:
```sql
ALTER TABLE users ADD COLUMN score INT NOT NULL DEFAULT 0; -- dangerous on large tables
```

Right — three-step migration:
```sql
-- Step 1: Add nullable (instant)
ALTER TABLE users ADD COLUMN score INT;

-- Step 2: Backfill existing rows in batches
UPDATE users SET score = 0 WHERE score IS NULL AND id BETWEEN 1 AND 10000;
-- ...repeat for all rows, or use a background job

-- Step 3: Add NOT NULL constraint after backfill (still may lock)
ALTER TABLE users ALTER COLUMN score SET NOT NULL;
-- Or: add a CHECK constraint first, validate separately
ALTER TABLE users ADD CONSTRAINT users_score_not_null CHECK (score IS NOT NULL) NOT VALID;
ALTER TABLE users VALIDATE CONSTRAINT users_score_not_null;  -- non-blocking
```

### Rename a column (zero-downtime)

You can't rename a column without breaking existing app code in the same deploy. Do it in phases:

```
Phase 1: Add new column, write to both old and new
Phase 2: Backfill new column from old
Phase 3: Read from new column
Phase 4: Stop writing to old column
Phase 5: Drop old column
```

### Add a unique constraint

Wrong:
```sql
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email); -- locks table
```

Right:
```sql
-- Build the index without locking
CREATE UNIQUE INDEX CONCURRENTLY idx_users_email ON users(email);

-- Then attach it as a constraint (fast)
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE USING INDEX idx_users_email;
```

### Add a foreign key

```sql
-- NOT VALID skips checking existing rows (fast)
ALTER TABLE orders
  ADD CONSTRAINT fk_orders_users
  FOREIGN KEY (user_id) REFERENCES users(id)
  NOT VALID;

-- Validate existing rows separately (doesn't block writes, only takes a share lock)
ALTER TABLE orders VALIDATE CONSTRAINT fk_orders_users;
```

## Batched Backfills

Never update millions of rows in one statement — it holds a lock and creates a massive transaction:

```sql
-- Bad: locks the table, giant transaction
UPDATE users SET score = compute_score(id);

-- Good: small batches with pauses
DO $$
DECLARE
  batch_size INT := 1000;
  last_id    BIGINT := 0;
  max_id     BIGINT;
BEGIN
  SELECT MAX(id) INTO max_id FROM users;
  WHILE last_id < max_id LOOP
    UPDATE users
    SET score = 0
    WHERE id > last_id AND id <= last_id + batch_size
      AND score IS NULL;
    last_id := last_id + batch_size;
    PERFORM pg_sleep(0.01);  -- brief pause to let other queries through
  END LOOP;
END $$;
```

## Migration Checklist

Before running a migration in production:

1. **Test on a copy of prod data** — restore a snapshot and run the migration
2. **Measure time** — know how long it will take
3. **Have a rollback plan** — how do you undo this if it goes wrong?
4. **Check for locks** — will this block reads or writes?
5. **Coordinate with deploys** — the schema and code must be compatible during the transition

## Tips

- `CREATE INDEX CONCURRENTLY` is almost always better than `CREATE INDEX` in production
- PostgreSQL 11+ makes adding columns with defaults safe and fast
- Use `NOT VALID` + `VALIDATE CONSTRAINT` for new foreign keys and check constraints
- Keep transactions short — a long migration transaction blocks autovacuum and bloats the WAL
- Never run a backfill inside the same transaction as the schema change

## See Also

- [[Transactions]] — DDL inside transactions
- [[Locking]] — What operations cause locks
- [[Practical Patterns]] — Other operational patterns
- [[Databases]]
