---
tags:
  - react
  - javascript
type: note
related:
  - "[[React]]"
  - "[[State]]"
  - "[[Hooks]]"
---
# Forms

## Controlled vs Uncontrolled

**Controlled**: React state is the source of truth. The input value is always in sync with state.

```jsx
function EmailInput() {
  const [email, setEmail] = useState('');

  return (
    <input
      type="email"
      value={email}
      onChange={e => setEmail(e.target.value)}
    />
  );
}
```

**Uncontrolled**: The DOM is the source of truth. Read the value with a ref when needed.

```jsx
function FileUpload() {
  const fileRef = useRef(null);

  function handleSubmit() {
    const file = fileRef.current.files[0];
    uploadFile(file);
  }

  return <input type="file" ref={fileRef} />;
}
```

Use controlled for most inputs. Use uncontrolled for file inputs (can't set value programmatically) and when you need to integrate with non-React DOM libraries.

## Basic Form

```jsx
function LoginForm() {
  const [form, setForm] = useState({ email: '', password: '' });
  const [error, setError] = useState('');

  function handleChange(e) {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  }

  async function handleSubmit(e) {
    e.preventDefault();  // prevent page reload
    setError('');
    try {
      await api.login(form);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="email"
        type="email"
        value={form.email}
        onChange={handleChange}
      />
      <input
        name="password"
        type="password"
        value={form.password}
        onChange={handleChange}
      />
      {error && <p className="error">{error}</p>}
      <button type="submit">Login</button>
    </form>
  );
}
```

## Checkboxes and Selects

```jsx
// Checkbox — use checked, not value
<input
  type="checkbox"
  checked={isActive}
  onChange={e => setIsActive(e.target.checked)}
/>

// Select
<select value={selectedColor} onChange={e => setSelectedColor(e.target.value)}>
  <option value="">Pick a color</option>
  <option value="red">Red</option>
  <option value="blue">Blue</option>
</select>

// Multi-select
<select
  multiple
  value={selected}  // array of values
  onChange={e => setSelected([...e.target.selectedOptions].map(o => o.value))}
>
```

## Validation

### On submit

```jsx
function validate(form) {
  const errors = {};
  if (!form.email) errors.email = 'Required';
  else if (!/\S+@\S+\.\S+/.test(form.email)) errors.email = 'Invalid email';
  if (!form.password) errors.password = 'Required';
  else if (form.password.length < 8) errors.password = 'Min 8 characters';
  return errors;
}

function handleSubmit(e) {
  e.preventDefault();
  const errors = validate(form);
  if (Object.keys(errors).length > 0) {
    setErrors(errors);
    return;
  }
  submitForm(form);
}
```

### On blur (validate when leaving a field)

```jsx
const [touched, setTouched] = useState({});

<input
  name="email"
  onBlur={() => setTouched(prev => ({ ...prev, email: true }))}
/>
{touched.email && errors.email && <span>{errors.email}</span>}
```

## useReducer for Complex Forms

For forms with many fields and complex validation, `useReducer` is cleaner than multiple `useState` calls:

```jsx
function formReducer(state, action) {
  switch (action.type) {
    case 'SET_FIELD':
      return { ...state, values: { ...state.values, [action.field]: action.value } };
    case 'SET_ERROR':
      return { ...state, errors: { ...state.errors, [action.field]: action.error } };
    case 'RESET':
      return initialState;
    default:
      return state;
  }
}
```

## Form Libraries

For non-trivial forms, use a library:

| Library | Best for |
|---------|----------|
| **React Hook Form** | Performance-focused, minimal re-renders, uncontrolled |
| **Formik** | Controlled, lots of built-in helpers, widely used |
| **TanStack Form** | Type-safe, flexible |

React Hook Form is currently the most popular for new projects:

```jsx
import { useForm } from 'react-hook-form';

function LoginForm() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = data => api.login(data);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register('email', { required: 'Required', pattern: { value: /\S+@\S+/, message: 'Invalid email' } })}
      />
      {errors.email && <span>{errors.email.message}</span>}
      <button type="submit">Login</button>
    </form>
  );
}
```

## See Also

- [[State]] — Managing form state with useState and useReducer
- [[Hooks]] — useRef for uncontrolled inputs
- [[React]]
