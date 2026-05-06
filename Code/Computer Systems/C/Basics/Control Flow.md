

Control flow statements determine the order in which code executes.

## Conditional Statements

### If Statement
```c
if (condition) {
    // do stuff
}
```

### If-Else Statement
```c
if (condition) {
    // do stuff
} else {
    // do other stuff
}
```

## Loops

### While Loop
```c
while(condition) {
    // do while condition is true
}
```

### Do-While Loop
```c
do {
    // execute at least once
} while(condition);
```

### For Loop
```c
for (initializer; condition; updater) {
    // 1. Run initializer expression
    // 2. If condition holds go to step 3, else goto 6
    // 3. Do stuff in body
    // 4. Run the updater expression
    // 5. Go to 2
    // 6. End
}
```

## Operators

### Comparison Operators
`<`, `>`, `<=`, `>=`, `==`

### Logical Operators
- `!` - NOT
- `&&` - AND
- `||` - OR

## Loop Control

- **`continue`** - Skip the rest of the current iteration of the innermost loop
- **`break`** - Exit the current loop entirely

## Related Topics
- [[Scope]]
- [[Code/Topics/Computer Systems/C/Basics/Functions]]