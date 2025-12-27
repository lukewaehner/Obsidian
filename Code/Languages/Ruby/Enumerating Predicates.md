---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Enumeration]]'
  - '[[Arrays]]'
  - '[[Booleans]]'
---
# Enumerating Predicates

Methods that test collections and return boolean values.

## Overview

Predicate methods return `true` or `false` based on conditions applied to collection elements. They answer questions like "does any element match?", "do all elements match?", or "is this value present?". These methods are part of the `Enumerable` module and work on arrays, hashes, ranges, and other collections.

## Quick Reference

| Method | Returns `true` when... | Example |
|--------|------------------------|---------|
| `include?` | Collection contains value | `[1,2,3].include?(2)` → `true` |
| `any?` | At least one element matches | `[1,2,3].any?(&:even?)` → `true` |
| `all?` | Every element matches | `[2,4,6].all?(&:even?)` → `true` |
| `none?` | No elements match | `[1,3,5].none?(&:even?)` → `true` |
| `one?` | Exactly one element matches | `[1,2,3].one?(&:even?)` → `true` |
| `empty?` | Collection has no elements | `[].empty?` → `true` |

## Checking for Presence

### include? / member?

Check if a specific value exists in the collection:

```ruby
numbers = [1, 2, 3, 4, 5]

numbers.include?(3)   # => true
numbers.include?(10)  # => false
numbers.member?(3)    # => true (alias)
```

On hashes, checks keys by default:

```ruby
prices = { apple: 1.0, banana: 0.5 }

prices.include?(:apple)  # => true
prices.key?(:apple)      # => true (more explicit)
prices.value?(1.0)       # => true (check values)
prices.has_value?(0.5)   # => true
```

On strings:

```ruby
"hello world".include?("world")  # => true
"hello world".include?("xyz")    # => false
```

## Conditional Predicates

### any?

Returns `true` if the block returns truthy for at least one element:

```ruby
numbers = [1, 2, 3, 4, 5]

numbers.any? { |n| n > 4 }      # => true (5 matches)
numbers.any? { |n| n > 10 }     # => false
numbers.any?(&:even?)           # => true (2, 4 match)
```

Without a block, checks if any element is truthy:

```ruby
[nil, false, true].any?   # => true
[nil, false, nil].any?    # => false
[].any?                   # => false
```

With a pattern (Ruby 2.5+):

```ruby
[1, 2, 3].any?(Integer)       # => true
["a", "b", 1].any?(String)    # => true
[1, 2, 3].any?(4..10)         # => false
```

### all?

Returns `true` if the block returns truthy for every element:

```ruby
numbers = [2, 4, 6, 8]

numbers.all? { |n| n.even? }   # => true
numbers.all? { |n| n < 10 }    # => true
numbers.all? { |n| n < 5 }     # => false (6, 8 fail)
numbers.all?(&:even?)          # => true
```

Without a block, checks if all elements are truthy:

```ruby
[1, true, "hi"].all?      # => true
[1, nil, "hi"].all?       # => false
[].all?                   # => true (vacuous truth)
```

With a pattern:

```ruby
[1, 2, 3].all?(Integer)       # => true
[1, 2, 3].all?(1..5)          # => true
["a", "b", 1].all?(String)    # => false
```

### none?

Returns `true` if the block returns falsy for every element (opposite of `any?`):

```ruby
numbers = [1, 3, 5, 7]

numbers.none? { |n| n.even? }  # => true
numbers.none? { |n| n > 10 }   # => true
numbers.none? { |n| n > 5 }    # => false (7 matches)
numbers.none?(&:even?)         # => true
```

Without a block, checks if no elements are truthy:

```ruby
[nil, false].none?        # => true
[nil, false, 1].none?     # => false
[].none?                  # => true
```

### one?

Returns `true` if the block returns truthy for exactly one element:

```ruby
numbers = [1, 2, 3, 4, 5]

numbers.one? { |n| n > 4 }     # => true (only 5)
numbers.one? { |n| n > 3 }     # => false (4 and 5)
numbers.one? { |n| n > 10 }    # => false (none)
numbers.one?(&:even?)          # => false (2 and 4)

[1, 2, 3].one? { |n| n == 2 }  # => true
```

