Arrays and pointers are deeply interconnected in C. Understanding this relationship is essential for working with arrays effectively.

---

## Array Basics

Arrays in C are contiguous blocks of memory that store elements of the same type. You can initialize and access them using bracket notation:

```c
int main(int argc, char **argv) {
    // Initialize the array
    int nums[4] = { 1, 2, 3, 4 };
    
    // Overwrite elements
    nums[0] = 42;
    nums[1] = 4321;
    
    for (int i = 0; i < 4; i++) {
        printf("nums[%d]: %d\n", i, nums[i]);
    }
    return 0;
}
```

---

## Stack Smashing

#memory

Arrays in C don't track their own size - there's no built-in way to query an array's length. This can lead to dangerous out-of-bounds access:

```c
int main(int argc, char **argv) {
    // Initialize the array with 4 elements
    int nums[4] = { 1, 2, 3, 4 };
    
    // DANGER: Writing past the array bounds
    for (int i = 0; i < 10; i++) {
        nums[i] = i * 2;
        printf("nums[%d]: %d\n", i, nums[i]);
    }
    return 0;
}
```

> **Warning:** This code will run, but you're writing into memory beyond the array. If you continue far enough, you might overwrite the return address or other important stack data, causing the program to crash. This is called **stack smashing** and should be avoided.

See [[Pointer Safety]] for more on avoiding these dangerous scenarios.

---

## Pointer Arithmetic with Arrays

Arrays and pointers are closely related. When you use an array name, it decays to a pointer to its first element. You can use [[Pointer Arithmetic]] to access array elements:

```c
int main(int argc, char **argv) {
    int nums[4] = { 1, 2, 3, 4 };
    
    for (int i = 0; i < 4; i++) {
        printf("nums[%d]: %d\n", i, *(nums + i));
    }
    return 0;
}
```

### Array Access Equivalents

The following expressions are all equivalent ways to access array elements:

- `nums[i]` - standard bracket notation
- `*(nums + i)` - pointer arithmetic with [[Dereferencing]]
- `*(i + nums)` - commutative property
- `i[nums]` - yes, this actually works! (but please don't use it)

The bracket notation `nums[i]` is just syntactic sugar for `*(nums + i)`.

---

## Strings as Character Arrays

In C, there is no dedicated string type. Strings are simply arrays of characters terminated by a null character (`\0`):

```c
int main(int argc, char **argv) {
    char name1[] = "CS3650";  // Compiler adds null terminator
    char name2[7] = { 'C', 'S', '3', '6', '5', '0', '\0' };
    
    for (int i = 0; i < 6; i++) {
        printf("name1[%d]: %c, name2[%d]: %c\n", 
            i, *(name1 + i), i, *(name2 + i));
    }
    return 0;
}
```

> **Note:** When using string literal syntax (`"CS3650"`), you don't need to specify the array size - the compiler automatically allocates enough space including room for the null terminator (`\0`).

**Output:**
```
name1[0]: C, name2[0]: C
name1[1]: S, name2[1]: S
name1[2]: 3, name2[2]: 3
name1[3]: 6, name2[3]: 6
name1[4]: 5, name2[4]: 5
name1[5]: 0, name2[5]: 0
```

---

## Pointers to Strings: Array vs String Literal

There's an important distinction between character arrays and pointers to string literals:

```c
int main(int argc, char **argv) {
    char name1[] = "CS3650";        // Array on the stack (mutable)
    char name2[7] = { 'C', 'S', '3', '6', '5', '0', '\0' };
    
    char *name3 = name1;            // Pointer to the array
    char *name4 = "CS3650";         // Pointer to string literal in read-only memory
    
    for (int i = 0; i < 6; i++) {
        printf("name1[%d]: %c, name2[%d]: %c\n", 
            i, *(name1 + i), i, *(name2 + i));
    }
    
    // This works - modifying array on stack
    name1[0] = 'X';
    puts(name1);  // Prints: XS3650
    
    // This compiles but CRASHES at runtime
    puts(name4);      // Prints: CS3650
    name4[0] = 'X';   // SEGMENTATION FAULT - attempting to modify read-only memory!
    puts(name4);
    
    return 0;
}
```

### Key Difference

| Declaration | Memory Location | Mutable? |
|-------------|----------------|----------|
| `char name1[] = "CS3650"` | Stack (local variable) | ✅ Yes |
| `char *name4 = "CS3650"` | Read-only data segment | ❌ No |

When you create a pointer to a string literal (`char *ptr = "text"`), that string is stored in read-only memory. Any attempt to modify it will cause a **segmentation fault**.

See [[Pointer Declaration]] for more on declaring pointers correctly.

---

## Key Takeaways

1. **Array-pointer relationship**: Array names decay to pointers to their first element
2. **Pointer arithmetic**: `array[i]` is equivalent to `*(array + i)`
3. **No size tracking**: C arrays don't know their own length - track it separately
4. **Strings are arrays**: Strings are just `char` arrays with a null terminator
5. **String literals are read-only**: Pointers to string literals point to immutable memory
6. **Stack smashing danger**: Writing beyond array bounds corrupts the stack

---

## Related Topics

- [[Pointer Basics]] - foundational pointer concepts
- [[Pointer Arithmetic]] - how pointer math works with arrays
- [[Dereferencing]] - accessing values through pointers
- [[Pointer Declaration]] - declaring pointers correctly
- [[Pointer Safety]] - avoiding dangerous pointer operations
- [[Allocating Memory]] - dynamic memory allocation for arrays
- [[Example Code]] - complete working examples

#important #memory #arrays