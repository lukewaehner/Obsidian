## Overview

Macros are defined using the `#define` directive and perform textual substitution during preprocessing. There are two types: constant macros and parametrized (function-like) macros.

## Constant Macros

### Basic Syntax

```c
#define COUNT 100
#define COURSE "Computer Systems"
#define PI 3.14159
```

Wherever `COUNT` appears in the code, the preprocessor replaces it with `100`.

### The Substitution Problem

**Important:** Macros are simple text substitution—they don't evaluate expressions at definition time.

```c
#define X 10 + 2

int a = X;        // Expands to: 10 + 2 (correct)
int b = 3 * X;    // Expands to: 3 * 10 + 2 = 32 (likely not what we want!)
```

### Solution: Always Use Parentheses

```c
#define X (10 + 2)

int b = 3 * X;    // Expands to: 3 * (10 + 2) = 36 (correct!)
```

**Rule of thumb:** Wrap the entire macro expression in parentheses.

## Function-Like Macros

### Basic Syntax

```c
#define max(a, b) ((a) > (b) ? (a) : (b))
#define square(x) ((x) * (x))
#define abs(x) ((x) < 0 ? -(x) : (x))
```

Usage:
```c
printf("%d\n", max(3, 4));     // Expands to: ((3) > (4) ? (3) : (4))
int result = square(5);         // Expands to: ((5) * (5))
```

### The Argument Substitution Problem

Macro arguments are substituted without evaluation:

```c
#define dbl(x) (2 * x)

printf("%d\n", dbl(10 + 1));
// Expands to: (2 * 10 + 1) = 21  Wrong! We wanted 22
```

### Solution: Parenthesize All Arguments

```c
#define dbl(x) (2 * (x))

printf("%d\n", dbl(10 + 1));
// Expands to: (2 * (10 + 1)) = 22  Correct!
```

**Rule of thumb:** Wrap the entire macro body AND each argument usage in parentheses.

## Complete Macro Template

```c
#define MACRO_NAME(arg1, arg2) \
    (((arg1) operator (arg2)) ? (result1) : (result2))
//   ^                       ^   ^      ^    ^      ^
//   |                       |   |      |    |      |
// Outer parens    Inner parens for each argument usage
```

## Macros vs. Functions

| Feature       | Macros                           | Functions              |
| ------------- | -------------------------------- | ---------------------- |
| Type checking | None                             | Yes                    |
| Code size     | Larger (inlined everywhere)      | Smaller                |
| Performance   | Faster (no call overhead)        | Slower (call overhead) |
| Debugging     | Harder                           | Easier                 |
| Side effects  | Can evaluate args multiple times | Args evaluated once    |

### Side Effect Danger

```c
#define max(a, b) ((a) > (b) ? (a) : (b))

int x = 5;
int result = max(x++, 10);
// Expands to: ((x++) > (10) ? (x++) : (10))
// x gets incremented TWICE if x > 10!
```

## Best Practices

1. **Use ALL_CAPS** - Convention for macro names
2. **Parenthesize everything** - Arguments and entire expression
3. **Prefer const or inline functions** - When possible (C99+)
4. **Avoid side effects** - Don't use `++`, `--`, or function calls as arguments
5. **Document carefully** - Macros can be tricky to understand

## When to Use Macros

Good uses:
- Constants that need to be compile-time values
- Conditional compilation
- Header guards
- Simple, type-agnostic utilities

Avoid for:
- Complex logic (use functions instead)
- Anything with side effects
- When type safety matters


---

**Related Notes:**
- [[The Preprocessor]] - Overview of preprocessing
- [[Typedef]] - Type aliases vs. macros
- [[Inline Functions]] - Modern alternative to macros