# Declaration vs Definition

Understanding the difference between declaring and defining functions is crucial in C programming.

## Function Declaration

A **declaration** tells the compiler about a function's name, return type, and parameters. It's like a promise that the function exists somewhere.

### Example Declaration:
```c
double pow(double base, int exp);
```

- Also called a "function prototype"
- Usually placed in header files or at the top of source files
- Ends with a semicolon
- No function body

## Function Definition

A **definition** provides the actual implementation of the function - what it does.

### Example Definition:
```c
double pow(double base, int exp) {
    double result = 1;
    
    for (int i = 0; i <= exp; i++) {
        result *= base;
    }
    
    return result;
}
```

- Contains the complete function body
- Must match the declaration exactly
- Only one definition per function allowed

## Key Differences

| Declaration | Definition |
|------------|------------|
| Prototype only | Complete implementation |
| Ends with `;` | Has `{ }` body |
| Can appear multiple times | Only once |
| Usually in headers | Usually in source files |

## Related Topics
- [[Functions]]
- [[Scope]]