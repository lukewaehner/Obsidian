---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Modules]]"
---
# Tooling

Node.js, npm, package.json, and the JavaScript ecosystem.

## Node.js

JavaScript runtime outside the browser. Built on V8 (Chrome's JS engine).

```bash
node --version         # check version
node script.js         # run a file
node                   # REPL (interactive prompt)
node -e "console.log('hello')"  # run inline code
```

### nvm — Node Version Manager

Manage multiple Node versions:

```bash
nvm install 20         # install Node 20
nvm use 20             # switch to Node 20
nvm alias default 20   # set default version
nvm ls                 # list installed versions
```

## npm — Package Manager

Comes with Node. Manages dependencies and scripts.

```bash
npm init               # create package.json (interactive)
npm init -y            # create package.json with defaults

npm install            # install all dependencies from package.json
npm install express    # add a dependency
npm install -D eslint  # add a dev dependency
npm uninstall express

npm update             # update packages
npm outdated           # show outdated packages
npm audit              # check for security vulnerabilities
npm audit fix          # auto-fix vulnerabilities
```

### Alternatives

```bash
pnpm install           # faster, disk-efficient (hard links)
yarn install           # Meta's package manager, similar to npm
bun install            # Bun runtime + package manager (fast)
```

## package.json

Every project has one:

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "start": "node src/index.js",
    "dev": "node --watch src/index.js",
    "build": "vite build",
    "test": "vitest",
    "lint": "eslint src/"
  },
  "dependencies": {
    "express": "^4.18.0"
  },
  "devDependencies": {
    "eslint": "^8.0.0",
    "vite": "^5.0.0",
    "vitest": "^1.0.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

Run scripts: `npm run dev`, `npm test` (no `run` needed for test/start).

### package-lock.json

Locks exact dependency versions for reproducible installs. Always commit this for applications.

## Bundlers

Transform and bundle source files for production. Tree-shake unused code, handle imports, optimize.

| Tool | Use case |
|------|----------|
| **Vite** | Modern apps — fast dev server, Rollup for production |
| **esbuild** | Extremely fast, great for tools/libraries |
| **Rollup** | Libraries — clean ESM output |
| **webpack** | Legacy, complex apps — highly configurable |

```bash
# Vite project
npm create vite@latest my-app -- --template vanilla
cd my-app && npm install && npm run dev
```

## TypeScript

JavaScript with static types. Compiles to plain JavaScript.

```bash
npm install -D typescript
npx tsc --init         # create tsconfig.json
npx tsc                # compile
npx tsc --watch        # watch mode

# Or use ts-node for direct execution
npm install -D ts-node
npx ts-node src/index.ts
```

```json
// tsconfig.json (minimal)
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "outDir": "dist"
  }
}
```

## Linting and Formatting

### ESLint — Linter

```bash
npm install -D eslint
npx eslint --init      # interactive setup
npx eslint src/        # lint directory
npx eslint src/ --fix  # auto-fix
```

### Prettier — Formatter

```bash
npm install -D prettier
npx prettier --write src/   # format in place
npx prettier --check src/   # check only (CI)
```

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

## Testing

```bash
# Vitest (recommended for new projects — fast, ESM-native)
npm install -D vitest
npx vitest             # watch mode
npx vitest run         # single run

# Jest (common in older projects)
npm install -D jest
npx jest
npx jest --watch
```

## Useful Node.js Built-ins

```js
// File system
import { readFile, writeFile, mkdir } from 'fs/promises';
const content = await readFile('file.txt', 'utf8');
await writeFile('out.txt', 'hello');

// Path
import { join, resolve, dirname, extname } from 'path';
join('src', 'index.js')        // 'src/index.js'
resolve('./src/index.js')      // absolute path

// Environment
process.env.NODE_ENV           // 'development' | 'production'
process.env.PORT ?? 3000
process.argv                   // command line arguments
process.cwd()                  // current working directory

// URL (ESM)
import { fileURLToPath } from 'url';
const __dirname = fileURLToPath(new URL('.', import.meta.url));
```

## Tips

- Use `"type": "module"` in package.json for ESM in Node — otherwise `.mjs` extension required
- Commit `package-lock.json` for apps, not for libraries
- Use `node --watch` (Node 18+) instead of nodemon for simple dev servers
- Run one-off package commands with `npx` without installing globally

## See Also

- [[Modules]] — ES modules and CommonJS
- [[JavaScript]]
