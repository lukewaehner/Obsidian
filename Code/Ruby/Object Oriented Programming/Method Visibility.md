---
tags:
  - ruby
  - oop
type: note
related:
  - '[[Object Oriented Programming]]'
  - '[[Encapsulation]]'
  - '[[Class Methods and Variables]]'
  - '[[Code/Languages/Ruby/Classes]]'
---
# Method Visibility

Controlling access to methods with public, private, and protected.

## Overview

Ruby provides three visibility levels for methods: `public`, `private`, and `protected`. Unlike languages like Java, Ruby's visibility is more about communicating intent than enforcing strict access control—methods can always be called using `send`. Understanding when and how to use each level is key to writing clear, maintainable code.

## The Three Visibility Levels

### public (Default)

Callable from anywhere by anyone:

```ruby
class User
  def greet  # public by default
    "Hello!"
  end

  public  # Explicit (rarely needed)

  def farewell
    "Goodbye!"
  end
end

user = User.new
user.greet     # => "Hello!"
user.farewell  # => "Goodbye!"
```

### private

Callable only within the class, without explicit receiver:

```ruby
class BankAccount
  def initialize(balance)
    @balance = balance
  end

  def transfer(amount, to_account)
    return "Insufficient funds" unless can_withdraw?(amount)
    withdraw(amount)
    to_account.deposit(amount)
    "Transferred #{amount}"
  end

  def deposit(amount)
    @balance += amount
  end

  private

  def can_withdraw?(amount)
    @balance >= amount
  end

  def withdraw(amount)
    @balance -= amount
  end
end

account = BankAccount.new(100)
account.transfer(50, other)  # Works
account.withdraw(50)         # NoMethodError: private method
account.can_withdraw?(50)    # NoMethodError: private method
```

### protected

Callable within the class AND by other instances of the same class (or subclasses):

```ruby
class Person
  def initialize(age)
    @age = age
  end

  def older_than?(other)
    age > other.age  # Can call protected method on other person
  end

  protected

  def age
    @age
  end
end

alice = Person.new(30)
bob = Person.new(25)

alice.older_than?(bob)  # => true (protected allows this)
alice.age               # => NoMethodError (can't call from outside)
```

## Declaration Styles

### Section Style

Most common—all methods after the keyword have that visibility:

```ruby
class Example
  def public_one
  end

  def public_two
  end

  private

  def private_one
  end

  def private_two
  end

  protected

  def protected_one
  end
end
```

### Inline Style

Apply visibility to specific methods:

```ruby
class Example
  def method_a
  end

  def method_b
  end

  def method_c
  end

  private :method_b
  protected :method_c
end
```

### Method Definition Style (Ruby 2.1+)

```ruby
class Example
  private def secret_method
    "secret"
  end

  protected def internal_method
    "internal"
  end

  public def open_method
    "open"
  end
end
```

### Return Value Trick

`private` and friends return the method name, enabling:

```ruby
class Example
  # These are equivalent
  def method_a; end
  private :method_a

  # More concise
  private def method_b
  end
end
```

## Private in Depth

### No Explicit Receiver Rule

Private methods cannot be called with an explicit receiver (not even `self`):

```ruby
class Example
  def test
    helper           # Works (implicit self)
    self.helper      # NoMethodError in older Ruby
  end

  private

  def helper
    "helping"
  end
end
```

**Note:** Ruby 2.7+ allows `self.private_method` for calling private methods.

### Private and Inheritance

Private methods ARE inherited but remain private:

```ruby
class Parent
  private

  def secret
    "parent's secret"
  end
end

class Child < Parent
  def reveal
    secret  # Works! Private methods are inherited
  end
end

Child.new.reveal  # => "parent's secret"
Child.new.secret  # => NoMethodError
```

### Private Setters

Private setter methods need explicit `self`:

```ruby
class User
  def initialize(name)
    self.name = name  # Must use self for setter
  end

  def rename(new_name)
    self.name = new_name  # Must use self for setter
  end

  private

  attr_writer :name
  attr_reader :name

  public :name  # Make getter public
end
```

