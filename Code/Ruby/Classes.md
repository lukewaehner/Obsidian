---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Modules]]'
  - '[[Functions]]'
---
# Classes

Classes are blueprints for creating objects, encapsulating data and behavior together.

## Overview

In Ruby, everything is an object, and classes define the structure and behavior of those objects. Classes hold instance variables (state) and methods (behavior). Every class inherits from `Object` by default.

## Basic Usage

```ruby
class Greeter
  def initialize(name = "World")
    @name = name
  end

  def say_hi
    puts "Hi, #{@name}!"
  end

  def say_bye
    puts "Bye #{@name}, see you soon."
  end
end
```

### Object Creation

```ruby
greeter = Greeter.new("Luke")

greeter.say_hi   # => Hi, Luke!
greeter.say_bye  # => Bye Luke, see you soon.
```

### Attribute Accessors

Expose instance variables with getters and setters:

```ruby
class Greeter
  attr_accessor :name  # Creates both getter and setter

  def initialize(name = "World")
    @name = name
  end

  def say_hi
    puts "Hi, #{@name}!"
  end
end
```

```ruby
greeter = Greeter.new("Luke")
greeter.name         # => "Luke"
greeter.name = "Jeff"
greeter.name         # => "Jeff"
```

| Accessor | Creates |
|----------|---------|
| `attr_reader :name` | Getter only (`name`) |
| `attr_writer :name` | Setter only (`name=`) |
| `attr_accessor :name` | Both getter and setter |

## Key Concepts

### Instance Variables

Prefixed with `@`, scoped to the instance:

```ruby
class Counter
  def initialize
    @count = 0
  end

  def increment
    @count += 1
  end

  def value
    @count
  end
end
```

### Class Variables and Methods

Shared across all instances:

```ruby
class User
  @@count = 0  # Class variable

  def initialize(name)
    @name = name
    @@count += 1
  end

  def self.count  # Class method
    @@count
  end
end

User.new("Alice")
User.new("Bob")
User.count  # => 2
```

### Inheritance

```ruby
class Animal
  def speak
    "..."
  end
end

class Dog < Animal
  def speak
    "Woof!"
  end
end

class Cat < Animal
  def speak
    "Meow!"
  end
end

Dog.new.speak  # => "Woof!"
Cat.new.speak  # => "Meow!"
```

### Calling Parent Methods

```ruby
class Child < Parent
  def greet
    super + " Nice to meet you!"  # Calls Parent#greet
  end
end
```

## Common Patterns

### Duck Typing

Ruby cares about behavior, not type:

```ruby
class MegaGreeter
  attr_accessor :names

  def initialize(names = "World")
    @names = names
  end

  def say_hi
    if @names.nil?
      puts "..."
    elsif @names.respond_to?(:each)
      @names.each { |name| puts "Hello, #{name}!" }
    else
      puts "Hello, #{@names}!"
    end
  end
end

MegaGreeter.new(["Alice", "Bob"]).say_hi
# Hello, Alice!
# Hello, Bob!

MegaGreeter.new("World").say_hi
# Hello, World!
```

### Private and Protected Methods

```ruby
class BankAccount
  def initialize(balance)
    @balance = balance
  end

  def withdraw(amount)
    return "Insufficient funds" unless sufficient_funds?(amount)
    @balance -= amount
  end

  private

  def sufficient_funds?(amount)
    @balance >= amount
  end
end
```

### Struct for Simple Classes

```ruby
Person = Struct.new(:name, :age) do
  def adult?
    age >= 18
  end
end

person = Person.new("Alice", 30)
person.name   # => "Alice"
person.adult? # => true
```

## Tips

- Use `attr_reader` by default; only add `attr_writer` or `attr_accessor` when mutation is needed
- Prefer composition over inheritance—use modules for shared behavior
- Class names are constants and must start with a capital letter
- Use `private` for internal helper methods
- Ruby has single inheritance only; use [[Modules]] for multiple behavior mixing

## See Also

- [[Modules]] — Mixins and namespacing
- [[Functions]] — Method definitions
- [[Ruby]]
