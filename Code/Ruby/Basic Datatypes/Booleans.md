---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Basic Datatypes]]'
---
# Booleans

Boolean logic and truthiness in Ruby.

## Overview

Ruby has two boolean values: `true` and `false`. Uniquely, Ruby also treats `nil` as falsy—everything else is truthy, including `0`, `""`, and `[]`.

## Basic Usage

```ruby
true             # => true
false            # => false
nil              # => nil (falsy, but not false)

# Boolean expressions
5 > 3            # => true
5 == 5           # => true
5 != 3           # => true
"hello".empty?   # => false
```

## Key Concepts

### Truthiness

Only `false` and `nil` are falsy. Everything else is truthy:

```ruby
# Falsy values (only two!)
false
nil

# Truthy values (everything else)
true
0              # Truthy! (unlike some languages)
""             # Truthy!
[]             # Truthy!
{}             # Truthy!
```

### Boolean Operators

```ruby
# AND - returns first falsy or last value
true && true     # => true
true && false    # => false
nil && true      # => nil
"a" && "b"       # => "b"

# OR - returns first truthy or last value
true || false    # => true
nil || "default" # => "default"
false || nil     # => nil

# NOT
!true            # => false
!nil             # => true
!!nil            # => false (double bang for boolean conversion)
```

### `and`/`or` vs `&&`/`||`

Lower precedence—use for control flow, not assignment:

```ruby
# && has higher precedence (use for expressions)
result = value && other

# 'and' has lower precedence (use for control flow)
do_something and do_next_thing

# Gotcha:
x = false || true   # x = true
x = false or true   # x = false (parsed as (x = false) or true)
```

### Comparison Operators

```ruby
5 == 5           # => true (equality)
5 === 5          # => true (case equality, used in case statements)
5.eql?(5)        # => true (type + value equality)
5.equal?(5)      # => true (same object?)

5 <=> 3          # => 1  (spaceship: -1, 0, or 1)
3 <=> 5          # => -1
5 <=> 5          # => 0
```

## Common Patterns

### Conditional Assignment

```ruby
# Set default if nil or false
name ||= "Anonymous"

# Only assign if currently nil/false
@cached ||= expensive_computation

# Safe navigation (nil won't raise error)
user&.name       # => nil if user is nil, otherwise user.name
```

### Boolean Conversion

```ruby
# Double bang converts to boolean
!!"hello"        # => true
!!nil            # => false
!!0              # => true

# Or use ternary
value ? true : false
```

### Predicate Methods

Methods ending in `?` return booleans by convention:

```ruby
[].empty?        # => true
"hello".include?("ell")  # => true
5.even?          # => false
5.odd?           # => true
nil.nil?         # => true
5.between?(1, 10) # => true
defined?(foo)    # => nil or "local-variable"
```

### Guard Clauses

```ruby
def process(user)
  return unless user          # Guard against nil
  return if user.banned?      # Early exit
  
  # Main logic
  user.process!
end
```

### Short-Circuit Evaluation

```ruby
# Second expression only evaluated if needed
user && user.admin?           # Safe if user might be nil
expensive_check || default    # Skips default if check passes

# Modern alternative: safe navigation
user&.admin?                  # Same as user && user.admin?
```

## Tips

- Remember: only `false` and `nil` are falsy—`0` and `""` are truthy
- Use `&&`/`||` for boolean logic, `and`/`or` for control flow
- Prefer `unless` over `if !` for readability
- Use `!!value` to convert any value to a strict boolean
- Safe navigation (`&.`) is cleaner than `&& chains`
- Predicate methods should always return `true` or `false`, not just truthy/falsy

## See Also

- [[Basic Datatypes]] — Overview of Ruby types
- [[Ruby]]
