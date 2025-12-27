
---

## Overview

The C preprocessor (CPP) is a text processing engine that runs as the first phase of compilation, before the actual compiler sees your code. It modifies the source text based on preprocessor directives (commands starting with `#`).

## What the Preprocessor Does

The preprocessor performs three main operations:

1. **File Inclusion** - Includes requested header files into your source
2. **Macro Expansion** - Defines and expands textual macros and constants
3. **Conditional Compilation** - Selects which code sections to include based on conditions

## How It Works

```
source.c → Preprocessor → source.i → Compiler → Assembly → Executable
```

The preprocessor outputs a modified `.i` file that the compiler then processes. This is purely text manipulation—no compilation happens yet.

## Common Preprocessor Directives

| Directive | Purpose | Example |
|-----------|---------|---------|
| `#include` | Include header files | `#include <stdio.h>` |
| `#define` | Define macros/constants | `#define MAX 100` |
| `#undef` | Undefine a macro | `#undef MAX` |
| `#ifdef` | Conditional compilation | `#ifdef DEBUG` |
| `#ifndef` | If not defined | `#ifndef _HEADER_H_` |
| `#if` | Conditional expression | `#if VERSION > 2` |
| `#else` | Alternative branch | `#else` |
| `#elif` | Else-if branch | `#elif VERSION == 2` |
| `#endif` | End conditional | `#endif` |

## Example: Header Guards

A common preprocessor pattern to prevent multiple inclusions:

```c
#ifndef MY_HEADER_H
#define MY_HEADER_H

// Header contents here

#endif // MY_HEADER_H
```

## Example: Conditional Compilation

Compile different code for different platforms or build modes:

```c
#ifdef DEBUG
    printf("Debug: x = %d\n", x);
#endif

#ifdef _WIN32
    // Windows-specific code
#else
    // Unix/Linux code
#endif
```

## Viewing Preprocessor Output

To see what the preprocessor does to your code:

```bash
gcc -E source.c -o source.i
```

This generates the preprocessed file without compiling.

## Key Characteristics

- **Text-based** - Pure string substitution and manipulation
- **No type checking** - Happens before compilation
- **Global scope** - Preprocessor symbols are global to the file
- **No debugging** - Errors appear in expanded code, not original

---

**Related Notes:**
- [[Macros]] - Defining constants and function-like macros
- [[Include]] - Textual substitution
- [[if, ifdef, ifndef, elif, else]] - Conditional compilation
- [[Header Files]] - External Libraries or Files
- [[Assembly & Compilation Pipeline]] - Full compilation process