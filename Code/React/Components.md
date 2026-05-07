---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Props]]"
  - "[[State]]"
---
# Components

The building block of React UIs. A component is a function that returns JSX.

## Functional Components

```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}</h1>;
}

// Arrow function style
const Greeting = ({ name }) => <h1>Hello, {name}</h1>;
```

Components must be capitalized — lowercase names are treated as HTML elements.

## JSX

JSX looks like HTML but compiles to `React.createElement` calls. Key differences:

```jsx
// class → className
<div className="container">

// style takes an object, camelCase properties
<div style={{ backgroundColor: 'red', fontSize: 16 }}>

// htmlFor instead of for
<label htmlFor="email">

// Self-close everything with no children
<input type="text" />
<img src="photo.png" alt="" />

// JavaScript in {}
<p>{user.name.toUpperCase()}</p>
<button onClick={() => handleClick(id)}>Save</button>
```

## Rendering Lists

Always provide a `key` prop when rendering arrays. Keys must be stable and unique among siblings.

```jsx
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

Never use array index as key if the list can reorder or have items added/removed — React uses keys to match old and new elements, and wrong keys cause subtle bugs.

## Conditional Rendering

```jsx
// Ternary
{isLoading ? <Spinner /> : <Content />}

// Short-circuit (render nothing or component)
{error && <ErrorMessage message={error} />}

// Early return
function Profile({ user }) {
  if (!user) return null;
  return <div>{user.name}</div>;
}
```

`0` renders as `"0"`, not nothing — use `!!count &&` or ternary if the value might be 0.

## Component Composition

Prefer composition over deeply nested prop drilling:

```jsx
function Card({ children, title }) {
  return (
    <div className="card">
      <h2>{title}</h2>
      {children}
    </div>
  );
}

// Usage
<Card title="Orders">
  <OrderList orders={orders} />
</Card>
```

## Fragments

Return multiple elements without a wrapping DOM node:

```jsx
function Row({ label, value }) {
  return (
    <>
      <dt>{label}</dt>
      <dd>{value}</dd>
    </>
  );
}

// Named fragment when you need a key
items.map(item => (
  <React.Fragment key={item.id}>
    <dt>{item.label}</dt>
    <dd>{item.value}</dd>
  </React.Fragment>
))
```

## Portals

Render a component into a different DOM node — useful for modals, tooltips, overlays:

```jsx
import { createPortal } from 'react-dom';

function Modal({ children }) {
  return createPortal(
    <div className="modal">{children}</div>,
    document.getElementById('modal-root')
  );
}
```

## See Also

- [[Props]] — Passing data to components
- [[State]] — Local component state
- [[React]]
