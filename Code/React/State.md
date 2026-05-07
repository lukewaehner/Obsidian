---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Components]]"
  - "[[Effects]]"
  - "[[Hooks]]"
---
# State

Local component state that triggers re-renders when it changes.

## useState

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

`useState` returns `[currentValue, setter]`. Calling the setter schedules a re-render with the new value.

## Functional Updates

When the new state depends on the old state, pass a function to avoid stale closures:

```jsx
// Wrong — can use stale count in async/batched updates
setCount(count + 1);

// Correct — always gets the latest value
setCount(prev => prev + 1);

// Example: toggling
setIsOpen(prev => !prev);

// Example: adding to an array
setItems(prev => [...prev, newItem]);
```

Always use functional updates inside `setTimeout`, `setInterval`, or when calling the setter multiple times in one handler.

## Object and Array State

State is replaced, not merged (unlike `this.setState` in class components). Spread manually:

```jsx
const [user, setUser] = useState({ name: 'Alice', age: 30 });

// Wrong — loses other fields
setUser({ name: 'Bob' });

// Correct
setUser(prev => ({ ...prev, name: 'Bob' }));

// Arrays: always create a new array
const [items, setItems] = useState([]);

// Add
setItems(prev => [...prev, newItem]);

// Remove
setItems(prev => prev.filter(item => item.id !== id));

// Update one item
setItems(prev => prev.map(item =>
  item.id === id ? { ...item, done: true } : item
));
```

## State Initialization

Avoid expensive computations on every render:

```jsx
// Wrong — parseSavedData runs on every render
const [data, setData] = useState(parseSavedData(localStorage.getItem('data')));

// Correct — lazy initializer runs only once
const [data, setData] = useState(() => parseSavedData(localStorage.getItem('data')));
```

## Lifting State Up

When two sibling components need to share state, move the state to their closest common parent:

```jsx
function App() {
  const [selectedId, setSelectedId] = useState(null);

  return (
    <>
      <ItemList onSelect={setSelectedId} />
      <ItemDetail id={selectedId} />
    </>
  );
}
```

## Derived State

Don't store things in state that can be computed from existing state or props:

```jsx
// Wrong — fullName is redundant state
const [firstName, setFirstName] = useState('');
const [lastName, setLastName] = useState('');
const [fullName, setFullName] = useState('');

// Correct — derive it
const fullName = `${firstName} ${lastName}`;
```

If the derivation is expensive, use `useMemo` instead of state.

## State vs useRef

Use `useState` when the value should trigger re-renders. Use `useRef` when you need to store a value that persists across renders but doesn't affect the UI (like a timer ID, previous value, or DOM node).

## Batching

React batches multiple state updates in event handlers into a single re-render:

```jsx
function handleClick() {
  setCount(c => c + 1);  // doesn't re-render yet
  setFlag(f => !f);       // doesn't re-render yet
  // re-renders once here
}
```

In React 18+, batching also happens inside `setTimeout`, promises, and native event handlers.

## See Also

- [[Hooks]] — useReducer for complex state
- [[Effects]] — Side effects after state changes
- [[Performance]] — Avoiding unnecessary re-renders
- [[React]]
