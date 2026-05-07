---
tags:
  - sql
type: note
related:
  - "[[Databases]]"
---
# Date and Time

Handling dates, times, and timezones in SQL (PostgreSQL).

## Types

```sql
DATE            -- date only: '2024-01-15'
TIME            -- time only (no timezone): '14:30:00'
TIMETZ          -- time with timezone: '14:30:00+05:00' (avoid)
TIMESTAMP       -- date + time, NO timezone awareness: '2024-01-15 14:30:00'
TIMESTAMPTZ     -- date + time WITH timezone: stored as UTC, displayed in session tz
INTERVAL        -- a duration: '3 days', '2 hours 30 minutes'
```

**Always use `TIMESTAMPTZ`** for timestamps in applications. `TIMESTAMP` stores exactly what you give it with no timezone context — dangerous when your app or database server changes timezones.

## Current Time

```sql
NOW()               -- current timestamp with timezone (transaction start)
CURRENT_TIMESTAMP   -- same as NOW()
CLOCK_TIMESTAMP()   -- actual current time (changes within a transaction, unlike NOW())
CURRENT_DATE        -- today's date
CURRENT_TIME        -- current time with timezone
```

`NOW()` returns the same value throughout a transaction. Use `CLOCK_TIMESTAMP()` if you need the real wall-clock time for each row in a bulk insert.

## Timezone Handling

```sql
-- Set session timezone
SET timezone = 'America/New_York';

-- Convert to a specific timezone for display
SELECT created_at AT TIME ZONE 'America/New_York' FROM events;
SELECT created_at AT TIME ZONE 'UTC' FROM events;

-- Store as UTC explicitly
INSERT INTO events (created_at) VALUES ('2024-01-15 14:30:00 America/New_York');
-- PostgreSQL converts to UTC on insert if column is TIMESTAMPTZ
```

The golden rule: **store UTC, display in local time**. Application code should convert to local time for display — not SQL.

## Date Arithmetic

```sql
-- Add/subtract intervals
NOW() + INTERVAL '7 days'
NOW() - INTERVAL '1 hour'
NOW() + INTERVAL '1 year 3 months'

-- Date difference
AGE(timestamp1, timestamp2)               -- interval: '1 year 2 months 5 days'
EXTRACT(day FROM timestamp1 - timestamp2) -- number of days
DATE_PART('day', timestamp1 - timestamp2) -- same

-- Days between two dates
'2024-03-01'::date - '2024-01-01'::date  -- 60 (integer days)
```

## Extracting Parts

```sql
EXTRACT(year  FROM created_at)  -- 2024
EXTRACT(month FROM created_at)  -- 1 (January)
EXTRACT(day   FROM created_at)  -- 15
EXTRACT(hour  FROM created_at)  -- 14
EXTRACT(dow   FROM created_at)  -- 0=Sunday, 1=Monday...
EXTRACT(epoch FROM created_at)  -- Unix timestamp (seconds since 1970)

DATE_PART('month', created_at)  -- same as EXTRACT
```

## Truncating

```sql
DATE_TRUNC('day',   created_at)  -- '2024-01-15 00:00:00+00'
DATE_TRUNC('month', created_at)  -- '2024-01-01 00:00:00+00'
DATE_TRUNC('year',  created_at)  -- '2024-01-01 00:00:00+00'
DATE_TRUNC('hour',  created_at)  -- '2024-01-15 14:00:00+00'
DATE_TRUNC('week',  created_at)  -- previous Monday
```

### Group by time bucket

```sql
-- Orders per day
SELECT DATE_TRUNC('day', created_at) AS day, COUNT(*)
FROM orders
GROUP BY day
ORDER BY day;

-- Revenue per month
SELECT
  DATE_TRUNC('month', created_at) AS month,
  SUM(total) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
```

## Filtering by Date

```sql
-- Today
WHERE created_at >= CURRENT_DATE
  AND created_at < CURRENT_DATE + INTERVAL '1 day'

-- Last 7 days
WHERE created_at >= NOW() - INTERVAL '7 days'

-- Specific month
WHERE DATE_TRUNC('month', created_at) = DATE_TRUNC('month', '2024-03-01'::date)

-- Better (index-friendly): avoid functions on the column
WHERE created_at >= '2024-03-01' AND created_at < '2024-04-01'
```

**Index tip**: wrapping a column in a function (`DATE_TRUNC(col)`) prevents index use. Use range conditions on the raw column instead.

## Formatting

```sql
TO_CHAR(created_at, 'YYYY-MM-DD')          -- '2024-01-15'
TO_CHAR(created_at, 'Month DD, YYYY')      -- 'January 15, 2024'
TO_CHAR(created_at, 'HH24:MI:SS')          -- '14:30:00'
TO_CHAR(amount, 'FM$999,999.00')           -- '$1,234.56'
```

## Parsing

```sql
TO_TIMESTAMP('2024-01-15 14:30:00', 'YYYY-MM-DD HH24:MI:SS')
'2024-01-15'::date
'2024-01-15 14:30:00'::timestamp
'2024-01-15 14:30:00+05'::timestamptz
```

## Common Gotchas

**Comparing TIMESTAMP to TIMESTAMPTZ**: PostgreSQL will convert, but assuming the server's local timezone — produces wrong results if the server timezone doesn't match your data.

**BETWEEN with timestamps**: `BETWEEN '2024-01-01' AND '2024-01-31'` misses rows on Jan 31 after midnight. Use `>= AND <` instead:

```sql
-- Misses 2024-01-31 14:30:00
WHERE created_at BETWEEN '2024-01-01' AND '2024-01-31'

-- Correct
WHERE created_at >= '2024-01-01' AND created_at < '2024-02-01'
```

**Daylight saving time**: `INTERVAL '1 day'` always adds 24 hours. `INTERVAL '1 day'` in a timezone-aware context around a DST transition may not equal 24 hours of local time. For "calendar days," use `DATE_TRUNC`.

## See Also

- [[Filtering and Ordering]] — Using dates in WHERE clauses
- [[Aggregation]] — Grouping by date
- [[Databases]]
