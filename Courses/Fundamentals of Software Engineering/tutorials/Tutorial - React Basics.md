---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - react
  - frontend
  - hooks
  - tutorial
type: tutorial
course: "[[Fundamentals of Software Engineering]]"
status: notes
---
# Tutorial — React Basics

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/tutorials/week3-react-basics>, retrieved 2026-09-24.
> Every section has a "View in sandbox" CodeSandbox link.

**Assigned in**: [[Module 05 - React Basics]]
**Needed for**: [[Activity 05 - Enhancing a TODO Tracker in React]] · [[Individual Project 2]]
**Prerequisite**: [[Tutorial - TypeScript Basics]] · Node 22+

This page covers what the lecture covers, plus `useEffect`, which the slides leave to
[[Module 06 - React Hooks]]. Only the parts that add to or differ from
[[Module 05 - React Basics|the lecture note]] are recorded here.

## Scaffolding a project

```sh
npm create vite@latest my-app -- --template react-ts   # rolldown-vite? No · install and start? Yes
cd my-app && npm install && npm run dev                # serves on localhost:5173
```

It does not create a git repo, so it's safe to run inside an existing one. The page later says
`npm start`. That script doesn't exist in a Vite project. Use `npm run dev`.

## Components

- A component is a **function** returning TSX. Class components are obsolete, so don't write
  them
- It returns **one** top-level element. Use `<>…</>` (a fragment) to group siblings without an
  extra `div`
- Use `className`, not `class`, because `class` is a reserved word in JS
- Each instance has its own independent state, props, and lifecycle

> [!warning] Skip the `defaultProps` pattern this tutorial teaches
> The tutorial sets `Header.defaultProps = { name: "World" }`. For function components that is
> **deprecated in React 18.3** (the version the course repo pins) and **removed in React 19**.
> Use a default in the destructured parameter:
> ```tsx
> function Header({ name = "World" }: { name?: string }) {
>   return <h1>Hello, {name}</h1>;
> }
> ```

## Events

- React event props are **camelCase** and take a **function**, not a string:
  `onClick={incrementCounter}`, not `onclick="incrementCounter()"`
- Event types come from React: `import { MouseEvent } from "react"`, then
  `(event: MouseEvent) => { event.preventDefault(); … }`

The tutorial's child-to-parent example has four children (`CounterContent`,
`IncrementCounterButton`, `DecrementCounterButton`, `CustomCounterButton`) around one parent that
holds `counter`. Every child receives either the value or a callback. None of them holds the
count. It is the lecture's "keep state in the parent" advice taken all the way.

## `useState` details

- The initial value is used **only on the first render**
- State updates are **asynchronous and may be batched**. Use the updater form
  `setCount(prev => prev + 1)` when the next value depends on the current one
- **Arrays**: `list.push(x); setList(list)` does **not** re-render, because it's the same
  reference. Copy first: `setList([...list, x])`

## `useEffect`

Runs code at a point in the component's lifecycle. It replaces the old class-component methods
(`componentDidMount`, `componentDidUpdate`, …).

| Dependency argument | Effect runs |
| --- | --- |
| *omitted* | after **every** render |
| `[]` | once, after the first render (mount) |
| `[count]` | after mount, then whenever `count` changes |
| returns a function | that function runs as **cleanup** before the next run and on unmount |

```tsx
useEffect(() => {
  console.log(`The current count is ${count}`);
  return () => console.log("cleaning up");
}, [count]);
```

> [!warning] Object dependencies are compared by reference
> ```tsx
> counter.count += counter.increment;
> setCounter(counter);                  // same object: no re-render, effect doesn't fire
>
> setCounter({ ...counter, count: counter.count + counter.increment });  // fires
> ```
> A dependency on the whole object (`[counter]`) fires when **any** field changes. To react to one
> field, depend on that field: `[counter.count]`.

The page lists more hooks to explore on your own: `useRef`, `useContext`, `useCallback`,
`useMemo`, `useReducer`.

## Questions / Gaps

## Related

- [[Module 05 - React Basics]]
- [[Module 06 - React Hooks]] — `useEffect` and custom hooks, formally
- [[Activity 05 - Enhancing a TODO Tracker in React]]
- [[Individual Project 2]]
- [[Tutorial - TypeScript Basics]]
