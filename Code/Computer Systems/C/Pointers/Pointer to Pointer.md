Pointers can point to other pointers, creating multiple levels of indirection.

## Double Pointer Declaration

Use `**` to declare a pointer to a pointer:

```c
int **ppi;  // Pointer to a pointer to an integer
```

## Complete Example

```c
int i = 42;
int *pi = &i;      // pi points to i
int **ppi = &pi;   // ppi points to pi

printf("%d %d %d\\n", i, *pi, **ppi);
// Output: 42 42 42
```

## Visual Representation

```
Memory Layout:

i:    [42]
      ↑
pi:   [address of i]
      ↑  
ppi:  [address of pi]

Access Methods:
- i        → 42 (direct access)
- *pi      → 42 (one level of indirection)
- **ppi    → 42 (two levels of indirection)
```

## How It Works

- `ppi` stores the address of `pi`
- `*ppi` dereferences to get the value of `pi` (which is the address of `i`)
- `**ppi` dereferences twice to get the value of `i`

## Use Cases

Double pointers are commonly used for:
- Modifying pointers in functions
- Dynamic 2D arrays
- Command line arguments (`char **argv`)
- Linked list operations where you need to modify the head pointer

## Function Parameter Example

```c
void modify_pointer(int **pp) {
    int new_value = 100;
    *pp = &new_value;  // Change what the original pointer points to
}
```

## Related Topics
- [[Pointer Basics]]
- [[Dereferencing]]
- [[Address-of Operator]]
- [[Code/Topics/Computer Systems/C/Basics/Functions]]

#important #memory