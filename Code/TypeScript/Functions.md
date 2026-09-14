---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Types]]"
date: 2026-09-14
---
# Functions

Take in data, process it, return a result. **One function, one job.**

JavaScript lets you assign functions to variables, pass them to other functions, return them from functions, attach them to objects and prototypes, write properties onto them, and read those back. TypeScript models all of it with the type system — what it adds is **types for the parameters and the return value**.

## The Shape

```ts
function functionName(argument1: <type>, defaultArgument: <type> = value, optionalArgument?: <type>): <return type> {
  // Function body
}
```

Order matters: required, then defaulted/optional.

## Typing the Function

Untyped JavaScript:

```ts
// Named function
function add(a, b) {
  return a + b;
}
```

Typed:

```ts
function add(a: number, b: number): number {
  return a + b;
}
```

The rule the tutorial states, and it's the one to internalize:

> You will usually explicitly annotate function parameters — TypeScript will always infer types throughout the body of your function, but in most cases it won't infer types for your parameters. The return type is inferred, but it's a good practice to explicitly annotate it.

So: **annotate parameters because you must, annotate the return because you should.** The return annotation isn't for the compiler, it's a check on *you* — it fails at the function definition if the body returns the wrong thing, instead of failing at some distant call site.

Unannotated parameters are implicitly `any`, which `noImplicitAny` in [[Tooling|tsconfig]] rejects.

## Invoking the Function

No extra type information at the call site — pass arguments, and TypeScript checks they're compatible with the parameter types.

```ts
add(1, 2);         // evaluates to 3
```

And it's quick to complain when they aren't:

```ts
add(1);            // Error TS2554: Expected 2 arguments, but got 1.
add(1, 'a');       // Error TS2345: Argument of type '"a"' is not assignable
                   // to parameter of type 'number'.
```

Arity is part of the contract, which is not true in plain JavaScript — `add(1)` there returns `NaN` at runtime.

## Optional and Default Parameters

`?` marks a parameter optional. **Required parameters must come first, followed by optional ones.**

```ts
function log(message: string, userId?: string) {
  let time = new Date().toLocaleTimeString()
  console.log(time, message, userId || 'Not signed in')
}

log('Page loaded') // Logs "12:38:31 PM Page loaded Not signed in"
log('User signed in', 'da763be') // Logs "12:38:31 PM User signed in da763be"
```

Inside the body, `userId` is typed `string | undefined` — you have to handle the absent case, which is what the `|| 'Not signed in'` is doing.

A **default value** achieves something similar: callers no longer have to pass it.

```ts
function log(message: string, userId = 'Not signed in') {
  let time = new Date().toISOString()
  console.log(time, message, userId)
}

log('User clicked on a button', 'da763be')
log('User signed out')
```

| | Optional `?` | Default `= value` |
| --- | --- | --- |
| Type inside body | `T \| undefined` | `T` — never undefined |
| Must be last | **yes** | no |
| Type annotation | required | inferred from the default |

Prefer a default when there *is* a sensible default. It removes a branch from the body.

## Rest Parameters

Accept a variable number of arguments by grouping them into an array. **Must be the last parameter.**

```ts
function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}

sum(1, 2, 3); // evaluates to 6
sum(4, 5); // evaluates to 9
```

The type is the *array* type (`number[]`), not the element type. Inside the body it's an ordinary array — note the [[Array Functions|`reduce`]] with its initial value `0`, which is what makes `sum()` with no arguments return `0` rather than throw.

## Arrow Functions

Also called fat arrow functions. Functions with **lexical `this` and `arguments`** — especially useful in class methods to preserve context when using higher-order functions.

```ts
let sum = (x: number, y: number): number => {
    return x + y;
}

sum(10, 20); //returns 30
```

`(x: number, y: number)` are the parameter types, `: number` is the return type, and `=>` separates the signature from the body. The right side of `=>` can contain one or more statements.

A single-expression body can drop the braces and the `return` — the form you'll see most in callbacks:

```ts
const sum = (x: number, y: number): number => x + y;
```

### The `this` difference

This is the real reason arrow functions exist:

```ts
class Counter {
    count: number = 0;
    // Using a regular function
    incrementWithRegularFunction() {
        setTimeout(function() {
            this.count++; // Error: 'this' is undefined
            console.log(this.count);
        }, 1000);
    }

    // Using an arrow function
    incrementWithArrowFunction() {
        setTimeout(() => {
            this.count++; // 'this' refers to the Counter instance
            console.log(this.count);
        }, 1000);
    }
}

const counter = new Counter();
counter.incrementWithArrowFunction(); // Logs: 1
```

The arrow function in `incrementWithArrowFunction()` keeps its reference to the `Counter` instance. The regular function loses it: a `function` expression gets its own `this`, bound by **how it was called**, and `setTimeout` calls it with no receiver.

An arrow function has no `this` of its own — it closes over the `this` of the enclosing scope, at the point it was *written*. That's what "lexical `this`" means, and it makes the arrow the default choice for any callback inside a class method.

## Function Overloads

Specify a function that can be called in different ways by writing **overload signatures**: some number of signatures (usually two or more), followed by the implementation body.

```ts
//function makeDate() with one parameter
function makeDate(timestamp: number): Date;
//function makeDate() with three parameters
function makeDate(m: number, d: number, y: number): Date;
//function makeDate() with one parameter and 2 default parameters
function makeDate(mOrTimestamp: number, d?: number, y?: number): Date {
  if (d !== undefined && y !== undefined) {
    return new Date(y, mOrTimestamp, d);
  } else {
    return new Date(mOrTimestamp);
  }
}
const d1 = makeDate(12345678);
const d2 = makeDate(5, 5, 5);
const d3 = makeDate(1, 3); //No overload expects 2 arguments, but overloads do exist that expect either 1 or 3 arguments.
```

Three things to notice:

1. The **implementation signature is not callable**. It exists to be wide enough to satisfy both overloads. `makeDate(1, 3)` matches it structurally but is still an error, because only the two declared overloads are public.
2. The body must handle every overload — hence the `d !== undefined && y !== undefined` check.
3. Overloads are a **type-level** construct. Only one function is emitted.

> [!tip] Prefer a union or optional parameters first
> Overloads are the right tool when the parameter *count* changes meaning, as above. If the types vary but the arity doesn't, a union parameter (`id: string | number`) is simpler and keeps one signature to read.

## Tips
- Annotate the return type. It localizes the error to the function instead of the caller, and it documents intent.
- Default to arrow functions for callbacks and `function` declarations for top-level named functions — the latter hoist and give better stack traces.
- One job per function. If the name needs "and", it's two functions.
- A parameter only one caller ever passes is a smell; so is a `boolean` flag parameter that switches behavior. Split the function.
- Functions are values: `(a: number) => string` is a type you can put on a variable or a parameter.

## See Also
- [[Array Functions]] — callbacks in practice
- [[Classes]] — methods, and where the `this` problem lives
- [[Generics]] — functions that work over multiple types
- [[Types]] · [[Tuples]] — returning more than one value
- [[Tutorial - TypeScript Basics]] · [[CS4530 Code Style Guide]]
