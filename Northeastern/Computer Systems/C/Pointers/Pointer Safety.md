Common dangers when working with pointers and how to avoid them.

## The Uninitialized Pointer Danger

**Dangerous Code:**
```c
int main(int argc, char **argv) {
    int x = 12;
    int *pi;  // Uninitialized pointer
    
    printf("%d\\n", *pi);  // DANGER: Undefined behavior
    
    return 0;
}
```

**Problem:** Since `pi` isn't pointed to anything, it contains whatever random value was in that memory location. Dereferencing it accesses random memory.

## Safe Initialization

**Safe Code:**
```c
int main(int argc, char **argv) {
    int x = 12;
    int *pi = NULL;  // Initialize to NULL
    
    // Check before using
    if (pi != NULL) {
        printf("%d\\n", *pi);
    }
    
    return 0;
}
```

## Using Assertions for Safety

```c
#include <stdio.h>
#include <assert.h>

int main(int argc, char **argv) {
    int x = 12;
    int *pi = NULL;
    
    assert(pi != NULL);  // Program will terminate if pi is NULL
    printf("%d\\n", *pi);  // This relies on the validity of pi
    
    return 0;
}
```

## Common Pointer Errors

### 1. Segmentation Fault
- Dereferencing NULL or invalid pointers
- Accessing memory you don't own

### 2. Memory Leaks
- Forgetting to free dynamically allocated memory

### 3. Dangling Pointers
- Using pointers after the memory they point to has been freed

### 4. Wild Pointers
- Using uninitialized pointers

## Best Practices

1. **Always initialize pointers** - Use `NULL` if you don't have a value yet
2. **Check for NULL** - Before dereferencing, verify the pointer isn't NULL
3. **Set to NULL after freeing** - Prevent accidental reuse of freed memory
4. **Use assertions** - For debugging and catching errors early
5. **Avoid returning addresses of local variables** - They become invalid after function returns

## Safe Pointer Pattern

```c
int *ptr = NULL;  // Initialize

// Get a valid address
int value = 42;
ptr = &value;

// Check before use
if (ptr != NULL) {
    printf("Value: %d\\n", *ptr);
}

// Clean up (if dynamically allocated)
// free(ptr);
// ptr = NULL;
```

## Related Topics
- [[Pointer Declaration]]
- [[Dereferencing]]
- [[Pointer Basics]]

#important #memory