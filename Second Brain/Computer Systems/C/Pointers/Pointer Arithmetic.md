Pointer arithmetic allows you to perform mathematical operations on pointers to navigate through memory. When you add or subtract from a pointer, C automatically scales the operation by the size of the pointed-to type.

## Core Concept

When you add an integer `n` to a pointer, the pointer moves forward by `n * sizeof(type)` bytes in memory:

```
ptr + n  →  ptr + (n * sizeof(*ptr))
```

This automatic scaling is what makes pointer arithmetic powerful and type-safe.

## How It Works

The key insight from the [[Example Code]] is that pointer arithmetic is **scaled by the size of the type being pointed to**:

```c
int *pi = &k;
pi = pi + 1;  // Actually adds sizeof(int) bytes, typically 4 bytes
```

Even though we write `+ 1`, the actual memory address increases by the size of an `int` (usually 4 bytes on most systems).

## Example with Different Types

From the example code, we can see how different pointer types scale differently:

```c
char c = 10;
char *pc = &c;

int k = 13;
int *pi = &k;

int **ppi = &pi;
```

### Size Comparison

```c
sizeof(c)   = 1  // char is 1 byte
sizeof(pc)  = 8  // pointer itself is 8 bytes (on 64-bit systems)
sizeof(*pc) = 1  // dereferenced char is 1 byte
```

### Arithmetic Scaling

- `pc + 1` → moves 1 byte forward (size of char)
- `pi + 1` → moves 4 bytes forward (size of int)
- `ppi + 1` → moves 8 bytes forward (size of pointer)

## Walking Through Memory

The example demonstrates pointer arithmetic moving through stack variables:

```c
int i = 11;
int j = 12;
int k = 13;

int *pi = &k;
printf("%p = %d\n", pi, *pi);  // <Address> = 13

pi = pi + 1;  // Move to next int in memory
printf("%p = %d\n", pi, *pi);  // <Address> = 12 (variable j)

pi = pi + 1;  // Move to next int
printf("%p = %d\n", pi, *pi);  // <Address> = 11 (variable i)
```

### Stack Layout

```
Higher addresses
    ┌────────┐
i   │   11   │ ← pi after adding 2
    ├────────┤
j   │   12   │ ← pi after adding 1
    ├────────┤
k   │   13   │ ← pi initially
    └────────┘
Lower addresses
```

> **Note:** Variables on the stack typically grow downward, but by adding to the pointer we move "up" through earlier declarations.

## Operations Supported

Pointer arithmetic supports:

1. **Addition**: `ptr + n` - move forward n elements
2. **Subtraction**: `ptr - n` - move backward n elements
3. **Increment**: `ptr++` - move to next element
4. **Decrement**: `ptr--` - move to previous element
5. **Difference**: `ptr2 - ptr1` - number of elements between pointers

## Common Use with Arrays

Pointer arithmetic is most commonly used with [[Arrays]]:

```c
int nums[4] = {10, 20, 30, 40};
int *ptr = nums;  // Points to first element

printf("%d\n", *ptr);      // 10
printf("%d\n", *(ptr+1));  // 20
printf("%d\n", *(ptr+2));  // 30

// Equivalent to:
printf("%d\n", nums[0]);   // 10
printf("%d\n", nums[1]);   // 20
printf("%d\n", nums[2]);   // 30
```

In fact, `nums[i]` is just syntactic sugar for `*(nums + i)`.

## Pointer to Pointer Arithmetic

The example also shows arithmetic on multi-level pointers:

```c
int *pi = &k;
int **ppi = &pi;

ppi = ppi + 1;  // Adds 8 bytes (size of a pointer on 64-bit)
```

This is useful when working with arrays of pointers or [[Pointer to Pointer]] scenarios.

## Important Safety Considerations

**Dangers of pointer arithmetic:**
- **Going out of bounds**: Moving a pointer beyond allocated memory causes undefined behavior
- **Type mismatch**: The pointer must point to the correct type
- **Uninitialized pointers**: Never do arithmetic on uninitialized pointers

See [[Pointer Safety]] for more details on avoiding these issues.

## Key Takeaways

1. Adding `n` to a pointer moves it forward by `n * sizeof(type)` bytes
2. C handles the scaling automatically based on pointer type
3. Pointer arithmetic is the foundation of array indexing
4. Different pointer types scale by different amounts
5. Always ensure pointers remain within valid memory bounds

## Related Topics

- [[Pointer Basics]] - foundational pointer concepts
- [[Dereferencing]] - accessing values through pointers
- [[Arrays]] - primary use case for pointer arithmetic
- [[Pointer to Pointer]] - arithmetic with multi-level pointers
- [[Example Code]] - complete code demonstration
- [[Pointer Safety]] - avoiding pointer arithmetic pitfalls

#important #memory #arrays