---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Async]]"
  - "[[Types]]"
---
# Error Handling

try/catch, error types, custom errors, and async error patterns.

## try / catch / finally

```js
try {
  const data = JSON.parse(input);   // might throw
  process(data);
} catch (err) {
  console.error(err.message);
} finally {
  cleanup();  // always runs — whether or not an error was thrown
}
```

`finally` runs even if the `try` or `catch` block returns:

```js
function example() {
  try {
    return 'try';
  } finally {
    console.log('finally runs!');  // logs before function returns
  }
}
```

## Error Object

```js
const err = new Error('something went wrong');
err.message   // 'something went wrong'
err.name      // 'Error'
err.stack     // stack trace as a string
```

## Built-in Error Types

```js
TypeError       // wrong type: null.property, calling non-function
RangeError      // value out of range: new Array(-1)
ReferenceError  // undefined variable
SyntaxError     // invalid code (usually parse-time, not catchable)
URIError        // malformed URI
EvalError       // rare, related to eval()
```

```js
try {
  null.property;
} catch (err) {
  err instanceof TypeError  // true
  err.name                  // 'TypeError'
}
```

## Custom Errors

Extend `Error` to create typed errors:

```js
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

class NetworkError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.name = 'NetworkError';
    this.statusCode = statusCode;
  }
}
```

```js
function validateAge(age) {
  if (typeof age !== 'number') {
    throw new ValidationError('Age must be a number', 'age');
  }
  if (age < 0 || age > 150) {
    throw new ValidationError('Age out of range', 'age');
  }
}

try {
  validateAge(-5);
} catch (err) {
  if (err instanceof ValidationError) {
    console.error(`Validation failed on field: ${err.field}`);
  } else {
    throw err;  // rethrow unknown errors
  }
}
```

## Throwing

You can throw anything, but always throw an `Error` instance (gives you a stack trace):

```js
throw new Error('message');           // always do this
throw new TypeError('wrong type');
throw new ValidationError('bad');

// Don't do these
throw 'string error';   // no stack trace
throw { code: 404 };    // no stack trace
```

## Async Error Handling

### Promise .catch

```js
fetch('/api/data')
  .then(res => res.json())
  .then(data => process(data))
  .catch(err => {
    console.error('Request failed:', err.message);
  });
```

### async/await try/catch

```js
async function fetchData() {
  try {
    const res = await fetch('/api/data');
    if (!res.ok) throw new NetworkError('Request failed', res.status);
    return await res.json();
  } catch (err) {
    if (err instanceof NetworkError) {
      console.error(`HTTP ${err.statusCode}: ${err.message}`);
    } else {
      throw err;  // rethrow unexpected errors
    }
    return null;
  }
}
```

### Handling errors from Promise.all

If any promise rejects, `Promise.all` rejects immediately:

```js
try {
  const [a, b] = await Promise.all([fetchA(), fetchB()]);
} catch (err) {
  // err is from whichever promise failed first
  // you don't know which one without additional info
}

// Use allSettled to handle each independently
const results = await Promise.allSettled([fetchA(), fetchB()]);
for (const result of results) {
  if (result.status === 'rejected') {
    console.error(result.reason);
  }
}
```

## Error Propagation

Re-throw errors you can't handle, so callers can deal with them:

```js
async function loadUser(id) {
  try {
    return await fetchUser(id);
  } catch (err) {
    if (err instanceof NetworkError && err.statusCode === 404) {
      return null;  // handle known case
    }
    throw err;  // let unknown errors propagate
  }
}
```

## Global Error Handling

Catch unhandled errors at the top level:

```js
// Browser
window.addEventListener('error', (event) => {
  console.error(event.error);
});

window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled promise rejection:', event.reason);
});

// Node.js
process.on('uncaughtException', (err) => {
  console.error(err);
  process.exit(1);  // must exit after uncaughtException
});

process.on('unhandledRejection', (reason) => {
  console.error('Unhandled rejection:', reason);
});
```

## Tips

- Always throw `Error` instances — string throws have no stack trace
- Catch specific error types and rethrow the rest
- `finally` is useful for cleanup (close connections, release locks)
- Never swallow errors silently with an empty `catch` block
- In async code, every `await` call can throw — wrap in try/catch or chain `.catch`

## See Also

- [[Async]] — Async error handling patterns
- [[Types]] — instanceof and type checking
- [[JavaScript]]
