## Overview

Structs are user-defined data types in C that allow you to store multiple values of different types together. They're similar to Java classes, but with key differences:
- All fields are public
- No methods (only data)
- Require explicit use of the `struct` keyword

## Basic Syntax

### Declaration

```c
struct address {
    unsigned int house_no;
    char street[32];
    char city[24];
    char state[3];
    unsigned int zip;
}
```

### Creating Instances

Structs occupy a separate namespace, so you must use the `struct` keyword when declaring variables:

```c
struct address home, work;
```

This creates two separate `address` struct instances.

## Accessing Fields

Use the dot operator (`.`) to access struct members:

```c
work.house_no = 360;
strcpy(work.street, "Huntington Ave");
strcpy(work.city, "Boston");
strcpy(work.state, "MA");
work.zip = 02115;
```

## Nested Structs

Structs can contain other structs as fields:

```c
struct person {
    char first[32];
    char last[32];
    struct address home;
}
```

Access nested fields using multiple dot operators:

```c
struct person student;
strcpy(student.first, "John");
student.home.house_no = 360;
```

## Function Parameters and Return Values

Structs can be passed to and returned from functions:

```c
struct address get_address(struct person p) {
    return p.home;
}
```

**Note:** Passing structs by value copies the entire struct. For large structs, consider passing pointers instead for better performance.

## Simplifying with Typedef

Writing `struct` repeatedly can be verbose. See [[Typedef]] for how to create type aliases that eliminate this repetition.

---

**Related Notes:**
- [[Typedef]] - Creating type aliases
- [[Pointers with Structs]] - Working with struct pointers
- [[Computer Systems/C/Basics/Data Types]] - Overview of C data types