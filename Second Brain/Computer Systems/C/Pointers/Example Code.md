## Pointer Declaration:

```c
int *pi = NULL;        // Pointer to an integer
char *pc = NULL;       // Pointer to a character  
float *pf = NULL;      // Pointer to a float

// Declare multiple pointers
int *p1, *p2, *p3;     // All three are pointers to int

// Note: This declares one pointer and one regular variable
int *ptr, value;       // ptr is pointer, value is regular int
```

> Always initialize pointers to NULL if not immediately assigning an address. Uninitialized pointers contain random values and cause undefined behavior.

---

## Address-of Operator:

```c
int i = 42;
int *pi = &i;  // pi now points to where i is stored

i = 43;
printf("%d %d\n", i, *pi);  // 43 43

*pi = 44;
printf("%d %d\n", i, *pi);  // 44 44

int j = 123;
pi = &j;  // Now pi points to j instead
printf("%d %d\n", i, *pi);  // 44 123
```

> The `&` operator gets the memory address of a variable. You can reassign pointers to point to different variables at any time.

---

## Dereferencing:

```c
int i = 42;
int *pi = &i;

printf("i = %d, *pi = %d\n", i, *pi);  // i = 42, *pi = 42

*pi = 100;  // Change the value through the pointer
printf("i = %d, *pi = %d\n", i, *pi);  // i = 100, *pi = 100
```

> The `*` operator dereferences a pointer, accessing the value at the address it stores. You can both read and write through dereferenced pointers.

---

## Pointer to Pointer:

```c
int i = 42;
int *pi = &i;      // pi points to i
int **ppi = &pi;   // ppi points to pi

printf("%d %d %d\n", i, *pi, **ppi);
// Output: 42 42 42

// ppi stores address of pi
// *ppi gets the value of pi (which is address of i)
// **ppi gets the value of i
```

> Double pointers create multiple levels of indirection. Commonly used for command line arguments (`char **argv`), modifying pointers in functions, and dynamic 2D arrays.

---

## Pointer Arithmetic:

```c
int main(int argc, char **argv) {
	int i = 11;
	int j = 12;
	int k = 13;
	
	char c = 10;
	
	char *pc = &c;
	
	printf("sizeof(c) = %zu, sizeof(pc) = %zu, sizeof(*pc) = %zu\n",
		 sizeof(c), sizeof(pc), sizeof(*pc)); // 1, 8, 1
	
	int *pi = &k;
	int **ppi = &pi;
	int ***pppi = &ppi;
	
	printf("%p = %d\n", pi, *pi);
	// <Address> = 13 
	
	pi = pi + 1; // pi + sizeof(*pi) * 1 -> Pointer arithmetic
	
	printf("%p = %d\n", pi, *pi);
	// <Address> = 12
	
	ppi = ppi + 1; // Adds 8, because it points to a pointer (8 byte)
	
	return 0;
}
```

> By adding 1 to pi we can see that we are moving up the stack, going from k (initial set), to j, to i. Pointer arithmetic automatically scales by the size of the pointed-to type.

---

## Pointer Safety:

```c
// ❌ DANGEROUS - Uninitialized pointer
int main(int argc, char **argv) {
    int x = 12;
    int *pi;  // Contains random value
    
    printf("%d\n", *pi);  // UNDEFINED BEHAVIOR
    
    return 0;
}

// ✅ SAFE - Properly initialized
int main(int argc, char **argv) {
    int x = 12;
    int *pi = NULL;  // Initialize to NULL
    
    // Check before using
    if (pi != NULL) {
        printf("%d\n", *pi);
    }
    
    return 0;
}

// Using assertions for safety
#include <assert.h>

int main(int argc, char **argv) {
    int x = 12;
    int *pi = NULL;
    
    assert(pi != NULL);  // Program terminates if pi is NULL
    printf("%d\n", *pi);
    
    return 0;
}
```

> Always initialize pointers to NULL and check before dereferencing. Assertions help catch errors during development.

---
