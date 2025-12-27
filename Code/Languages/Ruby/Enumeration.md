---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Arrays]]'
  - '[[Hashes]]'
  - '[[Code/Languages/Ruby/Loops]]'
---
# Enumeration

Methods for iterating over and transforming collections in Ruby.

## Overview

The `Enumerable` module provides a rich set of traversal and searching methods for collections. Arrays, hashes, ranges, and other collections include this module. These methods accept blocks to define behavior for each element.

## Basic Iteration

### Each

The fundamental iterator—executes a block for each element, returns the original collection:

```ruby
items = ['a', 'b', 'c']

items.each { |item| puts "Item: #{item}" }
# Item: a
# Item: b
# Item: c 
# => ["a", "b", "c"]
```

Multi-line blocks use `do`/`end`:

```ruby
[1, 2].each do |n|
  doubled = n * 2
  puts "Original: #{n}, Doubled: #{doubled}"
end
# Original: 1, Doubled: 2
# Original: 2, Doubled: 4
```

### Each on Hashes

With key and value:

```ruby
prices = { "apple" => 1, "banana" => 2 }

prices.each { |key, value| puts "#{key}: $#{value}" }
# apple: $1
# banana: $2
```

With pair (as array):

```ruby
prices.each { |pair| puts pair.inspect }
# ["apple", 1]
# ["banana", 2]
```

### Each With Index

Access both element and index:

```ruby
['a', 'b', 'c'].each_with_index { |item, i| puts "#{i}: #{item}" }
# 0: a
# 1: b
# 2: c
```

## Transforming Collections

### Map / Collect

Transform each element, return new array:

```ruby
[1, 2, 3].map { |n| n * 2 }     # => [2, 4, 6]
[1, 2, 3].collect { |n| n * 2 } # => [2, 4, 6] (alias)

# Symbol-to-proc shorthand
["hi", "bye"].map(&:upcase)     # => ["HI", "BYE"]
```

### Flat Map

Map and flatten one level:

```ruby
[[1, 2], [3, 4]].flat_map { |arr| arr.map { |n| n * 2 } }
# => [2, 4, 6, 8]
```

## Filtering Collections

### Select / Filter

Return elements where block is truthy:

```ruby
[1, 2, 3, 4, 5].select { |n| n.even? }  # => [2, 4]
[1, 2, 3, 4, 5].filter { |n| n > 3 }    # => [4, 5] (alias)
```

On hashes:

```ruby
responses = { 'Alice' => 'yes', 'Bob' => 'no', 'Carol' => 'yes' }
responses.select { |person, answer| answer == 'yes' }
# => {"Alice"=>"yes", "Carol"=>"yes"}
```

### Reject

Return elements where block is falsy (opposite of select):

```ruby
[1, 2, 3, 4, 5].reject { |n| n.even? }  # => [1, 3, 5]

items = ['a', 'b', 'c']
items.reject { |item| item == 'b' }     # => ['a', 'c']
```

### Find / Detect

Return first matching element:

```ruby
[1, 2, 3, 4].find { |n| n.even? }    # => 2
[1, 2, 3, 4].detect { |n| n > 10 }   # => nil (alias)
```

### Find All

Alias for `select`:

```ruby
[1, 2, 3, 4].find_all { |n| n.even? }  # => [2, 4]
```

## Reducing Collections

### Reduce / Inject

Combine elements into a single value:

```ruby
# Sum
[1, 2, 3, 4].reduce { |sum, n| sum + n }      # => 10
[1, 2, 3, 4].reduce(0) { |sum, n| sum + n }   # => 10 (with initial value)
[1, 2, 3, 4].reduce(:+)                        # => 10 (symbol shorthand)

# Product
[1, 2, 3, 4].inject(:*)                        # => 24

# Build a hash
[:a, :b, :c].reduce({}) { |hash, key| hash.merge(key => key.to_s) }
# => {:a=>"a", :b=>"b", :c=>"c"}
```

### Sum (Ruby 2.4+)

```ruby
[1, 2, 3, 4].sum          # => 10
[1, 2, 3, 4].sum(100)     # => 110 (with initial value)
```

## Checking Conditions

| Method | Description | Example |
|--------|-------------|---------|
| `any?` | At least one matches | `[1,2,3].any?(&:even?)` → `true` |
| `all?` | All match | `[2,4,6].all?(&:even?)` → `true` |
| `none?` | None match | `[1,3,5].none?(&:even?)` → `true` |
| `one?` | Exactly one matches | `[1,2,3].one?(&:even?)` → `true` |
| `include?` | Contains value | `[1,2,3].include?(2)` → `true` |
| `member?` | Alias for include? | `[1,2,3].member?(2)` → `true` |

