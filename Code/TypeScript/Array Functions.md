---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Arrays]]"
date: 2026-09-14
---
# Array Functions

`forEach`, `map`, `filter`, and `reduce`. Each iterates an array and performs a transformation or computation, taking a **callback** applied to every element.

These are the operators [[Loops|the course wants you to reach for before writing a loop]].

## At a Glance

| Method | Callback returns | Result | Length |
| --- | --- | --- | --- |
| `forEach` | ignored | `undefined` — nothing | n/a |
| `map` | the new element | new array | same as input |
| `filter` | `boolean` — keep? | new array | ≤ input |
| `reduce` | the new accumulator | a single value of any type | n/a |

None of the four mutates the original array.

## forEach

Calls a function for each element. **Unlike `map`, `filter`, and `reduce`, `forEach` does not return a value.**

```ts
array.forEach(callback[, thisObject]);
```

```ts
let num = [7, 8, 9];
num.forEach(function (value) {
  console.log(value);
});
```

Because it returns nothing, `forEach` is for **side effects only** — logging, writing to the DOM, pushing to something external. If you want a result, you want one of the other three.

```ts
const doubled = num.forEach(n => n * 2);   // doubled is undefined — a silent bug
```

## Map

Transforms the array according to the applied function and returns the updated array. Works on each element.

```ts
array.map(callback[, object])
```

- `callback` — a function producing an element of the new array from an element of the current one.
- `object` — object to use as `this` when executing `callback`.
- **Return type**: list

```ts
// Calculate cube of each element with the help of map.
function cube(n) {
   return n * n * n;
}
var arr = new Array(1, 2, 3, 4)
var newArr = arr.map(cube);
console.log(newArr)  // Output : [1,8,27,64]
```

Here a function called `cube` is created and then passed as a **callback** into `map()`. The callback doesn't have to be an inline arrow — any function of the right shape works.

Typed, in the style the course expects:

```ts
const cube = (n: number): number => n * n * n;
const cubes: number[] = [1, 2, 3, 4].map(cube);   // [1, 8, 27, 64]
```

`map` can change the element type: `string[]` in, `number[]` out.

```ts
const lengths: number[] = ['a', 'bb', 'ccc'].map(s => s.length);   // [1, 2, 3]
```

## Filter

Filters out elements on the basis of a condition and returns the result as a list. It pushes the current element into a new array when the callback returns `true`.

```ts
array.filter(callback[, object])
```

- `callback` — a function providing an element of the new array from an element of the current one.
- `object` — object to use as `this` when executing `callback`.
- **Return type**: list

```ts
// Calculate a list of even elements from an array
arr = new Array(1, 2, 3, 6, 5, 4)
var newArr = arr.filter(function(record) {
    return record % 2 == 0;
}); // output => [2,6,4]
```

Note the original preserves order: `[2, 6, 4]`, not `[2, 4, 6]`. `filter` removes, it never reorders.

Typed version, with the strict equality the course requires:

```ts
const evens: number[] = [1, 2, 3, 6, 5, 4].filter(n => n % 2 === 0);
```

## Reduce

Works on a callback for each element, reducing the result of that callback from one array element to the next — collapsing the array into a **single value**.

```ts
array.reduce(callback[, initialValue])
```

- `callback` — the function to execute on each value in the array.
- `initialValue` — the object to use as the first argument of the first call of the callback.

```ts
// To calculate product of every element of an array,
var arr = new Array (1,2,3,4,5)
var val = arr.reduce(function(a,b){
   return a*b;
});
// output => 120
```

With no `initialValue`, the first element becomes the starting accumulator and iteration begins at the second.

Accumulating a field out of a list of objects:

```ts
var employees = [
   { id: 20, name: 'Ajay', salary:30000 },
   { id: 24, name: 'Vijay', salary:35000 },
   { id: 56, name: 'Rahul', salary:32000 },
   { id: 88, name: 'Raman', salary:38000 }
];
var totalSalary = employees.reduce(function (total, record) {
   return total + record.salary;
}, 0);

// It will return the total salary of all the employees.
```

The `0` at the end is the `initialValue`, and it's doing real work: without it the first accumulator would be the *employee object*, and `employeeObject + 35000` is string concatenation.

> [!warning] Always pass `initialValue`
> Two reasons. It makes the accumulator's type explicit, and `[].reduce((a, b) => a + b)` on an **empty array with no initial value throws a TypeError**. With `0` it returns `0`.

The accumulator doesn't have to be the element type — that's what makes `reduce` the general case of all four:

```ts
// group names by first letter: string[] -> Record<string, string[]>
const byLetter = names.reduce<Record<string, string[]>>((acc, name) => {
  const key = name[0];
  acc[key] = [...(acc[key] ?? []), name];
  return acc;
}, {});
```

## Choosing Between Them

Ask what shape you want back:

- Same length, different values → **`map`**
- Fewer elements, same values → **`filter`**
- One value → **`reduce`**
- No value, just effects → **`forEach`**

They chain, and chaining is where they get good:

```ts
const total: number = employees
  .filter(e => e.salary > 31000)
  .map(e => e.salary)
  .reduce((sum, s) => sum + s, 0);
```

## Related Methods Worth Knowing

| Method | Does |
| --- | --- |
| `find` | first element matching a predicate, or `undefined` |
| `findIndex` | index of first match, or `-1` |
| `some` | `true` if **any** element matches |
| `every` | `true` if **all** elements match |
| `flatMap` | `map` then flatten one level |
| `sort` | **mutates in place** — copy first: `[...arr].sort()` |
| `includes` | `true` if the value is present |

`some` and `find` are the early-exit escape hatch `forEach` doesn't have.

## Tips
- Callbacks get `(element, index, array)`. Take only what you use — `arr.map((x, i) => ...)`.
- A `map` callback with a side effect and no meaningful return is a `forEach` written wrong.
- Don't `push` inside a `map`. If you're mutating an outer array, you wanted `filter` or `reduce`.
- `Number.parseInt` is the classic callback trap: `['1','2','3'].map(parseInt)` gives `[1, NaN, NaN]`, because `parseInt` receives the index as its radix. Wrap it: `.map(s => parseInt(s, 10))`.
- `sort` mutates and compares as **strings** by default — `[10, 9].sort()` is `[10, 9]`. Pass a comparator: `.sort((a, b) => a - b)`.

## See Also
- [[Arrays]] — the underlying type
- [[Loops]] — what these replace, and when a loop is still right
- [[Functions]] — arrow functions and callback typing
- [[Generics]] — how `map<T, U>` is typed
- [[Tutorial - TypeScript Basics]]
