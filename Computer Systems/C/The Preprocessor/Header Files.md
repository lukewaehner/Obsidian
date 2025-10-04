
---

## Overview

Header files (`.h` files) are a fundamental component of C programming that separate interface declarations from implementation. They enable code organization, reusability, and modular design by providing a contract between different parts of a program.

## Purpose of Header Files

Header files serve several critical purposes:

1. **Declare interfaces** - Function prototypes and type definitions
2. **Share declarations** - Make functions and types available across multiple source files
3. **Prevent duplication** - Write declarations once, use them everywhere
4. **Enable modularity** - Separate interface from implementation
5. **Improve compilation** - Only expose what's necessary

## Basic Structure

Every header file should follow this structure:

```c
// mymodule.h

#ifndef MYMODULE_H
#define MYMODULE_H

// Include dependencies
#include <stdio.h>
#include "othertypes.h"

// Constants and macros
#define MAX_BUFFER 256

// Type definitions
typedef struct {
    int id;
    char name[50];
} item_t;

// Function declarations
void initialize_module(void);
int process_item(item_t *item);
void cleanup_module(void);

#endif // MYMODULE_H
```

## Header Guards

Header guards prevent multiple inclusion problems:

### The Problem

```c
// types.h
struct person {
    char name[50];
};

// utils.h
#include "types.h"

// main.c
#include "types.h"
#include "utils.h"  // Includes types.h again!
// Error: redefinition of 'struct person'
```

### The Solution

```c
// types.h
#ifndef TYPES_H
#define TYPES_H

struct person {
    char name[50];
};

#endif // TYPES_H
```

Now the contents are only included once, even if the header is included multiple times.

### Naming Convention

Header guard names should be:
- All uppercase
- Based on the filename
- Unique across the project

```c
// math_utils.h → MATH_UTILS_H
// src/network/tcp.h → SRC_NETWORK_TCP_H or NETWORK_TCP_H
```

## What Goes in Header Files

### Function Declarations (Prototypes)

```c
// math_utils.h
int add(int a, int b);
double calculate_average(double *values, int count);
void sort_array(int *arr, size_t len);
```

The actual implementations go in the corresponding `.c` file.

### Type Definitions

```c
// Forward declarations for incomplete types
struct node;

// Complete struct definitions
typedef struct {
    int x;
    int y;
} point_t;

// Enumerations
typedef enum {
    STATUS_OK,
    STATUS_ERROR,
    STATUS_PENDING
} status_t;

// Type aliases
typedef unsigned char byte_t;
```

### Macro Definitions

```c
#define MAX_SIZE 100
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define DEBUG_PRINT(x) printf("DEBUG: %s = %d\n", #x, (x))
```

### Global Variable Declarations

```c
// Declare with 'extern' - don't define!
extern int global_counter;
extern const char *program_name;
```

The actual definitions go in exactly one `.c` file:

```c
// utils.c
int global_counter = 0;
const char *program_name = "MyProgram";
```

## What NOT to Put in Header Files

### Function Definitions

**Wrong:**
```c
// header.h
int add(int a, int b) {
    return a + b;
}
// This causes "multiple definition" errors if included in multiple files!
```

**Right:**
```c
// header.h
int add(int a, int b);

// implementation.c
int add(int a, int b) {
    return a + b;
}
```

**Exception:** `static inline` functions can be in headers:

```c
// header.h
static inline int add(int a, int b) {
    return a + b;
}
```

### Variable Definitions

**Wrong:**
```c
// header.h
int global_var = 10;  // Definition!
```

**Right:**
```c
// header.h
extern int global_var;  // Declaration

// source.c
int global_var = 10;  // Definition
```

### Executable Code

Never put statements or logic in headers - only declarations.

## Header and Source File Pairs

A typical module consists of a header and source file:

```c
// person.h
#ifndef PERSON_H
#define PERSON_H

typedef struct {
    char first_name[50];
    char last_name[50];
    int age;
} person_t;

void person_init(person_t *p, const char *first, const char *last, int age);
void person_print(const person_t *p);
int person_get_age(const person_t *p);

#endif // PERSON_H
```

```c
// person.c
#include <stdio.h>
#include <string.h>
#include "person.h"

void person_init(person_t *p, const char *first, const char *last, int age) {
    strncpy(p->first_name, first, sizeof(p->first_name) - 1);
    strncpy(p->last_name, last, sizeof(p->last_name) - 1);
    p->age = age;
}

void person_print(const person_t *p) {
    printf("%s %s, age %d\n", p->first_name, p->last_name, p->age);
}

int person_get_age(const person_t *p) {
    return p->age;
}
```

```c
// main.c
#include <stdio.h>
#include "person.h"

int main(void) {
    person_t student;
    person_init(&student, "John", "Doe", 21);
    person_print(&student);
    return 0;
}
```