## Sorting and Ordering

### Sort

```ruby
[3, 1, 4, 1, 5].sort                    # => [1, 1, 3, 4, 5]
[3, 1, 4, 1, 5].sort { |a, b| b <=> a } # => [5, 4, 3, 1, 1] (descending)
```

### Sort By

Sort by a derived value:

```ruby
words = ["apple", "pie", "banana"]
words.sort_by { |w| w.length }          # => ["pie", "apple", "banana"]
words.sort_by(&:length)                  # => same, shorthand
```

### Min, Max, Minmax

```ruby
[3, 1, 4].min                # => 1
[3, 1, 4].max                # => 4
[3, 1, 4].minmax             # => [1, 4]

["apple", "pie"].min_by(&:length)  # => "pie"
["apple", "pie"].max_by(&:length)  # => "apple"
```

## Grouping and Partitioning

### Group By

```ruby
[1, 2, 3, 4, 5, 6].group_by { |n| n % 3 }
# => {1=>[1, 4], 2=>[2, 5], 0=>[3, 6]}

words = ["ant", "bear", "cat"]
words.group_by { |w| w.length }
# => {3=>["ant", "cat"], 4=>["bear"]}
```

### Partition

Split into two arrays based on condition:

```ruby
[1, 2, 3, 4, 5].partition { |n| n.even? }
# => [[2, 4], [1, 3, 5]]

evens, odds = [1, 2, 3, 4, 5].partition(&:even?)
```

### Take and Drop

```ruby
[1, 2, 3, 4, 5].take(3)                    # => [1, 2, 3]
[1, 2, 3, 4, 5].drop(3)                    # => [4, 5]
[1, 2, 3, 4, 5].take_while { |n| n < 4 }   # => [1, 2, 3]
[1, 2, 3, 4, 5].drop_while { |n| n < 4 }   # => [4, 5]
```

## Key Concepts

### Bang Methods (In-Place Modification)

Most enumerable methods return new collections. Use `!` variants to modify in place:

```ruby
arr = [3, 1, 2]

arr.sort        # => [1, 2, 3] (new array)
arr             # => [3, 1, 2] (unchanged)

arr.sort!       # => [1, 2, 3]
arr             # => [1, 2, 3] (modified)
```

Works with `map!`, `select!`, `reject!`, etc.

### Saving Results

Non-bang methods require assignment:

```ruby
arr = [1, 2]
doubled = arr.map { |n| n * 2 }

arr      # => [1, 2] (original)
doubled  # => [2, 4] (new)
```

### Lazy Enumeration

For large or infinite collections, chain without processing all elements:

```ruby
(1..Float::INFINITY).lazy.select(&:even?).take(5).to_a
# => [2, 4, 6, 8, 10]
```

## Common Patterns

### Chaining Methods

```ruby
[1, 2, 3, 4, 5]
  .select(&:even?)
  .map { |n| n * 10 }
  .sum
# => 60
```

### Counting Occurrences

```ruby
letters = ['a', 'b', 'a', 'c', 'a', 'b']
letters.tally  # => {"a"=>3, "b"=>2, "c"=>1}

# Or with group_by + transform_values
letters.group_by(&:itself).transform_values(&:count)
```

### Finding Duplicates

```ruby
arr = [1, 2, 2, 3, 3, 3]
arr.tally.select { |k, v| v > 1 }.keys  # => [2, 3]
```

### Compact Map

Remove nils from mapping:

```ruby
[1, nil, 2, nil, 3].compact           # => [1, 2, 3]
["1", "a", "2"].map { |s| Integer(s) rescue nil }.compact  # => [1, 2]

# Ruby 2.7+ has filter_map
["1", "a", "2"].filter_map { |s| Integer(s) rescue nil }   # => [1, 2]
```

## Tips

- `each` returns the original collection; use `map` when you need transformed results
- Use symbol-to-proc (`&:method`) for simple transformations
- Prefer `select`/`reject` over `each` + conditional + push
- Chain methods rather than creating intermediate variables
- Use `reduce` with a block for complex accumulation, symbol for simple operations
- `find` returns `nil` if nothing matches; `select` returns an empty array
- Bang methods (`!`) raise errors on some collections if no changes are made
- Use `lazy` for memory-efficient processing of large collections

## See Also

- [[Arrays]] — Array-specific methods
- [[Hashes]] — Hash-specific enumeration
- [[Code/Languages/Ruby/Loops]] — Traditional loop constructs
- [[Ruby]]
