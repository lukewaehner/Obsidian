---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[Props]]"
  - "[[Hooks]]"
  - "[[State]]"
---
# Context

Share values across a component tree without passing props at every level. Best for global data: auth, theme, locale, feature flags.

## Basic Setup

```jsx
import { createContext, useContext, useState } from 'react';

// 1. Create the context
const ThemeContext = createContext('light');  // default value

// 2. Provide it near the top of your tree
function App() {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Router />
    </ThemeContext.Provider>
  );
}

// 3. Consume it anywhere in the tree
function Button({ children }) {
  const { theme } = useContext(ThemeContext);
  return <button className={`btn-${theme}`}>{children}</button>;
}
```

## Custom Hook Pattern

Export a hook instead of the context directly — cleaner API and lets you add validation:

```jsx
// auth-context.jsx
const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = async (credentials) => {
    const user = await api.login(credentials);
    setUser(user);
  };

  const logout = () => {
    api.logout();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used inside AuthProvider');
  return ctx;
}

// Usage — no need to import AuthContext directly
const { user, login } = useAuth();
```

## What to Put in Context

Good candidates:
- Current user / auth state
- Theme (light/dark)
- Locale / i18n
- Feature flags
- Toast/notification system

Bad candidates:
- Data that only a few components need (use prop drilling or lift state instead)
- Frequently changing values (every context change re-renders all consumers)

## Performance: Splitting Contexts

When a context value changes, **all** consumers re-render. Split contexts by update frequency:

```jsx
// Don't put fast and slow-changing data in the same context
const UserContext = createContext(null);    // changes rarely
const CartContext = createContext(null);   // changes often

// Components that only care about user won't re-render on cart updates
```

## Performance: Memoizing the Value

```jsx
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  // Without useMemo, new object reference every render = all consumers re-render
  const value = useMemo(() => ({ theme, setTheme }), [theme]);

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}
```

## Multiple Providers

Nest providers at the root — order matters if one provider consumes another:

```jsx
function App() {
  return (
    <AuthProvider>
      <ThemeProvider>
        <LocaleProvider>
          <Router />
        </LocaleProvider>
      </ThemeProvider>
    </AuthProvider>
  );
}
```

## Context vs State Management Libraries

| Situation | Use |
|-----------|-----|
| Simple global state (auth, theme) | Context |
| Complex state with many transitions | Zustand or Redux |
| Server state (API data, caching) | React Query or SWR |
| Prop drilling 2-3 levels | Just pass props |

Context is not a state management solution on its own — it's a transport mechanism. For complex client state (shopping cart, multi-step forms), Zustand is simpler and avoids re-render issues.

## See Also

- [[Props]] — When prop drilling is fine
- [[State]] — Local state before reaching for context
- [[Custom Hooks]] — Encapsulating context logic
- [[React]]
