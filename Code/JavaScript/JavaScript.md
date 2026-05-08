---
tags:
  - javascript
type: moc
---
# JavaScript

A dynamic, interpreted language for the web and beyond (Node.js, Deno, Bun).

## Core Language

- [[Variables]] — var, let, const, scope, hoisting
- [[Types]] — primitives, coercion, equality, truthy/falsy
- [[Functions]] — declarations, expressions, arrows, this, closures
- [[Control Flow]] — if/else, loops, switch, optional chaining
- [[Destructuring]] — arrays, objects, defaults, renaming, rest

## Data Structures

- [[Arrays]] — methods, spread, Array.from
- [[Objects]] — literals, shorthand, spread, Object methods
- [[Maps and Sets]] — Map, Set, WeakMap, WeakSet

## Object Oriented

- [[Classes]] — class syntax, inheritance, private fields, static
- [[Prototypes]] — prototype chain, Object.create

## Functional

- [[Closures]] — scope chain, module pattern, memoization
- [[Iterators]] — for...of, Symbol.iterator, generators

## Async

- [[Async]] — event loop, callbacks, Promises, async/await

## Ecosystem

- [[Modules]] — ES modules, CommonJS, dynamic import
- [[Error Handling]] — try/catch, custom errors, async errors
- [[Tooling]] — Node.js, npm, package.json, common tools

## Quick Reference

```js
// Variables
const x = 5;
let y = 10;

// Arrow function
const add = (a, b) => a + b;

// Destructuring
const { name, age } = person;
const [first, ...rest] = arr;

// Async/await
const data = await fetch(url).then(r => r.json());

// Optional chaining
const city = user?.address?.city ?? 'unknown';

// Array methods
const evens = nums.filter(n => n % 2 === 0);
const doubled = nums.map(n => n * 2);
const sum = nums.reduce((acc, n) => acc + n, 0);

// Spread
const merged = { ...defaults, ...overrides };
const combined = [...arr1, ...arr2];
```

## See Also

- [[React]] — UI framework built on JavaScript
- [[Code]] — Main programming hub

```folder-overview
id: b5f03421-30c2-4a9b-a740-52cb0c0005f3
folderPath: Code/JavaScript
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="b5f03421-30c2-4a9b-a740-52cb0c0005f3"></span>
- [[Code/JavaScript/Arrays.md|Arrays]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Async.md|Async]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Classes.md|Classes]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Closures.md|Closures]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Control Flow.md|Control Flow]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Destructuring.md|Destructuring]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Error Handling.md|Error Handling]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Functions.md|Functions]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Iterators.md|Iterators]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Maps and Sets.md|Maps and Sets]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Modules.md|Modules]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Objects.md|Objects]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Prototypes.md|Prototypes]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Tooling.md|Tooling]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Types.md|Types]] <span class="fv-link-list-item"></span>
- [[Code/JavaScript/Variables.md|Variables]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="b5f03421-30c2-4a9b-a740-52cb0c0005f3"></span>
