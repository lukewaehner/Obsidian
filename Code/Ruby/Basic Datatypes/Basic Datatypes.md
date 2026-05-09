---
tags:
  - ruby
type: moc
---
# Basic Datatypes

Core data types in Ruby for representing primitive values.

## Overview

Ruby is dynamically typed—variables don't have fixed types, but values do. Everything in Ruby is an object, including basic types like integers and booleans.

## Types

- [[Strings]] — Mutable text sequences
- [[Symbols]] — Immutable identifiers
- [[Booleans]] — True, false, and nil

## Numbers

Ruby has several numeric types:

```ruby
# Integer (arbitrary precision)
42
1_000_000      # Underscores for readability

# Float (double precision)
3.14
2.5e6          # Scientific notation

# Rational (exact fractions)
Rational(1, 3) # => (1/3)
1/3r           # => (1/3)

# Complex
Complex(2, 3)  # => (2+3i)
2 + 3i         # => (2+3i)
```

## Type Checking

```ruby
42.class           # => Integer
3.14.class         # => Float
"hello".class      # => String
:symbol.class      # => Symbol
true.class         # => TrueClass
nil.class          # => NilClass

# Check type
42.is_a?(Integer)  # => true
42.is_a?(Numeric)  # => true (parent class)
```

## Type Conversion

```ruby
# To String
42.to_s            # => "42"
3.14.to_s          # => "3.14"

# To Integer
"42".to_i          # => 42
3.9.to_i           # => 3 (truncates)

# To Float
"3.14".to_f        # => 3.14
42.to_f            # => 42.0

# To Symbol
"name".to_sym      # => :name

# To Array
"a,b,c".split(",") # => ["a", "b", "c"]
(1..3).to_a        # => [1, 2, 3]
```

## Quick Reference

| Type | Example | Mutable | Use Case |
|------|---------|---------|----------|
| Integer | `42` | No | Whole numbers |
| Float | `3.14` | No | Decimal numbers |
| String | `"hello"` | Yes | Text content |
| Symbol | `:name` | No | Identifiers, hash keys |
| TrueClass | `true` | No | Boolean logic |
| FalseClass | `false` | No | Boolean logic |
| NilClass | `nil` | No | Absence of value |

## See Also

- [[Ruby]]

%% Begin Waypoint %%
- [[Booleans]]
- [[Strings]]
- [[Symbols]]

%% End Waypoint %%
