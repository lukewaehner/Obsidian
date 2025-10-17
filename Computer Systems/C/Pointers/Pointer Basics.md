A pointer is a special variable that holds the memory address of another variable.

## What is a Pointer?

- A representation of a location in memory
- A special variable holding an address
- Pointers have a type, so C knows what type of data we are pointing to

## Why Use Pointers?

- Enable dynamic memory allocation
- Allow functions to modify variables from calling code
- Provide efficient array and string handling
- Enable creation of complex data structures (linked lists, trees, etc.)

## Memory Concept

```
Memory:    [Value] [Value] [Value] [Value]
Addresses:  0x100   0x104   0x108   0x10C
                     ↑
            Pointer stores this address
```

When you have a pointer, it stores the address (like `0x104`) rather than the actual value.

## Related Topics
- [[Pointer Declaration]]
- [[Address-of Operator]]
- [[Arrays]]

#important #memory