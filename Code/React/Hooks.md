---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[State]]"
  - "[[Effects]]"
  - "[[Performance]]"
  - "[[Custom Hooks]]"
---
# Hooks

React's built-in hooks. Hooks are functions that start with `use` and can only be called at the top level of a component or another hook.

## useReducer

An alternative to `useState` for complex state with multiple sub-values or update logic:

```jsx
import { useReducer } from 'react';

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return { count: 0 };
    default:
      throw new Error(`Unknown action: ${action.type}`);
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <>
      <p>{state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </>
  );
}
```

Prefer `useReducer` when:
- Multiple state values that change together
- Next state depends on previous state in complex ways
- State logic is complex enough to test separately

## useRef

Stores a mutable value that persists across renders without causing re-renders.

```jsx
import { useRef } from 'react';

// Access DOM nodes
function TextInput() {
  const inputRef = useRef(null);

  return (
    <>
      <input ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
    </>
  );
}

// Store mutable values (like instance variables)
function Timer() {
  const timerRef = useRef(null);

  function start() {
    timerRef.current = setInterval(tick, 1000);
  }

  function stop() {
    clearInterval(timerRef.current);
  }
}
```

`ref.current` is writable and doesn't trigger re-renders when changed.

## useCallback

Returns a memoized function — same function instance between renders unless deps change:

```jsx
import { useCallback } from 'react';

function Parent({ userId }) {
  const handleSave = useCallback((data) => {
    api.save(userId, data);
  }, [userId]);  // new function only when userId changes

  return <ExpensiveChild onSave={handleSave} />;
}
```

Mainly useful when passing callbacks to memoized child components (`React.memo`) or as dependencies of other hooks. Without it, a new function instance is created every render, breaking memoization.

## useMemo

Memoizes a computed value — only recalculates when deps change:

```jsx
import { useMemo } from 'react';

function ProductList({ products, filter }) {
  const filtered = useMemo(
    () => products.filter(p => p.category === filter),
    [products, filter]
  );

  return filtered.map(p => <Product key={p.id} {...p} />);
}
```

Don't reach for `useMemo` by default — it has overhead. Use it when:
- The computation is demonstrably slow (measured with the profiler)
- The result is used as a dep in another hook and identity matters

## useContext

Read a context value. See [[Context]] for the full pattern.

```jsx
const theme = useContext(ThemeContext);
```

## useId

Generate a stable unique ID that's consistent between server and client renders:

```jsx
import { useId } from 'react';

function FormField({ label }) {
  const id = useId();
  return (
    <>
      <label htmlFor={id}>{label}</label>
      <input id={id} />
    </>
  );
}
```

Don't use for list keys — use data IDs for that.

## useDeferredValue

Defer updating a part of the UI during a transition. The deferred value "lags behind" the current value, keeping the UI responsive while a slow render catches up:

```jsx
import { useDeferredValue } from 'react';

function SearchResults({ query }) {
  const deferredQuery = useDeferredValue(query);
  // deferredQuery may be stale — results re-render in the background
  return <Results query={deferredQuery} />;
}
```

## useTransition

Mark a state update as non-urgent — React can interrupt it to handle higher-priority updates:

```jsx
import { useTransition } from 'react';

function FilterBar({ onFilterChange }) {
  const [isPending, startTransition] = useTransition();

  function handleChange(filter) {
    startTransition(() => {
      onFilterChange(filter);  // treat this update as low priority
    });
  }

  return (
    <>
      {isPending && <Spinner />}
      <select onChange={e => handleChange(e.target.value)} />
    </>
  );
}
```

## Hook Rules

1. Only call hooks at the top level — never inside loops, conditions, or nested functions
2. Only call hooks from React functions — components or other hooks

The `eslint-plugin-react-hooks` package enforces both rules.

## See Also

- [[State]] — useState in depth
- [[Effects]] — useEffect and useLayoutEffect
- [[Context]] — useContext with providers
- [[Performance]] — memo, useMemo, useCallback together
- [[Custom Hooks]] — Building your own hooks
- [[React]]
