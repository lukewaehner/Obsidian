---
tags:
  - ruby
  - oop
type: note
related:
  - '[[Object Oriented Programming]]'
  - '[[Inheritance]]'
  - '[[Modules as Mixins]]'
  - '[[Code/Languages/Ruby/Classes]]'
---
# Polymorphism

Multiple object types responding to the same interface.

## Overview

Polymorphism means "many forms"—the ability for different objects to respond to the same message (method call) in their own way. Ruby achieves polymorphism primarily through duck typing: if an object responds to the methods you call, it works, regardless of its class. This is more flexible than inheritance-based polymorphism in statically-typed languages.

## Duck Typing

"If it walks like a duck and quacks like a duck, it's a duck."

Ruby doesn't care *what* an object is, only *what it can do*:

```ruby
class Duck
  def speak
    "Quack!"
  end
end

class Dog
  def speak
    "Woof!"
  end
end

class Car
  def speak
    "Beep beep!"
  end
end

def make_it_speak(thing)
  thing.speak  # Works with any object that has a speak method
end

make_it_speak(Duck.new)  # => "Quack!"
make_it_speak(Dog.new)   # => "Woof!"
make_it_speak(Car.new)   # => "Beep beep!"
```

### No Common Ancestor Required

Unlike Java or C++, these classes don't need to inherit from a common class or implement a formal interface:

```ruby
class Logger
  def write(message)
    puts "[LOG] #{message}"
  end
end

class FileWriter
  def initialize(path)
    @file = File.open(path, 'a')
  end

  def write(message)
    @file.puts(message)
  end
end

class ArrayBuffer
  def initialize
    @messages = []
  end

  def write(message)
    @messages << message
  end
end

# All three work interchangeably
def process(writer, data)
  writer.write("Processing: #{data}")
end

process(Logger.new, "test")
process(FileWriter.new("log.txt"), "test")
process(ArrayBuffer.new, "test")
```

## respond_to?

Check if an object can handle a method before calling it:

```ruby
def make_noise(thing)
  if thing.respond_to?(:speak)
    thing.speak
  elsif thing.respond_to?(:to_s)
    thing.to_s
  else
    "???"
  end
end

make_noise(Duck.new)  # => "Quack!"
make_noise("hello")   # => "hello"
make_noise(42)        # => "42"
```

### respond_to? with Private Methods

```ruby
class Secret
  private

  def hidden
    "secret"
  end
end

obj = Secret.new
obj.respond_to?(:hidden)        # => false
obj.respond_to?(:hidden, true)  # => true (include private)
```

## Method Overriding

Classic polymorphism through inheritance:

```ruby
class Shape
  def area
    raise NotImplementedError, "Subclass must implement area"
  end

  def describe
    "A shape with area #{area}"
  end
end

class Rectangle < Shape
  def initialize(width, height)
    @width = width
    @height = height
  end

  def area
    @width * @height
  end
end

class Circle < Shape
  def initialize(radius)
    @radius = radius
  end

  def area
    Math::PI * @radius ** 2
  end
end

shapes = [Rectangle.new(3, 4), Circle.new(5)]
shapes.each { |s| puts s.describe }
# A shape with area 12
# A shape with area 78.53981633974483
```

## Operator Overloading

Define how operators work on your objects:

```ruby
class Vector
  attr_reader :x, :y

  def initialize(x, y)
    @x, @y = x, y
  end

  def +(other)
    Vector.new(x + other.x, y + other.y)
  end

  def *(scalar)
    Vector.new(x * scalar, y * scalar)
  end

  def ==(other)
    x == other.x && y == other.y
  end

  def to_s
    "(#{x}, #{y})"
  end
end

a = Vector.new(1, 2)
b = Vector.new(3, 4)

puts a + b      # => (4, 6)
puts a * 3      # => (3, 6)
puts a == b     # => false
```

### Common Operators to Override

| Operator | Method | Use Case |
|----------|--------|----------|
| `+`, `-`, `*`, `/` | `+`, `-`, `*`, `/` | Arithmetic |
| `==` | `==` | Equality |
| `<=>` | `<=>` | Comparison (with Comparable) |
| `[]` | `[]` | Index access |
| `[]=` | `[]=` | Index assignment |
| `<<` | `<<` | Append |
| `to_s` | `to_s` | String conversion |
| `to_a` | `to_a` | Array conversion |

## Implicit Interfaces

Ruby's "interfaces" are implicit—defined by usage, not declaration:

