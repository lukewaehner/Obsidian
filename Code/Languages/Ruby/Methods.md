---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Classes]]'
  - '[[Modules]]'
---
# Methods

Defining and using methods in Ruby.

## Overview

Methods are reusable blocks of code that perform specific tasks. In Ruby, methods are defined with `def` and always return a value—either explicitly with `return` or implicitly as the last evaluated expression.

Ruby has a massive standard library of built-in methods:

```ruby
"hello".reverse      # => "olleh"
"hello".upcase       # => "HELLO"
[3, 1, 2].sort       # => [1, 2, 3]
5.times { puts "hi" }
```

## Defining Methods

```ruby
def greet
  "Hello, World!"
end

puts greet  # => Hello, World!
```

### With Parameters

```ruby
def greet(name)
  "Hello, #{name}!"
end

greet("Alice")  # => "Hello, Alice!"
```

### Default Parameters

```ruby
def greet(name = "World")
  "Hello, #{name}!"
end

greet          # => "Hello, World!"
greet("Bob")   # => "Hello, Bob!"
```

### Multiple Parameters

```ruby
def introduce(name, age, city = "Unknown")
  "#{name}, #{age}, from #{city}"
end

introduce("Alice", 30)           # => "Alice, 30, from Unknown"
introduce("Bob", 25, "Boston")   # => "Bob, 25, from Boston"
```

## Naming Conventions

Methods can use letters, numbers, and `_`, `?`, `!`, `=` characters.

```ruby
method_name      # ✓ valid (snake_case preferred)
_private_method  # ✓ valid (conventionally private)
method_27        # ✓ valid
calculate!       # ✓ valid (bang method)
empty?           # ✓ valid (predicate method)
value=           # ✓ valid (setter method)

1_method         # ✗ invalid (starts with number)
method?_name     # ✗ invalid (? not at end)
begin            # ✗ invalid (reserved word)
```

### Documentation Convention

Use `#` to denote instance methods:

```ruby
String#reverse    # Instance method on String
Integer#times     # Instance method on Integer
Array.new         # Class method (note the dot)
```

## Return Values

### Implicit Return

The last expression is automatically returned:

```ruby
def add(a, b)
  a + b  # Returned implicitly
end

add(2, 3)  # => 5
```

```ruby
def even_odd(number)
  if number.even?
    "Even"
  else
    "Odd"
  end
end

even_odd(4)  # => "Even"
even_odd(7)  # => "Odd"
```

### Explicit Return

Use `return` for early exits:

```ruby
def divide(a, b)
  return nil if b.zero?
  a / b
end

divide(10, 2)  # => 5
divide(10, 0)  # => nil
```

### Multiple Return Values

```ruby
def min_max(array)
  [array.min, array.max]
end

min, max = min_max([3, 1, 4, 1, 5])
min  # => 1
max  # => 5
```

## Key Concepts

### Predicate Methods (`?`)

Return a boolean value:

```ruby
5.even?           # => false
6.even?           # => true
"".empty?         # => true
[1, 2].include?(2) # => true

# Define your own
def adult?(age)
  age >= 18
end

adult?(21)  # => true
```

### Bang Methods (`!`)

Mutate the caller or indicate danger:

```ruby
name = "ALICE"

name.downcase     # => "alice" (returns new string)
name              # => "ALICE" (unchanged)

name.downcase!    # => "alice" (mutates in place)
name              # => "alice" (changed!)
```

```ruby
# Define your own
def normalize!(string)
  string.strip!
  string.downcase!
  string
end
```

> **Convention**: Methods with `!` usually have a non-mutating counterpart without `!`

### Setter Methods (`=`)

Define attribute writers:

```ruby
class Person
  def name=(new_name)
    @name = new_name.capitalize
  end
  
  def name
    @name
  end
end

person = Person.new
person.name = "alice"  # Calls name= method
person.name            # => "Alice"
```

### Method Chaining

```ruby
"  hello world  ".strip.capitalize.reverse
# => "dlrow olleH"

# Enable chaining by returning self
class Builder
  def initialize
    @parts = []
  end
  
  def add(part)
    @parts << part
    self  # Return self for chaining
  end
  
  def build
    @parts.join(" ")
  end
end

Builder.new.add("Hello").add("World").build
# => "Hello World"
```

## Advanced Parameters

### Keyword Arguments

```ruby
def create_user(name:, email:, admin: false)
  { name: name, email: email, admin: admin }
end

create_user(name: "Alice", email: "a@b.com")
# => { name: "Alice", email: "a@b.com", admin: false }
```

### Splat Operator (`*`)

Collect variable arguments into an array:

```ruby
def sum(*numbers)
  numbers.reduce(0, :+)
end

sum(1, 2, 3, 4)  # => 10
sum(10, 20)      # => 30
```

### Double Splat (`**`)

Collect keyword arguments into a hash:

```ruby
def log(message, **options)
  level = options[:level] || "INFO"
  puts "[#{level}] #{message}"
end

log("Starting", level: "DEBUG", timestamp: true)
# => [DEBUG] Starting
```

### Block Parameter (`&`)

Accept a block as an explicit parameter:

```ruby
def with_timing(&block)
  start = Time.now
  result = block.call
  puts "Took #{Time.now - start}s"
  result
end

with_timing { sleep(0.1); "done" }
# Took 0.1s
# => "done"
```

### Yielding to Blocks

```ruby
def repeat(n)
  n.times { yield }
end

repeat(3) { puts "Hello" }
# Hello
# Hello
# Hello
```

```ruby
def transform(value)
  yield(value)
end

transform(5) { |n| n * 2 }  # => 10
```

## Common Patterns

### Guard Clauses

Exit early to reduce nesting:

```ruby
def process(user)
  return "No user" unless user
  return "Banned" if user[:banned]
  return "Inactive" unless user[:active]
  
  "Processing #{user[:name]}"
end
```

### Method Objects

Get a reference to a method:

```ruby
def double(n)
  n * 2
end

m = method(:double)
m.call(5)           # => 10
[1, 2, 3].map(&m)   # => [2, 4, 6]
```

### Checking Method Existence

```ruby
"hello".respond_to?(:upcase)  # => true
"hello".respond_to?(:foo)     # => false

# Useful in conditionals
obj.do_something if obj.respond_to?(:do_something)
```

## Tips

- Use snake_case for method names: `calculate_total` not `calculateTotal`
- Omit parentheses for methods with no arguments: `array.length` not `array.length()`
- Use `?` suffix for methods returning booleans
- Use `!` suffix for methods that mutate or are dangerous
- Keep methods short—if it's over 10 lines, consider splitting
- Use keyword arguments for methods with 3+ parameters
- Prefer implicit returns for simple methods

## See Also

- [[Classes]] — Instance and class methods
- [[Modules]] — Organizing methods
- [[Ruby]]
