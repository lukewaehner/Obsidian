---
tags:
  - ruby
type: note
related:
  - "[[Ruby]]"
  - "[[Code/Languages/Ruby/Loops]]"
  - "[[Hashes]]"
---
# Arrays

Ordered, indexed collections of elements in Ruby.

## Overview

Arrays allow you to create and manipulate ordered collections of data. Each element has an index (starting at 0), and arrays can contain any combination of types—numbers, strings, objects, or even other arrays—though keeping similar types together is best practice.

## Creating Arrays

### Array Literals

```ruby
num_array = [1, 2, 3, 4, 5]
str_array = ["This", "is", "a", "small", "array"]
mixed = [1, "two", :three, [4, 5]]
```

### Array.new

```ruby
Array.new               # => []
Array.new(3)            # => [nil, nil, nil]
Array.new(3, 7)         # => [7, 7, 7]
Array.new(3, true)      # => [true, true, true]

# With a block (each element is unique)
Array.new(3) { |i| i * 2 }  # => [0, 2, 4]
Array.new(3) { [] }         # => [[], [], []] (three different arrays)
```

### Other Creation Methods

```ruby
%w[apple banana cherry]     # => ["apple", "banana", "cherry"]
%i[one two three]           # => [:one, :two, :three]
(1..5).to_a                 # => [1, 2, 3, 4, 5]
"a,b,c".split(",")          # => ["a", "b", "c"]
```

## Accessing Elements

### By Index

Zero-based indexing; negative indices count from the end:

```ruby
str_array = ["This", "is", "a", "small", "array"]

str_array[0]      # => "This"
str_array[1]      # => "is"
str_array[4]      # => "array"
str_array[-1]     # => "array" (last element)
str_array[-2]     # => "small" (second to last)
str_array[100]    # => nil (invalid index)
```

### Ranges and Slices

```ruby
arr = [0, 1, 2, 3, 4, 5]

arr[1..3]         # => [1, 2, 3] (inclusive range)
arr[1...3]        # => [1, 2]    (exclusive range)
arr[1, 3]         # => [1, 2, 3] (start index, length)
arr.slice(1, 3)   # => [1, 2, 3] (same as above)
```

### First and Last

```ruby
str_array = ["This", "is", "a", "small", "array"]

str_array.first       # => "This"
str_array.last        # => "array"
str_array.first(2)    # => ["This", "is"]
str_array.last(2)     # => ["small", "array"]
```

### Safe Access

```ruby
arr = [1, 2, 3]

arr.fetch(1)              # => 2
arr.fetch(100)            # => IndexError!
arr.fetch(100, "default") # => "default"
arr.fetch(100) { |i| "No index #{i}" }  # => "No index 100"
```

## Adding Elements

### To the End

```ruby
num_array = [1, 2]

num_array.push(3, 4)    # => [1, 2, 3, 4]
num_array << 5          # => [1, 2, 3, 4, 5]
num_array.append(6)     # => [1, 2, 3, 4, 5, 6]
```

### To the Beginning

```ruby
num_array = [2, 3, 4]

num_array.unshift(1)    # => [1, 2, 3, 4]
num_array.prepend(0)    # => [0, 1, 2, 3, 4]
```

### At a Specific Position

```ruby
arr = [1, 2, 4, 5]
arr.insert(2, 3)        # => [1, 2, 3, 4, 5] (insert at index 2)
arr.insert(2, :a, :b)   # => [1, 2, :a, :b, 3, 4, 5] (multiple values)
```

## Removing Elements

### From the End

```ruby
num_array = [1, 2, 3, 4, 5]

num_array.pop           # => 5 (returns removed element)
num_array               # => [1, 2, 3, 4]
num_array.pop(2)        # => [3, 4] (removes last 2)
num_array               # => [1, 2]
```

### From the Beginning

```ruby
num_array = [1, 2, 3, 4, 5]

num_array.shift         # => 1 (returns removed element)
num_array               # => [2, 3, 4, 5]
num_array.shift(2)      # => [2, 3] (removes first 2)
num_array               # => [4, 5]
```

### By Value

```ruby
arr = [1, 2, 3, 2, 4]

arr.delete(2)           # => 2 (removes ALL 2s)
arr                     # => [1, 3, 4]

arr = [1, 2, 3, 4, 5]
arr.delete_at(2)        # => 3 (removes at index 2)
arr                     # => [1, 2, 4, 5]
```

### By Condition

