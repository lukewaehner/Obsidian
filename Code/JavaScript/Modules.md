---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Closures]]"
  - "[[Tooling]]"
---
# Modules

Organizing code into reusable, encapsulated files.

## ES Modules (ESM)

The standard module system. Used in modern browsers and Node.js (`.mjs` or `"type": "module"` in package.json).

### Named exports

```js
// math.js
export const PI = 3.14159;

export function add(a, b) { return a + b; }

export class Calculator {
  multiply(a, b) { return a * b; }
}
```

```js
// main.js
import { PI, add, Calculator } from './math.js';
import { add as sum } from './math.js';   // rename on import
import * as math from './math.js';        // import all as namespace
```

### Default export

One per file — no name required at declaration:

```js
// greet.js
export default function greet(name) {
  return `Hello, ${name}`;
}

// or anonymous
export default (name) => `Hello, ${name}`;
```

```js
// main.js
import greet from './greet.js';       // any name — it's the default
import sayHi from './greet.js';       // also fine
```

### Mixed exports

```js
// utils.js
export const VERSION = '1.0';
export function helper() {}
export default class MyClass {}
```

```js
import MyClass, { VERSION, helper } from './utils.js';
```

### Re-exporting

Aggregate exports from multiple files in an index:

```js
// index.js
export { add, subtract } from './math.js';
export { default as greet } from './greet.js';
export * from './utils.js';
```

```js
import { add, greet } from './index.js';  // one import for everything
```

## CommonJS (CJS)

The original Node.js module system. Still common in older code and Node packages.

```js
// math.js
const PI = 3.14159;
function add(a, b) { return a + b; }

module.exports = { PI, add };
// or assign individually:
// module.exports.PI = PI;
// exports.add = add;  // exports is shorthand for module.exports
```

```js
// main.js
const { PI, add } = require('./math');
const math = require('./math');  // get entire exports object
```

### Default-style export in CJS

```js
// greet.js
module.exports = function greet(name) {
  return `Hello, ${name}`;
};
```

```js
const greet = require('./greet');
```

## ESM vs CJS

| | ESM | CommonJS |
|---|---|---|
| Syntax | `import` / `export` | `require` / `module.exports` |
| Loading | Static (analyzed at parse time) | Dynamic (runs at require time) |
| Top-level await | Yes | No |
| Tree-shaking | Yes | No |
| File extension | `.mjs` or `"type":"module"` | `.cjs` or default in Node |
| Browser support | Native | No (needs bundler) |

Use ESM for new projects. CJS is unavoidable when working with older Node packages.

## Dynamic Imports

Load modules lazily at runtime — returns a Promise:

```js
// Load only when needed
async function loadModule() {
  const { add } = await import('./math.js');
  return add(1, 2);
}

// Conditional loading
if (condition) {
  const module = await import('./heavy-feature.js');
  module.init();
}
```

Useful for code splitting — bundlers (Vite, webpack) split dynamic imports into separate chunks.

## Module Scope

Each module has its own scope — top-level variables are not global:

```js
// a.js
let secret = 'only in a.js';
export const public = 'shared';

// b.js
import { public } from './a.js';
// secret is inaccessible — module scope is private
```

## Tips

- Use named exports for libraries — they're easier to tree-shake and refactor
- Use default exports for the "main thing" a file provides (a class, a component)
- Avoid `export default` for plain objects — named exports are more discoverable
- ESM `import` paths need the extension in Node (`.js`) — bundlers handle this for you
- Circular imports work but are confusing — restructure if you encounter them

## See Also

- [[Closures]] — Module pattern before modules existed
- [[Tooling]] — Bundlers (Vite, webpack) and Node.js setup
- [[JavaScript]]
