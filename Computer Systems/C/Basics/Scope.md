Scope in C determines where variables are accessible within your program.

## Block Scope

Scope is delimited by curly braces `{` and `}`

- Any variable declared within a block is only visible inside that block and its sub-blocks
- Variables declared in outer blocks are accessible in inner blocks
- Variables declared in inner blocks "shadow" variables with the same name in outer blocks

## Example

```c
int main() {
    int x = 10;        // x is accessible throughout main()
    
    if (x > 5) {
        int y = 20;    // y is only accessible within this if block
        printf("%d\\n", x); // Can access x from outer scope
    }
    
    // printf("%d\\n", y); // ERROR: y is not accessible here
    
    return 0;
}
```

## Related Topics
- [[Computer Systems/C/Basics/Functions]]
- [[Control Flow]]