```ruby
# Anything with each can be "Enumerable-like"
class Fibonacci
  include Enumerable

  def initialize(limit)
    @limit = limit
  end

  def each
    a, b = 0, 1
    while a <= @limit
      yield a
      a, b = b, a + b
    end
  end
end

fib = Fibonacci.new(100)
fib.map { |n| n * 2 }      # => [0, 2, 2, 4, 6, 10, 16, 26, 42, 68, 110, 178]
fib.select(&:even?)        # => [0, 2, 8, 34]
fib.take(5)                # => [0, 1, 1, 2, 3]
```

## Key Concepts

### Structural Typing vs Nominal Typing

Ruby uses **structural typing** (duck typing):

```ruby
# Java/C++ (nominal): "Is this object declared as type X?"
# Ruby (structural): "Can this object do X?"

def print_length(obj)
  puts obj.length  # Works with String, Array, Hash, or any object with length
end

print_length("hello")     # => 5
print_length([1, 2, 3])   # => 3
print_length({a: 1})      # => 1
```

### Polymorphism Through Blocks

Blocks enable runtime polymorphism:

```ruby
def process_data(data, &transformation)
  data.map(&transformation)
end

numbers = [1, 2, 3, 4, 5]

process_data(numbers) { |n| n * 2 }      # => [2, 4, 6, 8, 10]
process_data(numbers) { |n| n.to_s }     # => ["1", "2", "3", "4", "5"]
process_data(numbers) { |n| n ** 2 }     # => [1, 4, 9, 16, 25]
```

### The Null Object Pattern

Avoid nil checks with polymorphic null objects:

```ruby
class User
  attr_reader :name, :email

  def initialize(name, email)
    @name = name
    @email = email
  end

  def greet
    "Hello, #{name}!"
  end
end

class GuestUser
  def name
    "Guest"
  end

  def email
    nil
  end

  def greet
    "Hello, stranger!"
  end
end

def welcome(user)
  puts user.greet  # Works with User or GuestUser
end

welcome(User.new("Alice", "alice@example.com"))  # => Hello, Alice!
welcome(GuestUser.new)                            # => Hello, stranger!
```

## Common Patterns

### Strategy Pattern

Swap algorithms at runtime:

```ruby
class PaymentProcessor
  def initialize(strategy)
    @strategy = strategy
  end

  def process(amount)
    @strategy.charge(amount)
  end
end

class CreditCardStrategy
  def charge(amount)
    "Charging $#{amount} to credit card"
  end
end

class PayPalStrategy
  def charge(amount)
    "Sending $#{amount} via PayPal"
  end
end

class CryptoStrategy
  def charge(amount)
    "Transferring #{amount} in crypto"
  end
end

processor = PaymentProcessor.new(CreditCardStrategy.new)
processor.process(100)  # => "Charging $100 to credit card"

processor = PaymentProcessor.new(PayPalStrategy.new)
processor.process(100)  # => "Sending $100 via PayPal"
```

### Coercion Methods

Let Ruby convert your objects automatically:

```ruby
class Temperature
  attr_reader :celsius

  def initialize(celsius)
    @celsius = celsius
  end

  def to_f
    celsius.to_f
  end

  def to_i
    celsius.to_i
  end

  def to_s
    "#{celsius}°C"
  end

  # Called by arithmetic operations
  def coerce(other)
    [other, celsius]
  end
end

temp = Temperature.new(25)
puts temp + 5     # => 30 (uses coerce)
puts "Temp: #{temp}"  # => "Temp: 25°C" (uses to_s)
```

### Method Missing as Polymorphism

Dynamic method handling:

```ruby
class FlexibleStruct
  def initialize(hash = {})
    @data = hash
  end

  def method_missing(name, *args)
    if name.to_s.end_with?('=')
      @data[name.to_s.chomp('=').to_sym] = args.first
    else
      @data[name]
    end
  end

  def respond_to_missing?(name, include_private = false)
    true
  end
end

person = FlexibleStruct.new(name: "Alice")
person.name          # => "Alice"
person.age = 30
person.age           # => 30
person.anything      # => nil
```

## Tips

- Embrace duck typing—check capabilities, not types
- Use `respond_to?` for safety in dynamic situations
- Override operators thoughtfully—follow conventions (e.g., `+` returns a new object)
- Consider the Null Object pattern to eliminate nil checks
- Define `to_s`, `to_a`, `to_h` for natural type conversions
- Remember: polymorphism is about substitutability—can object A be used where object B is expected?

## See Also

- [[Object Oriented Programming]]
- [[Inheritance]] — Polymorphism through class hierarchies
- [[Modules as Mixins]] — Polymorphism through shared behavior
- [[Code/Languages/Ruby/Classes|Classes]] — Class fundamentals
- [[Ruby]]
