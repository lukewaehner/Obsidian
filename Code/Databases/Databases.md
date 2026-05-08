---
tags:
  - sql
  - databases
type: moc
---
# Databases

Relational databases, SQL queries, database design, and production patterns.

## SQL Fundamentals

- [[SQL Basics]] — SELECT/FROM/WHERE, sub-languages
- [[Filtering and Ordering]] — WHERE, LIKE, ORDER BY, DISTINCT
- [[Aggregation]] — GROUP BY, HAVING, aggregate functions
- [[Joins]] — inner, outer, natural, anti/semi-joins
- [[Subqueries]] — correlated, CTEs, EXISTS, WITH clause
- [[Set Operations]] — UNION, INTERSECT, EXCEPT
- [[NULL Values]] — NULL behavior, three-valued logic, COALESCE
- [[Window Functions]] — OVER, PARTITION BY, RANK, ROW_NUMBER
- [[Recursion in SQL]] — recursive CTEs

## Data Modification

- [[Data Modification]] — INSERT, UPDATE, DELETE, RETURNING, upserts, bulk ops

## Transactions and Concurrency

- [[Transactions]] — BEGIN/COMMIT/ROLLBACK, ACID, savepoints
- [[Isolation Levels]] — read committed, repeatable read, serializable
- [[Locking]] — SELECT FOR UPDATE, SKIP LOCKED, deadlocks, advisory locks

## Performance

- [[Indexes]] — B-tree, composite, partial, covering, expression indexes
- [[EXPLAIN]] — reading query plans, scan types, join types
- [[Query Performance]] — slow query log, N+1, pg_stat_statements, vacuum

## Practical Patterns

- [[Practical Patterns]] — soft deletes, audit logs, optimistic locking, conditional aggregation
- [[Pagination]] — LIMIT/OFFSET vs cursor-based pagination
- [[Migrations]] — safe schema changes, ALTER TABLE, batched backfills, zero-downtime

## Data & Time

- [[Date and Time]] — TIMESTAMPTZ, date arithmetic, truncation, timezone gotchas

## Database Design

- [[Database Schemas]] — CREATE TABLE, data types
- [[Keys and Constraints]] — primary keys, foreign keys, other constraints
- [[Entity-Relationship Diagrams]] — ERD components, relationships, cardinality

```folder-overview
id: 6d632e96-976e-4c57-852a-3b51468fd3bf
folderPath: Code/Databases
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="6d632e96-976e-4c57-852a-3b51468fd3bf"></span>
- [[Code/Databases/Date and Time.md|Date and Time]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="6d632e96-976e-4c57-852a-3b51468fd3bf"></span>
