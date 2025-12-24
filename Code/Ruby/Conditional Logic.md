---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Booleans]]'
---
# Conditional Logic

Control flow structures for branching and decision-making in Ruby.

## Overview

Ruby provides expressive conditionals including `if`/`elsif`/`else`, `unless`, `case`, and the ternary operator. Ruby also supports inline (modifier) syntax for concise one-liners.

## Basic Usage

### If / Elsif / Else

```ruby
age = 15

if age >= 21
  puts "Can drink"
elsif age >= 18
  puts "Can vote"
else
  puts "A child"
end
```

### Inline (Modifier) Syntax

```ruby
puts "Welcome!" if logged_in?
puts "Access denied" unless authorized?
```

### Unless

The opposite of `if`—executes when the condition is false:

```ruby
age = 19

unless age < 18
  puts "Get a job"
end

# Inline
puts "Welcome to adulthood" unless age < 18

# With else (less common, often clearer as if/else)
unless age < 18
  puts "You're an adult"
else
  puts "You're a minor"
end
```

### Ternary Operator

One-line `if`/`else`:

```ruby
age = 19
status = age < 18 ? "minor" : "adult"
puts status  # => "adult"
```

### Case Statements

Pattern matching with multiple branches:

```ruby
grade = 'B'

result = case grade
  when 'A' then "Excellent!"
  when 'B' then "Good job"
  when 'C' then "You passed"
  when 'D', 'F' then "See me after class"
  else "Invalid grade"
end
```

Multi-line case branches:

```ruby
case grade
when 'A'
  puts "You're a genius"
  scholarship = true
when 'B', 'C'
  puts "Solid work"
  scholarship = false
else
  puts "Keep trying"
  summer_school = true
end
```

Case with ranges and types:

```ruby
case score
when 90..100 then "A"
when 80...90 then "B"
when 70...80 then "C"
else "F"
end

case value
when String then value.upcase
when Integer then value * 2
when Array then value.first
else value
end
```

## Key Concepts

### Comparison Operators

```ruby
5 == 5     # => true  (equality)
5 != 3     # => true  (inequality)
5 > 3      # => true  (greater than)
5 < 3      # => false (less than)
5 >= 5     # => true  (greater than or equal)
5 <= 5     # => true  (less than or equal)
```

### Equality Methods

```ruby
# == : Value equality
5 == 5.0           # => true

# eql? : Value AND type equality
5.eql?(5.0)        # => false (Integer vs Float)
5.eql?(5)          # => true

# equal? : Same object in memory
a = "hello"
b = "hello"
a.equal?(b)        # => false (different objects)
a.equal?(a)        # => true

# For integers, small numbers are cached:
a = 5
b = 5
a.equal?(b)        # => true (same object due to caching)
```

### Spaceship Operator

Returns `-1`, `0`, or `1` for comparisons:

```ruby
5 <=> 10   # => -1 (left is less)
5 <=> 5    # => 0  (equal)
5 <=> 3    # => 1  (left is greater)

# Commonly used in sorting
[3, 1, 2].sort { |a, b| a <=> b }  # => [1, 2, 3]
[3, 1, 2].sort { |a, b| b <=> a }  # => [3, 2, 1]
```

### Case Equality (`===`)

The `case` statement uses `===` under the hood:

```ruby
# These are equivalent:
case value
when 1..10 then "small"
when Integer then "number"
when /hello/ then "greeting"
end

# Using === directly:
(1..10) === 5      # => true
Integer === 5      # => true
/hello/ === "hello world"  # => true
```

## Common Patterns

### Guard Clauses

Exit early to reduce nesting:

```ruby
def process_user(user)
  return "No user" unless user
  return "Banned" if user.banned?
  return "Inactive" unless user.active?
  
  # Main logic here
  user.process!
end
```

### Conditional Assignment

```ruby
# Assign if nil or false
name ||= "Anonymous"

# Assign only if nil (not false)
name = name.nil? ? "Anonymous" : name

# Safe navigation
user&.profile&.avatar  # Returns nil if any part is nil
```

### Boolean Expressions as Values

```ruby
# Conditionals return values
status = if premium? then "VIP" else "Standard" end

# Use the result directly
puts if success? then "Done!" else "Failed" end
```

### Pattern Matching (Ruby 3.0+)

```ruby
case user
in { name:, role: "admin" }
  puts "Admin: #{name}"
in { name:, role: }
  puts "User: #{name} (#{role})"
else
  puts "Unknown"
end
```

### Combining Conditions

```ruby
# AND
if logged_in? && admin?
  show_dashboard
end

# OR
if guest? || expired?
  redirect_to_login
end

# Grouped
if (admin? || moderator?) && verified?
  allow_action
end
```

## Tips

- Prefer `unless` over `if !` for readability
- Avoid `unless` with `else`—use `if`/`else` instead
- Use guard clauses to reduce nesting and improve clarity
- Ternary is great for simple assignment, but avoid nesting them
- Case statements are cleaner than long `elsif` chains
- Remember: only `false` and `nil` are falsy—`0` and `""` are truthy
- Use `then` for single-line case branches, omit for multi-line

## See Also

- [[Booleans]] — Truthiness and boolean operators
- [[Ruby]]
