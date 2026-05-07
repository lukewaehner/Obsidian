---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Hooks]]"
  - "[[Effects]]"
  - "[[State]]"
---
# Custom Hooks

Extract stateful logic into reusable functions. A custom hook is any function that starts with `use` and calls other hooks inside.

## Why Custom Hooks

- Avoid duplicating logic across components
- Keep components focused on rendering
- Make logic testable in isolation

## Basic Pattern

```jsx
// Extract state + effect logic into a hook
function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handler = () => setWidth(window.innerWidth);
    window.addEventListener('resize', handler);
    return () => window.removeEventListener('resize', handler);
  }, []);

  return width;
}

// Clean component
function Banner() {
  const width = useWindowWidth();
  return <div>{width > 768 ? 'Desktop' : 'Mobile'}</div>;
}
```

## useLocalStorage

```jsx
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setStoredValue = (newValue) => {
    setValue(newValue);
    localStorage.setItem(key, JSON.stringify(newValue));
  };

  return [value, setStoredValue];
}

// Usage
const [theme, setTheme] = useLocalStorage('theme', 'light');
```

## useDebounce

```jsx
function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debounced;
}

// Usage — only fires search when user stops typing
function SearchBox() {
  const [query, setQuery] = useState('');
  const debouncedQuery = useDebounce(query, 400);

  useEffect(() => {
    if (debouncedQuery) fetchResults(debouncedQuery);
  }, [debouncedQuery]);
}
```

## useFetch

A minimal data-fetching hook (in real projects, use React Query instead):

```jsx
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;

    setLoading(true);
    fetch(url)
      .then(res => res.json())
      .then(data => { if (!cancelled) setData(data); })
      .catch(err => { if (!cancelled) setError(err); })
      .finally(() => { if (!cancelled) setLoading(false); });

    return () => { cancelled = true; };
  }, [url]);

  return { data, loading, error };
}

// Usage
const { data, loading, error } = useFetch('/api/users');
```

## usePrevious

Access the previous value of a prop or state:

```jsx
function usePrevious(value) {
  const ref = useRef();
  useEffect(() => {
    ref.current = value;
  });
  return ref.current;
}

// Usage
function Counter({ count }) {
  const prevCount = usePrevious(count);
  return <p>Changed from {prevCount} to {count}</p>;
}
```

## useMediaQuery

```jsx
function useMediaQuery(query) {
  const [matches, setMatches] = useState(
    () => window.matchMedia(query).matches
  );

  useEffect(() => {
    const mq = window.matchMedia(query);
    const handler = (e) => setMatches(e.matches);
    mq.addEventListener('change', handler);
    return () => mq.removeEventListener('change', handler);
  }, [query]);

  return matches;
}

const isMobile = useMediaQuery('(max-width: 768px)');
```

## useToggle

```jsx
function useToggle(initial = false) {
  const [value, setValue] = useState(initial);
  const toggle = useCallback(() => setValue(v => !v), []);
  return [value, toggle];
}

const [isOpen, toggleOpen] = useToggle();
```

## Rules for Custom Hooks

- Name must start with `use`
- Each component that calls the hook gets its own isolated state — hooks don't share state between components, just the logic
- Can accept parameters and return anything

## See Also

- [[Hooks]] — Built-in hooks reference
- [[Effects]] — useEffect patterns used in custom hooks
- [[Data Fetching]] — React Query for production data fetching
- [[React]]
