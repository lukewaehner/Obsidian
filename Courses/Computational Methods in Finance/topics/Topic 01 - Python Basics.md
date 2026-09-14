---
tags:
  - lecture
  - finance
  - python
  - northeastern
  - python-basics
type: lecture
course: "[[Computational Methods in Finance]]"
module: 1
week: 2
date: 2026-09-09
status: notes
---

# Topic 01 — Python Basics

Lecture for [[Computational Methods in Finance]].

> [!info] Source
> `Topic 1 Python Language Basics-Part I.ipynb` and `Topic 1 Python Language Basics-Part II.ipynb`
> (Prof. Lingfei Kong, Canvas). Both track **Chapter 2, §2.3** of Wes McKinney,
> *[Python for Data Analysis](https://wesmckinney.com/book/python-basics)*, 3rd ed.

## Meetings

- **Tue Sep 15** — Python Basics
- **Fri Sep 18** — Python Basics

## Assigned Material

- [ ] `Topic 1 Python Language Basics-Part I.ipynb` (Canvas)
- [ ] `Topic 1 Python Language Basics-Part II.ipynb` (Canvas)
- [ ] `Topic 1_ Python Language Basics-Part I.pdf` (Canvas)
- [ ] McKinney ch. 2 §2.3 — [Python Language Basics](https://wesmckinney.com/book/python-basics)

## Due This Session

- [[Topic 1 Extra Practice]] — Sep 20
- [[DataCamp Classroom Enrollment]] — Sep 20

## Notes

> [!tip] If the notebook won't open locally
> Upload the `.ipynb` to Google Drive and open it with
> [Google Colab](https://colab.research.google.com/) — Colab Pro is free for students once you
> verify your `.edu` address. Kong asks you to come to office hours early in the semester if
> you're still fighting the local Jupyter install.
>
> **Mac quirk:** in JupyterLab, a new cell sometimes appears in the wrong place relative to the
> cell you inserted below. Workaround Kong gives — launch Lab from Terminal, then paste the URL
> into **Google Chrome** rather than using the browser it auto-opens.

### Part I — Objects, Variables, Types, and Built-ins

#### Language semantics: indentation, not braces

Python structures code with **whitespace** instead of braces. A colon opens an indented block,
and everything in the block must be indented by the same amount until the block ends.

```python
if 3 < 4:
    print("3 is less than 4")
else:
    print("3 is NOT less than 4")
```

Code runs **top to bottom**. In a notebook this matters more than in a script: a cell can only
use names that an *already-executed* cell defined, and re-running cells out of order is the
single most common source of confusing results.

#### Comments

Anything after `#` on a line is ignored. Use it for notes or to switch off code without deleting
it. Select lines and press `Ctrl` + `/` (Windows/Linux) or `Cmd` + `/` (Mac) to toggle comments
in a notebook cell.

#### Everything is an object

> An important characteristic of the Python language is the consistency of its *object model*.
> Every number, string, data structure, function, class, module, and so on, are referred to as
> *Python objects*. Each object has an associated *type* and internal data.

| Object | Example |
| --- | --- |
| Number | `5`, `7.1` |
| String | `'Taylor'` — an ordered sequence of characters |
| Boolean | `True`, `False` |
| List | `['apple', 'banana', 'cherry']` — an ordered collection of objects |

Python is **dynamically typed** — you never declare a type when you create a variable.

#### Variables

Variables are **names** that track information. Assignment creates a *reference* to the object on
the right-hand side. A variable is created when it is first assigned, and it must be assigned
before it can be used (otherwise: `NameError: name 'x2' is not defined`).

```python
x = 5
x          # implicit print — JupyterLab shows the LAST expression in a cell
print(x)   # explicit print — works anywhere in the cell
```

> [!note] Implicit vs. explicit print
> A bare variable on the last line of a cell displays its value. That's a *notebook* behavior, not
> a Python one — it won't happen in a `.py` script, and it only applies to the last expression.
> Use `print()` when you want more than one value out of a cell.

[Naming rules](https://www.w3schools.com/python/python_variables_names.asp):

- Must start with a letter or underscore — never a digit
- Only alphanumerics and underscores (`A`–`z`, `0`–`9`, `_`)
- **Case-sensitive** — `age`, `Age`, and `AGE` are three different variables
- Cannot be a [Python keyword](https://www.w3schools.com/python/python_ref_keywords.asp)

#### Booleans behave like 1 and 0

`True` and `False` arithmetic-ize to `1` and `0`. Named booleans just make code readable.

```python
x == 5        # True   — '==' asks a question
x <= 3        # False
True * 7      # 7
True + 3 + False * 2   # 4
```

> [!warning] `=` vs `==`
> `=` **assigns**. `==` **tests equality** and returns a boolean. `!=` tests inequality.

#### Lists and indexing

A list is a collection of objects in square brackets, comma-separated. **Indexing starts at 0.**

```
          0          1           2
          ↓          ↓           ↓
fruits = ['apple', 'banana',  'cherry']
```

```python
fruits[0]   # 'apple'
fruits[1]   # 'banana'
```

#### Binary operators (McKinney Table 2.1)

| Operator | Meaning |
| --- | --- |
| `a + b` | Add |
| `a - b` | Subtract `b` from `a` |
| `a * b` | Multiply |
| `a / b` | Divide — **always returns a float** |
| `a // b` | Floor-divide, dropping the fractional remainder |
| `a % b` | Modulo — the remainder of `a / b` |
| `a ** b` | `a` to the power `b` |
| `a & b` | Booleans: `True` if both are `True` |
| `a \| b` | Booleans: `True` if either is `True` |
| `a ^ b` | Booleans: `True` if **exactly one** is `True` (XOR) |
| `a == b` / `a != b` | Equal / not equal |
| `a < b`, `a <= b`, `a > b`, `a >= b` | Ordering comparisons |
| `a is b` / `a is not b` | Same object / different objects in memory |

The three worth memorizing because Excel has no equivalent:

```python
13 / 2     # 6.5
13 // 2    # 6    floor division
13 % 2     # 1    remainder
```

> [!tip] Modulo is the divisibility test
> `n % k == 0` means "`n` is a multiple of `k`." `n % 2 == 0` is the standard even check. This
> shows up constantly in the exercises.

#### Reference semantics: `is` vs `==`

This is the one genuinely surprising idea in Part I.

```python
a = [1, 2, 3]
b = a          # b is a NEW NAME for the SAME object
c = a.copy()   # c is a NEW object with the same values

a is b   # True  — same object
a is c   # False — different objects
a == c   # True  — same values
```

Because `b` and `a` are the same object, mutating through one name is visible through the other:

```python
b.append(4)
b   # [1, 2, 3, 4]
a   # [1, 2, 3, 4]  ← changed too!
c   # [1, 2, 3]     ← untouched
```

> [!danger] Don't give one object multiple names
> Kong flags this explicitly as bad practice. The bug it causes is silent: you "modify `b`" and
> some other part of your analysis reading `a` quietly changes underneath you. When you want an
> independent copy, say so — `.copy()`.

#### Scalar types (McKinney Table 2.2)

| Type | What it holds |
| --- | --- |
| `None` | The Python "null" value — exactly one `None` object exists |
| `str` | String; Unicode (UTF-8) text |
| `int` | Arbitrary-precision signed integer |
| `float` | Double-precision (64-bit) floating point — **there is no separate `double`** |
| `bool` | `True` or `False` |
| ~~`bytes`~~ | Raw ASCII bytes — struck out; not covered in this class |

Dates and times are *not* scalars here; they come from the `datetime` module and get their own
treatment in [[Topic 07 - Pandas Time Series]].

```python
type(12)        # int
type(12.0001)   # float
```

#### Strings

Single or double quotes both work. Kong prefers single quotes — no shift key.

```python
st = "Hello, World!"
type(st)              # str

st.upper()            # 'HELLO, WORLD!'
st.lower()            # 'hello, world!'
"H" in st             # True   — 'in' / 'not in' test containment
st + 'Exciting'       # 'Hello, World!Exciting'   — no space added
st + ' ' + 'Exciting' # 'Hello, World! Exciting'
st * 4                # repeats the string four times
```

> [!note] Strings are immutable
> You cannot edit a string in place. Every "modification" builds a **new** string — which is why
> `st.replace('World', 'Boston')` has to be assigned to something to be useful:
> ```python
> st2 = st.replace('World', 'Boston')   # 'Hello, Boston!'
> ```

##### `str.split()`

[`str.split(sep=None, maxsplit=-1)`](https://www.w3schools.com/python/ref_string_split.asp)
returns a **list** of the pieces.

- `sep` — optional; the delimiter. Default `None` means *any run of whitespace*.
- `maxsplit` — optional; how many splits to perform. Default `-1` means all of them.

```python
'Welcome to   FINA. 4335'.split()   # ['Welcome', 'to', 'FINA.', '4335']
```

Note that the default collapses the three consecutive spaces — whitespace splitting treats a run
as one separator. Passing an explicit `sep=' '` would *not*, and would leave empty strings in the
result.

#### Booleans and logical operators

Capitalized `True` / `False` — different from R's `TRUE` and from C-style `true`.

```python
(5 > 1) and (10 > 5)   # True
True and False         # False
False or True          # True
(5 < 1) or (10 > 5)    # True
```

`&` substitutes for `and`, and `|` for `or`. `^` is XOR and has no keyword form.

> [!tip] Parenthesize your comparisons
> `&` and `|` bind *tighter* than `<`, `>`, and `==`, so `5 > 1 & 10 > 5` does not mean what it
> looks like. Always write `(5 > 1) & (10 > 5)`. This becomes mandatory in
> [[Topic 04 - Pandas Introduction]], where `&` / `|` are the *only* option for filtering.

#### Built-in functions

Always available, no import needed: `type()`, `print()`, `len()`, `range()`.

To read a function's **docstring**: type `len?` in a cell, or press `Shift` + `Tab` with the
cursor between the parentheses in JupyterLab. In Colab, hover over the function name.

##### `len()`

```python
len('Hello')   # 5
```

##### `print()`

Prints one or many objects, separated by a blank space by default.

```python
print('Hello', 'NEU')            # Hello NEU
print('Hello', 'NEU', sep=',')   # Hello,NEU
```

##### `range(start, stop, step)`

Returns an **iterator** of evenly spaced integers — not a list. Wrap it in `list()` to see it.

| Parameter | Required? | Default |
| --- | --- | --- |
| `start` | optional | `0` |
| `stop` | **required** | — |
| `step` | optional | `1` |

> [!important] Half-open intervals
> Python ranges are **closed on the left, open on the right** — `start` is included, `stop` is
> excluded. This convention runs through slicing, `iloc`, and everything else in the course.

```python
list(range(2, 6, 1))   # [2, 3, 4, 5]
list(range(0, 6))      # [0, 1, 2, 3, 4, 5]
list(range(6))         # [0, 1, 2, 3, 4, 5]
list(range(5, 0))      # []            — can't count up from 5 to 0
list(range(5, 0, -1))  # [5, 4, 3, 2, 1]
```

#### Type casting

"Recast" a value into another type with `int()`, `float()`, `str()`, `bool()`.

```python
s = '3.14159'
type(s)          # str
1 + s            # TypeError — can't add int and str
1 + float(s)     # 4.14159
str(1) + s       # '13.14159'   — string concatenation, not arithmetic

fval = float(s)  # 3.14159
int(fval)        # 3            — TRUNCATES toward zero, does not round
```

> [!warning] `*` means different things by type
> `s * 2` repeats the string → `'3.141593.14159'`.
> `fval * 2` multiplies → `6.28318`.
> Same operator, entirely different operation. Check your types when a result looks absurd.

**Truthiness** — most nonzero values cast to `True`:

```python
bool(3.14159)   # True
bool(0)         # False
bool(-1)        # True   — nonzero, even though negative
bool(None)      # False
```

### Part II — Control Flow and Imports

#### `if`, `elif`, `else`

Same idea as Excel's `IF()`, but the branches are indented blocks rather than nested arguments.

- `if` runs its block only when the condition is `True`.
- `else` runs when the `if` condition is `False`. It's optional.
- `elif` adds extra conditions, checked **in order**, between them. Also optional, and you can
  have as many as you want.

```python
x = -3
if x < 0:
    print("It's negative")
elif x == 0:
    print('Equal to zero')
elif x < 5:
    print('Positive but smaller than 5')
else:
    print('Positive and larger than or equal to 5')
```

> [!note] Order matters in a chain
> Only the **first** matching branch runs. The third test is written `x < 5` rather than
> `0 < x < 5` precisely because the earlier branches have already eliminated the negatives and
> zero. Reordering the branches would change the output.

#### `for` loops

Loop over a collection — a list, a tuple, a range.

```python
color = ['red', 'blue', 'yellow']
for i in color:
    print(i)
```

The loop variable (`i` here) takes each *value* in turn, not an index. That's different from
C-style `for (i = 0; i < n; i++)` loops.

**Nested loops** — a loop inside a loop; the inner one runs to completion for every pass of the
outer one:

```python
for i in ['red', 'yellow']:
    for j in ['apple', 'pear']:
        print(i, j)
# red apple / red pear / yellow apple / yellow pear
```

#### Augmented assignment

`count += 1` is shorthand for `count = count + 1`. Also `-=`, `*=`, `/=`.

#### The accumulator pattern

Three variations Kong walks through, and they're the backbone of most of the homework. Every one
of them is: **initialize a variable before the loop, update it inside the loop, use it after.**

```python
list0 = [3, 5, -3, 2]

# 1. Cumulative sum
total = 0
for i in list0:
    total += i
print("The cumulative sum is", total)          # 7

# 2. Count elements
cumcount = 0
for i in list0:
    cumcount += 1
print("There are", cumcount, "elements")       # 4

# 3. Count elements matching a condition
cumcount = 0
for i in list0:
    if i > 0:
        cumcount += 1
print("There are", cumcount, "positive elements")   # 3
```

> [!tip] Initialize to the identity element
> Sums start at `0`; **products start at `1`**. Starting a running product at `0` gives you `0`
> forever. Counting starts at `0`.

#### `continue`

Skips the rest of the current iteration and jumps to the next one.

```python
color = ['red', 'blue', 'yellow', 'purple']
for i in color:
    if i == 'blue':
        continue
    print(i)
# red / yellow / purple
```

#### `break`

Exits the loop entirely — no further iterations at all.

```python
for i in color:
    if i == 'yellow':
        break
    print(i)
# red / blue
```

> [!important] Where you put `break` changes the answer
> ```python
> for i in color:
>     print(i)
>     if i == 'yellow':
>         break
> # red / blue / yellow   ← 'yellow' IS printed
> ```
> Printing before the check means the triggering element is processed; checking first means it
> isn't. This exact distinction is the point of the sum-before-5 exercise below, and it's quiz
> bait.

#### `while` loops

Runs a block repeatedly **until the condition becomes `False`** (or a `break` fires). Use it when
you don't know the iteration count in advance.

```python
error = 50
while error > 1:
    error = error / 4
    print(error)
# 12.5
# 3.125
# 0.78125
```

Three iterations: 50 → 12.5 → 3.125 → 0.78125, at which point `error > 1` is `False` and the loop
stops.

> [!warning] The notebook's walkthrough has a typo
> The markdown cell stepping through this loop by hand says the second iteration leaves
> `error1` at **2.125**. It's **3.125** (`12.5 / 4`). The conclusion — still greater than 1, so
> the loop continues — is unaffected.

> [!danger] Infinite loops
> If the condition never becomes `False`, the loop never ends:
> ```python
> error = 50
> while error > 1:
>     error = error + 4   # error only grows — never terminates
> ```
> To escape: **Kernel → Interrupt** in JupyterLab, or `Ctrl` + `C` in the terminal. Make sure
> every `while` loop contains something that moves the condition toward `False`.

#### Imports

A **module** is a `.py` file holding functions, classes, and variables. Python ships with many.
`math` provides the mathematical functions.

```python
import math
math.ceil(1.2)          # 2   — must qualify with the module name

import math as m        # 'as' gives the import a different name
m.ceil(1.2)             # 2

from math import ceil   # import one specific function
ceil(1.2)               # 2   — now unqualified
```

> [!note] Which form to use
> The aliased form (`import x as y`) is the course convention for the big libraries —
> `import numpy as np`, `import pandas as pd` from [[Topic 03 - NumPy]] onward. Keeping the
> namespace prefix means you always know where a function came from; `from math import *` would
> not, and is why nobody does it.

To list every built-in module: `import sys; print(sys.builtin_module_names)`.

## Exercises

Worked answers to the in-notebook exercises. Try them before reading.

### Part I

**Booleans as numbers** (`x = 5`)

```python
bool2 = x <= 4     # False
bool2 * 2          # 0
bool2 + 5 - True   # 4   → 0 + 5 - 1
```

**Operators** — `a1 = 7 ** 3` → `343`, `a2 = a1 + 100` → `443`

```python
a1 % 4 != 0                       # True   — 343 % 4 == 3, so not a multiple of 4
(a1 < 150) and (a1 % 10 == 3)     # False  — 343 is not < 150, though 343 % 10 == 3
(200 <= a1 <= 400) or (a1 * 4 > 1300)   # True — both sides True (1372 > 1300)
```

**Predict the output**

```python
print((4/2 == 2) & (10 < 8))    # False  — True & False
print((5 < 1) ^ (8 > 5))        # True   — exactly one is True
print((5 % 2 == 0) | (10 > 9))  # True   — False | True
```

**`range()` construction**

```python
a1 = list(range(0, 21, 2))    # evens 0–20  → stop is 21 because 20 must be included
a2 = list(range(1, 20, 2))    # odds 1–19   → stop is 20
a3 = list(range(6, 0, -1))    # 6 down to 1 → stop is 0
a4 = list(range(6, -1, -1))   # 6 down to 0 → stop is -1
```

The whole exercise is one idea: **`stop` is one step past the last value you want.** Counting
down means one step *below*.

### Part II

**Fix the indentation** — decision logic on salary and commute:

```python
salary = 55000; commute_minutes = 61

if salary >= 60000:
    decision = 'accept'
else:
    if commute_minutes <= 60:
        decision = 'accept'
    else:
        decision = 'reject'
print(decision)     # reject
```

The nested `if` could be flattened to an `elif` chain — `elif commute_minutes <= 60:` / `else:` —
which reads better and is what you'd write in practice.

**Word lengths**

```python
animals = ['cat', 'dog', 'elephant']
for i in animals:
    print(len(i))    # 3 / 3 / 8
```

**Cumulative product of the positive numbers**

```python
list1 = [5, 12, -5, 6]
cumprod = 1                   # ← 1, not 0
for i in list1:
    if i > 0:
        cumprod *= i
print(cumprod)                # 360
```

**Count elements that are neither boolean nor string** — uses `continue`

```python
list1 = [1, 2, None, 4, None, 5, False, '4335']    # note: list1 is REASSIGNED here
cumcount = 0
for i in list1:
    if isinstance(i, bool) or isinstance(i, str):
        continue
    cumcount += 1
print(cumcount)               # 6
```

`None` counts — it is neither a `bool` nor a `str`. `False` and `'4335'` are the two exclusions.

**Sum before reaching 5** — `sequence = [3, 2, 0, 4, 5, 2]`

| | Code | Result |
| --- | --- | --- |
| **A** ✅ | `break` **before** `sum_til5 += value` | `9` — sums 3+2+0+4, stops at 5 |
| **B** | `break` **after** `sum_til5 += value` | `14` — 5 gets added before the break |

**A** is the correct answer: "before reaching 5" means 5 itself is excluded.

## Key Takeaways

- **Everything is an object** with a type, and Python is dynamically typed — you never declare
  types, but you still have to *know* them. `*` on a string repeats; `*` on a float multiplies.
- **Assignment binds a name to an object, not a value.** `b = a` aliases; `c = a.copy()` copies.
  `is` compares identity, `==` compares value. Mutating an aliased list changes both names.
- **`/` always floats. `//` floors. `%` gives the remainder** — and `n % k == 0` is the
  divisibility test that every "is it even / is it a multiple" question reduces to.
- **Ranges and slices are half-open**: `start` included, `stop` excluded. `stop` is one step past
  the last value you want. This convention repeats everywhere in NumPy and Pandas.
- **The accumulator pattern** — initialize before the loop, update inside, read after — covers
  sums, counts, conditional counts, and products. Sums start at `0`; products start at `1`.
- **`continue` skips one iteration; `break` abandons the loop.** Whether the triggering element
  gets processed depends entirely on whether you act before or after the check.
- **Every `while` loop needs something that drives the condition toward `False`.** Kernel →
  Interrupt is the escape hatch when it doesn't.
- **Import with an alias** (`import math as m`) to keep the namespace prefix — the convention the
  rest of the course runs on with `np` and `pd`.

## Open Questions

- Does `isinstance(i, bool)` or `type(i) == bool` match what CodeGrade expects for the
  "neither boolean nor string" style of question? `isinstance` is the standard answer, but
  `isinstance(True, int)` is also `True`, which could matter if a prompt asks about integers.
- Are the in-notebook exercises graded anywhere, or is [[Topic 1 Extra Practice]] in CodeGrade
  the only graded version?

## Related

- [[Computational Methods in Finance]]
- [[Topic 00 - Course Intro and Setup]]
- [[Topic 02 - Data Structures and Functions]] — lists get the full treatment there; `b.append(4)`
  above is a preview
- [[Topic 1 Extra Practice]]
