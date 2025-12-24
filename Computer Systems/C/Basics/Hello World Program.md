The basic structure of a C program demonstrated through the classic "Hello, World!" example.

## Code Example

```c
#include <stdio.h>

int main(int argc, char**argv) {
    printf("Hello, World!\\n");
    
    return 0;
}
```

## Key Components

- **`#include <stdio.h>`** - Includes the standard input/output library
- **`int main()`** - The entry point of every C program
- **`argc, char**argv`** - Command line arguments (argument count and argument vector)
- **`printf()`** - Function to print formatted output
- **`return 0;`** - Indicates successful program execution

## Related Topics
- [[Computer Systems/C/Basics/Functions]]
- [[Data Types]]