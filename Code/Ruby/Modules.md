---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
---
# Modules

Modules provide namespacing and mixin functionality in Ruby.

## Overview

Modules serve two primary purposes:

1. **Namespacing** — Grouping related classes/methods under a common name to avoid collisions
2. **Mixins** — Sharing behavior across classes without inheritance

Unlike classes, modules cannot be instantiated.

## Basic Usage

### Namespacing

```ruby
module Payments
  class CreditCard
    def charge(amount)
      # ...
    end
  end
  
  class PayPal
    def charge(amount)
      # ...
    end
  end
end

# Usage
card = Payments::CreditCard.new
card.charge(100)
```

### Mixins with `include`

```ruby
module Loggable
  def log(message)
    puts "[LOG] #{message}"
  end
end

class Order
  include Loggable
  
  def process
    log("Processing order...")
  end
end

Order.new.process  # => [LOG] Processing order...
```

## Key Concepts

### `include` vs `extend` vs `prepend`

```ruby
module Greeting
  def hello
    "Hello!"
  end
end

class Person
  include Greeting   # Adds as instance methods
end
Person.new.hello     # => "Hello!"

class Robot
  extend Greeting    # Adds as class methods
end
Robot.hello          # => "Hello!"

class Animal
  prepend Greeting   # Inserts BEFORE class methods (overrides)
end
```

### Module Methods

Define methods callable on the module itself:

```ruby
module MathUtils
  def self.square(n)
    n * n
  end
  
  # Alternative syntax
  module_function
  
  def cube(n)
    n ** 3
  end
end

MathUtils.square(4)  # => 16
MathUtils.cube(3)    # => 27
```

## Common Patterns

### Callbacks with `included`

```ruby
module Timestamps
  def self.included(base)
    base.extend(ClassMethods)
  end
  
  module ClassMethods
    def has_timestamps
      attr_accessor :created_at, :updated_at
    end
  end
end

class Post
  include Timestamps
  has_timestamps
end
```

### The `Comparable` Mixin

```ruby
class Version
  include Comparable
  
  attr_reader :major, :minor
  
  def initialize(major, minor)
    @major, @minor = major, minor
  end
  
  def <=>(other)
    [major, minor] <=> [other.major, other.minor]
  end
end

Version.new(2, 0) > Version.new(1, 9)  # => true
```

## Tips

- Use modules for shared behavior; use inheritance for "is-a" relationships
- `prepend` is useful for wrapping/decorating existing methods
- Check if a module is included with `is_a?` or `include?`
- Ruby's `Enumerable` and `Comparable` are classic mixin examples

## See Also

- [[Ruby]]
