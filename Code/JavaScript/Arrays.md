---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Destructuring]]"
  - "[[Iterators]]"
---
# Arrays

Creating, transforming, and consuming arrays in JavaScript.

## Creating Arrays

```js
const a = [1, 2, 3];
const b = new Array(3);         // [empty × 3] — avoid this
const c = Array.from({ length: 3 }, (_, i) => i);  // [0, 1, 2]
const d = Array.from('hello');  // ['h','e','l','l','o']
const e = Array.of(1, 2, 3);    // [1, 2, 3]
const f = [...a, ...b];         // spread to combine
```

## Accessing & Checking

```js
const arr = [10, 20, 30];

arr[0]           // 10
arr.at(-1)       // 30 — negative index from end
arr.length       // 3

arr.includes(20) // true
arr.indexOf(20)  // 1  (returns -1 if not found)
arr.find(n => n > 15)       // 20 — first match
arr.findIndex(n => n > 15)  // 1  — index of first match
Array.isArray(arr)           // true
```

## Mutating Methods

These modify the array in place:

```js
const arr = [1, 2, 3];

arr.push(4)          // add to end → [1,2,3,4], returns new length
arr.pop()            // remove from end → returns 4
arr.unshift(0)       // add to start → [0,1,2,3]
arr.shift()          // remove from start → returns 0
arr.reverse()        // reverse in place
arr.sort()           // sort in place (lexicographic by default!)
arr.sort((a, b) => a - b)   // numeric ascending
arr.sort((a, b) => b - a)   // numeric descending
arr.fill(0, 1, 3)    // fill indices 1–2 with 0
arr.splice(1, 2)     // remove 2 elements at index 1, returns them
arr.splice(1, 0, 'a', 'b')  // insert without removing
```

## Non-Mutating Methods

These return new arrays/values:

```js
const arr = [1, 2, 3, 4, 5];

arr.slice(1, 3)      // [2, 3] — end index exclusive
arr.slice(-2)        // [4, 5] — from end
arr.concat([6, 7])   // [1,2,3,4,5,6,7]
arr.join(' - ')      // '1 - 2 - 3 - 4 - 5'
arr.toReversed()     // new reversed array (ES2023)
arr.toSorted((a,b) => b - a) // new sorted array (ES2023)
```

## Iteration Methods

### forEach — side effects only, returns undefined

```js
[1, 2, 3].forEach(n => console.log(n));
```

### map — transform each element

```js
[1, 2, 3].map(n => n * 2)        // [2, 4, 6]
['a','b'].map((v, i) => `${i}:${v}`)  // ['0:a', '1:b']
```

### filter — keep elements matching predicate

```js
[1, 2, 3, 4].filter(n => n % 2 === 0)  // [2, 4]
users.filter(u => u.active)
```

### reduce — accumulate to single value

```js
[1, 2, 3, 4].reduce((acc, n) => acc + n, 0)   // 10
[1, 2, 3].reduce((acc, n) => [...acc, n * 2], [])  // [2,4,6]

// Without initial value — first element is accumulator
[1, 2, 3].reduce((a, b) => a + b)   // 6
```

### find / findIndex

```js
[1, 2, 3, 4].find(n => n > 2)       // 3 — first match or undefined
[1, 2, 3, 4].findIndex(n => n > 2)  // 2 — index or -1
```

### some / every

```js
[1, 2, 3].some(n => n > 2)   // true — at least one
[1, 2, 3].every(n => n > 0)  // true — all
```

### flat / flatMap

```js
[[1,2],[3,4]].flat()           // [1,2,3,4] — depth 1
[1,[2,[3]]].flat(Infinity)     // [1,2,3] — all levels

[[1,2],[3,4]].flatMap(a => a)  // [1,2,3,4]
[1, 2].flatMap(n => [n, n*2])  // [1,2,2,4] — map then flatten 1 level
```

## Spread and Combining

```js
const a = [1, 2];
const b = [3, 4];

[...a, ...b]          // [1, 2, 3, 4]
[0, ...a, ...b, 5]    // [0, 1, 2, 3, 4, 5]
[...a]                // shallow copy

// Pass array as arguments
Math.max(...[1, 5, 3])  // 5
```

## Destructuring

```js
const [first, second, ...rest] = [1, 2, 3, 4, 5];
// first=1, second=2, rest=[3,4,5]

const [a, , b] = [1, 2, 3];  // skip element: a=1, b=3

// Default values
const [x = 0, y = 0] = [10];  // x=10, y=0

// Swap
let p = 1, q = 2;
[p, q] = [q, p];
```

## Sorting

Default `sort()` is lexicographic (alphabetical), which breaks for numbers:

```js
[10, 9, 2, 1].sort()              // [1, 10, 2, 9] — wrong!
[10, 9, 2, 1].sort((a, b) => a - b)  // [1, 2, 9, 10] — correct

// Sort objects
users.sort((a, b) => a.name.localeCompare(b.name));
orders.sort((a, b) => b.date - a.date);  // descending by date
```

## Tips

- Prefer `map`/`filter`/`reduce` over loops for transformations
- `find` returns the element, `findIndex` returns the index — both return `undefined`/`-1` on miss
- `push` / `pop` are O(1), `shift` / `unshift` are O(n)
- Use `arr.at(-1)` instead of `arr[arr.length - 1]`
- Always provide a comparator to `sort()` when sorting numbers or objects
- Spread `[...arr]` for a shallow copy — `arr.slice()` works too

## See Also

- [[Destructuring]] — Array destructuring in depth
- [[Iterators]] — for...of, custom iterables
- [[Objects]] — Object equivalents
- [[JavaScript]]
