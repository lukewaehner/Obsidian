#important #memory 

---
- A representation of a location in memory, a special variable holding an address
- Pointers have a type, so C knows what type we are pointing to

---
### Declaring:
Use * after the type name

```c
int *pi
```

- Note: if a pointer isn't set to anything right away, its best to initialize it to `NULL`:
```c
int *pi = NULL;
```

---
### De-referencing:
- Getting the value a pointer points to is called dereferencing and is denoted by putting * before the variable name:

```c
printf("%d\n", %pi);
```

---
### Address-of Operator
- The easiest way to getting a pointer to point to something meaningful is to give it an address:
- The address-of operator & serves this purpose:

```c
int i = 42;
int *pi = &i; // pi now points to where i is stored

i = 43;
printf("%d %d\n", i, *pi); // 43 43

*pi = 44;
printf("%d %d\n", i, *pi); // 44 44

int j = 123;
pi = &j;
printf("%d %d\n", i, *pi); // 44 123
```


---
### Pointers Pointing to Pointers
- Pointers can point to other pointers:

```c
int i = 42;
int *pi = &i;
int **ppi = &pi;

printf("%d %d %d\n", i, *pi, **ppi);
// 42 42 42
```


---
### Dangers:
```c
int main(int argc, char **argv) {
	int x = 12;
	int *pi;
	
	printf("%d\n", *pi);
	
	return 0;
}
```

- Since, its not pointed to anything, it will return whatever junk is on the register the compiler decided to use.
- We should be setting the pointer to NULL if we don't have anything to set it to yet, but it will cause segmentation fault if not pointed to and used.

```c
#include <stdio.h>
#include <assert.h>

int main(int argc, char **argv) {
	int x = 12;
	int *pi = NULL;
	
	assert(pi != NULL)
	// this relise on the validity of pi.
	printf("%d\n", *pi);
	
	return 0;
}
```