```ruby
arr = [1, 2, 3, 4, 5]

arr.delete_if { |n| n.even? }   # => [1, 3, 5]
arr.reject! { |n| n > 3 }       # => [1, 3]
arr.keep_if { |n| n.odd? }      # => [1, 3]
```

## Combining Arrays

### Concatenation

```ruby
a = [1, 2, 3]
b = [3, 4, 5]

a + b           # => [1, 2, 3, 3, 4, 5] (new array)
a.concat(b)     # => [1, 2, 3, 3, 4, 5] (modifies a)
[*a, *b]        # => [1, 2, 3, 3, 4, 5] (splat operator)
```

### Difference

```ruby
[1, 1, 1, 2, 2, 3, 4] - [1, 4]  # => [2, 2, 3]
```

### Intersection and Union

```ruby
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

a & b           # => [3, 4]        (intersection)
a | b           # => [1, 2, 3, 4, 5, 6] (union, removes duplicates)
```

## Common Methods

| Method | Description | Example |
|--------|-------------|---------|
| `empty?` | Check if array is empty | `[].empty?` → `true` |
| `length` / `size` | Number of elements | `[1,2,3].length` → `3` |
| `count` | Count matching elements | `[1,2,2,3].count(2)` → `2` |
| `include?` | Check if element exists | `[1,2,3].include?(2)` → `true` |
| `index` | Find index of element | `[1,2,3].index(2)` → `1` |
| `reverse` | Reverse order | `[1,2,3].reverse` → `[3,2,1]` |
| `sort` | Sort elements | `[3,1,2].sort` → `[1,2,3]` |
| `uniq` | Remove duplicates | `[1,1,2,2].uniq` → `[1,2]` |
| `flatten` | Flatten nested arrays | `[[1,2],[3]].flatten` → `[1,2,3]` |
| `compact` | Remove nil values | `[1,nil,2].compact` → `[1,2]` |
| `join` | Convert to string | `[1,2,3].join("-")` → `"1-2-3"` |
| `sample` | Random element(s) | `[1,2,3].sample` → `2` |
| `shuffle` | Randomize order | `[1,2,3].shuffle` → `[2,3,1]` |

## Key Concepts

### Mutating vs Non-Mutating

Most methods have a `!` variant that modifies in place:

```ruby
arr = [3, 1, 2]

arr.sort        # => [1, 2, 3] (returns new array)
arr             # => [3, 1, 2] (unchanged)

arr.sort!       # => [1, 2, 3] (modifies in place)
arr             # => [1, 2, 3] (changed)
```

### Arrays Are Objects

```ruby
arr = [1, 2, 3]
arr.class       # => Array
arr.methods     # => (very long list of available methods)
```

## Common Patterns

### Iterating

```ruby
[1, 2, 3].each { |n| puts n }
[1, 2, 3].each_with_index { |n, i| puts "#{i}: #{n}" }
[1, 2, 3].map { |n| n * 2 }     # => [2, 4, 6]
[1, 2, 3].select { |n| n > 1 }  # => [2, 3]
```

### Transforming

```ruby
# Map with symbol shorthand
["hi", "bye"].map(&:upcase)     # => ["HI", "BYE"]

# Reduce to single value
[1, 2, 3, 4].reduce(:+)         # => 10
```

### Checking Conditions

```ruby
[1, 2, 3].any? { |n| n > 2 }    # => true
[1, 2, 3].all? { |n| n > 0 }    # => true
[1, 2, 3].none? { |n| n > 5 }   # => true
[1, 2, 3].one? { |n| n > 2 }    # => true
```

### Destructuring

```ruby
first, *rest = [1, 2, 3, 4]
first   # => 1
rest    # => [2, 3, 4]

a, b, c = [1, 2, 3]
# a=1, b=2, c=3
```

## Tips

- Use `<<` (shovel) for appending single elements—it's faster and more idiomatic than `push`
- Prefer `first`/`last` over `[0]`/`[-1]` for readability
- Use `fetch` when you want to raise an error on missing indices
- Remember: `Array.new(3, [])` creates 3 references to the SAME array; use a block instead
- Use `%w[]` and `%i[]` for arrays of strings and symbols
- Check the [Array documentation](https://ruby-doc.org/core/Array.html) for 150+ methods

## See Also

- [[Code/Languages/Ruby/Loops]] — Iterating over arrays
- [[Hashes]] — Key-value collections
- [[Ruby]]
