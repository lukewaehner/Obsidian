---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Objects]]"
  - "[[Arrays]]"
---
# Maps and Sets

Key-value and unique-value collections with cleaner semantics than plain objects.

## Map

A key-value store where any value (including objects) can be a key.

```js
const m = new Map();

m.set('name', 'Alice');
m.set(42, 'the answer');
m.set({ id: 1 }, 'an object key');

m.get('name')    // 'Alice'
m.get(42)        // 'the answer'
m.has('name')    // true
m.size           // 3
m.delete('name')
m.clear()
```

### Creating from entries

```js
const m = new Map([
  ['a', 1],
  ['b', 2],
  ['c', 3],
]);
```

### Iterating

```js
for (const [key, value] of m) {}
for (const key of m.keys()) {}
for (const value of m.values()) {}

[...m.entries()]  // [['a',1], ['b',2], ...]
[...m.keys()]
[...m.values()]
```

### Map vs Object

| | Map | Object |
|---|---|---|
| Key types | Any value | Strings and Symbols only |
| Order | Insertion order guaranteed | Insertion order (mostly) |
| Size | `m.size` | `Object.keys(o).length` |
| Iteration | Directly iterable | Needs `Object.entries()` |
| Default keys | None | Inherits from prototype |

Use `Map` when:
- Keys are not strings (e.g., using objects or numbers as keys)
- You frequently add/remove keys
- You need to know the size easily
- Key ordering matters strictly

Use plain objects when:
- Keys are always strings
- You're representing a data record (e.g., a user)
- You need JSON serialization

## WeakMap

Like `Map`, but keys must be objects and are held weakly — they don't prevent garbage collection.

```js
const cache = new WeakMap();

function process(obj) {
  if (cache.has(obj)) return cache.get(obj);
  const result = heavyComputation(obj);
  cache.set(obj, result);
  return result;
}
// When obj is garbage collected, its cache entry disappears automatically
```

Not iterable. Use for caching or storing private data per object without memory leaks.

## Set

A collection of unique values. Duplicates are silently ignored.

```js
const s = new Set();
s.add(1);
s.add(2);
s.add(1);   // ignored — already exists

s.has(1)    // true
s.size      // 2
s.delete(1)
s.clear()

// From array (deduplication)
const unique = new Set([1, 2, 2, 3, 3, 3]);
// Set {1, 2, 3}
```

### Creating and converting

```js
const set = new Set([1, 2, 3]);

// Set → Array
[...set]             // [1, 2, 3]
Array.from(set)      // [1, 2, 3]

// Deduplicate array
const deduped = [...new Set(arr)];
```

### Iterating

```js
for (const value of set) {}
set.forEach(value => {});

[...set.values()]
[...set.entries()]  // [[v,v], [v,v]...] — key === value for Sets
```

### Set operations

JavaScript doesn't have built-in set operations, but they're easy to build:

```js
const a = new Set([1, 2, 3, 4]);
const b = new Set([3, 4, 5, 6]);

// Union
const union = new Set([...a, ...b]);         // {1,2,3,4,5,6}

// Intersection
const intersection = new Set([...a].filter(x => b.has(x)));  // {3,4}

// Difference
const difference = new Set([...a].filter(x => !b.has(x)));   // {1,2}
```

## WeakSet

Like `Set`, but holds objects weakly. Values must be objects.

```js
const seen = new WeakSet();

function processOnce(obj) {
  if (seen.has(obj)) return;
  seen.add(obj);
  doWork(obj);
}
```

Not iterable. Use for tracking object membership without preventing garbage collection.

## Tips

- Use `new Set(arr)` to deduplicate an array in one line
- `Map` preserves insertion order — useful when order of iteration matters
- `WeakMap` and `WeakSet` don't prevent garbage collection — ideal for caches and metadata attached to objects
- `Map.get(key)` returns `undefined` for missing keys — use `has` to distinguish missing from `undefined` values

## See Also

- [[Objects]] — Plain object as key-value store
- [[Arrays]] — Array deduplication and iteration
- [[Iterators]] — Iterating collections
- [[JavaScript]]
