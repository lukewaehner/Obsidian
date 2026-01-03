---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Conditional Logic]]'
  - '[[Hashes]]'
  - '[[Arrays]]'
---
# Pattern Matching

Structural matching and deconstruction of data in Ruby 3+.

## Overview

Pattern matching allows you to match data against patterns and destructure it in one step. Introduced in Ruby 2.7 and stabilized in Ruby 3.0, it provides a powerful alternative to conditional logic for working with complex data structures. If the data conforms to the pattern, it matches and can be deconstructed into variables.

## Basic Syntax

### case/in vs case/when

```ruby
# Traditional case/when (uses ===)
grade = 'C'
case grade
when 'A' then puts 'Great'
when 'B' then puts 'Good'
when 'C' then puts 'Well Done'
else puts 'See me'
end

# Pattern matching with case/in
case grade
in 'A' then puts 'Great'
in 'B' then puts 'Good'
in 'C' then puts 'Well Done'
else puts 'See me'
end
```

### Return Values

Pattern matching expressions return values:

```ruby
grade = 'C'

result = case grade
  in 'A' then 1
  in 'B' then 2
  in 'C' then 3
  else 0
end

result  # => 3
```

### Rightward Assignment (=>)

For single-pattern matching when you know the structure:

```ruby
login = { username: 'alice', password: 'secret123' }

login => { username: username }
puts username  # => "alice"

# Equivalent to:
case login
in { username: username }
  puts username
end
```

## Pattern Types

### Value Pattern

Match against specific values using `===`:

```ruby
case 42
in 42 then :matched
end
# => :matched
```

### Type Pattern

Check object types:

```ruby
input = 3

case input
in String then 'input is a String'
in Integer then 'input is an Integer'
in Array then 'input is an Array'
end
# => "input is an Integer"
```

**Note:** Ruby evaluates `Integer === 3` (not `3 === Integer`), which is why this works.

### Variable Pattern

Bind matched values to variables:

```ruby
age = 15

case age
in a
  puts a
end
# => 15
```

**Warning:** Variable patterns always match and rebind:

```ruby
a = 5

case 1
in a
  a
end

a  # => 1 (variable was reassigned!)
```

### Pin Operator (^)

Match against an existing variable's value without rebinding:

```ruby
expected = 5

case 5
in ^expected then :match
end
# => :match

case 10
in ^expected then :match
else :no_match
end
# => :no_match
```

### As Pattern (=>)

Capture the matched value while also matching a pattern:

```ruby
case [1, 2, 3]
in [1, 2, _] => arr
  arr
end
# => [1, 2, 3]
```

### Alternative Pattern (|)

Match against multiple options:

```ruby
case 0
in 0 | 1 | 2
  :small_number
end
# => :small_number

case :red
in :red | :green | :blue
  :primary_color
end
# => :primary_color
```

### Guard Conditions (if/unless)

Add conditions to patterns:

```ruby
value = 10

case value
in n if n > 5
  :large
in n
  :small
end
# => :large

case [1, 2]
in [a, b] unless a == b
  :different
end
# => :different
```

## Array Patterns

### Basic Matching

```ruby
case [1, 2, 3]
in [1, 2, 3] then :exact_match
in [1, _, _] then :starts_with_one
end
# => :exact_match
```

### Type Checking Elements

```ruby
case [1, "hello", :symbol]
in [Integer, String, Symbol]
  :match
end
# => :match
```

### Underscore Wildcard

Match any value without binding:

```ruby
case [1, 2, 3, 4]
in [_, _, 3, 4]
  :match
end
# => :match
```

### Splat Operator (*)

Match variable-length arrays:

```ruby
# Match rest of elements
case [1, 2, 3, 4, 5]
in [1, 2, *rest]
  rest
end
# => [3, 4, 5]

# Match beginning and end
case [1, 2, 3, 4, 5, 6, 7]
in [first, *middle, last]
  { first: first, middle: middle, last: last }
end
# => {:first=>1, :middle=>[2, 3, 4, 5, 6], :last=>7}

# Ignore middle elements
case [1, 2, 3, 4, 5]
in [1, 2, *, 4, 5]
  :match
end
# => :match
```

### Variable Binding

```ruby
case [1, 2, 3, 4, 5]
in [1, 2, 3, a, b]
  "a=#{a}, b=#{b}"
end
# => "a=4, b=5"
```

### Nested Arrays

```ruby
case [1, 2, [3, 4]]
in [_, _, [3, 4]]
  :match
end
# => :match

# Capture nested elements
case [1, 2, [3, 4, 5]]
in [_, _, [3, *rest] => nested]
  { rest: rest, nested: nested }
end
# => {:rest=>[4, 5], :nested=>[3, 4, 5]}
```

