---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Ruby - Modules]]'
---
# Functions

Methods (functions) in Ruby for defining reusable behavior.

## Overview

In Ruby, functions are called **methods**. They're defined with `def` and always return a value—either explicitly with `return` or implicitly as the last evaluated expression.

## Basic Usage

```ruby
def hello
  puts "Hello, World!"
end

hello    # => Hello, World!
hello()  # => Hello, World! (parentheses optional)
```

### With Parameters

```ruby
def greet(name)
  puts "Hello, #{name}!"
end

greet("Luke")  # => Hello, Luke!
```

### Default Parameters

```ruby
def greet(name = "World")
  puts "Hello, #{name.capitalize}!"
end

greet("luke")  # => Hello, Luke!
greet          # => Hello, World!
```

## Key Concepts

### Implicit Returns

The last expression is automatically returned:

```ruby
def add(a, b)
  a + b  # No return keyword needed
end

add(2, 3)  # => 5
```

Use `return` for early exits:

```ruby
def divide(a, b)
  return nil if b.zero?
  a / b
end
```

### Keyword Arguments

Named parameters for clarity:

```ruby
def create_user(name:, email:, admin: false)
  { name: name, email: email, admin: admin }
end

create_user(name: "Alice", email: "alice@example.com")
# => {:name=>"Alice", :email=>"alice@example.com", :admin=>false}
```

### Splat Operators

```ruby
# *args collects extra positional arguments into an array
def sum(*numbers)
  numbers.reduce(0, :+)
end
sum(1, 2, 3, 4)  # => 10

# **kwargs collects extra keyword arguments into a hash
def log(message, **options)
  puts "#{options[:level] || 'INFO'}: #{message}"
end
log("Starting", level: "DEBUG")  # => DEBUG: Starting
```

### Blocks, Procs, and Lambdas

Methods can accept blocks:

```ruby
def with_timing
  start = Time.now
  result = yield  # Execute the block
  puts "Took #{Time.now - start}s"
  result
end

with_timing { sleep(1); "done" }
# Took 1.00123s
# => "done"
```

Explicit block parameter:

```ruby
def transform(value, &block)
  block.call(value)
end

transform(5) { |n| n * 2 }  # => 10
```

## Common Patterns

### Predicate Methods (ending in `?`)

```ruby
def admin?(user)
  user[:role] == "admin"
end

admin?({ role: "admin" })  # => true
```

### Bang Methods (ending in `!`)

Indicate mutation or danger:

```ruby
def normalize!(string)
  string.strip!
  string.downcase!
  string
end

name = "  ALICE  "
normalize!(name)
name  # => "alice" (mutated in place)
```

### Method Chaining

Return `self` to enable chaining:

```ruby
class Builder
  def initialize
    @parts = []
  end

  def add(part)
    @parts << part
    self
  end

  def build
    @parts.join(" ")
  end
end

Builder.new.add("Hello").add("World").build
# => "Hello World"
```

### Guard Clauses

```ruby
def process(user)
  return unless user
  return if user[:banned]
  
  # Main logic here
  puts "Processing #{user[:name]}"
end
```

## Tips

- Omit parentheses for methods with no arguments: `user.save` not `user.save()`
- Use keyword arguments for methods with 3+ parameters for readability
- Convention: `?` suffix for boolean returns, `!` suffix for mutation/danger
- Methods are always associated with objects—even top-level methods belong to `main`
- Use `method(:name)` to get a Method object you can pass around

## See Also

- [[Ruby - Modules]] — Organizing methods into reusable units
- [[Ruby]]
