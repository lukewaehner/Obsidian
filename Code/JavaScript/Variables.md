---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Closures]]"
  - "[[Functions]]"
---
# Variables

Declaring and scoping variables in JavaScript.

## Declarations

```js
var x = 1;    // function-scoped, hoisted, re-declarable
let y = 2;    // block-scoped, not hoisted, no re-declare
const z = 3;  // block-scoped, must initialize, binding is immutable
```

Prefer `const` by default. Use `let` when you need to reassign. Avoid `var`.

## Scope

### Block scope (let / const)

```js
{
  let a = 1;
  const b = 2;
}
// a and b not accessible here

if (true) {
  let msg = 'hi';
}
// msg not accessible here
```

### Function scope (var)

```js
function example() {
  var x = 1;
  if (true) {
    var x = 2;   // same variable — var ignores blocks
    console.log(x); // 2
  }
  console.log(x);   // 2
}
```

### Global scope

Variables declared outside any function or block become properties of the global object (`window` in browsers, `global` in Node).

```js
var globalVar = 'everywhere';   // window.globalVar in browsers
let globalLet = 'also global';  // NOT on window object
```

## Hoisting

Declarations are moved to the top of their scope before execution.

### var is hoisted and initialized to undefined

```js
console.log(x);  // undefined — not an error
var x = 5;
console.log(x);  // 5

// Equivalent to:
var x;
console.log(x);  // undefined
x = 5;
```

### Function declarations are fully hoisted

```js
greet();          // 'hello' — works before declaration

function greet() {
  console.log('hello');
}
```

### let and const: Temporal Dead Zone (TDZ)

`let` and `const` are hoisted but NOT initialized. Accessing them before the declaration throws a ReferenceError.

```js
console.log(x);  // ReferenceError: Cannot access 'x' before initialization
let x = 5;
```

The TDZ is the period between entering the scope and reaching the declaration.

## const Is Not Deeply Immutable

The binding is immutable, but the value can still be mutated if it's an object or array:

```js
const obj = { x: 1 };
obj.x = 2;       // fine — mutating the object
obj = { x: 2 };  // TypeError — can't reassign the binding

const arr = [1, 2, 3];
arr.push(4);     // fine
arr = [];        // TypeError
```

Use `Object.freeze()` to prevent mutation:

```js
const point = Object.freeze({ x: 1, y: 2 });
point.x = 99;  // silently fails (throws in strict mode)
```

## Variable Naming

```js
// camelCase for variables and functions
let firstName = 'Alice';
const maxRetries = 3;

// PascalCase for classes and constructors
class UserAccount {}

// UPPER_SNAKE_CASE for constants known at compile time
const MAX_CONNECTIONS = 100;

// _ prefix convention for "private" (no enforcement)
let _internalState = {};
```

## Tips

- Default to `const` — switch to `let` only when you need to reassign
- Never use `var` in modern code
- Declare variables at the top of their block to avoid TDZ confusion
- `const` on an object/array doesn't freeze it — use `Object.freeze()` if needed

## See Also

- [[Closures]] — How scope chain works across functions
- [[Functions]] — Function scope and closures
- [[JavaScript]]
