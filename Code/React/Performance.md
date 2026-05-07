---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Hooks]]"
  - "[[State]]"
  - "[[Components]]"
---
# Performance

React re-renders a component when its state or props change. This is usually fast and fine — optimize only after measuring a real problem.

## When React Re-renders

A component re-renders when:
1. Its own state changes
2. Its parent re-renders (even if props didn't change)
3. A context it consumes changes

By default, when a parent re-renders, all children re-render too, regardless of whether their props changed.

## React.memo

Wraps a component to skip re-renders if props haven't changed (shallow comparison):

```jsx
const ExpensiveList = React.memo(function ExpensiveList({ items }) {
  return items.map(item => <Item key={item.id} {...item} />);
});

// Now the parent can re-render without re-rendering ExpensiveList
// — as long as items hasn't changed
```

`React.memo` only helps if the parent re-renders frequently and the component is slow to render. If the child is fast, the memoization check costs more than just re-rendering.

## useMemo

Memoize an expensive computation:

```jsx
const sortedItems = useMemo(
  () => [...items].sort((a, b) => b.score - a.score),
  [items]
);
```

Also used to maintain referential stability for objects/arrays that are used as deps elsewhere:

```jsx
// Without useMemo: new array reference every render → triggers re-renders
// downstream
const filters = useMemo(
  () => ({ category, minPrice }),
  [category, minPrice]
);
```

## useCallback

Memoize a function so it keeps the same reference between renders:

```jsx
const handleDelete = useCallback((id) => {
  setItems(prev => prev.filter(item => item.id !== id));
}, []);  // stable reference — no deps that change

// Pass to a memoized child without breaking its memo
<MemoizedRow onDelete={handleDelete} />
```

Without `useCallback`, a new function instance is created each render, which breaks `React.memo` on children that receive it as a prop.

## The Three Together

```jsx
const Parent = ({ data }) => {
  // Stable function reference
  const handleClick = useCallback((id) => {
    setSelected(id);
  }, []);

  // Expensive computation memoized
  const processed = useMemo(
    () => expensiveTransform(data),
    [data]
  );

  return <Child items={processed} onClick={handleClick} />;
};

// Only re-renders if items or onClick reference changes
const Child = React.memo(({ items, onClick }) => {
  return items.map(item => (
    <button key={item.id} onClick={() => onClick(item.id)}>
      {item.label}
    </button>
  ));
});
```

## Code Splitting

Lazy-load components to split the bundle:

```jsx
import { lazy, Suspense } from 'react';

const AdminPanel = lazy(() => import('./AdminPanel'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      {isAdmin && <AdminPanel />}
    </Suspense>
  );
}
```

The `AdminPanel` bundle only loads when it's first rendered.

## List Virtualization

For very long lists (thousands of rows), only render what's visible using a library:

```jsx
import { FixedSizeList } from 'react-window';

function VirtualList({ items }) {
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {({ index, style }) => (
        <div style={style}>{items[index].name}</div>
      )}
    </FixedSizeList>
  );
}
```

## Profiling

Use the React DevTools Profiler to find what's slow before optimizing:

1. Open React DevTools > Profiler tab
2. Click record, interact with the UI, stop recording
3. Inspect which components rendered and how long they took
4. Look for components that re-render more than expected

## Pitfalls That Break Memoization

```jsx
// New object every render — breaks React.memo
<Child options={{ size: 'large' }} />
// Fix: useMemo or lift the object out of the component

// New function every render — breaks React.memo
<Child onClick={() => doThing(id)} />
// Fix: useCallback

// New array every render
<Child items={data.filter(x => x.active)} />
// Fix: useMemo
```

## When NOT to Optimize

- Most components are fast enough — don't add memo/useMemo/useCallback everywhere
- Each one adds code complexity and makes the component harder to read
- Memoization itself has a cost — it's only a win if the computation/render it saves is more expensive

Measure first with the profiler. Optimize the components that actually show up as bottlenecks.

## See Also

- [[Hooks]] — useMemo, useCallback, useTransition, useDeferredValue
- [[State]] — Batching, derived state (avoiding unnecessary state)
- [[Context]] — Splitting contexts to avoid unnecessary re-renders
- [[React]]