## Include Order

Organize includes in a consistent order:

```c
// Recommended order:
#include <standard_library.h>    // C standard library
#include <system_headers.h>      // System/OS headers
#include <third_party/lib.h>     // Third-party libraries
#include "project/module.h"      // Project headers
#include "local.h"               // Local headers
```

**Best practice:** Always include the module's own header first in the `.c` file:

```c
// person.c
#include "person.h"  // Own header first - ensures it's self-contained
#include <stdio.h>
#include <string.h>
```

This ensures the header is self-contained and doesn't rely on other headers being included first.

## Self-Contained Headers

Every header should be self-contained - it should compile on its own without requiring specific includes beforehand.

**Bad:**
```c
// point.h (requires stdio.h to be included first)
void print_point(point_t *p);
```

**Good:**
```c
// point.h (self-contained)
#ifndef POINT_H
#define POINT_H

#include <stdio.h>  // Include dependencies

typedef struct {
    int x;
    int y;
} point_t;

void print_point(point_t *p);

#endif // POINT_H
```

## Forward Declarations

Reduce dependencies by using forward declarations when possible:

```c
// file_manager.h
#ifndef FILE_MANAGER_H
#define FILE_MANAGER_H

// Forward declaration - don't need to include person.h
struct person;

void save_person(struct person *p, const char *filename);
struct person *load_person(const char *filename);

#endif // FILE_MANAGER_H
```

This works because we're only using pointers, not the complete type definition.

## Interface vs. Implementation

Headers define the **interface** (what users can call), while source files contain the **implementation** (how it works).

### Public Interface (Header)

```c
// string_utils.h
char *string_duplicate(const char *str);
void string_to_upper(char *str);
```

### Private Implementation (Source)

```c
// string_utils.c
#include <stdlib.h>
#include <ctype.h>
#include "string_utils.h"

// Private helper - not in header
static size_t count_chars(const char *str) {
    size_t count = 0;
    while (*str++) count++;
    return count;
}

char *string_duplicate(const char *str) {
    size_t len = count_chars(str);
    // ... implementation
}

void string_to_upper(char *str) {
    while (*str) {
        *str = toupper(*str);
        str++;
    }
}
```

Functions marked `static` are private to the source file and not exposed to users.

## Common Patterns

### Opaque Pointers (Information Hiding)

```c
// database.h
typedef struct database database_t;  // Incomplete type

database_t *database_create(const char *path);
void database_destroy(database_t *db);
void database_insert(database_t *db, const char *key, const char *value);
```

```c
// database.c
struct database {
    // Implementation details hidden from users
    char *path;
    int fd;
    // ...
};
```

Users can only work with pointers, keeping implementation details private.

### Module Initialization

```c
// network.h
void network_init(void);
void network_shutdown(void);
```

Provides clear initialization and cleanup functions for modules.

## Compilation Example

```bash
# Compile individual object files
gcc -c person.c -o person.o
gcc -c main.c -o main.o

# Link together
gcc person.o main.o -o program

# Or all at once
gcc person.c main.c -o program
```

## Best Practices

1. **Always use header guards** - Prevents multiple inclusion errors
2. **Keep headers minimal** - Only include what's necessary
3. **Make headers self-contained** - Include all dependencies
4. **Use forward declarations** - Reduce compile-time dependencies
5. **One module per header** - Clear organization
6. **Consistent naming** - `module.h` and `module.c` pairs
7. **Document public interfaces** - Add comments for users
8. **Use extern for globals** - Declare in header, define once in source
9. **Avoid including .c files** - Only include headers
10. **Keep implementation private** - Use `static` for internal functions

## Common Errors

### Multiple Definition Errors

**Problem:**
```c
// header.h
int counter = 0;  // Definition in header

// file1.c and file2.c both include header.h
// Error: multiple definition of 'counter'
```

**Solution:**
```c
// header.h
extern int counter;  // Declaration

// file1.c
int counter = 0;  // Definition in ONE source file
```

### Circular Dependencies

**Problem:**
```c
// a.h includes b.h
// b.h includes a.h
```

**Solution:** Use forward declarations and reorganize dependencies.

### Missing Header Guards

**Problem:** Including the same header twice causes redefinition errors.

**Solution:** Always use header guards in every header file.

## Modern Alternative: #pragma once

Some modern compilers support `#pragma once` as an alternative to header guards:

```c
// myheader.h
#pragma once  // Non-standard but widely supported

// Header contents
```

However, traditional header guards are more portable and universally supported.

---

**Related Notes:**
- [[Include]] - The `#include` directive
- [[Declaration vs Definition]] - Understanding declarations
- [[The Preprocessor]] - Preprocessing overview
- [[Scope]] - Variable and function scope