---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Closures]]"
  - "[[Arrays]]"
---
# Functions

Defining, calling, and working with functions in JavaScript.

## Declarations vs Expressions

### Function declaration — hoisted

```js
greet('Alice');  // works — fully hoisted

function greet(name) {
  return `Hello, ${name}`;
}
```

### Function expression — not hoisted

```js
greet('Alice');  // TypeError: greet is not a function

const greet = function(name) {
  return `Hello, ${name}`;
};
```

### Arrow function — concise, no own `this`

```js
const greet = (name) => `Hello, ${name}`;
const double = n => n * 2;           // parens optional for single param
const getObj = () => ({ key: 'val' }); // wrap object literal in parens

// Multi-line
const add = (a, b) => {
  const result = a + b;
  return result;
};
```

## Parameters

### Default parameters

```js
function greet(name = 'World') {
  return `Hello, ${name}`;
}
greet()         // 'Hello, World'
greet('Alice')  // 'Hello, Alice'
```

### Rest parameters — collect remaining args into array

```js
function sum(...nums) {
  return nums.reduce((acc, n) => acc + n, 0);
}
sum(1, 2, 3, 4)  // 10
```

### Destructuring in parameters

```js
function greet({ name, age = 0 }) {
  return `${name} is ${age}`;
}
greet({ name: 'Alice', age: 30 });

function first([head, ...tail]) {
  return head;
}
first([1, 2, 3]);  // 1
```

## Return Values

```js
// Functions return undefined by default
function nothing() {}
nothing()  // undefined

// Arrow functions with no braces: implicit return
const double = n => n * 2;

// Multiple returns
function abs(n) {
  if (n < 0) return -n;
  return n;
}
```

## this Binding

`this` depends on how a function is called, not where it's defined.

### Regular function — `this` set by call site

```js
const obj = {
  name: 'Alice',
  greet() {
    console.log(this.name);  // 'Alice' — called as obj.greet()
  }
};

const fn = obj.greet;
fn();  // undefined — lost context, this is global/undefined in strict mode
```

### Arrow function — `this` inherited from enclosing scope

```js
const obj = {
  name: 'Alice',
  greet() {
    const inner = () => console.log(this.name);
    inner();  // 'Alice' — arrow uses enclosing this
  }
};
```

### Explicit binding

```js
function greet() { console.log(this.name); }
const obj = { name: 'Alice' };

greet.call(obj);           // 'Alice' — call with args: fn.call(ctx, a, b)
greet.apply(obj);          // 'Alice' — apply with array: fn.apply(ctx, [a, b])
const bound = greet.bind(obj);
bound();                   // 'Alice' — returns new function, doesn't call
```

### Class methods and `this` loss

```js
class Timer {
  constructor() { this.count = 0; }

  tick() { this.count++; }
}

const t = new Timer();
setInterval(t.tick, 1000);           // broken — this is undefined
setInterval(() => t.tick(), 1000);   // fine — arrow preserves context
setInterval(t.tick.bind(t), 1000);   // fine — explicit bind
```

## Higher-Order Functions

Functions that take or return other functions:

```js
// Takes a function
function repeat(n, fn) {
  for (let i = 0; i < n; i++) fn(i);
}
repeat(3, i => console.log(i));  // 0, 1, 2

// Returns a function
function multiplier(factor) {
  return n => n * factor;
}
const double = multiplier(2);
const triple = multiplier(3);
double(5);  // 10
triple(5);  // 15
```

## IIFE — Immediately Invoked Function Expression

Execute a function the moment it's defined. Used to create a private scope:

```js
const result = (function() {
  const private = 'secret';
  return private.toUpperCase();
})();

// Arrow version
const result = (() => 'hello')();
```

## Pure Functions

A function is pure if it always returns the same output for the same input and has no side effects:

```js
// Pure
const add = (a, b) => a + b;

// Impure — depends on external state
let total = 0;
const addToTotal = n => { total += n; };
```

Pure functions are easier to test and reason about. Prefer them where possible.

## Tips

- Use arrow functions for callbacks and short expressions
- Use regular functions (or methods) when you need `this`
- Arrow functions cannot be used as constructors
- Avoid mutating function parameters — treat them as read-only
- Name your functions, even when assigning to variables — better stack traces

## See Also

- [[Closures]] — Scope chain and captured variables
- [[Arrays]] — Higher-order methods (map, filter, reduce)
- [[Classes]] — Methods and this
- [[JavaScript]]
