
Arrays in C are collections of elements of the same type stored in contiguous memory locations.

## Key Concepts

- Arrays are essentially pointers with convenient syntax
- Elements are stored contiguously in memory
- Array name points to the first element
- Uses 0-based indexing
- Can have static or dynamic sizing

## Array Declaration

```c
float nums[4]; // create an array for 4 floats
```

This creates space for 4 floats in memory.

## Array Access and Assignment

```c
float nums[4];
nums[0] = 0.1;
nums[1] = 3.14;
nums[2] = 1.5;
nums[3] = 3214;

printf("2nd element: %f\\n", nums[1]); // prints 3.14
```

## Array Initialization

Arrays can be initialized at declaration:

```c
float nums[4] = { 0.1, 3.14, 1.5, 3214 };

printf("2nd element: %f\\n", nums[1]); // prints 3.14

int nums[4] = { 1 };
printf("1st element: %f\n", nums[0]); // prints 1
printf("2st element: %f\n", nums[1]); // prints 0
```

> Any numbers not initialized, eg `nums[1...3]` get zeroed out.
## Memory Layout

```
nums[0]  nums[1]  nums[2]  nums[3]
[0.1  ]  [3.14 ]  [1.5  ]  [3214 ]
   ↑
 nums points here
```

## Related Topics
- [[Data Types]]
- [[Scope]]
- [[Functions]]