## Protected in Depth

### When to Use Protected

Primarily for comparison operations between instances:

```ruby
class Rectangle
  def initialize(width, height)
    @width = width
    @height = height
  end

  def larger_than?(other)
    area > other.area
  end

  def same_size?(other)
    area == other.area
  end

  protected

  def area
    @width * @height
  end
end

a = Rectangle.new(3, 4)  # area = 12
b = Rectangle.new(2, 5)  # area = 10

a.larger_than?(b)  # => true
a.area             # => NoMethodError
```

### Protected vs Private

| Scenario | private | protected |
|----------|---------|-----------|
| `self.method` | (pre-2.7) / ✓ (2.7+) | ✓ |
| `other.method` (same class) | | ✓ |
| `other.method` (subclass) | | ✓ |
| External call | | |

## Private Class Methods

### private_class_method

```ruby
class Service
  def self.call(params)
    validate!(params)
    execute(params)
  end

  def self.validate!(params)
    raise ArgumentError if params.empty?
  end

  def self.execute(params)
    "Executed with #{params}"
  end

  private_class_method :validate!, :execute
end

Service.call(name: "test")  # Works
Service.validate!({})       # NoMethodError: private method
```

### Alternative: class << self

```ruby
class Service
  class << self
    def call(params)
      validate!(params)
      execute(params)
    end

    private

    def validate!(params)
      raise ArgumentError if params.empty?
    end

    def execute(params)
      "Executed with #{params}"
    end
  end
end
```

## Bypassing Visibility

### send

Calls any method regardless of visibility:

```ruby
class Secret
  private

  def hidden
    "You found me"
  end
end

obj = Secret.new
obj.hidden           # NoMethodError
obj.send(:hidden)    # => "You found me"
```

### public_send

Only calls public methods:

```ruby
obj.public_send(:hidden)  # NoMethodError
obj.public_send(:to_s)    # Works
```

### instance_eval

Execute code in object's context:

```ruby
obj.instance_eval { hidden }  # => "You found me"
```

## Common Patterns

### Reveal Intent with Visibility

```ruby
class OrderProcessor
  # Public API - what users of this class should call
  def process(order)
    validate(order)
    calculate_total(order)
    apply_discounts(order)
    finalize(order)
  end

  private

  # Implementation details - subject to change
  def validate(order)
    # ...
  end

  def calculate_total(order)
    # ...
  end

  def apply_discounts(order)
    # ...
  end

  def finalize(order)
    # ...
  end
end
```

### Testing Private Methods

```ruby
# Option 1: Test through public interface (preferred)
describe OrderProcessor do
  it "processes valid orders" do
    result = processor.process(valid_order)
    expect(result).to be_successful
  end
end

# Option 2: Use send for unit testing internals
describe OrderProcessor do
  it "validates orders" do
    expect {
      processor.send(:validate, invalid_order)
    }.to raise_error(ValidationError)
  end
end

# Option 3: Extract to separate class
class OrderValidator
  def validate(order)  # Now public and testable
    # ...
  end
end
```

### Hook Methods

```ruby
class Plugin
  def self.inherited(subclass)
    register(subclass)
  end

  def self.register(klass)
    (@plugins ||= []) << klass
  end
  private_class_method :register

  def self.plugins
    @plugins || []
  end
end
```

## Tips

- Use `private` for implementation details that shouldn't be called directly
- Use `protected` sparingly—mainly for comparisons between instances
- Visibility is about intent and documentation, not security
- Prefer the section style (`private` on its own line) for clarity
- Test behavior through public interfaces when possible
- Use `send` for testing, but sparingly
- Remember: private methods are inherited
- Consider extracting frequently-tested private methods into separate classes

## See Also

- [[Object Oriented Programming]]
- [[Encapsulation]] — Broader encapsulation concepts
- [[Class Methods and Variables]] — Class-level visibility
- [[Code/Languages/Ruby/Classes|Classes]] — Class fundamentals
- [[Ruby]]
