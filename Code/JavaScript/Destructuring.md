---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Arrays]]"
  - "[[Objects]]"
---
# Destructuring

Unpacking values from arrays and objects into named variables.

## Array Destructuring

```js
const [a, b, c] = [1, 2, 3];   // a=1, b=2, c=3

// Skip elements
const [first, , third] = [1, 2, 3];   // first=1, third=3

// Rest
const [head, ...tail] = [1, 2, 3, 4];  // head=1, tail=[2,3,4]

// Default values
const [x = 0, y = 0] = [10];   // x=10, y=0

// Nested
const [[a, b], [c, d]] = [[1, 2], [3, 4]];

// Swap variables
let p = 1, q = 2;
[p, q] = [q, p];

// From function return
const [min, max] = getRange();
```

## Object Destructuring

```js
const { name, age } = { name: 'Alice', age: 30 };

// Rename
const { name: userName } = { name: 'Alice' };
// userName = 'Alice', `name` is not declared

// Default values
const { role = 'guest' } = { name: 'Alice' };
// role = 'guest'

// Rename + default
const { status: userStatus = 'active' } = {};
// userStatus = 'active'

// Rest
const { name, ...rest } = { name: 'Alice', age: 30, city: 'NYC' };
// name='Alice', rest={ age: 30, city: 'NYC' }
```

## Nested Destructuring

```js
const user = {
  name: 'Alice',
  address: {
    city: 'NYC',
    zip: '10001'
  },
  scores: [95, 87, 92]
};

const { name, address: { city } } = user;
// name='Alice', city='NYC', `address` not declared

const { scores: [first, ...others] } = user;
// first=95, others=[87, 92]

// Deep nesting
const { a: { b: { c } } } = { a: { b: { c: 42 } } };
// c = 42
```

## In Function Parameters

Destructure directly in the function signature:

```js
// Object param
function greet({ name, age = 0 }) {
  return `${name} is ${age}`;
}
greet({ name: 'Alice', age: 30 });

// Array param
function first([head]) { return head; }
first([1, 2, 3]);  // 1

// With rename and default
function connect({ host = 'localhost', port = 3000 } = {}) {
  return `${host}:${port}`;
}
connect()                     // 'localhost:3000'
connect({ port: 8080 })      // 'localhost:8080'
```

The `= {}` default at the end makes the whole object optional — lets you call `connect()` without args.

## In Loops

```js
const users = [{ name: 'Alice', age: 30 }, { name: 'Bob', age: 25 }];

for (const { name, age } of users) {
  console.log(`${name}: ${age}`);
}

// Object entries
for (const [key, value] of Object.entries(obj)) {
  console.log(`${key} = ${value}`);
}
```

## Common Patterns

### Import-style selection

```js
const { useState, useEffect } = React;
const { readFile, writeFile } = fs.promises;
```

### Swapping

```js
let a = 1, b = 2;
[a, b] = [b, a];
```

### Ignore values

```js
const [, second] = [1, 2, 3];
const { name, age: _ } = user;  // discard age
```

### Mixed array/object

```js
const { users: [first, second] } = response;
```

## Tips

- When renaming, remember: `{ name: alias }` — `name` is the key, `alias` is the variable
- Always provide a default for the whole object param `= {}` so the function can be called without args
- Nested destructuring can get hard to read — consider splitting into multiple lines
- Rest (`...`) must always be last

## See Also

- [[Arrays]] — Array methods and spread
- [[Objects]] — Object spread and methods
- [[Functions]] — Destructuring in parameters
- [[JavaScript]]