### Brackets Optional

```ruby
case [1, 2, 3, 4]
in 1, 2, 3, 4
  :match
end
# => :match
```

## Hash Patterns

**Note:** Pattern matching only works with symbol keys, not string keys.

### Basic Matching

```ruby
case { a: 'apple', b: 'banana' }
in { a: 'apple', b: 'banana' }
  :exact_match
end
# => :exact_match
```

### Variable Binding

```ruby
# Explicit binding
case { a: 'apple', b: 'banana' }
in { a: a, b: b }
  "#{a} and #{b}"
end
# => "apple and banana"

# Shorthand (variable name matches key)
case { a: 'apple', b: 'banana' }
in { a:, b: }
  "#{a} and #{b}"
end
# => "apple and banana"
```

### Partial Matching

Hashes match even with extra keys:

```ruby
case { a: 1, b: 2, c: 3 }
in { a: 1 }
  :match  # Matches even though b and c exist
end
# => :match
```

### Exact Matching with **nil

```ruby
case { a: 1, b: 2 }
in { a: 1, **nil }
  :exact
else
  :has_extra_keys
end
# => :has_extra_keys

case { a: 1 }
in { a: 1, **nil }
  :exact
end
# => :exact
```

### Double Splat (**)

Capture remaining keys:

```ruby
case { a: 'ant', b: 'ball', c: 'cat' }
in { a: 'ant', **rest }
  rest
end
# => {:b=>"ball", :c=>"cat"}
```

### Capture Entire Hash

```ruby
case { a: 'ant', b: 'ball' }
in { a: 'ant' } => hash
  hash
end
# => {:a=>"ant", :b=>"ball"}
```

## Find Pattern (Ruby 3.0+)

Match a subsequence within an array:

```ruby
case [1, 2, 3, 4, 5]
in [*, 2, 3, *]
  :found_2_and_3
end
# => :found_2_and_3

# Capture before and after
case [1, 2, 3, 4, 5]
in [*pre, 3, *post]
  { before: pre, after: post }
end
# => {:before=>[1, 2], :after=>[4, 5]}
```

### Practical Example

```ruby
data = [
  { name: 'Alice', role: 'admin' },
  { name: 'Bob', role: 'user' },
  { name: 'Carol', role: 'user' }
]

name = 'Bob'

case data
in [*, { name: ^name, role: role }, *]
  "#{name} is a #{role}"
else
  "Not found"
end
# => "Bob is a user"
```

## Common Patterns

### Destructuring API Responses

```ruby
response = { status: 200, body: { user: { name: 'Alice', id: 42 } } }

case response
in { status: 200, body: { user: { name:, id: } } }
  "Found user #{name} with id #{id}"
in { status: 404 }
  "Not found"
in { status: status }
  "Error: #{status}"
end
# => "Found user Alice with id 42"
```

### Processing Command Arguments

```ruby
def process(args)
  case args
  in []
    "No arguments"
  in [single]
    "One argument: #{single}"
  in [first, second]
    "Two arguments: #{first}, #{second}"
  in [first, *rest]
    "First: #{first}, rest: #{rest}"
  end
end

process([])           # => "No arguments"
process([:a])         # => "One argument: a"
process([:a, :b])     # => "Two arguments: a, b"
process([:a, :b, :c]) # => "First: a, rest: [:b, :c]"
```

### Type-Based Dispatch

```ruby
def handle(event)
  case event
  in { type: 'click', x:, y: }
    "Click at (#{x}, #{y})"
  in { type: 'keypress', key: }
    "Key pressed: #{key}"
  in { type: 'scroll', direction: 'up' | 'down' => dir }
    "Scrolled #{dir}"
  else
    "Unknown event"
  end
end
```

### Validating Data Structures

```ruby
def valid_user?(data)
  case data
  in { name: String, age: Integer, email: String }
    true
  else
    false
  end
end

valid_user?({ name: "Alice", age: 30, email: "alice@example.com" })  # => true
valid_user?({ name: "Alice", age: "30" })  # => false
```

## Tips

- Use `case/in` for multiple pattern branches
- Use `=>` (rightward assignment) for single known structures
- Use `^` to match against existing variable values
- Hash patterns match subsets by default; use `**nil` for exact matching
- Pattern matching works best with symbol keys in hashes
- Guard conditions (`if`/`unless`) add flexibility to patterns
- The find pattern `[*, pattern, *]` searches within arrays
- NoMatchingPatternError is raised if no pattern matches and no `else` clause

## See Also

- [[Conditional Logic]] — Traditional case/when statements
- [[Hashes]] — Hash fundamentals
- [[Arrays]] — Array fundamentals
- [[Ruby]]
