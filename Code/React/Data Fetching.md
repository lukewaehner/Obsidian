---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Effects]]"
  - "[[State]]"
  - "[[Custom Hooks]]"
---
# Data Fetching

## The Problem with useEffect Fetching

Fetching in `useEffect` works but has a lot of rough edges you have to handle manually:

```jsx
// You need to handle all of this yourself:
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {
  let cancelled = false;
  setLoading(true);
  fetch('/api/users')
    .then(res => res.json())
    .then(data => { if (!cancelled) setData(data); })
    .catch(err => { if (!cancelled) setError(err); })
    .finally(() => { if (!cancelled) setLoading(false); });
  return () => { cancelled = true; };
}, []);
```

This doesn't handle: caching, deduplication, background refetch, stale data, pagination, optimistic updates, or refetch on window focus. Use a library for anything beyond one-off fetches.

## React Query (TanStack Query)

The standard for server state in React apps.

### Setup

```jsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router />
    </QueryClientProvider>
  );
}
```

### useQuery

```jsx
import { useQuery } from '@tanstack/react-query';

function UserProfile({ userId }) {
  const { data: user, isLoading, isError, error } = useQuery({
    queryKey: ['user', userId],  // cache key — refetch if userId changes
    queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json()),
  });

  if (isLoading) return <Spinner />;
  if (isError) return <Error message={error.message} />;

  return <div>{user.name}</div>;
}
```

Query keys uniquely identify the data. Same key = same cached result. Change a key value = new fetch.

```jsx
// List query
queryKey: ['users', { status: 'active', page: 1 }]

// Nested resource
queryKey: ['users', userId, 'posts']
```

### useMutation

```jsx
import { useMutation, useQueryClient } from '@tanstack/react-query';

function DeleteButton({ userId }) {
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: (id) => fetch(`/api/users/${id}`, { method: 'DELETE' }),
    onSuccess: () => {
      // Invalidate and refetch the users list
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });

  return (
    <button
      onClick={() => mutation.mutate(userId)}
      disabled={mutation.isPending}
    >
      {mutation.isPending ? 'Deleting...' : 'Delete'}
    </button>
  );
}
```

### Optimistic Updates

Update the UI immediately, roll back if the mutation fails:

```jsx
const mutation = useMutation({
  mutationFn: updateUser,
  onMutate: async (newUser) => {
    await queryClient.cancelQueries({ queryKey: ['user', newUser.id] });
    const previous = queryClient.getQueryData(['user', newUser.id]);
    queryClient.setQueryData(['user', newUser.id], newUser);
    return { previous };  // return context for rollback
  },
  onError: (err, newUser, context) => {
    queryClient.setQueryData(['user', newUser.id], context.previous);
  },
  onSettled: (data, err, newUser) => {
    queryClient.invalidateQueries({ queryKey: ['user', newUser.id] });
  },
});
```

### Pagination

```jsx
const { data, isPreviousData } = useQuery({
  queryKey: ['users', page],
  queryFn: () => fetchUsers(page),
  keepPreviousData: true,  // keep old data while new page loads
});
```

### Useful Options

```jsx
useQuery({
  queryKey: ['users'],
  queryFn: fetchUsers,
  staleTime: 5 * 60 * 1000,      // don't refetch for 5 minutes
  gcTime: 10 * 60 * 1000,         // keep in cache for 10 minutes
  refetchOnWindowFocus: false,    // default is true
  retry: 2,                        // retry failed requests 2 times
  enabled: !!userId,               // only run when userId is truthy
});
```

## SWR

A simpler alternative from Vercel, good for basic cases:

```jsx
import useSWR from 'swr';

const fetcher = url => fetch(url).then(r => r.json());

function UserProfile({ userId }) {
  const { data, error, isLoading } = useSWR(`/api/users/${userId}`, fetcher);

  if (isLoading) return <Spinner />;
  if (error) return <Error />;
  return <div>{data.name}</div>;
}
```

## Suspense for Data Fetching

React Suspense lets you declaratively handle loading states. Requires framework support (Next.js App Router) or React Query with `suspense: true`:

```jsx
// The component "suspends" while loading
function UserProfile({ userId }) {
  const { data } = useSuspenseQuery({
    queryKey: ['user', userId],
    queryFn: () => api.getUser(userId),
  });
  // No loading check needed — component only renders when data is ready
  return <div>{data.name}</div>;
}

// Parent handles the loading state
<Suspense fallback={<Spinner />}>
  <UserProfile userId={userId} />
</Suspense>
```

## Server State vs Client State

- **Server state** (API data): use React Query or SWR — they handle caching, sync, and background updates
- **Client state** (UI, local): use `useState`, `useReducer`, or Zustand

Don't put API data in `useState` and try to sync it — that's what React Query replaces.

## See Also

- [[Effects]] — useEffect for simple one-off fetches
- [[Custom Hooks]] — Wrapping fetch logic in hooks
- [[State]] — Managing loading/error state manually
- [[React]]
