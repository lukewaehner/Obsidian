---
type: problem
source: neetcode
number: 36
url: https://neetcode.io/problems/valid-sudoku
difficulty: Medium
pattern: Arrays & Hashing
patterns: ["Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]", "[[Career/Prep/topics/Data Structures/Arrays|Arrays]]"]
solved_on: 2026-09-01
attempts: 1
aid: unaided
revisit: false
time: O(1) — the board is always 81 cells
space: O(1)
language: python
---

# 36 · Valid Sudoku

> [!question]- Problem
> Determine whether a 9×9 Sudoku board is valid. Only the filled cells need checking.

## Idea

Every cell belongs to exactly one row, one column and one box, so one pass with three families of sets settles it.

## Optimal

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                # 0, 0 = box 0 
                # 8, 8 = box 8

                bid = (r//3) * 3 + (c//3)
                
                if val in rows[r] or val in cols[c] or val in boxes[bid]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[bid].add(val)
        return True
```

## Why it works

The naive reading of this problem is three separate passes — rows, then
columns, then boxes. They collapse into one because each cell's membership in
all three groups is computable from `(r, c)` alone, so a single traversal can
update all three.

The box index is the only piece of real arithmetic:

```
bid = (r // 3) * 3 + (c // 3)
```

`r // 3` gives the box row (0–2), `c // 3` the box column (0–2), and the `* 3`
flattens that 2-D coordinate into 0–8. It is the same row-major flattening as
indexing a 2-D array with `row * width + col`.

Returning on the first collision rather than collecting all violations is
correct because validity is a conjunction — one duplicate is fatal.

> [!tip] Why the complexity is O(1)
> The board is fixed at 81 cells, so this is constant time and constant space
> by definition. Saying “O(n²) for an n×n board” is the better interview
> answer, since it shows the shape of the algorithm rather than exploiting the
> fixed size.

## Template

Flattening a 2-D block coordinate:

```python
block = (r // size) * size + (c // size)
```

## Related

- [[Career/Prep/problems/Arrays & Hashing/217 · Contains Duplicate|217 · Contains Duplicate]] — the seen-set core, applied three ways at once
