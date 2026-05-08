
---

## Set Operations

Combining results from multiple queries.

---

## UNION

Combines results, removing duplicates.

```sql
SELECT a FROM R
UNION
SELECT a FROM U
```

| R.a | U.a | Result |
| --- | --- | --- |
| 1 | 2 | 1 |
| 2 | 3 | 2 |
|  | 4 | 3 |
|  |  | 4 |

---

## UNION ALL

Combines results, keeping duplicates.

```sql
SELECT a FROM R
UNION ALL
SELECT a FROM U
```

Result: 1, 2, 2, 3, 4

---

## INTERSECT

Returns rows that appear in both queries.

```sql
SELECT a FROM R
INTERSECT
SELECT a FROM U
```

Result: 2 (appears in both)

---

## EXCEPT (MINUS)

Returns rows from first query that don't appear in second.

```sql
SELECT a FROM R
EXCEPT
SELECT a FROM U
```

Result: 1 (in R but not U)

---

## Theta Joins

Join with non-equality condition.

```sql
SELECT R.a, U.a AS b
FROM R, U
WHERE R.a < U.a
```

Returns pairs where R.a is less than U.a.

```folder-overview
id: c9ea63f0-6409-44fe-93bf-263bff3d322b
folderPath: Code/Databases/Set Operations
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
<span class="fv-link-list-start" id="c9ea63f0-6409-44fe-93bf-263bff3d322b"></span>
<span class="fv-link-list-end" id="c9ea63f0-6409-44fe-93bf-263bff3d322b"></span>
