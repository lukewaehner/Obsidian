---
tags:
  - ruby
  - oop
type: note
related:
  - '[[Object Oriented Programming]]'
  - '[[Method Visibility]]'
  - '[[Code/Languages/Ruby/Classes]]'
---
# Class Methods and Variables

Class-level state and behavior in Ruby.

## Overview

While instance methods and variables belong to individual objects, class methods and variables belong to the class itself. Understanding the distinction—and when to use each—is essential for proper Ruby OOP design. Ruby also has a third option, class instance variables, which avoid some pitfalls of class variables.

## Class Methods

### Defining Class Methods

Methods called on the class itself, not instances:

```ruby
class User
  def self.create(name)
    new(name).tap(&:save)
  end

  def initialize(name)
    @name = name
  end

  def save
    puts "Saving #{@name}"
  end
end

User.create("Alice")  # Called on class
# vs
User.new("Bob").save  # Called on instance
```

### Multiple Syntaxes

```ruby
class Calculator
  # Most common: self.method_name
  def self.add(a, b)
    a + b
  end

  # Alternative: class << self block
  class << self
    def subtract(a, b)
      a - b
    end

    def multiply(a, b)
      a * b
    end
  end
end

Calculator.add(2, 3)       # => 5
Calculator.subtract(5, 2)  # => 3
Calculator.multiply(4, 3)  # => 12
```

### Common Use Cases

```ruby
class Product
  # Factory methods
  def self.from_json(json)
    data = JSON.parse(json)
    new(data['name'], data['price'])
  end

  # Finders (database-style)
  def self.find(id)
    # Query database...
  end

  def self.find_by(attributes)
    # Query by attributes...
  end

  # Configuration
  def self.configure
    yield(configuration)
  end

  def self.configuration
    @configuration ||= Configuration.new
  end

  # Utility/helper methods
  def self.valid_price?(price)
    price.is_a?(Numeric) && price >= 0
  end

  def initialize(name, price)
    @name = name
    @price = price
  end
end
```

## Understanding self

`self` refers to different things depending on context:

```ruby
class Demo
  puts self  # => Demo (inside class definition, self is the class)

  def self.class_method
    puts self  # => Demo (in class method, self is the class)
  end

  def instance_method
    puts self  # => #<Demo:0x...> (in instance method, self is the instance)
  end
end
```

### self in Different Contexts

```ruby
class Example
  # Class level
  @class_instance_var = "class level"  # self is Example

  def self.class_level_self
    self  # => Example
  end

  def instance_level_self
    self  # => the instance
  end

  def call_own_method
    self.public_method   # Explicit self
    public_method        # Implicit self (preferred)
    self.private_method  # Error! Can't call private with explicit self
    private_method       # Works
  end
end
```

## Class Variables (@@)

Shared across the class and ALL subclasses:

```ruby
class Animal
  @@count = 0

  def initialize
    @@count += 1
  end

  def self.count
    @@count
  end
end

class Dog < Animal
end

class Cat < Animal
end

Animal.new
Dog.new
Cat.new

Animal.count  # => 3
Dog.count     # => 3 (same counter!)
Cat.count     # => 3 (same counter!)
```

### The Class Variable Problem

Class variables are shared across inheritance hierarchies, which is often unexpected:

```ruby
class Parent
  @@value = "parent"

  def self.value
    @@value
  end

  def self.value=(v)
    @@value = v
  end
end

class Child < Parent
end

Parent.value         # => "parent"
Child.value          # => "parent"

Child.value = "child"

Parent.value         # => "child" (Parent changed too!)
Child.value          # => "child"
```

## Class Instance Variables (@)

Each class gets its own variable (not shared with subclasses):

```ruby
class Animal
  @count = 0  # Class instance variable

  def self.count
    @count
  end

  def self.increment
    @count += 1
  end
end

class Dog < Animal
  @count = 0  # Dog's own counter
end

class Cat < Animal
  @count = 0  # Cat's own counter
end

Animal.increment
Animal.increment
Dog.increment

Animal.count  # => 2
Dog.count     # => 1
Cat.count     # => 0 (unchanged)
```

