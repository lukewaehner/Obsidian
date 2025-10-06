## Overview

The `#include` directive performs textual inclusion of the specified file during preprocessing. It literally copies the contents of the included file into your source code at that location.

## Syntax

There are two forms of the `#include` directive:

### Angle Brackets (System Headers)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
```

- Used for **standard library headers** and system-provided files
- Compiler searches in **system include directories** (like `/usr/include`)
- Searches predefined paths set by the compiler

### Quotation Marks (User Headers)

```c
#include "myheader.h"
#include "utils/helper.h"
#include "../common/types.h"
```

- Used for **your own header files**
- Compiler searches in the **current directory first**, then system directories
- Can include relative paths

## What Goes in Header Files

Header files (`.h` files) typically contain:

### 1. Function Declarations (Prototypes)

```c
// math_utils.h
int add(int a, int b);
double calculate_average(double *values, int count);
```

### 2. Macro Definitions

```c
// constants.h
#define MAX_SIZE 100
#define PI 3.14159
#define MIN(a, b) ((a) < (b) ? (a) : (b))
```

### 3. Type Definitions

```c
// types.h
typedef struct {
    char name[50];
    int age;
} person_t;

typedef enum {
    RED,
    GREEN,
    BLUE
} color_t;
```

### 4. Global Variable Declarations

```c
// globals.h
extern int global_counter;
extern char *program_name;
```

**Note:** Use `extern` for declarations in headers. The actual definition goes in a `.c` file.

## How Include Works

When the preprocessor encounters `#include`, it:

1. Locates the specified file
2. Reads its entire contents
3. Replaces the `#include` line with the file's contents
4. Continues processing

**Example:**

```c
// Before preprocessing
#include <stdio.h>

int main() {
    printf("Hello\n");
}

// After preprocessing (simplified)
// ... entire contents of stdio.h ...
// (thousands of lines of declarations)

int main() {
    printf("Hello\n");
}
```

## Header Guards

To prevent multiple inclusions of the same header (which causes errors), always use header guards:

```c
// myheader.h
#ifndef MYHEADER_H
#define MYHEADER_H

// Header contents here
void my_function(void);

#endif // MYHEADER_H
```

Without guards, including the same header twice causes redefinition errors:

```c
// main.c
#include "types.h"
#include "utils.h"  // Also includes types.h internally

// Without guards: error - types defined twice!
```

## Common Standard Library Headers

| Header | Purpose | Key Functions |
|--------|---------|---------------|
| `<stdio.h>` | Input/Output | `printf`, `scanf`, `fopen`, `fclose` |
| `<stdlib.h>` | General utilities | `malloc`, `free`, `atoi`, `rand` |
| `<string.h>` | String operations | `strcpy`, `strcmp`, `strlen`, `strcat` |
| `<math.h>` | Math functions | `sqrt`, `pow`, `sin`, `cos` |
| `<stdbool.h>` | Boolean type | `bool`, `true`, `false` |
| `<stdint.h>` | Fixed-width integers | `uint32_t`, `int64_t` |
| `<assert.h>` | Assertions | `assert` |
| `<time.h>` | Time/Date | `time`, `clock`, `strftime` |

## Best Practices

### 1. Only Include What You Need

```c
// Bad: Including unnecessary headers
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Good: Only include what you use
#include <stdio.h>
```

### 2. Include Headers in the Right Order

```c
// Recommended order:
#include <system_headers.h>    // Standard library first
#include <third_party.h>       // Third-party libraries
#include "your_headers.h"      // Your headers last
```

### 3. Use Header Guards Always

Every header file should have guards to prevent multiple inclusion issues.

### 4. Don't Include .c Files

```c
#include "implementation.c"    // Wrong! Never do this
#include "header.h"            // Correct - include headers only
```

### 5. Forward Declarations

Sometimes you can avoid including headers by using forward declarations:

```c
// Instead of: #include "person.h"
struct person;  // Forward declaration

void process_person(struct person *p);
```

This reduces compilation dependencies and speeds up builds.

## Include Path Configuration

You can specify additional include directories using the `-I` flag:

```bash
gcc -I/path/to/headers -I../include main.c -o program
```

Now the compiler will search these directories when looking for headers.

## Common Errors

### 1. File Not Found

```c
#include "nonexistent.h"
// Error: nonexistent.h: No such file or directory
```

**Solution:** Check the file path and include directories.

### 2. Circular Includes

```c
// a.h includes b.h
// b.h includes a.h
// Causes: infinite loop or redefinition errors
```

**Solution:** Use forward declarations and header guards properly.

### 3. Multiple Definitions

```c
// header.h (without guards)
int global_var = 10;  // Definition in header

// main.c includes header twice
// Error: multiple definition of 'global_var'
```

**Solution:** Use `extern` in headers, define in one `.c` file, and use header guards.

## Example Project Structure

```
project/
├── include/
│   ├── types.h
│   ├── utils.h
│   └── config.h
├── src/
│   ├── main.c
│   ├── utils.c
│   └── helper.c
└── Makefile
```

```c
// In src/main.c
#include <stdio.h>
#include "../include/types.h"
#include "../include/utils.h"
```

Or compile with:
```bash
gcc -I include src/main.c src/utils.c -o program
```

---

**Related Notes:**
- [[The Preprocessor]] - Preprocessor overview
- [[Macros]] - Defining constants and macros
- [[Header Files]] - Best practices for header files