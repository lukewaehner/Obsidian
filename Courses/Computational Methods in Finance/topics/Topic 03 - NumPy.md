---
tags:
  - lecture
  - finance
  - python
  - northeastern
  - numpy
type: lecture
course: "[[Computational Methods in Finance]]"
module: 3
week: 4
date: 2026-09-09
status: notes
---

# Topic 03 — NumPy

Lecture for [[Computational Methods in Finance]].

> [!info] Source
> `Topic 3 NumPy Basics.ipynb` and `Topic 3 - NumPy Basics.pdf` (Prof. Lingfei Kong, Canvas,
> "Notes: numpy" module, first seen 2026-09-27). Tracks **Chapter 4** of Wes McKinney,
> *[Python for Data Analysis](https://wesmckinney.com/book/numpy-basics)*, 3rd ed. Outputs below
> were re-run locally with NumPy 2.0 and match the PDF's printed outputs.

## Meetings

- **Tue Sep 29** — NumPy
- **Fri Oct 2** — NumPy · Quiz 2 in class

## Assigned Material

- [ ] `Topic 3 NumPy Basics.ipynb` (Canvas)
- [ ] `Topic 3 - NumPy Basics.pdf` (Canvas) — same notebook, printed with outputs
- [ ] McKinney ch. 4 — [NumPy Basics: Arrays and Vectorized Computation](https://wesmckinney.com/book/numpy-basics)

## Due This Session

- [[Quiz 2]] — in class Oct 2
- [[HW1]] — Oct 4
- [[DataCamp Assignment 1]] — Oct 4

## Notes

Kong flags this in the notebook as a **"super difficult and long"** topic. It is also the
foundation pandas is built on, so everything here comes back in [[Topic 04 - Pandas Introduction]].
The five goals:

1. Creating arrays
2. Indexing and slicing arrays
3. Math on arrays
4. Functions and methods on arrays
5. Conditional logic with arrays (`np.where()`)

```python
import numpy as np
%precision 4     # notebook magic: DISPLAY 4 decimals; the stored values keep full precision
```

### The ndarray

> An ndarray is a generic multidimensional container for **homogeneous** data; that is, all of
> the elements must be the **same** type. Every array has a **shape**, a tuple indicating the size
> of each **dimension**, and a **dtype**, an object describing the data type of the array.

Three attributes to check on any array:

| Attribute | Returns | `arr1` below | `arr2` below |
| --- | --- | --- | --- |
| `.shape` | tuple of sizes per dimension | `(5,)` | `(2, 4)` |
| `.dtype` | element type | `float64` | `int64` |
| `.ndim` | number of dimensions | `1` | `2` |

#### Creating arrays with `np.array()`

`np.array()` takes any sequence (list, tuple, array) and returns a new array.

```python
data1 = [6, 7.5, 8, 0, 1]        # list
arr1 = np.array(data1)
arr1                             # array([6. , 7.5, 8. , 0. , 1. ])
```

> [!note] Homogeneous means upcasting
> The list mixes ints and a float, so `np.array()` **re-casts every element to float**. An array
> never holds mixed types the way a list does.

A **2-D array** is an array whose elements are 1-D arrays. Think of it as a matrix: the first
index is the row, the second the column.

```python
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]   # list of lists
arr2 = np.array(data2)
```

|  | col 0 | col 1 | col 2 | col 3 |
| --- | --- | --- | --- | --- |
| **row 0** | 1 | 2 | 3 | 4 |
| **row 1** | 5 | 6 | 7 | 8 |

Mini-exercises from the notebook:

```python
data1[-1], arr1[-1]      # 1, 1.0  — last element
arr1[2]                  # 8.0     — third element
data2[1][0]              # 5       — list: consecutive indexing only
arr2[1][0], arr2[1, 0]   # 5, 5    — array: either form works
```

#### Creation functions (McKinney Table 4.1)

| Function | Does |
| --- | --- |
| `np.array` | Convert a sequence to an ndarray; infers dtype, **copies** the input by default |
| `np.arange` | Like `range`, but returns an ndarray |
| `np.ones` | All 1s, given shape and dtype |
| `np.zeros` | All 0s |
| `np.empty` | Allocates memory but **does not fill it** — contents are garbage, not zeros |

```python
np.zeros(5)          # array([0., 0., 0., 0., 0.])
np.ones((2, 3))      # 2×3 of 1.  — shape is ONE tuple argument, note the double parens
np.arange(0, 11)     # array([ 0,  1, ..., 10])   same as np.arange(11)
np.arange(-5, 5, 1)  # array([-5, -4, ..., 4])
```

`np.arange(0, 11)` beats `np.array(range(0, 11))` — it builds the array directly instead of going
through a Python range first. The range is **half-open**, same as [[Topic 01 - Python Basics|Topic 01]]:
`stop` is excluded.

#### Random arrays and the seed

`np.random` generates arrays of samples from many distributions. The **seed** is the starting point
of the generator: set the same seed and you get the same "random" numbers, which is what makes
results reproducible.

```python
np.random.seed(1000)
arr_1 = np.random.randint(1, 101, (3, 4))   # 3×4 ints from [1, 101) — i.e. 1..100
# [[52 88 72 65]
#  [95 93  2 62]
#  [ 1 90 46 41]]

np.random.randint(1, 101, (3, 4))           # run again WITHOUT re-seeding → different array
```

> [!warning] The seed only fixes the next draw sequence
> The seed resets the generator once. Every later call keeps advancing it, so a cell re-run without
> re-running the `seed` line gives new numbers. In a notebook, put the `seed` call **in the same cell**
> as the draw you want reproducible.

`randint(low, high, size)` is half-open on `high`: to include 100, pass `101`.

#### Transposing

> Transposing is a special form of reshaping that similarly returns a view on the underlying data
> without copying anything.

$$
A = \begin{bmatrix} a & b & c \\ d & e & f \end{bmatrix}_{2 \times 3}
\qquad
A^T = \begin{bmatrix} a & d \\ b & e \\ c & f \end{bmatrix}_{3 \times 2}
$$

```python
arr_2d = np.arange(6).reshape((2, 3))   # [[0 1 2]
                                        #  [3 4 5]]
arr_2d.T                                # [[0 3]
                                        #  [1 4]
                                        #  [2 5]]
arr_2d.shape, arr_2d.T.shape            # (2, 3), (3, 2)
```

> [!note] `.T` on a 1-D array does nothing
> `np.array([1, 2, 4, 5]).T` has shape `(4,)`, identical to the original. A 1-D array has no
> separate row and column axis to swap — it is not a "row vector" in the matrix sense.

### Arithmetic with arrays

> Arrays are important because they enable you to express batch operations on data without writing
> any for loops. NumPy users call this **vectorization**. Any arithmetic operations between
> **equal-size** arrays applies the operation element-wise.

```python
arr1 = np.array([[1, 2.5],
                 [4, 5.5]])
arr2 = np.array([[1, 2],
                 [3, 4]])

arr1 + arr2    # [[2.  4.5]
               #  [7.  9.5]]
arr1 * arr2    # [[ 1.   5. ]
               #  [12.  22. ]]   — ELEMENT-wise, not matrix multiplication
```

The same thing with lists takes a nested loop:

```python
result = []
for i in range(len(list1)):
    row_sum = []
    for j in range(len(list1[i])):
        row_sum.append(list1[i][j] + list2[i][j])
    result.append(row_sum)
```

`+`, `-`, `*`, `/`, `**` are all element-wise on arrays.

> [!warning] `+` and `*` mean different things for lists and arrays
> `[1, 2] + [3, 4]` **concatenates** to `[1, 2, 3, 4]`; `np.array([1, 2]) + np.array([3, 4])`
> **adds** to `array([4, 6])`. Same for `*`: a list repeats, an array multiplies.

#### Universal functions (ufuncs)

> A universal function, or ufunc, is a function that performs element-wise operations on data in
> ndarrays.

| ufunc | Operator equivalent |
| --- | --- |
| `np.add(a, b)` | `a + b` |
| `np.multiply(a, b)` | `a * b` |
| `np.sqrt(a)` | `a ** 0.5` |

#### Broadcasting

Element-wise math normally needs two arrays of the **same shape**.
[Broadcasting](https://numpy.org/devdocs/user/basics.broadcasting.html) relaxes that — the simplest
case is an array and a scalar. NumPy "stretches" the scalar to the array's shape:

```python
arr1 + 2       # [[3.  4.5]
               #  [6.  7.5]]

# identical to:
arr1 + np.array([[2, 2],
                 [2, 2]])
```

### Indexing and slicing

1-D arrays index and slice like lists.

```python
arr = np.arange(-5, 5)    # [-5 -4 -3 -2 -1  0  1  2  3  4]
arr[5]                    # 0
arr[5:8]                  # array([0, 1, 2])
```

#### Assigning a scalar to a slice broadcasts

```python
equiv_list = list(range(-5, 5))
equiv_list[5:8] = 1000               # TypeError: can only assign an iterable
equiv_list[5:8] = [1000, 1000, 1000] # lists need a same-size list

arr[5:8] = 1000                      # arrays just broadcast the scalar
arr                                  # [-5 -4 -3 -2 -1 1000 1000 1000  3  4]
```

#### Slices are views, not copies

> An important first distinction from Python's built-in lists is that **array slices are views on
> the original array**. This means that the data is **not copied**, and any modifications to the
> view will be reflected in the source array.

```python
arr_slice = arr[5:8]
arr_slice[1] = 12345
arr          # [-5 -4 -3 -2 -1  1000 12345  1000  3  4]   ← original changed

arr_slice[:] = 64          # [:] = "every element of this view"
arr          # [-5 -4 -3 -2 -1  64  64  64  3  4]

arr_slice_2 = arr[5:8].copy()
arr_slice_2[:] = 2001
arr          # [-5 -4 -3 -2 -1  64  64  64  3  4]         ← unchanged; it was a copy
```

> [!danger] This is the opposite of lists
> A **list** slice `lst[5:8]` is a new list; editing it leaves `lst` alone. An **array** slice is a
> window onto the same memory. If you want an independent piece, call `.copy()` explicitly. This is
> the NumPy version of the aliasing trap from [[Topic 01 - Python Basics|Topic 01]].

#### 2-D indexing

```python
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
```

In 2-D, a single index returns a whole **row** (a 1-D array), not a scalar:

```python
arr2d[2]      # array([7, 8, 9])
arr2d[-1]     # array([7, 8, 9])
arr2d[:2]     # rows 0 and 1
```

Two equivalent ways to reach one element:

```python
arr2d[0][2]   # 3 — consecutive: take row 0, then element 2 of it
arr2d[0, 2]   # 3 — comma-separated [row, col]: the NumPy way
```

Slicing both axes with `[rows, cols]`:

| Expression | Selects | Result |
| --- | --- | --- |
| `arr2d[:2, 1:]` | rows 0–1, cols 1–end | `[[2, 3], [5, 6]]` |
| `arr2d[1, :2]` | row 1, cols 0–1 | `[4, 5]` (1-D) |
| `arr2d[:2, 2]` | rows 0–1, col 2 | `[3, 6]` (1-D) |
| `arr2d[[0, 2], :]` | rows 0 and 2 (a **list** of indices), all cols | `[[1, 2, 3], [7, 8, 9]]` |
| `arr2d[:, :1]` | all rows, col 0 | `[[1], [4], [7]]` (still 2-D) |

> [!tip] Integer vs. slice changes the dimension
> `arr2d[:, 0]` (integer) gives a **1-D** `[1, 4, 7]`. `arr2d[:, :1]` (slice) keeps it **2-D**,
> shape `(3, 1)`. A bare `:` selects the whole axis and is required to slice anything past the
> first dimension.

Assignment to a 2-D slice broadcasts too:

```python
arr2d[:2, 1:] = 0
# [[1 0 0]
#  [4 0 0]
#  [7 8 9]]
```

Kong's warning: slicing multi-dimensional arrays is tricky — **always check your output.**

#### Boolean indexing

A comparison on an array is element-wise and returns an array of booleans. Pass that back in as
an index to keep only the `True` positions.

```python
np.random.seed(505)
data = np.random.randint(-5, 10, (3, 2))
# [[ 4  7]
#  [ 0 -1]
#  [-2  9]]

data < 0          # [[False False]
                  #  [False  True]
                  #  [ True False]]
data[data < 0]    # array([-1, -2])    — a flat 1-D array of the matches

data[data < 0] = 0          # replace every negative with 0, in one step
# [[4 7]
#  [0 0]
#  [0 9]]
```

> [!warning] `&`, `|`, `~` — not `and`, `or`, `not`
> Python's `and` / `or` want a single `True`/`False` and raise on an array. Use the element-wise
> operators, and **parenthesize each comparison** — `&` binds tighter than `<`.
>
> ```python
> data[(data < 8) & (data > 0)]   # array([4, 7])
> ~(data < 8) & (data > 0)        # ~ inverts: True only where data >= 8 and > 0 → just the 9
> ```

#### Stock-price mini-exercise

```python
                 #   day1    day2    day3    day4
prices = np.array([[126.50, 128.30, 129.80, 131.20],     # Nvidia
                   [250.70, -248.30, -255.60, -257.90],  # Tesla
                   [ 15.40,  15.70,  16.10,  -16.25]])   # Rivian

prices[2, 1]                     # 15.7 — Rivian, day 2
prices[1:, 1:3]                  # Tesla + Rivian, days 2–3
                                 # [[-248.3 -255.6]
                                 #  [  15.7   16.1]]
prices[1] = np.abs(prices[1])    # Tesla's row to absolute values, in place
```

Rows are stocks, columns are days — index as `[stock, day]`. "Day 2" is column **1**.

### Array-oriented programming

> This practice of replacing explicit loops with array expressions is commonly referred to as
> vectorization. In general, vectorized array operations will often be one or two (or more) orders
> of magnitude faster than their pure Python equivalents.

#### Conditional logic: `np.where`

`np.where(condition, x, y)` is the vectorized form of `x if condition else y`. With only the
condition, it returns the **indices** where the condition is `True`.

```python
np.random.seed(100)
arr = np.random.randint(0, 30, (5, 5))
# [[ 8 24  3  7 23]
#  [15 16 10 20  2]
#  [21  2  2 14  2]
#  [17 16 24 15  4]
#  [11 28 26 16 27]]
```

```python
np.where(arr % 2 == 0)                   # TUPLE of two index arrays: (row indices, col indices)
                                         # of every even value
arr[np.where(arr % 2 == 0)]              # the even values themselves, flattened
np.where(arr % 2 == 0, 'even', 'odd')    # same-shape array of labels
```

Nest `np.where` for more than two outcomes:

```python
np.where(arr % 2 == 0, 'even',
         np.where(arr % 3 == 0, 'odd and m3', 'other odd'))
# [['even' 'even' 'odd and m3' 'other odd' 'other odd']
#  ['odd and m3' 'even' 'even' 'even' 'even']
#  ...]
```

The inner `np.where` only matters where the outer condition is `False` — same logic as an
`if`/`elif`/`else` chain.

#### Math and statistical methods (McKinney Table 4.5)

| Method | Does |
| --- | --- |
| `sum` | Sum; empty array → 0 |
| `mean` | Arithmetic mean; empty array → NaN |
| `std`, `var` | Standard deviation, variance — **denominator n by default** |
| `min`, `max` | Min, max |
| `argmin`, `argmax` | **Index** of the min / max |
| `cumsum` | Running sum, starting from 0 |
| `cumprod` | Running product, starting from 1 |

Each is available as a method (`arr.sum()`) or a top-level function (`np.sum(arr)`).

> [!important] NumPy `std` is population; pandas `std` is sample
> NumPy's `.std()` / `.var()` divide by **n** (population). Pandas divides by **n − 1** (sample),
> which is the right choice for financial returns — you almost always have a sample. To get the
> sample statistic in NumPy, pass **`ddof=1`**. The exercise below asks for exactly this.

#### The `axis` argument

With no `axis`, a statistic runs over the **flattened** array and returns one number. With an
`axis`, it collapses that axis:

| Call | Collapses | Result |
| --- | --- | --- |
| `arr.mean()` | everything | one scalar |
| `arr.mean(axis=0)` | the rows | **one value per column** |
| `arr.mean(axis=1)` | the columns | **one value per row** |

> [!tip] Remembering axis
> `axis=0` moves **down** the rows and gives you column results. `axis=1` moves **across** the
> columns and gives you row results. In this course's data (rows = stocks, columns = periods):
> `axis=1` is "per stock", `axis=0` is "per period".

```python
np.random.seed(42)
arr = np.random.randn(5, 4)          # standard-normal draws
arr.sum()                            # -3.4260
arr.mean(axis=1)                     # row means:    [ 0.6323  0.4696 -0.214  -0.9896 -0.7547]
arr.mean(axis=0)                     # column means: [-0.1956 -0.2858 -0.1739 -0.03  ]
arr[0].mean()                        # mean of row 0
arr[:, -1].mean()                    # mean of the last column: -0.0300
arr.argmax(axis=1)                   # column index of each row's max: [3 2 1 0 1]
```

`cumsum` and `cumprod` don't aggregate — they return the intermediate results:

```python
arr = np.array([[1, 2, 3],
                [4, 6, 7]])
arr.cumsum()          # [ 1  3  6 10 16 23]      — flattened by default
arr.cumsum(axis=0)    # [[ 1  2  3]
                      #  [ 5  8 10]]             — running total down each column
arr.cumprod(axis=1)   # [[  1   2   6]
                      #  [  4  24 168]]          — running product across each row
```

`cumprod` is the one to remember for finance: compounding a series of gross returns
(`1 + r`) is a cumulative product.

#### Methods on boolean arrays

Booleans count as 1 and 0 ([[Topic 01 - Python Basics|Topic 01]]), so `sum` and `mean` on a boolean
array give a **count** and a **proportion**:

```python
np.random.seed(42)
arr = np.random.randint(-8, 10, size=(3, 2))
# [[-2  6]
#  [ 2 -1]
#  [-2  2]]

(arr > 0).sum()      # 3    — how many are positive
(arr > 0).mean()     # 0.5  — what fraction are positive

bools = np.array([[False, False, True],
                  [True, False, False]])
bools.any()          # True  — at least one True
bools.all()          # False — not every element is True
```

## Exercises

### Quarterly returns

```python
                #   Q1     Q2    Q3     Q4
rets = np.array([[0.11,  0.28,  0.22,  0.16],    # Nvidia
                 [-0.1,  0.2,  -0.3,   0.15],    # Tesla
                 [0.04,  0.1,   0.12, -0.1 ],    # Rivian
                 [0.14,  0.1,   0.4,   0.24]])   # Apple
```

Rows are stocks, columns are quarters.

```python
# 1. Maximum return across everything
max_return = rets.max()                              # 0.4

# 2. Average return per quarter (per column → axis=0)
quarterly_avg = rets.mean(axis=0)                    # [0.0475 0.17   0.11   0.1125]

# 3. Sample std per stock (per row → axis=1, sample → ddof=1)
stock_std = rets.std(axis=1, ddof=1)                 # [0.0737 0.2323 0.0993 0.1337]

# 4. Any negative return at all?
has_negative_return = (rets < 0).any()               # True

# 5. Share of negative returns per quarter
pct_negative_quarterly = (rets < 0).mean(axis=0)     # [0.25 0.   0.25 0.25]

# 6. Label each return 'high' (above median) or 'low'
rets1 = np.where(rets > np.median(rets), 'high', 'low')   # median = 0.13
```

> [!warning] Two traps in this exercise
> - **Q3 wants the *sample* std.** `rets.std(axis=1)` without `ddof=1` gives the population figure and
>   will not match the answer key.
> - **There is no `.median()` method.** `rets.median()` raises
>   `AttributeError: 'numpy.ndarray' object has no attribute 'median'` — the notebook's last cell
>   leaves this as a hint. Use the function `np.median(rets)`.

## Key Takeaways

- **An ndarray is homogeneous**: one dtype for every element, upcast if you mix ints and floats.
  Check `.shape`, `.dtype`, `.ndim` whenever an operation surprises you.
- **Arithmetic is element-wise.** `*` is not matrix multiplication, and `+` adds rather than
  concatenating the way it does for lists.
- **Broadcasting** stretches a scalar (or a compatible smaller array) to fit, which is why
  `arr + 2` and `arr[5:8] = 1000` just work.
- **Slices are views.** Edit a slice and you edit the original. `.copy()` when you need
  independence.
- **`[row, col]` indexing**; an integer index drops a dimension, a slice keeps it.
- **Boolean masks** select and replace in one step: `data[data < 0] = 0`. Combine conditions with
  `&`, `|`, `~` and parentheses, never `and`/`or`.
- **`np.where(cond, x, y)`** is a vectorized if/else; nest it for more branches.
- **`axis=0` gives per-column results, `axis=1` per-row.** No axis means the whole flattened array.
- **NumPy `std` defaults to population (n); pandas defaults to sample (n − 1).** Use `ddof=1` for
  returns.
- **`sum`/`mean` on booleans give count/proportion**, the standard way to answer "how many" and
  "what share" questions.

## Open Questions

- Will [[Quiz 2]] (Oct 2) cover NumPy past the first lecture? The quiz falls at the start of the second
  NumPy session, so anything taught on Oct 2 itself can't be on it.
- Is there a `with solution/` PDF coming for Topic 3, as there was for Topics 1 and 2? The answers above
  are worked locally, not from an answer key.

## Related

- [[Computational Methods in Finance]]
- [[Topic 01 - Python Basics]] — half-open ranges, booleans as 1/0, and the aliasing trap all recur
  here
- [[Topic 02 - Data Structures and Functions]] — list indexing and slicing, which NumPy extends
- [[Topic 04 - Pandas Introduction]] — built on the ndarray; `std` switches to the sample definition
- [[Topics 3-4 Extra Practice]]
- [[Quiz 2]]
