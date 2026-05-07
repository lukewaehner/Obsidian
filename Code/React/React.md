---
tags:
  - react
  - javascript
type: moc
related:
  - "[[Code]]"
  - "[[JavaScript]]"
---
# React

Component-based UI library. Renders components when state changes.

## Core Concepts

- [[Components]] — JSX, functional components, lists, fragments, portals
- [[Props]] — Passing data down, children, spread, prop drilling
- [[State]] — useState, functional updates, derived state, lifting state

## Hooks

- [[Effects]] — useEffect, cleanup, data fetching, what not to put in effects
- [[Hooks]] — useReducer, useRef, useCallback, useMemo, useId, useTransition
- [[Context]] — createContext, useContext, provider pattern, when to use
- [[Custom Hooks]] — Reusable logic: useDebounce, useLocalStorage, useFetch

## Patterns and Architecture

- [[Patterns]] — Compound components, HOC, controlled components, error boundaries
- [[Forms]] — Controlled vs uncontrolled, validation, React Hook Form
- [[Performance]] — React.memo, useMemo, useCallback, code splitting, profiling

## Production

- [[Data Fetching]] — React Query, SWR, optimistic updates, Suspense
- [[Routing]] — React Router v6, params, nested routes, protected routes
- [[Tooling]] — Vite, Next.js, TypeScript, testing, ESLint, common libraries

## Quick Reference

```jsx
// Component
function Card({ title, children }) {
  return <div className="card"><h2>{title}</h2>{children}</div>;
}

// State
const [count, setCount] = useState(0);
setCount(prev => prev + 1);  // use functional update when depending on prev

// Effect with cleanup
useEffect(() => {
  const sub = subscribe(userId);
  return () => sub.unsubscribe();
}, [userId]);

// Context
const ctx = useContext(MyContext);

// Memoization
const result = useMemo(() => expensive(data), [data]);
const fn = useCallback(() => doThing(id), [id]);
const MemoChild = React.memo(Child);
```
