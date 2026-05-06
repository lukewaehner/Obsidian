---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Functions]]"
  - "[[Variables]]"
---
# Closures

Functions that capture variables from their enclosing scope.

## What a Closure Is

A closure is a function bundled with the environment it was created in. When a function references variables from an outer scope, those variables are "closed over" — they stay alive as long as the function does.

```js
function makeCounter() {
  let count = 0;     // this variable is captured

  return function() {
    count++;
    return count;
  };
}

const counter = makeCounter();
counter()  // 1
counter()  // 2
counter()  // 3
// count lives on inside the returned function
```

`count` is not accessible from outside `makeCounter`, but the returned function keeps it alive.

## Scope Chain

Every function looks up the scope chain for variables it doesn't own:

```js
const x = 'global';

function outer() {
  const x = 'outer';

  function inner() {
    const x = 'inner';
    console.log(x);  // 'inner' — own scope wins
  }

  function middle() {
    console.log(x);  // 'outer' — walks up chain
  }

  inner();
  middle();
}
```

## Closures Share the Same Variable

Multiple functions closing over the same variable all see the same value — not a copy:

```js
function makeAdder(x) {
  return n => n + x;  // each call creates a new closure with its own x
}

const add5 = makeAdder(5);
const add10 = makeAdder(10);
add5(3)   // 8
add10(3)  // 13
```

## The Classic Loop Bug

```js
// Bug: all functions close over the same `i`
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Prints: 3, 3, 3

// Fix 1: use let (block-scoped, new binding per iteration)
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Prints: 0, 1, 2

// Fix 2: IIFE to capture the current value
for (var i = 0; i < 3; i++) {
  ((i) => setTimeout(() => console.log(i), 100))(i);
}
```

This is why `var` in loops is dangerous and `let` fixes it.

## Practical Patterns

### Factory functions

```js
function createUser(name, role) {
  let loginCount = 0;

  return {
    getName: () => name,
    getRole: () => role,
    login() {
      loginCount++;
      console.log(`${name} logged in (${loginCount}x)`);
    }
  };
}

const alice = createUser('Alice', 'admin');
alice.login();  // 'Alice logged in (1x)'
alice.getName() // 'Alice'
// loginCount is inaccessible from outside
```

### Memoization

Cache expensive computation results:

```js
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

const expensiveFn = memoize((n) => {
  // ...heavy computation...
  return n * n;
});
```

### Partial application

Fix some arguments, return a function for the rest:

```js
function multiply(a, b) { return a * b; }

function partial(fn, ...presetArgs) {
  return (...laterArgs) => fn(...presetArgs, ...laterArgs);
}

const double = partial(multiply, 2);
const triple = partial(multiply, 3);
double(5)  // 10
triple(5)  // 15
```

### Module pattern (pre-ES6 modules)

```js
const counter = (() => {
  let count = 0;

  return {
    increment() { count++; },
    decrement() { count--; },
    value() { return count; }
  };
})();

counter.increment();
counter.value()  // 1
// count is not accessible outside
```

## Tips

- Closures are how JavaScript implements data privacy — captured variables are invisible from outside
- Every function call creates a new closure — `makeCounter()` called twice gives two independent counters
- Be careful capturing variables in loops — use `let` or move the function outside the loop
- Closures can cause memory leaks if you hold references to them longer than needed (the outer scope stays alive)

## See Also

- [[Variables]] — Scope, hoisting, and let/const
- [[Functions]] — How functions work
- [[Modules]] — Modern alternative to the module pattern
- [[JavaScript]]
