---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
---
# Arithmetic

Math operations and the standard Math library in Ruby.

## Overview

Ruby supports standard arithmetic operators on numeric types. For advanced operations like square roots and trigonometry, use the `Math` module.

## Basic Usage

```ruby
# Basic operators
3 + 2   # => 5   (addition)
3 - 2   # => 1   (subtraction)
3 * 2   # => 6   (multiplication)
3 / 2   # => 1   (integer division)
3.0 / 2 # => 1.5 (float division)
3 % 2   # => 1   (modulo)
3 ** 2  # => 9   (exponentiation)

# Math module
Math.sqrt(9)    # => 3.0
Math.log(10)    # => 2.302...
Math.sin(0)     # => 0.0
Math::PI        # => 3.141592...
```

## Key Concepts

### Integer vs Float Division

Division between integers returns an integer (truncated):

```ruby
5 / 2     # => 2 (not 2.5!)
5.0 / 2   # => 2.5
5 / 2.0   # => 2.5
5.to_f / 2 # => 2.5
```

### Numeric Types

```ruby
42.class        # => Integer
3.14.class      # => Float
(2+3i).class    # => Complex
Rational(1, 3)  # => (1/3) - exact fractions
```

## Common Patterns

```ruby
# Rounding
3.7.round     # => 4
3.7.floor     # => 3
3.2.ceil      # => 4
3.14159.round(2) # => 3.14

# Absolute value
-5.abs        # => 5

# Min/max
[3, 1, 4, 1, 5].min  # => 1
[3, 1, 4, 1, 5].max  # => 5

# Clamping to a range
15.clamp(0, 10)  # => 10
-5.clamp(0, 10)  # => 0

# Check if even/odd
4.even?  # => true
5.odd?   # => true
```

## Tips

- Always use floats when you need decimal precision in division
- `Math.sqrt` returns a Float even for perfect squares
- Use `Rational` for exact fractional arithmetic (avoids floating point errors)
- Ruby has no `++` or `--` operators; use `+= 1` or `-= 1` instead

## See Also

- [[Ruby]]
