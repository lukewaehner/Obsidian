Pointers to structs are essential for efficient memory management and function parameter passing in C. They allow you to work with struct data without copying entire structures.

---

## Declaring Pointers to Structs

You can declare pointers to structs using either the full `struct` keyword or a typedef alias:

```c
struct person *p;    // Using struct keyword
person_t *p;         // Using typedef alias
```

Both declarations create a pointer that can hold the address of a `person` struct. See [[Typedef]] for how to create type aliases like `person_t`.

---

## Getting the Address of a Struct

Use the [[Address-of Operator]] (`&`) to get the address of a struct variable:

```c
struct address work;
struct address *current = &work;
```

This creates a pointer `current` that points to the `work` struct.

---

## Dynamic Memory Allocation for Structs

Structs can be allocated dynamically on the heap using `malloc()` with `sizeof()` to determine the required memory:

```c
struct person *luke = malloc(sizeof(struct person));

// Using typedef alias (cleaner)
person_t *luke = malloc(sizeof(person_t));
```

> **Important:** Always check if `malloc()` succeeded before using the pointer. See [[Allocating Memory]] for proper memory management techniques.

**Safe allocation pattern:**
```c
person_t *luke = malloc(sizeof(person_t));
if (luke == NULL) {
    fprintf(stderr, "Memory allocation failed!\n");
    return 1;
}

// Use the struct...

free(luke);  // Don't forget to free when done!
luke = NULL; // Prevent dangling pointer
```

---

## Arrays of Structs

You can create arrays of structs either statically or dynamically:

### Static Array
```c
person_t class[80];  // Array of 80 person structs on the stack
```

### Dynamic Array
```c
person_t *friends = malloc(5 * sizeof(person_t));

// Access nested fields
for (int i = 0; i < 5; i++) {
    if (strcmp(friends[i].home.street, "Huntington Ave") == 0) {
        printf("%s lives close!\n", friends[i].first);
    }
}

// Don't forget to free
free(friends);
```

For dynamic arrays, you use bracket notation (`friends[i]`) just like static arrays, even though `friends` is a pointer.

---

## The Arrow Operator (`->`)

When accessing struct fields through a pointer, C provides the arrow operator (`->`) as convenient shorthand:

### Two Equivalent Ways

```c
// Method 1: Dereference first, then access field
(*p).home.city

// Method 2: Use arrow operator (preferred)
p->home.city
```

The arrow operator `->` is much more readable and is the standard way to access fields through pointers.

### Complete Example

```c
int lives_in_boston(person_t *p) {
    // Using arrow operator (clean and readable)
    return strcmp(p->home.city, "Boston") == 0;
    
    // Equivalent but uglier:
    // return strcmp((*p).home.city, "Boston") == 0;
}
```

### Nested Struct Access

The arrow operator works seamlessly with nested structs:

```c
person_t *student = malloc(sizeof(person_t));

// Accessing nested struct fields
student->home.house_no = 360;
strcpy(student->home.street, "Huntington Ave");
strcpy(student->home.city, "Boston");
```

Here, `student->home` gives you the `address` struct, and then `.house_no` accesses its field.

---

## Why Use Pointers to Structs?

### 1. Avoid Expensive Copies

Passing structs by value copies the entire struct to the function's stack frame. For large structs, this is inefficient:

```c
// Bad: Copies entire struct (expensive)
void process_person(person_t p) {
    // Works with a copy...
}

// Good: Passes only an 8-byte pointer (efficient)
void process_person(person_t *p) {
    // Works with original using p->field
}
```

### 2. Enable Modification

Passing a pointer allows the function to modify the original struct:

```c
void update_address(person_t *p, const char *new_city) {
    strcpy(p->home.city, new_city);  // Modifies original
}

person_t student;
update_address(&student, "Cambridge");  // student is now modified
```

### 3. Work with Dynamic Data Structures

Pointers enable building complex data structures like linked lists and trees:

```c
typedef struct node {
    int data;
    struct node *next;  // Pointer to next node
} node_t;
```

See Linked List for more on pointer-based data structures.

---

## Memory Layout Considerations

When working with struct pointers, remember:

```
Stack:              Heap:
┌─────────────┐    ┌──────────────────┐
│  person_t *p│───▶│ person_t struct  │
│  (8 bytes)  │    │ (actual size)    │
└─────────────┘    └──────────────────┘
```

- The pointer itself is typically 8 bytes (on 64-bit systems)
- The struct it points to can be much larger
- Heap-allocated structs must be manually freed with `free()`

---

## Common Patterns and Best Practices

### 1. Initialization Pattern
```c
person_t *create_person(const char *first, const char *last) {
    person_t *p = malloc(sizeof(person_t));
    if (p == NULL) {
        return NULL;
    }
    
    strcpy(p->first, first);
    strcpy(p->last, last);
    return p;
}

// Usage
person_t *student = create_person("John", "Doe");
if (student != NULL) {
    // Use student...
    free(student);
}
```

### 2. NULL Pointer Checks
```c
void print_person(person_t *p) {
    if (p == NULL) {
        printf("Error: NULL pointer!\n");
        return;
    }
    
    printf("%s %s\n", p->first, p->last);
}
```

### 3. Const Correctness
```c
// Pointer is const (can't point elsewhere)
person_t *const p = &student;

// Struct data is const (can't modify fields)
const person_t *p = &student;

// Both are const
const person_t *const p = &student;
```

---

## Key Takeaways

1. **Arrow operator (`->`)**: Preferred way to access fields through struct pointers
2. **Efficiency**: Pass pointers to avoid copying large structs
3. **Dynamic allocation**: Use `malloc()` with `sizeof()` for heap allocation
4. **Memory management**: Always `free()` dynamically allocated structs
5. **NULL checks**: Verify pointers before dereferencing
6. **Arrays**: Can create arrays of structs both statically and dynamically

---

## Related Topics

- [[Code/Topics/Computer Systems/C/Basics/Structs|Structs]] - Basic syntax and usage
- [[Typedef]] - Creating type aliases for cleaner code
- [[Pointer Basics]] - Fundamental pointer concepts
- [[Dereferencing]] - Accessing values through pointers
- [[Address-of Operator]] - Getting addresses of variables
- [[Pointer Arithmetic]] - Navigating through memory
- [[Allocating Memory]] - Dynamic memory management
- [[Pointer Safety]] - Avoiding common pointer pitfalls

#important #memory #structs