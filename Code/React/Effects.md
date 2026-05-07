---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[State]]"
  - "[[Hooks]]"
  - "[[Data Fetching]]"
---
# Effects

`useEffect` runs code after the component renders — for syncing with external systems (APIs, subscriptions, DOM, timers).

## Basic Usage

```jsx
import { useEffect } from 'react';

useEffect(() => {
  // runs after render
  document.title = `You have ${count} messages`;
});
```

## Dependency Array

Controls when the effect re-runs:

```jsx
// No array — runs after every render
useEffect(() => { ... });

// Empty array — runs once after initial mount
useEffect(() => { ... }, []);

// With deps — runs when count or userId changes
useEffect(() => { ... }, [count, userId]);
```

The linter (`eslint-plugin-react-hooks`) will warn if you use a value inside the effect but omit it from deps. Don't ignore these warnings — they indicate stale closure bugs.

## Cleanup

Return a function to clean up subscriptions, timers, or event listeners:

```jsx
useEffect(() => {
  const timer = setInterval(() => {
    setTime(Date.now());
  }, 1000);

  return () => clearInterval(timer);  // cleanup on unmount or before re-run
}, []);

// Event listeners
useEffect(() => {
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);

// WebSocket
useEffect(() => {
  const ws = new WebSocket(url);
  ws.onmessage = handleMessage;
  return () => ws.close();
}, [url]);
```

Without cleanup, you get memory leaks or duplicate subscriptions.

## Data Fetching in Effects

The basic pattern (with caveats):

```jsx
useEffect(() => {
  let cancelled = false;

  async function fetchData() {
    setLoading(true);
    try {
      const data = await api.getUser(userId);
      if (!cancelled) setUser(data);
    } catch (err) {
      if (!cancelled) setError(err.message);
    } finally {
      if (!cancelled) setLoading(false);
    }
  }

  fetchData();
  return () => { cancelled = true; };  // prevent setting state on unmounted component
}, [userId]);
```

The `cancelled` flag prevents race conditions when `userId` changes before the first fetch completes.

For anything beyond trivial fetching, use a library like React Query or SWR instead — they handle caching, deduplication, refetch-on-focus, and all the edge cases.

## Common Patterns

### Run once on mount
```jsx
useEffect(() => {
  analytics.pageView(path);
}, []);
```

### Sync with external store
```jsx
useEffect(() => {
  const unsubscribe = store.subscribe(() => setState(store.getState()));
  return unsubscribe;
}, []);
```

### Debounce a value
```jsx
useEffect(() => {
  const timer = setTimeout(() => {
    onSearch(query);
  }, 300);
  return () => clearTimeout(timer);
}, [query]);
```

### Scroll to top on route change
```jsx
useEffect(() => {
  window.scrollTo(0, 0);
}, [pathname]);
```

## What NOT to Put in Effects

- **State transformations** — compute derived state directly, not in an effect
- **User event handling** — put that in event handlers, not effects
- **React-to-React synchronization** — if A changing should update B, lift state or use a single state object

```jsx
// Wrong — effect to sync two state values
useEffect(() => {
  setFullName(`${firstName} ${lastName}`);
}, [firstName, lastName]);

// Correct — derive it
const fullName = `${firstName} ${lastName}`;
```

## useLayoutEffect

Fires synchronously after DOM mutations but before the browser paints. Use for reading/writing layout (measuring DOM nodes, synchronous animations). Prefer `useEffect` unless you see a flicker.

```jsx
useLayoutEffect(() => {
  // Read DOM dimensions here without flash
  const rect = ref.current.getBoundingClientRect();
  setHeight(rect.height);
}, []);
```

## See Also

- [[Data Fetching]] — Patterns for fetching with hooks and libraries
- [[Hooks]] — Other hooks (useCallback, useMemo) for effects with deps
- [[Custom Hooks]] — Extracting effects into reusable hooks
- [[React]]
