---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Components]]"
  - "[[Props]]"
  - "[[Custom Hooks]]"
---
# Patterns

Common component and architecture patterns in React.

## Compound Components

A set of components that share implicit state through context — used together to build a flexible API:

```jsx
// The parent manages state; children opt into it via context
const AccordionContext = createContext(null);

function Accordion({ children }) {
  const [openIndex, setOpenIndex] = useState(null);
  return (
    <AccordionContext.Provider value={{ openIndex, setOpenIndex }}>
      <div>{children}</div>
    </AccordionContext.Provider>
  );
}

function AccordionItem({ index, title, children }) {
  const { openIndex, setOpenIndex } = useContext(AccordionContext);
  const isOpen = openIndex === index;
  return (
    <div>
      <button onClick={() => setOpenIndex(isOpen ? null : index)}>{title}</button>
      {isOpen && <div>{children}</div>}
    </div>
  );
}

Accordion.Item = AccordionItem;

// Usage
<Accordion>
  <Accordion.Item index={0} title="Section 1">Content 1</Accordion.Item>
  <Accordion.Item index={1} title="Section 2">Content 2</Accordion.Item>
</Accordion>
```

## Container / Presentational

Separate data fetching and business logic from rendering:

```jsx
// Container: knows about data, passes it down
function UserListContainer() {
  const { data, isLoading } = useQuery(['users'], fetchUsers);
  if (isLoading) return <Spinner />;
  return <UserList users={data} />;
}

// Presentational: pure rendering, easy to test and reuse
function UserList({ users }) {
  return (
    <ul>
      {users.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}
```

Custom hooks have largely replaced this pattern — the hook is the "container."

## Higher-Order Components (HOC)

A function that takes a component and returns a new enhanced component. Less common now — custom hooks are usually better.

```jsx
function withAuth(Component) {
  return function AuthenticatedComponent(props) {
    const { user } = useAuth();
    if (!user) return <Navigate to="/login" />;
    return <Component {...props} user={user} />;
  };
}

const ProtectedDashboard = withAuth(Dashboard);
```

## Controlled Component Pattern

Accept a value + onChange pair, letting the parent own the state. Mirrors how HTML inputs work:

```jsx
// Uncontrolled (owns state)
function UncontrolledSelect({ options }) {
  const [value, setValue] = useState(options[0].value);
  return <select value={value} onChange={e => setValue(e.target.value)}>...</select>;
}

// Controlled (parent owns state)
function Select({ value, onChange, options }) {
  return <select value={value} onChange={e => onChange(e.target.value)}>...</select>;
}

// Parent
<Select value={color} onChange={setColor} options={colorOptions} />
```

## Headless Components

Provide behavior and state with no UI — let the consumer render however they want:

```jsx
function useModal() {
  const [isOpen, setIsOpen] = useState(false);
  return {
    isOpen,
    open: () => setIsOpen(true),
    close: () => setIsOpen(false),
    toggle: () => setIsOpen(v => !v),
  };
}

// Consumer supplies all the UI
function App() {
  const modal = useModal();
  return (
    <>
      <button onClick={modal.open}>Open</button>
      {modal.isOpen && (
        <dialog>
          <button onClick={modal.close}>Close</button>
        </dialog>
      )}
    </>
  );
}
```

Libraries like Headless UI and Radix UI are built on this pattern.

## Error Boundaries

Catch rendering errors in child components and show a fallback. Must be a class component (no hook equivalent):

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, info) {
    logErrorToService(error, info.componentStack);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ?? <p>Something went wrong.</p>;
    }
    return this.props.children;
  }
}

// Usage
<ErrorBoundary fallback={<ErrorPage />}>
  <UserProfile />
</ErrorBoundary>
```

The `react-error-boundary` library provides a cleaner hook-friendly API.

## Slots Pattern

Pass named render areas as props — similar to Vue slots:

```jsx
function Layout({ header, sidebar, children }) {
  return (
    <div className="layout">
      <header>{header}</header>
      <aside>{sidebar}</aside>
      <main>{children}</main>
    </div>
  );
}

<Layout
  header={<NavBar />}
  sidebar={<FilterPanel />}
>
  <ProductList />
</Layout>
```

## See Also

- [[Components]] — Component basics and composition
- [[Custom Hooks]] — Extracting logic (replaces HOC/render props in most cases)
- [[Context]] — Used in compound components
- [[React]]
