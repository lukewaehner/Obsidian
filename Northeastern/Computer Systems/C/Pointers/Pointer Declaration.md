# Pointer Declaration

How to declare and initialize pointers in C.

## Declaration Syntax

Use `*` after the type name to declare a pointer:

```c
int *pi;        // Pointer to an integer
char *pc;       // Pointer to a character  
float *pf;      // Pointer to a float
double *pd;     // Pointer to a double
```

## Best Practice: Initialize to NULL

If a pointer isn't set to anything immediately, it's best practice to initialize it to `NULL`:

```c
int *pi = NULL;
char *pc = NULL;
float *pf = NULL;
```

## Why Initialize to NULL?

- Uninitialized pointers contain random memory addresses
- Dereferencing uninitialized pointers leads to undefined behavior
- `NULL` makes it clear the pointer doesn't point to valid data
- You can check if a pointer is `NULL` before using it

## Declaration Examples

```c
// Declare and initialize to NULL
int *numbers = NULL;
char *message = NULL;

// Declare multiple pointers
int *p1, *p2, *p3;  // All three are pointers to int

// Note: This declares one pointer and one regular variable
int *ptr, value;    // ptr is pointer, value is regular int
```

## Related Topics
- [[Pointer Basics]]
- [[Address-of Operator]]
- [[Pointer Safety]]

#important #memory