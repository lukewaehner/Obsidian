---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Arrays]]"
  - "[[Async]]"
---
# Iterators

The iteration protocol, for...of, generators, and async iteration.

## for...of vs for...in

```js
const arr = [10, 20, 30];

// for...of — iterates values (use this for arrays)
for (const value of arr) {
  console.log(value);  // 10, 20, 30
}

// for...in — iterates keys (use for objects)
for (const key in { a: 1, b: 2 }) {
  console.log(key);  // 'a', 'b'
}

// for...in on arrays gives string indices — avoid it for arrays
for (const i in arr) {
  console.log(i);   // '0', '1', '2' — strings, not numbers
}
```

## Built-in Iterables

Types that work with `for...of`:

```js
// Arrays
for (const x of [1, 2, 3]) {}

// Strings (iterates characters)
for (const ch of 'hello') { console.log(ch); }  // h, e, l, l, o

// Map
const m = new Map([['a', 1], ['b', 2]]);
for (const [key, val] of m) {}

// Set
for (const x of new Set([1, 2, 3])) {}

// Arguments object
function example() {
  for (const arg of arguments) {}
}

// NodeList (DOM)
for (const el of document.querySelectorAll('div')) {}
```

## The Iterator Protocol

An object is iterable if it has `Symbol.iterator` returning an iterator. An iterator has `next()` returning `{ value, done }`.

```js
// Manual iterator
const range = {
  from: 1,
  to: 5,
  [Symbol.iterator]() {
    let current = this.from;
    const last = this.to;
    return {
      next() {
        if (current <= last) {
          return { value: current++, done: false };
        }
        return { value: undefined, done: true };
      }
    };
  }
};

for (const n of range) {
  console.log(n);  // 1, 2, 3, 4, 5
}

[...range]  // [1, 2, 3, 4, 5]
```

## Generators

Functions that can pause and resume. `yield` pauses; `next()` resumes:

```js
function* count() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = count();
gen.next()  // { value: 1, done: false }
gen.next()  // { value: 2, done: false }
gen.next()  // { value: 3, done: false }
gen.next()  // { value: undefined, done: true }

// Generators are iterable
for (const n of count()) { console.log(n); }
[...count()]  // [1, 2, 3]
```

### Infinite sequences

```js
function* naturals() {
  let n = 1;
  while (true) {
    yield n++;
  }
}

function take(n, iter) {
  const result = [];
  for (const x of iter) {
    result.push(x);
    if (result.length === n) break;
  }
  return result;
}

take(5, naturals())  // [1, 2, 3, 4, 5]
```

### Delegating with yield*

```js
function* concat(...iterables) {
  for (const iter of iterables) {
    yield* iter;  // delegate to another iterable
  }
}

[...concat([1, 2], [3, 4], [5])]  // [1, 2, 3, 4, 5]
```

### Two-way communication

Generators can receive values via `next(value)`:

```js
function* accumulator() {
  let total = 0;
  while (true) {
    const n = yield total;  // yield current total, receive next number
    total += n;
  }
}

const acc = accumulator();
acc.next()    // { value: 0, done: false } — start it
acc.next(5)   // { value: 5, done: false }
acc.next(10)  // { value: 15, done: false }
```

## Async Iterators

For async data sources (streams, paginated APIs):

```js
async function* asyncRange(from, to) {
  for (let i = from; i <= to; i++) {
    await new Promise(r => setTimeout(r, 100));  // simulate async work
    yield i;
  }
}

// for await...of
for await (const n of asyncRange(1, 5)) {
  console.log(n);  // 1, 2, 3, 4, 5 — one per 100ms
}
```

### Paginated API example

```js
async function* fetchPages(url) {
  let nextUrl = url;
  while (nextUrl) {
    const res = await fetch(nextUrl);
    const data = await res.json();
    yield data.items;
    nextUrl = data.next;  // null when no more pages
  }
}

for await (const page of fetchPages('/api/items')) {
  for (const item of page) {
    process(item);
  }
}
```

## Tips

- Use `for...of` for arrays and iterables — cleaner than a `for` loop with an index
- Use `for...in` only for plain objects — it's confusing on arrays
- Generators are great for lazy sequences, infinite streams, and custom iterators
- `yield*` delegates to any iterable — including arrays and other generators
- Async generators + `for await...of` are the cleanest way to consume streaming data

## See Also

- [[Arrays]] — Array iteration methods
- [[Maps and Sets]] — Iterating Maps and Sets
- [[Async]] — Async/await and async iterators
- [[JavaScript]]
