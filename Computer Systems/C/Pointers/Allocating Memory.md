
---

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
	int i = 10;
	
	// Give it space for a int
	int *pi = malloc(4);	
	*pi = 42;
	
	printf("%p: %d\n", pi, *pi)
	
	(*pi)++;
	
	printf("%p: %d\n", pi, *pi)
	
	return 0
}
```

> Whenever we allocate memory, we need to deallocate it

```c
free(pi);
```

> This line will release all memory back to the stack

---
This doesn't let the address become inaccessible or invalid

```c
printf("%p: %d\n", pi, *pi) // Same address, just garbage now
```

If we keep running after we free it, set it to null
```c
pi = NULL;
```

---

After calling `malloc` we should definitely check we got space

```c
int *pi = malloc(4);

if (pi == NULL) {
	printf("Couldn't allocate! Exiting. \n")
	return 1;
}

assert(pi != NULL);
```

---

### Easy grabbing size

Instead of explicit 4 for int just use
```c
int *pi = malloc(sizeof(int));
```

You could even do

```c
int *pi = malloc(sizeof(pi))
```

But thats weird.

---
### Allocating an Array

```c
int *pi = malloc(10 * sizeof(int));

for (int i = 0; i < 10; i++) {
	pi[i] = i * i;
}

for (int i = 0; i < 10; i++) {
	printf("%d\n", pi[i]);
}
```