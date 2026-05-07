---
tags:
  - sql
  - transactions
type: note
related:
  - "[[Transactions]]"
  - "[[Isolation Levels]]"
  - "[[Databases]]"
---
# Locking

Controlling concurrent access to rows and tables to prevent race conditions.

## Why Locking Matters

Without locks, concurrent transactions can produce incorrect results even in a transaction:

```sql
-- Two requests both want to book the last seat

-- Request A                      -- Request B
BEGIN;                             BEGIN;
SELECT seats_left FROM events      SELECT seats_left FROM events
  WHERE id = 1;  -- returns 1        WHERE id = 1;  -- returns 1
                                   -- both see 1, both proceed
UPDATE events SET seats_left = 0   UPDATE events SET seats_left = 0
  WHERE id = 1;                      WHERE id = 1;
COMMIT;                            COMMIT;
-- Both committed — ticket oversold!
```

## SELECT FOR UPDATE

Locks selected rows until the transaction ends. Other transactions that try to SELECT FOR UPDATE the same rows will wait.

```sql
BEGIN;

SELECT seats_left FROM events
  WHERE id = 1
  FOR UPDATE;  -- locks this row

-- Now safe to check and update
UPDATE events SET seats_left = seats_left - 1
  WHERE id = 1 AND seats_left > 0;

COMMIT; -- lock released
```

Now Request B blocks at `SELECT FOR UPDATE` until Request A commits, then reads the updated value.

### SKIP LOCKED — non-blocking queue processing

Process available work without waiting for locked rows:

```sql
-- Job queue: multiple workers claim jobs without stepping on each other
BEGIN;
SELECT id FROM jobs
  WHERE status = 'pending'
  ORDER BY created_at
  LIMIT 1
  FOR UPDATE SKIP LOCKED;  -- skip rows locked by other workers

UPDATE jobs SET status = 'processing' WHERE id = $1;
COMMIT;
```

### NOWAIT — fail immediately instead of waiting

```sql
SELECT * FROM accounts
  WHERE id = 1
  FOR UPDATE NOWAIT;  -- ERROR if row is locked, rather than waiting
```

## Table-Level Locks

Postgres acquires table locks automatically for DDL and some operations. You can also lock explicitly:

```sql
-- Lock a table explicitly (prevents concurrent writes)
LOCK TABLE orders IN EXCLUSIVE MODE;

-- ROW EXCLUSIVE is what INSERT/UPDATE/DELETE acquire automatically
-- ACCESS EXCLUSIVE is what ALTER TABLE acquires
```

Most of the time you use row-level locks (`FOR UPDATE`), not table locks.

## Deadlocks

Two transactions each waiting for a lock the other holds:

```
T1 locks row A, tries to lock row B
T2 locks row B, tries to lock row A
→ Both wait forever
```

PostgreSQL detects deadlocks and kills one transaction with an error:

```
ERROR: deadlock detected
DETAIL: Process 12345 waits for ShareLock on transaction 67890;
        blocked by process 67890.
```

### Preventing deadlocks

Always acquire locks in the same order:

```sql
-- GOOD: both transactions lock the lower ID first
BEGIN;
SELECT * FROM accounts WHERE id = MIN($1, $2) FOR UPDATE;
SELECT * FROM accounts WHERE id = MAX($1, $2) FOR UPDATE;
...
```

Keep transactions short — the longer a transaction holds locks, the higher the chance of a deadlock.

## Advisory Locks

Application-level locks not tied to any row or table. Useful for distributed mutex patterns:

```sql
-- Try to acquire lock (returns true if acquired, false if already held)
SELECT pg_try_advisory_lock(12345);

-- Acquire and wait
SELECT pg_advisory_lock(12345);

-- Release
SELECT pg_advisory_unlock(12345);

-- Session-level (held until connection closes or explicit unlock)
SELECT pg_advisory_lock(hashtext('process_daily_report'));
```

Useful for: ensuring only one instance of a cron job runs, distributed feature flags, coordinating background workers.

## Lock Monitoring

```sql
-- See current locks and what's blocking what
SELECT
  pid,
  wait_event_type,
  wait_event,
  state,
  query
FROM pg_stat_activity
WHERE wait_event_type = 'Lock';

-- See lock details
SELECT * FROM pg_locks WHERE NOT granted;
```

## Tips

- Use `SELECT FOR UPDATE` whenever you read-then-write a row and correctness matters
- `SKIP LOCKED` is the right pattern for job queues — workers don't block each other
- Always lock multiple rows in a consistent order to avoid deadlocks
- Keep transactions short — locks are held until COMMIT/ROLLBACK
- Don't do network calls or slow I/O while holding locks

## See Also

- [[Transactions]] — BEGIN/COMMIT/ROLLBACK
- [[Isolation Levels]] — What transactions can see without explicit locks
- [[Databases]]
