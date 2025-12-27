---
tags:
  - ruby
  - oop
type: note
related:
  - '[[Object Oriented Programming]]'
  - '[[Code/Languages/Ruby/Classes]]'
  - '[[Modules as Mixins]]'
  - '[[Composition]]'
---
# Inheritance

Single inheritance model for sharing behavior between parent and child classes.

## Overview

Ruby uses single inheritance—each class can have only one direct parent. The child class inherits all methods and attributes from the parent, and can override or extend them. For sharing behavior across multiple class hierarchies, use [[Modules as Mixins]] instead.

## Basic Usage

### Defining Inheritance

Use `<` to inherit from a parent class:

```ruby
class Animal
  def initialize(name)
    @name = name
  end

  def speak
    "..."
  end

  def introduce
    "I'm #{@name}"
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

dog = Dog.new("Rex")
dog.introduce  # => "I'm Rex" (inherited)
dog.speak      # => "Woof!" (overridden)
```

### The Inheritance Chain

Every class ultimately inherits from `BasicObject`:

```ruby
Dog.ancestors
# => [Dog, Animal, Object, Kernel, BasicObject]

Dog.superclass        # => Animal
Animal.superclass     # => Object
Object.superclass     # => BasicObject
BasicObject.superclass # => nil
```

## Using super

### Basic super

Call the parent's implementation of the same method:

```ruby
class Animal
  def speak
    "Some sound"
  end
end

class Dog < Animal
  def speak
    super + "... Woof!"
  end
end

Dog.new.speak  # => "Some sound... Woof!"
```

### super with Arguments

```ruby
class Person
  def initialize(name)
    @name = name
  end
end

class Employee < Person
  def initialize(name, role)
    super(name)  # Pass name to Person#initialize
    @role = role
  end
end

# super vs super()
# super    — passes ALL arguments from current method to parent
# super()  — passes NO arguments to parent
# super(x) — passes specific arguments to parent
```

### super in Different Contexts

```ruby
class Parent
  def greet(greeting, name)
    "#{greeting}, #{name}!"
  end
end

class Child < Parent
  def greet(greeting, name)
    super              # Passes both: greeting and name
  end
end

class AnotherChild < Parent
  def greet(greeting, name)
    super("Hello", name)  # Passes "Hello" and name
  end
end
```

## Method Overriding

### Complete Override

Replace the parent's implementation entirely:

```ruby
class Vehicle
  def start
    "Starting engine..."
  end
end

class ElectricCar < Vehicle
  def start
    "Powering up silently..."
  end
end
```

### Extending Behavior

Add to the parent's implementation:

```ruby
class Logger
  def log(message)
    puts "[LOG] #{message}"
  end
end

class TimestampedLogger < Logger
  def log(message)
    super("[#{Time.now}] #{message}")
  end
end
```

## Type Checking

### is_a? / kind_of?

Check if object is an instance of a class or its ancestors:

```ruby
dog = Dog.new("Rex")

dog.is_a?(Dog)      # => true
dog.is_a?(Animal)   # => true
dog.is_a?(Object)   # => true
dog.is_a?(Cat)      # => false

dog.kind_of?(Animal)  # => true (alias for is_a?)
```

### instance_of?

Check exact class only (not ancestors):

```ruby
dog = Dog.new("Rex")

dog.instance_of?(Dog)     # => true
dog.instance_of?(Animal)  # => false
dog.instance_of?(Object)  # => false
```

### Class Comparison

```ruby
dog.class          # => Dog
dog.class == Dog   # => true
dog.class.ancestors.include?(Animal)  # => true
```

## Key Concepts

### What Gets Inherited

- Instance methods
- Class methods (defined with `self.`)
- Constants (with some scoping rules)

### What Doesn't Get Inherited

- Instance variables (they're created when assigned, not inherited)
- The `initialize` method must call `super` explicitly

```ruby
class Parent
  def initialize
    @parent_var = "I'm from parent"
  end
end

class Child < Parent
  def initialize
    # @parent_var won't exist unless we call super
    super
    @child_var = "I'm from child"
  end
end
```

### Method Lookup Order

Ruby searches for methods in this order:

1. The object's singleton class (if any)
2. Prepended modules
3. The object's class
4. Included modules
5. Parent class (repeat 2-4)
6. `Object`, `Kernel`, `BasicObject`

```ruby
module M
  def greet
    "Hello from M"
  end
end

class Parent
  def greet
    "Hello from Parent"
  end
end

class Child < Parent
  include M

  def greet
    "Hello from Child"
  end
end

Child.new.greet  # => "Hello from Child"
# If Child#greet didn't exist, it would find M#greet next
```

## Common Patterns

### Template Method Pattern

Define a skeleton in the parent, let children fill in details:

```ruby
class Report
  def generate
    header + body + footer
  end

  def header
    "=== Report ===\n"
  end

  def footer
    "\n=== End ==="
  end

  def body
    raise NotImplementedError, "Subclass must implement body"
  end
end

class SalesReport < Report
  def body
    "Sales data here..."
  end
end

class InventoryReport < Report
  def body
    "Inventory data here..."
  end
end
```

### Calling Grandparent Methods

Sometimes you need to skip the parent:

```ruby
class Grandparent
  def greet
    "Hello from Grandparent"
  end
end

class Parent < Grandparent
  def greet
    "Hello from Parent"
  end
end

class Child < Parent
  def greet
    # Skip Parent, call Grandparent directly
    Grandparent.instance_method(:greet).bind(self).call
  end
end
```

### Abstract Base Classes

Ruby doesn't have formal abstract classes, but you can simulate them:

```ruby
class AbstractVehicle
  def initialize
    raise NotImplementedError, "#{self.class} is abstract" if self.class == AbstractVehicle
  end

  def start
    raise NotImplementedError, "Subclass must implement start"
  end
end
```

## Tips

- Prefer composition over inheritance for "has-a" relationships
- Use inheritance for "is-a" relationships only
- Keep inheritance hierarchies shallow (2-3 levels max)
- Use `super` without parentheses carefully—it passes all arguments
- Consider modules/mixins when behavior is shared across unrelated classes
- Remember: Ruby has single inheritance, use mixins for multiple behavior sources

## See Also

- [[Object Oriented Programming]]
- [[Modules as Mixins]] — Alternative to inheritance
- [[Composition]] — "Has-a" relationships
- [[Code/Languages/Ruby/Classes|Classes]] — Class fundamentals
- [[Ruby]]
