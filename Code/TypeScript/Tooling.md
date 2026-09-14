---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Modules]]"
date: 2026-09-14
---
# Tooling

`tsconfig.json`, the naming conventions, and the linter/formatter setup — the rules that hold across a whole project rather than one file.

## tsconfig.json

**The presence of a `tsconfig.json` in a directory indicates that the directory is the root of a TypeScript project**, and sets the compiler's options.

The options split into two kinds.

### Options that control which errors get reported

| Option | Effect |
| --- | --- |
| `noImplicitAny` | Complains about certain uses of the `any` type — specifically, where TypeScript would have silently inferred it |
| `strict` | Sets a **lot** of other options, `noImplicitAny` among them |

`strict` is the one that matters. It's a bundle flag, and turning it on is the difference between TypeScript as a typechecker and TypeScript as documentation. What it includes:

```
strict: true
 ├── noImplicitAny                  unannotated parameters are an error
 ├── strictNullChecks               null and undefined are not assignable to T
 ├── strictFunctionTypes            parameter types checked contravariantly
 ├── strictBindCallApply            bind/call/apply are typechecked
 ├── strictPropertyInitialization   class fields must be initialized
 ├── noImplicitThis                 an untyped `this` is an error
 ├── useUnknownInCatchVariables     catch (e) gives unknown, not any
 └── alwaysStrict                   emit "use strict"
```

`strictNullChecks` is the highest-value one. Without it, `string` includes `null`, and every property access is a potential crash the compiler won't mention.

### Options that control what the compiler does

| Option | Effect |
| --- | --- |
| `noEmit` | Configures TypeScript to work **only as a type checker**. Disabled, the compiler outputs compiled `.js` files matching the `.ts` files |

`noEmit: true` is normal in a modern project: something else does the actual transpiling — Vite in the CS 4530 stack — and `tsc` is run purely as a check. Two tools, two jobs.

Other options you'll see:

| Option | Typical value | Why |
| --- | --- | --- |
| `target` | `ES2022` | which JavaScript version to emit |
| `module` | `ESNext` / `NodeNext` | which module system ([[Modules]]) |
| `moduleResolution` | `bundler` / `NodeNext` | how `import './x'` is resolved to a file |
| `jsx` | `react-jsx` | needed for `.tsx` in a React project |
| `lib` | `["ES2022", "DOM"]` | which built-in type declarations are available |
| `outDir` / `rootDir` | `dist` / `src` | where emitted output lands |
| `esModuleInterop` | `true` | interop between CommonJS and ES module imports |
| `sourceMap` | `true` | debuggable stack traces back to `.ts` |

A minimal example:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true
  },
  "include": ["src"]
}
```

There are many more options configuring TypeScript for different kinds of project — **a web server running directly in Node.js needs different configuration than a React project using JSX that runs in the browser.** That's why a monorepo typically has several `tsconfig.json` files (one per package, often extending a shared base) rather than one.

All options are documented in the [TSConfig Reference](https://www.typescriptlang.org/tsconfig/).

> [!important] Don't touch it in this course
> The tutorial: *"you should not need to manipulate TypeScript's configuration much in this class."* [[Individual Project 1]] states it harder — **you may not modify `tsconfig.json`.** If the compiler is complaining, the fix is in your code. Loosening the config to make an error disappear is the thing the rule exists to prevent.

## General Guidelines

The course's stated conventions:

### Naming

| Kind | Convention | Example |
| --- | --- | --- |
| File names | **kebab-case** | `game-board.ts` |
| Variables and functions | **camelCase** | `playerScore`, `getFullName` |
| Classes and constructor functions | **PascalCase** | `CheckingAccount` |

Types, interfaces, and enums also take PascalCase. Private properties start with `_` — see [[CS4530 Code Style Guide]].

### The rest

- **Prefer descriptive names over random letters.** `pendingOrders`, not `list2`.
- **Although typing is optional in TypeScript, it is not optional for this course.** Annotate parameters and return types.
- **Always use strict equality** — `===`, never `==`. See [[Control Flow]].
- **Use a linter**, as specified on the course website.
- **Use a prettifier**, if the linter doesn't already do it.
- **Use the general coding guidelines discussed in Week 1.**

## Linter and Formatter

Two different tools, often confused:

- **ESLint** — finds *problems*: unused variables, `==`, `any`, unreachable code, missing `await`. Some are auto-fixable.
- **Prettier** — settles *formatting*: quotes, semicolons, line width, indentation. No opinions about correctness.

The reason both are mandated is that they remove two categories of argument from code review entirely. Nobody debates indentation when Prettier decides it, and nobody has to remember to check for `==` when ESLint fails the build over it. Review time goes to logic instead.

```bash
npx tsc --noEmit        # typecheck only
npx eslint . --fix      # lint, auto-fixing what it can
npx prettier --write .  # format
```

Run these before committing. In CI they're a gate — see [[Tutorial - Development Environment Setup]] for the local setup.

## The Compile Pipeline

```
  your .ts files
        │
        ├──► tsc (noEmit)  ──► type errors    ← correctness
        ├──► eslint        ──► lint errors    ← problems
        ├──► prettier      ──► formatted      ← style
        │
        └──► Vite / esbuild ──► .js bundle    ← what actually runs
```

Worth internalizing: **the thing that runs your code does not typecheck it.** Vite strips the types and transpiles; it doesn't care whether they were correct. A type error will not stop your app from starting. That's why `tsc --noEmit` has to be a separate step in CI, and why "it runs" is not evidence that it compiles clean.

## Tips
- `strict: true` from day one on any new project. Retrofitting it onto an existing codebase is a migration.
- Configure your editor to format on save. Then formatting never appears in a diff.
- Keep formatting churn in its own commit, separate from logic — otherwise a reviewer can't find the real change.
- `tsc --noEmit --watch` in a spare terminal gives you errors as you type, independent of whatever the dev server thinks.
- Never add `// @ts-ignore` to silence something. `// @ts-expect-error` at least fails when the error goes away, so it can't rot silently.

## See Also
- [[Modules]] — `import` / `export`, which `module` and `moduleResolution` govern
- [[Types]] — `any` vs `unknown`, what `noImplicitAny` is guarding
- [[Control Flow]] — the strict equality rule
- [[Tutorial - Development Environment Setup]] — Node, VS Code, extensions
- [[CS4530 Code Style Guide]] — the linted ruleset for this course
- [[Tutorial - TypeScript Basics]]
