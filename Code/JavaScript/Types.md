---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Variables]]"
---
# Types

JavaScript's type system: primitives, coercion, and equality.

## Primitive Types

Seven primitive types — stored by value, immutable:

```js
'hello'          // string
42               // number
9007199254740991n // bigint
true / false     // boolean
undefined        // undefined
null             // null (typeof null === 'object' — a historic bug)
Symbol('id')     // symbol — unique identifier
```

Everything else is an **object** (arrays, functions, dates, regex, etc.) — stored by reference.

## typeof

```js
typeof 'hello'     // 'string'
typeof 42          // 'number'
typeof true        // 'boolean'
typeof undefined   // 'undefined'
typeof null        // 'object'  ← the famous bug
typeof {}          // 'object'
typeof []          // 'object'
typeof function(){} // 'function'
typeof Symbol()    // 'symbol'
typeof 42n         // 'bigint'
```

To check for null: `value === null`
To check for array: `Array.isArray(value)`

## undefined vs null

```js
let x;          // x is undefined — declared but not assigned
let y = null;   // y is null — explicitly "no value"

undefined == null  // true  (loose equality)
undefined === null // false (strict equality)
```

Convention: use `null` to explicitly signal "no value." `undefined` means "not yet assigned."

## Truthy and Falsy

Six **falsy** values — everything else is truthy:

```js
false
0
-0
0n        // BigInt zero
''        // empty string
null
undefined
NaN
```

```js
// Common truthy surprises
Boolean([])     // true  — empty array is truthy
Boolean({})     // true  — empty object is truthy
Boolean('0')    // true  — non-empty string
Boolean(-1)     // true  — any non-zero number
```

## Equality

### Strict equality === (always use this)

Compares value AND type. No coercion.

```js
1 === 1       // true
1 === '1'     // false — different types
null === null // true
NaN === NaN   // false — NaN is never equal to itself
```

### Loose equality == (avoid)

Coerces types before comparing. The rules are non-obvious:

```js
1 == '1'        // true
0 == false      // true
0 == ''         // true
null == undefined // true
null == 0       // false
```

Use `===` everywhere. The only common exception: `x == null` catches both `null` and `undefined`.

### Checking for NaN

```js
NaN === NaN     // false — can't use ===
Number.isNaN(NaN)   // true — use this
isNaN('hello')      // true — global isNaN coerces first, avoid it
Object.is(NaN, NaN) // true
```

## Type Coercion

JavaScript coerces types automatically in many situations.

### String coercion (+ operator)

```js
'5' + 3    // '53' — number coerced to string
'5' - 3    // 2    — string coerced to number (- doesn't concat)
'5' * '3'  // 15
```

### Numeric coercion

```js
Number('42')    // 42
Number('')      // 0
Number(null)    // 0
Number(true)    // 1
Number(false)   // 0
Number(undefined) // NaN
Number('hello') // NaN
```

### Explicit conversion

```js
String(42)        // '42'
String(null)      // 'null'
Number('3.14')    // 3.14
parseInt('42px')  // 42
parseFloat('3.14abc') // 3.14
Boolean(0)        // false
Boolean('hi')     // true
```

## Numbers

JavaScript has one number type (64-bit float):

```js
0.1 + 0.2 === 0.3   // false — floating point
0.1 + 0.2            // 0.30000000000000004

// Safe integer range
Number.MAX_SAFE_INTEGER  // 9007199254740991 (2^53 - 1)
Number.MIN_SAFE_INTEGER  // -9007199254740991

// Use BigInt for large integers
const big = 9999999999999999999n

// Useful number methods
(3.14159).toFixed(2)   // '3.14'
Number.isInteger(3.0)  // true
Number.isFinite(1/0)   // false
```

## Symbols

Unique, non-string property keys. Primarily used for library/framework internals:

```js
const id = Symbol('id');
const id2 = Symbol('id');
id === id2  // false — every Symbol is unique

const obj = { [id]: 123 };
obj[id]  // 123

// Well-known symbols hook into language behavior
Symbol.iterator   // makes objects iterable
Symbol.toPrimitive // custom type conversion
```

## Tips

- Use `===` always — `==` coercion rules are not worth memorizing
- Check for null/undefined with `value == null` or `value === null`
- Use `Number.isNaN` not the global `isNaN`
- Use `Array.isArray` to test for arrays — `typeof` won't help
- `typeof null === 'object'` is a 25-year-old bug in the language — remember it

## See Also

- [[Variables]] — Declarations and scope
- [[Objects]] — Reference types
- [[JavaScript]]
