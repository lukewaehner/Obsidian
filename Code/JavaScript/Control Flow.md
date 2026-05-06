---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Types]]"
  - "[[Functions]]"
---
# Control Flow

Conditionals, loops, and branching in JavaScript.

## if / else

```js
if (score >= 90) {
  grade = 'A';
} else if (score >= 80) {
  grade = 'B';
} else {
  grade = 'C';
}
```

### Ternary operator

```js
const label = isActive ? 'active' : 'inactive';

// Nested (keep shallow)
const grade = score >= 90 ? 'A' : score >= 80 ? 'B' : 'C';
```

### Short-circuit evaluation

```js
// && — return right side if left is truthy
const name = user && user.name;

// || — return right side if left is falsy
const name = user.name || 'Anonymous';

// ?? — return right side if left is null or undefined (not 0 or '')
const count = response.count ?? 0;
```

## switch

```js
switch (status) {
  case 'active':
    enable();
    break;              // required — fallthrough without it
  case 'pending':
  case 'review':        // two cases, same handler
    queue();
    break;
  default:
    disable();
}
```

`switch` uses strict equality (`===`).

## Loops

### for

```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// Reverse
for (let i = arr.length - 1; i >= 0; i--) {}
```

### while

```js
while (queue.length > 0) {
  process(queue.shift());
}
```

### do...while — always runs at least once

```js
do {
  input = prompt('Enter a number:');
} while (isNaN(input));
```

### for...of — iterates values

```js
for (const item of array) {}
for (const char of 'hello') {}
for (const [key, val] of map) {}
```

### for...in — iterates object keys

```js
for (const key in obj) {
  if (Object.hasOwn(obj, key)) {  // skip inherited properties
    console.log(key, obj[key]);
  }
}
```

### for...of with index (use entries)

```js
for (const [i, value] of arr.entries()) {
  console.log(i, value);
}
```

## break and continue

```js
for (const n of nums) {
  if (n === 0) break;      // exit loop entirely
  if (n < 0) continue;     // skip to next iteration
  process(n);
}
```

### Labeled break (for nested loops)

```js
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) break outer;  // exit both loops
  }
}
```

## Optional Chaining and Nullish Coalescing

```js
const city = user?.address?.city;         // undefined if any step is null/undefined
const name = user?.getName?.();           // call method if it exists
const first = arr?.[0];                   // safe index access

const label = user?.nickname ?? 'Guest';  // default if null/undefined
```

## Nullish Assignment

```js
let x = null;
x ??= 'default';    // assign only if null/undefined: x = 'default'

let y = 0;
y ||= 10;           // assign if falsy: y = 10 (0 is falsy)
y &&= y * 2;        // assign if truthy
```

## try / catch

```js
try {
  riskyOperation();
} catch (err) {
  handleError(err);
} finally {
  cleanup();
}
```

See [[Error Handling]] for full coverage.

## Tips

- Prefer `for...of` over index-based `for` loops for arrays
- Always use `break` in `switch` cases unless fallthrough is intentional
- Use `??` instead of `||` for defaults — `||` treats `0`, `''`, and `false` as missing
- `for...in` on arrays gives string indices and includes inherited properties — use `for...of` instead
- Optional chaining (`?.`) short-circuits — the rest of the chain is not evaluated if it hits null/undefined

## See Also

- [[Types]] — Truthy/falsy values, equality
- [[Error Handling]] — try/catch in depth
- [[Iterators]] — for...of and custom iterables
- [[Arrays]] — Array-specific iteration (forEach, map, etc.)
- [[JavaScript]]
