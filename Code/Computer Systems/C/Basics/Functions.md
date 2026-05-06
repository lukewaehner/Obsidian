Functions are reusable blocks of code that perform specific tasks.

## Function Syntax

```c
return_type function_name(type1 arg1, type2 arg2, ...)
```

## Void Functions

Functions that don't return anything have a return type `void`:

```c
void print_message(char* message) {
    printf("%s\\n", message);
}
```

## Function with Return Value

```c
int add(int a, int b) {
    return a + b;
}
```

## Key Points

- Functions must be declared before they are used
- The `main()` function is the entry point of every C program
- Parameters are passed by value (copies are made)
- Use `return` to send a value back to the caller

## Related Topics
- [[Declaration vs Definition]]
- [[Code/Topics/Computer Systems/C/Basics/Data Types]]
- [[Hello World Program]]