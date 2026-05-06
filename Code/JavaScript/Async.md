---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Error Handling]]"
  - "[[Functions]]"
---
# Async

Asynchronous programming in JavaScript: event loop, Promises, and async/await.

## The Event Loop

JavaScript is single-threaded. Async work is handled by offloading to the browser/Node runtime and resuming via callbacks when it's done.

```
Call Stack         Web APIs / Node APIs
    ↓                     ↓
[running code]     [setTimeout, fetch, fs.readFile...]
    ↓                     ↓
                    Task Queue / Microtask Queue
                          ↓
                    Event Loop picks up next task
```

- **Microtasks** (Promises) run before the next macrotask
- **Macrotasks** (setTimeout, setInterval, I/O) run one at a time

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
// Output: 1, 4, 3, 2
// Promise microtask runs before setTimeout macrotask
```

## Callbacks (Old Style)

```js
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) { console.error(err); return; }
  console.log(data);
});
```

Callbacks nest deeply ("callback hell") and error handling is inconsistent. Promises solve this.

## Promises

A Promise represents a value that will be available in the future. It's in one of three states: pending, fulfilled, or rejected.

```js
const p = new Promise((resolve, reject) => {
  setTimeout(() => resolve('done'), 1000);
  // or: reject(new Error('failed'))
});

p.then(value => console.log(value))   // 'done'
 .catch(err => console.error(err))
 .finally(() => console.log('always runs'));
```

### Chaining

`.then` returns a new Promise — you can chain them:

```js
fetch('/api/user')
  .then(res => res.json())          // returns a promise
  .then(user => user.name)          // transforms the value
  .then(name => console.log(name))
  .catch(err => console.error(err)); // catches any error in the chain
```

### Promise combinators

```js
// All resolve, or reject on first failure
Promise.all([p1, p2, p3]).then(([r1, r2, r3]) => { });

// Wait for all — get results regardless of success/failure
Promise.allSettled([p1, p2]).then(results => {
  results.forEach(r => {
    if (r.status === 'fulfilled') console.log(r.value);
    else console.log(r.reason);
  });
});

// First to resolve wins
Promise.race([p1, p2]).then(first => { });

// First to resolve successfully (ignores rejections)
Promise.any([p1, p2]).then(first => { });
```

### Creating resolved/rejected promises

```js
Promise.resolve(42)          // immediately fulfilled with 42
Promise.reject(new Error())  // immediately rejected
```

## async / await

Syntactic sugar over Promises — makes async code look synchronous:

```js
async function fetchUser(id) {
  const res = await fetch(`/api/users/${id}`);  // pauses here
  const user = await res.json();                 // pauses here
  return user;                                   // wraps in Promise.resolve
}

// async functions always return a Promise
fetchUser(1).then(user => console.log(user));

// Or await it from another async function
async function main() {
  const user = await fetchUser(1);
  console.log(user);
}
```

### Error handling with async/await

```js
// try/catch
async function fetchData() {
  try {
    const res = await fetch('/api/data');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error('Failed:', err.message);
    return null;
  }
}

// .catch on the returned Promise
fetchData().catch(console.error);
```

### Parallel execution

```js
// Sequential — slow (waits for each one)
const a = await fetchA();
const b = await fetchB();

// Parallel — fast (both start immediately)
const [a, b] = await Promise.all([fetchA(), fetchB()]);
```

### Async in loops

```js
// Sequential (each awaits before the next)
for (const id of ids) {
  const user = await fetchUser(id);
  console.log(user);
}

// Parallel (all start at once)
const users = await Promise.all(ids.map(id => fetchUser(id)));
```

Avoid `forEach` with async — it doesn't await:

```js
// WRONG — doesn't wait for any of them
ids.forEach(async (id) => {
  const user = await fetchUser(id);  // fire and forget
});

// CORRECT
for (const id of ids) { await fetchUser(id); }
// or
await Promise.all(ids.map(id => fetchUser(id)));
```

## Timers

```js
// setTimeout — run once after delay (ms)
const id = setTimeout(() => console.log('hello'), 1000);
clearTimeout(id);  // cancel it

// setInterval — run repeatedly
const id = setInterval(() => console.log('tick'), 1000);
clearInterval(id);  // cancel it

// Promise-based delay
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
await sleep(1000);  // pause for 1 second
```

## Tips

- `await` can only be used inside an `async` function (or top-level in ES modules)
- Forgetting `await` gives you a Promise object, not the value
- Use `Promise.all` for parallel work — sequential `await` is much slower
- Never use `forEach` with async callbacks — use `for...of` or `Promise.all`
- An unhandled Promise rejection crashes Node (adds a warning in browsers)

## See Also

- [[Error Handling]] — try/catch, custom errors
- [[Functions]] — async functions, callbacks
- [[Iterators]] — async iterators (for await...of)
- [[JavaScript]]