### Comparison: @@ vs @

| Aspect | Class Variable (`@@`) | Class Instance Variable (`@`) |
|--------|----------------------|------------------------------|
| Scope | Class + all subclasses | Single class only |
| Inherited? | Shared (same variable) | Not inherited |
| Override? | Affects parent | Independent |
| Recommended? | Rarely | Usually |

## Singleton Methods

Methods defined on a specific object (not its class):

```ruby
str = "hello"

def str.shout
  upcase + "!"
end

str.shout           # => "HELLO!"
"hello".shout       # => NoMethodError (only this specific string has it)
```

### Singleton Class

Every object has a hidden singleton class for its unique methods:

```ruby
class User
  def greet
    "Hello"
  end
end

alice = User.new

# Add method to alice's singleton class
def alice.greet
  "Hi, I'm Alice!"
end

bob = User.new

alice.greet  # => "Hi, I'm Alice!" (singleton method)
bob.greet    # => "Hello" (regular instance method)

# View singleton class
alice.singleton_class  # => #<Class:#<User:0x...>>
```

### Class Methods Are Singleton Methods

```ruby
class Demo
  def self.class_method
    "I'm a class method"
  end
end

# Equivalent to:
class Demo
end

def Demo.class_method
  "I'm a class method"
end

# Also equivalent to:
class Demo
  class << self
    def class_method
      "I'm a class method"
    end
  end
end
```

## Common Patterns

### Configuration Pattern

```ruby
class ApiClient
  class << self
    attr_accessor :api_key, :timeout, :base_url

    def configure
      yield(self)
    end
  end

  def initialize
    @api_key = self.class.api_key
    @timeout = self.class.timeout
  end
end

ApiClient.configure do |config|
  config.api_key = "secret123"
  config.timeout = 30
  config.base_url = "https://api.example.com"
end

client = ApiClient.new
```

### Registry Pattern

```ruby
class Plugin
  @registry = {}

  def self.register(name, klass)
    @registry[name] = klass
  end

  def self.find(name)
    @registry[name]
  end

  def self.all
    @registry.keys
  end
end

class ImagePlugin
  Plugin.register(:image, self)
end

class VideoPlugin
  Plugin.register(:video, self)
end

Plugin.find(:image)  # => ImagePlugin
Plugin.all           # => [:image, :video]
```

### Counter with Class Instance Variables

```ruby
class Model
  def self.inherited(subclass)
    subclass.instance_variable_set(:@count, 0)
  end

  @count = 0

  def self.count
    @count
  end

  def self.create
    @count += 1
    new
  end
end

class User < Model
end

class Post < Model
end

3.times { User.create }
2.times { Post.create }

User.count   # => 3
Post.count   # => 2
Model.count  # => 0
```

### Private Class Methods

```ruby
class Service
  def self.call(params)
    validate!(params)
    process(params)
  end

  def self.validate!(params)
    raise "Invalid!" if params.empty?
  end
  private_class_method :validate!

  def self.process(params)
    "Processed: #{params}"
  end
  private_class_method :process
end

Service.call(name: "test")  # Works
Service.validate!({})       # NoMethodError: private method
```

## Tips

- Prefer class instance variables (`@`) over class variables (`@@`)
- Use class methods for factories, finders, and configuration
- Remember: `self` changes meaning based on context
- Use `class << self` to define multiple class methods cleanly
- Private class methods require `private_class_method` declaration
- Class methods are inherited by subclasses
- Use the inherited hook to set up class instance variables in subclasses

## See Also

- [[Object Oriented Programming]]
- [[Method Visibility]] — Public, private, protected
- [[Code/Languages/Ruby/Classes|Classes]] — Class fundamentals
- [[Ruby]]
