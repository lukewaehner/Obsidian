# Dereferencing

Dereferencing is the process of getting the value that a pointer points to.

## The Dereference Operator

Use `*` before the pointer variable name to dereference it:

```c
int value = 42;
int *ptr = &value;

printf("%d\\n", *ptr);  // Prints: 42
```

## How Dereferencing Works

```
Memory:     [42]
Address:    0x100
            ↑
ptr stores 0x100

*ptr → "Go to address 0x100 and get the value" → 42
```

## Example with Modification

```c
int i = 42;
int *pi = &i;

printf("i = %d, *pi = %d\\n", i, *pi);  // i = 42, *pi = 42

*pi = 100;  // Change the value through the pointer
printf("i = %d, *pi = %d\\n", i, *pi);  // i = 100, *pi = 100
```

## Key Points

- `*ptr` gets the value at the address stored in `ptr`
- You can both read and write through dereferenced pointers
- Dereferencing a `NULL` pointer causes a segmentation fault
- The `*` operator has different meanings in declaration vs. dereferencing

## Common Error

```c
printf("%d\\n", %pi);  // ERROR: Should be *pi, not %pi
```

## Related Topics
- [[Pointer Declaration]]
- [[Address-of Operator]]
- [[Pointer Safety]]

#important #memory