Without a block:

```ruby
[nil, true, false].one?   # => true (only true)
[1, nil, nil].one?        # => true
[1, 2, nil].one?          # => false
```

## Emptiness Checks

### empty?

Returns `true` if collection has no elements:

```ruby
[].empty?                 # => true
[1, 2, 3].empty?          # => false
{}.empty?                 # => true
{ a: 1 }.empty?           # => false
"".empty?                 # => true
"hello".empty?            # => false
```

### Negation with any?

`any?` without a block is the opposite of `empty?`:

```ruby
arr = []
arr.empty?    # => true
arr.any?      # => false

arr = [1, 2]
arr.empty?    # => false
arr.any?      # => true
```

## Key Concepts

### Short-Circuit Evaluation

Predicates stop iterating as soon as the result is determined:

```ruby
# Stops at first match
[1, 2, 3, 4, 5].any? { |n| puts n; n > 2 }
# Prints: 1, 2, 3
# => true

# Stops at first failure
[2, 4, 5, 6, 8].all? { |n| puts n; n.even? }
# Prints: 2, 4, 5
# => false
```

### Truthy vs Falsy

Ruby predicates follow Ruby's truthiness rules—only `false` and `nil` are falsy:

```ruby
[0, "", []].all?          # => true (0, "", [] are truthy)
[1, false, "hi"].any?     # => true (1 is truthy)
[nil, false].none?        # => true
```

### Pattern Matching with ===

When passing an argument instead of a block, Ruby uses `===` for comparison:

```ruby
# Class check
[1, 2, 3].all?(Numeric)           # => true

# Range check
[1, 2, 3].all?(1..10)             # => true

# Regex check
["foo", "bar"].any?(/oo/)         # => true

# Proc check
is_positive = ->(n) { n > 0 }
[1, 2, 3].all?(is_positive)       # => true
```

## Common Patterns

### Validation

```ruby
def valid_scores?(scores)
  scores.all? { |s| s.between?(0, 100) }
end

valid_scores?([85, 92, 78])   # => true
valid_scores?([85, 105, 78])  # => false
```

### Finding Missing Data

```ruby
users = [
  { name: "Alice", email: "alice@example.com" },
  { name: "Bob", email: nil },
  { name: "Carol", email: "carol@example.com" }
]

users.any? { |u| u[:email].nil? }  # => true
users.all? { |u| u[:email] }       # => false
```

### Checking Array Overlap

```ruby
def arrays_overlap?(a, b)
  a.any? { |item| b.include?(item) }
end

arrays_overlap?([1, 2, 3], [3, 4, 5])  # => true
arrays_overlap?([1, 2], [3, 4])        # => false

# Or use set intersection
([1, 2, 3] & [3, 4, 5]).any?           # => true
```

### Guard Clauses

```ruby
def process_items(items)
  return [] if items.none?
  return items if items.all?(&:valid?)
  
  items.select(&:valid?)
end
```

### Combining Predicates

```ruby
numbers = [1, 2, 3, 4, 5]

# All positive AND at least one even
numbers.all?(&:positive?) && numbers.any?(&:even?)  # => true

# None negative AND none zero
numbers.none?(&:negative?) && numbers.none?(&:zero?)  # => true
```

## Tips

- Use `any?` without a block as a more readable alternative to `!empty?`
- `all?` returns `true` for empty collections (vacuous truth)—add an `any?` check if this matters
- Prefer symbol-to-proc (`&:even?`) for simple predicate checks
- Use pattern arguments (Ruby 2.5+) instead of blocks for type/range checks
- Remember short-circuit behavior when blocks have side effects
- `include?` uses `==` for comparison; for custom objects, ensure `==` is defined
- For large collections, consider `lazy` enumeration or breaking early with `find`

## See Also

- [[Enumeration]] — Full enumeration method reference
- [[Arrays]] — Array-specific methods
- [[Booleans]] — Truthiness in Ruby
- [[Ruby]]
