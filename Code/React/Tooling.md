---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[JavaScript/Tooling]]"
---
# Tooling

## Starting a Project

### Vite (recommended)

```bash
npm create vite@latest my-app -- --template react
cd my-app && npm install && npm run dev
```

Fast dev server with HMR, no config needed for most projects. Use `react-ts` template for TypeScript.

### Next.js

Full-stack React framework — server-side rendering, file-based routing, API routes, React Server Components. The default choice for production apps:

```bash
npx create-next-app@latest my-app
```

### Create React App

Deprecated and slow. Don't start new projects with it.

## TypeScript

TypeScript is standard in most teams. Key React types:

```tsx
// Component props
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
  children?: React.ReactNode;
}

function Button({ label, onClick, disabled = false }: ButtonProps) {
  return <button onClick={onClick} disabled={disabled}>{label}</button>;
}

// useState with explicit type
const [user, setUser] = useState<User | null>(null);

// useRef
const inputRef = useRef<HTMLInputElement>(null);

// Event types
function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
  setValue(e.target.value);
}
function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
  e.preventDefault();
}
function handleClick(e: React.MouseEvent<HTMLButtonElement>) { ... }

// forwardRef
const Input = React.forwardRef<HTMLInputElement, InputProps>((props, ref) => (
  <input ref={ref} {...props} />
));
```

## React DevTools

Browser extension (Chrome/Firefox). Two key tabs:

- **Components**: inspect the component tree, see props/state, highlight re-renders
- **Profiler**: record renders, see which components are slow

Essential for debugging re-render issues.

## Testing

### Vitest + React Testing Library

```bash
npm install -D vitest @testing-library/react @testing-library/user-event @testing-library/jest-dom jsdom
```

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';

describe('Counter', () => {
  it('increments on click', async () => {
    const user = userEvent.setup();
    render(<Counter />);

    expect(screen.getByText('Count: 0')).toBeInTheDocument();
    await user.click(screen.getByRole('button', { name: /increment/i }));
    expect(screen.getByText('Count: 1')).toBeInTheDocument();
  });
});
```

### Testing Library principles

- Query by role, label, text — not class names or IDs
- Test user behavior, not implementation details
- `getBy*` — throws if not found; `queryBy*` — returns null; `findBy*` — waits (async)

```jsx
// Preferred queries (in order)
screen.getByRole('button', { name: /submit/i })
screen.getByLabelText('Email')
screen.getByPlaceholderText('Search...')
screen.getByText('Hello')
screen.getByTestId('custom-id')  // last resort
```

### Mocking

```jsx
// Mock a module
vi.mock('../api', () => ({
  getUser: vi.fn().mockResolvedValue({ id: 1, name: 'Alice' }),
}));

// Mock React Query
const wrapper = ({ children }) => (
  <QueryClientProvider client={new QueryClient()}>
    {children}
  </QueryClientProvider>
);
render(<UserProfile id={1} />, { wrapper });
```

## ESLint and Prettier

```bash
npm install -D eslint eslint-plugin-react-hooks eslint-plugin-react-refresh prettier
```

Critical rules from `eslint-plugin-react-hooks`:
- `react-hooks/rules-of-hooks` — enforces hook rules (no conditional hooks)
- `react-hooks/exhaustive-deps` — warns about missing useEffect deps

## Storybook

Develop and document components in isolation:

```bash
npx storybook@latest init
```

```tsx
// Button.stories.tsx
export const Primary: Story = {
  args: { label: 'Click me', variant: 'primary' },
};
export const Disabled: Story = {
  args: { label: 'Click me', disabled: true },
};
```

## Common Libraries

| Need | Library |
|------|---------|
| Data fetching | React Query / SWR |
| Forms | React Hook Form |
| Global state | Zustand |
| Animation | Framer Motion |
| UI components | Radix UI, shadcn/ui, MUI |
| Date picking | React Day Picker |
| Virtual lists | react-window / TanStack Virtual |
| Error boundaries | react-error-boundary |
| Routing | React Router / TanStack Router |

## See Also

- [[JavaScript/Tooling]] — Node, npm, bundlers
- [[React]]
