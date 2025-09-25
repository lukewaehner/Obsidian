Code Snippet to understand

---
```c
#include <stdio.h>

int main(int argc, char**argv) {
	printf("Hello, World!\n")
	
	return 0;
}
```

--- 

Scope is delimited by `{` and `}`
- Any variable declared within the block is only visible inside of that block, and sub blocks


---
## Functions

`return_type function_name(type1 arg1, type2 arg2, ...)`

Functions that don't return anything have a return type `void`

---
## Control Flow

```c
if (something) {
	// do stuff
}

if (something) {
	// do stuff
} else {
	// do other stuff
}
```

 - While loops and do-while
```c
while(condition) {
	// do while holding condition
}
```

```c
do {

} while(condition);
```

```c
for (intiiliazer; condition; updater) {
	// 1. Run initializer expression
	// 2. If condition holds go to step 3, else goto 6
	// 3. Do stuff in body
	// 4. Run the updater expression
	// 5. Go to 2
	// 6. End	

}
```

- Comparison operators `<, >, <=, >=, ==`
- Logical operators: `!, &&, ||`
- You can skip the rest of the current iteration of the innermost loop with `continue`
- `Break` will break

---
## Types
#new

### Primitive
- **signed** and **unsigned** integral types:
> For unsigned use `unsighned short int`

| Type      | Byte           |
| --------- | -------------- |
| char      | 1 byte (8-bit) |
| short int | 16-bit         |
| int       | 32-bit         |
| long int  | 64-bit         |
| float     | 32-bit         |
| double    | 64-bit         |

### Arrays

### Pointers

### Structs

### Union
---
## Definition vs. Declaration

- Function declaration example:

```c
double pow(double base, int exp);
```

- Function definition example:

```c
double pow(double base, int exp) {
	double result = 1;
	
	for (int i = 0; i <= exp; i++) {
		result *= base;
	}
	
	return result;
}
```

---
### Arrays:
- Just pointers with some fancy syntax.
- Static versus Dynamic sizing.
```c
float nums[4]; // create an array for 4 floats
```

- This makes room for 4 floats
- They will be stored contiguously in memory
- `nums` points to the first element
- 0 based index indices

```c
float nums[4];
nums[0] = 0.1;
nums[1] = 3.14;
nums[2] = 1.5;
nums[3] = 3214;

printf("2nd element: %f\n", nums[1]);
```

They can also be initialized:
```c
float nums[4] = { 0.1, 3.14, 1.5, 3214 };

printf("2nd element: %f\n", nums[1]);
```