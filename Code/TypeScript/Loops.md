---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Array Functions]]"
date: 2026-09-14
---
# Loops

Three loop forms — and the course's recommendation to prefer array operators over all of them.

## The Three Forms

```ts
for (let i: number = 0; i < 10; i++) {
   console.log(i);
}

while (condition) {
  // statements
}

do {
  // statements
} while (condition)
```

## Entry-Level vs Exit-Level

- **Entry-level loops** — `for` and `while`. They evaluate the condition **before** executing any statements. A false condition on the first check means the body never runs.
- **Exit-level loop** — `do...while`. It **always executes the body at least once**, regardless of the condition, because the check happens at the bottom.

That's the whole distinction, and it's the only reason to pick `do...while`: you have work that must happen once before you can even evaluate whether to continue.

## Prefer Array Operators

> [!important] Course guidance
> When working with arrays, replace explicit loops with `.map()`, `.filter()`, `.reduce()`, and `.forEach()` where possible. These give clearer, more functional code.

```ts
// Instead of this:
const numbers = [1, 2, 3, 4, 5];
const doubled = [];
for (let i = 0; i < numbers.length; i++) {
    doubled.push(numbers[i] * 2);
}

// Prefer this:
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
```

The second version is shorter, but that's not the argument. The argument is that it has **no index variable to get wrong**, no mutable accumulator, and the name `map` tells a reader "same length, each element transformed" before they read the body. The `for` loop could be doing anything; you have to read it to find out.

Note also that the loop version declares `const doubled = []` — which infers `any[]`, the trap from [[Arrays]]. The `map` version can't have that bug.

See [[Array Functions]] for each operator.

## When an Explicit Loop Is Still Right

The recommendation is "where possible," not "always." Reach for a loop when:

- You need to **break early**. `for` has `break`; `forEach` does not (`some` / `find` are the functional equivalents).
- You're iterating something that isn't an array and isn't iterable.
- The body is genuinely imperative — I/O per item, or `await` per item in sequence.
- The loop isn't over a collection at all: `while (!done)`, retry loops, game loops.

## for...of and for...in

Two more forms worth knowing, though the tutorial doesn't cover them:

```ts
const nums = [10, 20, 30];

for (const n of nums) {      // for...of — iterates VALUES
  console.log(n);            // 10, 20, 30
}

for (const k in nums) {      // for...in — iterates KEYS (as strings!)
  console.log(k);            // "0", "1", "2"
}
```

`for...of` is the right index-free loop when you do need `break`. `for...in` over an array is almost always a bug — the keys are strings, and it picks up inherited enumerable properties.

## Tips
- `for (const x of arr)` over `for (let i = 0; ...)` whenever you don't need the index. No off-by-one surface.
- Use `let` not `var` for the loop counter. `var i` leaks out of the loop, and a closure created inside the body captures the *same* `i` — the classic "all my callbacks logged 10" bug. `let` gives a fresh binding per iteration.
- Don't mutate the array you're iterating. Build a new one.
- `await` inside a `for...of` runs sequentially; `await` inside `.forEach()` does **not** wait at all. Use `for...of` or `Promise.all` for async iteration.

## See Also
- [[Array Functions]] — the operators to prefer
- [[Control Flow]] — conditionals, `break` semantics in `switch`
- [[Arrays]] · [[Variables]]
- [[Tutorial - TypeScript Basics]]
