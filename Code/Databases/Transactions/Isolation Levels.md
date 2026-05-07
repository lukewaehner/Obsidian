---
tags:
  - sql
  - transactions
type: note
related:
  - "[[Transactions]]"
  - "[[Locking]]"
  - "[[Databases]]"
---
# Isolation Levels

Isolation levels control what a transaction can see from other concurrent transactions. Higher isolation = more correctness, less concurrency.

## The Problems Isolation Solves

### Dirty read

Reading uncommitted data from another transaction:

```
T1: UPDATE users SET balance = 0 WHERE id = 1;  -- not committed yet
T2: SELECT balance FROM users WHERE id = 1;      -- sees 0 (uncommitted)
T1: ROLLBACK;                                    -- T2 read data that never existed
```

### Non-repeatable read

Reading the same row twice gets different values:

```
T1: SELECT balance FROM accounts WHERE id = 1;   -- sees 100
T2: UPDATE accounts SET balance = 200 WHERE id = 1; COMMIT;
T1: SELECT balance FROM accounts WHERE id = 1;   -- sees 200 — changed!
```

### Phantom read

A query returns different rows on second execution because another transaction inserted/deleted:

```
T1: SELECT COUNT(*) FROM orders WHERE user_id = 5;  -- returns 3
T2: INSERT INTO orders (user_id, ...) VALUES (5, ...); COMMIT;
T1: SELECT COUNT(*) FROM orders WHERE user_id = 5;  -- returns 4 — new row appeared
```

## Isolation Levels

| Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|-------|-----------|---------------------|--------------|
| **Read Uncommitted** | Possible | Possible | Possible |
| **Read Committed** | Prevented | Possible | Possible |
| **Repeatable Read** | Prevented | Prevented | Possible |
| **Serializable** | Prevented | Prevented | Prevented |

### Read Committed (PostgreSQL default)

Each statement sees only committed data at the time the statement starts. The most common default.

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

Good for: most OLTP workloads. Reads are consistent per-statement, not per-transaction.

### Repeatable Read

A snapshot is taken at the start of the transaction. All reads within the transaction see that snapshot. Writes from other transactions committed after the snapshot are invisible.

```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

Good for: reports, analytics queries that must see a consistent view across multiple statements.

### Serializable

Transactions execute as if they ran serially (one at a time), even if concurrent. The database detects serialization conflicts and aborts one of them.

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

Good for: financial operations, inventory management, anything where a race condition would cause incorrect results. Be ready to retry aborted transactions.

```sql
-- Example: two transactions both read inventory and try to decrement it
-- Serializable will abort one of them if they conflict
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT quantity FROM inventory WHERE product_id = 1; -- reads 1
UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 1;
COMMIT; -- may fail with serialization error — retry
```

## Setting Isolation Level

```sql
-- For the current transaction
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
...

-- Or combined
BEGIN ISOLATION LEVEL REPEATABLE READ;

-- For the session
SET default_transaction_isolation = 'repeatable read';
```

## PostgreSQL Specifics

PostgreSQL uses **MVCC** (Multi-Version Concurrency Control) — readers never block writers and writers never block readers. It stores multiple versions of rows rather than using read locks.

- Read Committed: statement-level snapshot
- Repeatable Read: transaction-level snapshot  
- Serializable: uses SSI (Serializable Snapshot Isolation) — detects conflicts without locking

In practice: **Read Committed is fine for most work**. Upgrade to Repeatable Read for analytics queries. Use Serializable only when you need true correctness for concurrent writes.

## Tips

- The default (Read Committed) is correct for most operations
- If you're doing a multi-statement report and need consistent numbers, use Repeatable Read
- Serializable is correct but requires retry logic for serialization failures
- Don't confuse isolation level with `SELECT FOR UPDATE` — locking is a separate mechanism

## See Also

- [[Transactions]] — BEGIN/COMMIT/ROLLBACK
- [[Locking]] — Explicit row and table locks
- [[Databases]]
