
---

## Overview

`typedef` creates type aliases (synonyms) that make code more readable and reduce verbosity. It's particularly useful for simplifying struct declarations and creating semantic type names.

## Basic Syntax

```c
typedef <existing_type> <new_name>;
```

## Common Use Cases

### 1. Simplifying Struct Declarations

Instead of writing `struct person` every time:

```c
// Without typedef
struct person {
    char first[32];
    char last[32];
};

struct person student;  // Must use 'struct' keyword
```

Use typedef to create a cleaner alias:

```c
// With typedef
typedef struct person {
    char first[32];
    char last[32];
} person_t;

person_t student;  // No 'struct' keyword needed!
```

**Convention:** Type aliases often end with `_t` to indicate they're type definitions.

### 2. Creating Semantic Type Names

Make primitive types more descriptive:

```c
typedef unsigned char age_t;
typedef unsigned int student_id_t;

age_t student_age = 21;
student_id_t id = 123456;
```

This improves code readability by making the purpose of variables clearer.

### 3. Simplifying Complex Types

```c
// Function pointer typedef
typedef int (*compare_fn)(const void*, const void*);

// Now you can use it cleanly:
compare_fn my_comparator = &my_compare_function;
```

## Typedef vs. `#define`

| Feature | `typedef` | `#define` |
|---------|-----------|-----------|
| Type checking |  Yes |  No (text substitution) |
| Scope | Follows C scoping rules | Global (preprocessor) |
| Multiple declarations |  Allowed |  Error |
| Best for | Type aliases | Constants, macros |

**Prefer `typedef` for type definitions** as it provides better type safety.

## Best Practices

1. **Use meaningful names** - The alias should clarify intent
2. **Follow naming conventions** - Consider using `_t` suffix
3. **Don't overuse** - Only create aliases when they improve clarity
4. **Document complex typedefs** - Especially for function pointers

---

**Related Notes:**
- [[Computer Systems/C/Basics/Structs]] - User-defined data types
- [[Computer Systems/C/Basics/Data Types]] - Overview of C data types
- [[Pointers]] - Pointer type aliases