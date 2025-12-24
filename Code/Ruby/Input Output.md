---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
---
# Printing

Output methods for displaying text and debugging in Ruby.

## Overview

Ruby provides several methods for outputting text to the console. Each has different behavior regarding newlines and formatting, making them suited for different use cases.

## Basic Usage

```ruby
puts "Hello, World!"   # Prints with newline
print "Hello, "        # Prints without newline
print "World!\n"
p [1, 2, 3]            # Prints inspect representation
```

## Key Concepts

### `puts` — Print with Newline

Outputs each argument on its own line:

```ruby
puts "Hello"
puts "World"
# Hello
# World

puts "One", "Two", "Three"
# One
# Two
# Three

puts [1, 2, 3]  # Arrays print each element on its own line
# 1
# 2
# 3
```

### `print` — Print without Newline

Outputs without adding a newline:

```ruby
print "Loading"
print "."
print "."
print ".\n"
# Loading...
```

### `p` — Debug Print

Calls `.inspect` on the object, showing its internal representation:

```ruby
p "Hello"       # => "Hello" (with quotes)
p [1, 2, 3]     # => [1, 2, 3]
p nil           # => nil
p({a: 1, b: 2}) # => {:a=>1, :b=>2}

# Compare:
puts "Hello\tWorld"  # => Hello	World (tab rendered)
p "Hello\tWorld"     # => "Hello\tWorld" (shows escape)
```

### `pp` — Pretty Print

For complex nested structures:

```ruby
require 'pp'

data = { users: [{ name: "Alice", age: 30 }, { name: "Bob", age: 25 }] }

pp data
# {:users=>
#   [{:name=>"Alice", :age=>30},
#    {:name=>"Bob", :age=>25}]}
```

## Common Patterns

### String Interpolation

```ruby
name = "Ruby"
version = 3.2

puts "Hello, #{name}!"           # => Hello, Ruby!
puts "Version: #{version}"       # => Version: 3.2
puts "2 + 2 = #{2 + 2}"          # => 2 + 2 = 4
```

### Formatted Output

```ruby
# sprintf / format
puts sprintf("Price: $%.2f", 19.5)   # => Price: $19.50
puts format("Count: %05d", 42)       # => Count: 00042

# String interpolation alternative
puts "Price: $#{'%.2f' % 19.5}"      # => Price: $19.50
```

### Logging with Context

```ruby
def log(level, message)
  puts "[#{level.upcase}] #{Time.now}: #{message}"
end

log(:info, "Server started")
# [INFO] 2024-01-15 10:30:00 -0500: Server started
```

# Input Handling

```ruby
get_input = gets
# >> "Hello"
# get_input = "Hello\n"

puts get_input
# => "Hello"
```

Allowed Chaining of Methods

```ruby
get_input = gets.downcase.chomp
# => "Hello!"
# get_input = "hello!"
```
## Tips

- Use `puts` for user-facing output
- Use `p` for quick debugging (shows quotes, escapes, types)
- Use `pp` for inspecting complex nested data structures
- `puts nil` prints a blank line; `p nil` prints "nil"
- All three methods return `nil`

## See Also

- [[Ruby]]
