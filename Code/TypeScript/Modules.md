---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Tooling]]"
date: 2026-09-14
---
# Modules

**Each TypeScript file in a project is a separate JavaScript module.** By default, nothing defined in one module can be used in another.

- **`export`** makes variables and functions from a module visible outside it.
- **`import`** lets you use variables and functions exported by another module.

File-level privacy is the default, and it's the cheapest encapsulation available — a helper you don't export cannot be called, referenced, or depended on from anywhere else. Unlike [[Classes|`private`]], this one holds at runtime.

## Two Ways to Export

Put `export` before the declaration, or write a separate `export` statement:

```ts
// file1.ts

export interface Message {
  msg: string
}

export function add(x: number, y: number): number {
  return x + y;
}

function subtract(x: number, y: number): number {
  return x - y;
}

export const someVar: Message = { msg: 'Variables can be exported too.' };

function multiply(): void {
  throw new Error();
}

export { subtract };
```

Four things are exported (`Message`, `add`, `someVar`, `subtract`) and one is not: `multiply` is **private to `file1.ts`** and invisible to every other file in the project.

`subtract` shows the second form — declared normally, exported at the bottom. Useful when you want the public surface listed in one place.

## Importing

```ts
// file2.ts
import { add, someVar, subtract, type Message } from './file1.ts';

add(1, 2);
subtract(2, 1);
console.log(someVar);
const myMessage: Message = { msg: 'Hello' };
console.log(myMessage);
```

> [!important] Imported types need the `type` prefix
> `type Message` in the import list. The `type` keyword tells the compiler this import exists only for typechecking and should be **erased** from the emitted JavaScript.
>
> This matters because interfaces and type aliases have no runtime representation. Importing `Message` as a value would leave a runtime import of something that doesn't exist. `import type { Message }` also works for a whole type-only import.

## Default Exports

A module can have **at most one** default export, marked with `default` after `export`:

```ts
// file3.ts
export default function addOne(x: number): number {
  return x + 1;
}

export function addTwo(x: number): number {
  return x + 2;
}
```

A default export is imported **without curly braces**:

```ts
// file4.ts
import addOne from './file3.ts';
import { addTwo } from './file3.ts';

addOne(41);
addTwo(65);
```

The braces are the whole distinction: `{ addTwo }` names an export; a bare `addOne` takes the default, whatever it's called.

Both can be combined into one line:

```ts
// file4.ts
import addOne, { addTwo } from './file3.ts';

addOne(41);
addTwo(65);
```

**In React projects, the single React component exported from a file is usually a default export.** You'll see this throughout the CS 4530 codebase — `export default function GameBoard()`, imported as `import GameBoard from './game-board'`.

## Named vs Default

| | Named | Default |
| --- | --- | --- |
| How many per file | any number | at most one |
| Import syntax | `{ name }` | bare name |
| Renamed at import | `{ a as b }` | freely — no declared name to match |
| Refactor safety | rename propagates via the compiler | each importer picked its own name |
| Autocomplete on the module | yes | weaker |

**Prefer named exports.** The default's freedom to rename is the problem: three files can import the same thing under three names, and no tool can tell you they're the same. Reserve `default` for the convention that expects it — React components.

## Other Forms

```ts
import * as utils from './utils';        // namespace import — utils.add(1, 2)
export * from './helpers';               // re-export everything (barrel file)
export { add as sum } from './file1';    // re-export, renamed
const mod = await import('./heavy');     // dynamic import — lazy, returns a Promise
```

A **barrel** (`index.ts` that re-exports a folder) shortens import paths but can create cycles and defeat tree-shaking. Use it for a genuine public API boundary, not by habit.

## Circular Imports

`a.ts` imports `b.ts` which imports `a.ts`. The compiler tolerates it; the runtime may hand you `undefined` for a binding that hasn't been initialized yet, with a confusing error far from the cause.

The fix is almost never clever — it's that the two files share a concept that belongs in a third file both import.

## Tips
- Export the minimum. Anything not exported can be renamed or deleted without checking callers.
- `import type` for anything used only in annotations. Keeps the emitted JavaScript honest.
- Named exports by default; `export default` for React components.
- File names in **kebab-case** — `game-board.ts`, not `GameBoard.ts`. See [[CS4530 Code Style Guide]].
- An unused export is dead code the compiler can't warn you about, because it looks used from the module's perspective. Delete it.

## See Also
- [[Tooling]] — `tsconfig.json`, module resolution, the linter
- [[Interfaces]] · [[Type Aliases]] — the things needing `import type`
- [[Classes]] — the other encapsulation mechanism
- [[Tutorial - TypeScript Basics]]
