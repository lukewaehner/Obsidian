---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Components]]"
  - "[[State]]"
---
# Props

Props are how data flows from parent to child. They are read-only — a component never modifies its own props.

## Basic Props

```jsx
function Button({ label, onClick, disabled = false }) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}

// Usage
<Button label="Save" onClick={handleSave} />
<Button label="Delete" onClick={handleDelete} disabled={true} />
```

## Destructuring and Defaults

```jsx
// Default values in destructuring
function Avatar({ src, size = 40, alt = '' }) {
  return <img src={src} alt={alt} width={size} height={size} />;
}

// Rename during destructure
function Component({ className: customClass }) {
  return <div className={customClass} />;
}
```

## The children Prop

Anything between component tags becomes `children`:

```jsx
function Panel({ title, children }) {
  return (
    <div className="panel">
      <h3>{title}</h3>
      <div className="panel-body">{children}</div>
    </div>
  );
}

<Panel title="Stats">
  <p>Revenue: $12,000</p>
  <p>Orders: 420</p>
</Panel>
```

## Spreading Props

Pass through all props to a child element:

```jsx
function Input({ label, ...inputProps }) {
  return (
    <label>
      {label}
      <input {...inputProps} />
    </label>
  );
}

<Input label="Email" type="email" value={email} onChange={handleChange} />
```

## Prop Drilling Problem

When props need to pass through many layers of components that don't use them, it becomes prop drilling:

```jsx
// App → Page → Section → Widget — only Widget uses userId
function App() {
  return <Page userId={userId} />;
}
function Page({ userId }) {
  return <Section userId={userId} />;
}
function Section({ userId }) {
  return <Widget userId={userId} />;
}
```

Solutions:
- **Context** — for globally needed values (auth, theme, locale)
- **Component composition** — pass the already-rendered component down
- **State management** — Zustand, Redux for complex cases

## Passing Functions as Props

The most common pattern for child-to-parent communication:

```jsx
function SearchBox({ onSearch }) {
  const [query, setQuery] = useState('');

  return (
    <input
      value={query}
      onChange={e => setQuery(e.target.value)}
      onKeyDown={e => e.key === 'Enter' && onSearch(query)}
    />
  );
}

// Parent
<SearchBox onSearch={query => fetchResults(query)} />
```

## Render Props

Passing a function as a prop that returns JSX — a pattern for sharing behavior:

```jsx
function Mouse({ render }) {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return (
    <div onMouseMove={e => setPos({ x: e.clientX, y: e.clientY })}>
      {render(pos)}
    </div>
  );
}

<Mouse render={({ x, y }) => <p>Cursor: {x}, {y}</p>} />
```

In modern React, custom hooks usually replace render props.

## See Also

- [[Components]] — Component structure and JSX
- [[Context]] — Avoiding prop drilling for global data
- [[Custom Hooks]] — Sharing behavior without render props
- [[React]]
