---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Data Fetching]]"
  - "[[Components]]"
---
# Routing

React Router v6 is the standard client-side router. For server-rendered apps, use Next.js (its own router) instead.

## Setup

```bash
npm install react-router-dom
```

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/users" element={<UserList />} />
        <Route path="/users/:id" element={<UserDetail />} />
        <Route path="/settings/*" element={<Settings />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

## Navigation

```jsx
import { Link, NavLink, useNavigate } from 'react-router-dom';

// Declarative navigation
<Link to="/users">Users</Link>

// NavLink adds active class when the route matches
<NavLink to="/users" className={({ isActive }) => isActive ? 'active' : ''}>
  Users
</NavLink>

// Programmatic navigation
function LoginForm() {
  const navigate = useNavigate();

  async function handleSubmit(e) {
    await login(credentials);
    navigate('/dashboard');           // push
    navigate('/dashboard', { replace: true });  // replace (no back button)
    navigate(-1);                     // go back
  }
}
```

## Route Params

```jsx
import { useParams } from 'react-router-dom';

function UserDetail() {
  const { id } = useParams();  // from /users/:id
  // id is always a string, even if it looks like a number
  return <div>User {id}</div>;
}
```

## Search Params (Query String)

```jsx
import { useSearchParams } from 'react-router-dom';

function UserList() {
  const [searchParams, setSearchParams] = useSearchParams();
  const page = Number(searchParams.get('page') ?? 1);
  const filter = searchParams.get('status') ?? 'all';

  function goToPage(n) {
    setSearchParams(prev => {
      prev.set('page', String(n));
      return prev;
    });
  }

  return (
    <>
      <Filters value={filter} onChange={val => setSearchParams({ status: val })} />
      <Pagination page={page} onPageChange={goToPage} />
    </>
  );
}
```

## Nested Routes and Layout Routes

A layout route wraps child routes with shared UI (nav, sidebar):

```jsx
function App() {
  return (
    <Routes>
      <Route element={<AppLayout />}>          {/* layout with nav */}
        <Route path="/" element={<Home />} />
        <Route path="/users" element={<UserList />} />
        <Route path="/users/:id" element={<UserDetail />} />
      </Route>
      <Route path="/login" element={<Login />} />  {/* no layout */}
    </Routes>
  );
}

function AppLayout() {
  return (
    <>
      <NavBar />
      <main>
        <Outlet />   {/* renders the matched child route */}
      </main>
    </>
  );
}
```

## Protected Routes

```jsx
function ProtectedRoute({ children }) {
  const { user } = useAuth();
  const location = useLocation();

  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}

// Usage
<Route path="/dashboard" element={
  <ProtectedRoute>
    <Dashboard />
  </ProtectedRoute>
} />

// After login, redirect back to where they came from
function Login() {
  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from?.pathname ?? '/';

  async function handleLogin() {
    await login();
    navigate(from, { replace: true });
  }
}
```

## Outlet Context

Pass data from a layout route to its children:

```jsx
function UserLayout() {
  const { id } = useParams();
  const { data: user } = useQuery(['user', id], () => fetchUser(id));

  return (
    <>
      <UserHeader user={user} />
      <Outlet context={{ user }} />
    </>
  );
}

function UserPosts() {
  const { user } = useOutletContext();
  // ...
}
```

## Location State

Pass state between routes without putting it in the URL:

```jsx
// Navigate with state
navigate('/confirm', { state: { orderId: order.id } });

// Read on the other side
const { state } = useLocation();
console.log(state.orderId);
```

State is lost on page refresh — use URL params or query strings for data that should survive a refresh.

## See Also

- [[Data Fetching]] — Fetching based on route params
- [[Context]] — Auth context used in protected routes
- [[React]]
