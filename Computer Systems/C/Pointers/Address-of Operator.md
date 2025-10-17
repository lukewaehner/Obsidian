The address-of operator (`&`) gets the memory address of a variable.

## The & Operator

The easiest way to make a pointer point to something meaningful is to give it an address using `&`:

```c
int i = 42;
int *pi = &i;  // pi now points to where i is stored
```

## Complete Example

```c
int i = 42;
int *pi = &i; // pi now points to where i is stored

i = 43;
printf("%d %d\\n", i, *pi); // 43 43

*pi = 44;
printf("%d %d\\n", i, *pi); // 44 44

int j = 123;
pi = &j;  // Now pi points to j instead
printf("%d %d\\n", i, *pi); // 44 123
```

## What's Happening

1. **`pi = &i`** - pi stores the address of variable i
2. **`i = 43`** - Change i directly, pointer reflects the change
3. **`*pi = 44`** - Change i through the pointer
4. **`pi = &j`** - Point pi to a different variable (j)

## Visual Representation

```
Before pi = &j:
i: [44]     j: [123]
    ↑
   pi points here

After pi = &j:
i: [44]     j: [123]
             ↑
            pi points here
```

## Key Points

- `&variable` gives you the address of that variable
- You can reassign pointers to point to different variables
- Multiple pointers can point to the same variable
- The address-of operator works with any variable type

## Related Topics
- [[Pointer Declaration]]
- [[Dereferencing]]
- [[Pointer Basics]]

#important #memory