

---
## Basic idea

```c
int main(int argc, int **argv) {
	// Initialize the array like this
	int nums[4] = { 1, 2, 3, 4 };
	
	// Overwrite them
	nums[0] = 42;
	nums[1] = 4321;
	
	for (int i = 0; i < 4; i++) {
		printf("nums[%d]: %d\n", i, nums[i])
	}
	return 0;
}
```

---
### Stack Smashing
#memory

There isn't really a way to grab array sizing since they don't know their size. 

```c
int main(int argc, int **argv) {
	// Initialize the array like this
	int nums[4] = { 1, 2, 3, 4 };
	
	// Overwrite them
	nums[0] = 42;
	nums[1] = 4321;
	
	for (int i = 0; i < 10; i++) {
		nums[i] = i * 2;
		printf("nums[%d]: %d\n", i, nums[i])l
	}
	return 0;
}
```

> This will run, but if you keep going, you might start writing on main and it will fail then.
> This is called stack smashing and should be avoided ideally

---

### Memory access

```c
int main(int argc, int **argv) {
	// Initialize the array like this
	int nums[4] = { 1, 2, 3, 4 };
	
	for (int i = 0; i < 4; i++) {
		printf("nums[%d]: %d\n", i, *(nums + 1));
	}
	return 0;
}
```

> This is just the same as accessing `nums[i]`, since we are just showing up to the value in the stack

This also works with `*(nums + i)`, `*(i + nums)`, some psychos might even use `i[nums]`
Yes this fucking works for some reason.

---

### Strings as Arrays


Strings is not a type, its just an array of characters

```c
int main(int argc, char **argv) {
	char name1[] = "CS3650";
	char name2[7] = { 'C', 'S', '3', '6', '5', '0', '0' };
	
	for (int i = 0; i < 6; i++) {
		printf("name1[%d]: %c, name2[%d]: %c\n", 
			i, *(name1 + i), i, *(name2 + i))
	}
}
```

> Note, you don't have to put the number of elements for the string, but you need (char + 1) elements for a null character.

Prints:

```
name1[0]: C, name2[0]: C
name1[1]: S, name2[1]: S
name1[2]: 3, name2[2]: 3
name1[3]: 6, name2[3]: 6
name1[4]: 5, name2[4]: 5
name1[5]: 0, name2[5]: 0
```

### Pointers

```c
int main(int argc, char **argv) {
	char name1[] = "CS3650";
	char name2[7] = { 'C', 'S', '3', '6', '5', '0', '0' };
	
	char *name3 = name1;
	char *name4 = "CS3650"; // This points to a string literal, which is stored in read only mem
	
	for (int i = 0; i < 6; i++) {
		printf("name1[%d]: %c, name2[%d]: %c\n", 
			i, *(name1 + i), i, *(name2 + i))
	}
	
	name1[0] = 'X';
	puts(name1); // XS3650
	
	puts(name4); // CS3650
	name4[0] = 'X'; // SEGFAULTS here.
	puts(name4); 
	
	return 0;
}
```

