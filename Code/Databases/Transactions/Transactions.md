---
tags:
  - sql
  - transactions
type: note
related:
  - "[[Isolation Levels]]"
  - "[[Locking]]"
  - "[[Databases]]"
---
# Transactions

A transaction is a group of SQL statements that execute as a single unit — either all succeed or all are rolled back.

## Basic Syntax

```sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;   -- make changes permanent
-- or
ROLLBACK; -- undo everything since BEGIN
```

Without `BEGIN`, every statement is its own implicit transaction (autocommit mode).

## ACID Properties

| Property | Meaning |
|----------|---------|
| **Atomicity** | All statements commit or none do — no partial updates |
| **Consistency** | Transaction leaves the database in a valid state (constraints hold) |
| **Isolation** | Concurrent transactions don't interfere with each other |
| **Durability** | Committed data survives crashes |

## Savepoints

Partial rollback within a transaction:

```sql
BEGIN;

INSERT INTO orders (user_id, total) VALUES (1, 100);
SAVEPOINT after_order;

INSERT INTO order_items (order_id, product_id) VALUES (1, 999); -- might fail
-- If this fails, rollback to savepoint instead of entire transaction

ROLLBACK TO SAVEPOINT after_order;
-- order row still exists, bad item insert undone

COMMIT;
```

## Error Handling in Transactions

In PostgreSQL, any error inside a transaction aborts it — you can't run more statements until you ROLLBACK:

```sql
BEGIN;
INSERT INTO users (email) VALUES ('a@b.com');
INSERT INTO users (email) VALUES ('a@b.com'); -- duplicate, ERROR

-- Transaction is now aborted — any further statements fail
SELECT 1; -- ERROR: current transaction is aborted

ROLLBACK; -- must rollback before you can do anything else
```

## When to Use Transactions

### Always: multi-statement operations that must be atomic

```sql
-- Transferring money — must be atomic
BEGIN;
UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;

-- Without transaction: if the process crashes between the two updates,
-- money disappears from account 1 but never arrives in account 2
```

### Always: read-then-write patterns

```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE; -- lock the row
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Without transaction + FOR UPDATE, two concurrent requests could
-- both read the same balance and both deduct, causing overdraft
```

### Bulk operations for performance

```sql
-- Inserting 10,000 rows — each auto-commit row is a separate fsync
BEGIN;
INSERT INTO events (...) VALUES (...);
INSERT INTO events (...) VALUES (...);
-- ... 10,000 inserts
COMMIT;
-- Much faster: one fsync at the end
```

## What You Can't Roll Back

- DDL statements in some databases (MySQL auto-commits DDL)
- In PostgreSQL, DDL is transactional — you CAN roll back `CREATE TABLE`, `ALTER TABLE`, etc.
- `TRUNCATE` is transactional in PostgreSQL
- Sequences — `nextval()` advances even if you roll back

## Implicit Transactions in ORMs

ORMs wrap operations in transactions automatically. Know when yours does:

```python
# Rails/ActiveRecord — wraps each save in a transaction
user.save!

# Explicit transaction
User.transaction do
  account.debit(100)
  account.save!
  payment.credit(100)
  payment.save!
end
```

## Tips

- Keep transactions short — long transactions hold locks and block other queries
- Don't do network calls or slow operations inside a transaction
- Always handle transaction failure — don't assume COMMIT succeeded
- In PostgreSQL, DDL is transactional — you can roll back schema changes

## See Also

- [[Isolation Levels]] — What concurrent transactions can see
- [[Locking]] — Row and table locks inside transactions
- [[Databases]]

%% Begin Waypoint %%
- [[Isolation Levels]]
- [[Locking]]

%% End Waypoint %%
