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
# Encapsulation

Controlling access to an object's internal state and behavior.

## Overview

Encapsulation is the practice of hiding an object's internal details and exposing only what's necessary through a public interface. In Ruby, this is achieved through method visibility (`public`, `private`, `protected`) and accessor methods. Unlike some languages, Ruby's encapsulation is more about convention and intent than strict enforcement.

## Method Visibility

### public (Default)

Methods are public by default—callable from anywhere:

```ruby
class User
  def greet
    "Hello!"
  end
end

User.new.greet  # => "Hello!"
```

### private

Private methods can only be called within the class, without an explicit receiver:

```ruby
class BankAccount
  def initialize(balance)
    @balance = balance
  end

  def withdraw(amount)
    return "Insufficient funds" unless sufficient_funds?(amount)
    @balance -= amount
    "Withdrew #{amount}. Balance: #{@balance}"
  end

  def balance
    format_currency(@balance)
  end

  private

  def sufficient_funds?(amount)
    @balance >= amount
  end

  def format_currency(amount)
    "$#{'%.2f' % amount}"
  end
end

account = BankAccount.new(100)
account.withdraw(30)            # => "Withdrew 30. Balance: 70"
account.balance                 # => "$70.00"
account.sufficient_funds?(50)   # => NoMethodError: private method
account.format_currency(50)     # => NoMethodError: private method
```

### protected

Protected methods can be called by instances of the same class or subclasses:

```ruby
class Person
  def initialize(age)
    @age = age
  end

  def older_than?(other)
    age > other.age  # Can call protected method on other
  end

  protected

  def age
    @age
  end
end

alice = Person.new(30)
bob = Person.new(25)

alice.older_than?(bob)  # => true
alice.age               # => NoMethodError: protected method
```

## Visibility Declaration Styles

### Block Style (Most Common)

```ruby
class Example
  def public_method
    "I'm public"
  end

  private

  def private_method
    "I'm private"
  end

  def another_private_method
    "Also private"
  end

  protected

  def protected_method
    "I'm protected"
  end
end
```

### Inline Style

```ruby
class Example
  def method_a
    "public"
  end

  def method_b
    "will be private"
  end

  def method_c
    "will be protected"
  end

  private :method_b
  protected :method_c
end
```

### Definition Style (Ruby 2.1+)

```ruby
class Example
  private def secret_method
    "I'm private"
  end

  protected def internal_method
    "I'm protected"
  end
end
```

## Accessor Methods

### The Problem with Direct Access

```ruby
class User
  def initialize(name)
    @name = name
  end
end

user = User.new("Alice")
user.name        # => NoMethodError (no accessor)
user.name = "Bob" # => NoMethodError (no accessor)
```

### attr_reader, attr_writer, attr_accessor

```ruby
class User
  attr_reader :id           # Getter only
  attr_writer :password     # Setter only
  attr_accessor :name       # Both getter and setter

  def initialize(id, name)
    @id = id
    @name = name
  end
end

user = User.new(1, "Alice")
user.id              # => 1
user.id = 2          # => NoMethodError
user.name            # => "Alice"
user.name = "Bob"    # => "Bob"
user.password = "secret"  # Works
user.password        # => NoMethodError
```

### What Accessors Generate

```ruby
# attr_reader :name generates:
def name
  @name
end

# attr_writer :name generates:
def name=(value)
  @name = value
end

# attr_accessor :name generates both
```

### Custom Accessors with Validation

```ruby
class Product
  attr_reader :name, :price

  def initialize(name, price)
    @name = name
    self.price = price  # Use setter for validation
  end

  def price=(value)
    raise ArgumentError, "Price must be positive" if value < 0
    @price = value
  end
end

product = Product.new("Widget", 10)
product.price = -5  # => ArgumentError: Price must be positive
```

### Private Accessors

```ruby
class Person
  def initialize(ssn)
    @ssn = ssn
  end

  def masked_ssn
    "XXX-XX-#{ssn[-4..]}"
  end

  private

  attr_reader :ssn
end

person = Person.new("123-45-6789")
person.masked_ssn  # => "XXX-XX-6789"
person.ssn         # => NoMethodError: private method
```

## Key Concepts

### Private Doesn't Mean Invisible

Ruby's `private` is about intent, not security:

```ruby
class Secret
  private

  def hidden
    "You found me"
  end
end

secret = Secret.new
secret.hidden          # => NoMethodError
secret.send(:hidden)   # => "You found me" (bypasses private)
```

### Private Class Methods

```ruby
class Utility
  def self.public_helper
    private_helper
  end

  def self.private_helper
    "I'm private"
  end

  private_class_method :private_helper
end

Utility.public_helper   # => "I'm private"
Utility.private_helper  # => NoMethodError
```

### Private vs Protected

| Aspect | private | protected |
|--------|---------|-----------|
| Called on self? | Yes (implicit only) | Yes |
| Called on other instances? | No | Yes (same class/subclass) |
| Main use case | Internal helpers | Comparing instances |

```ruby
class Document
  def initialize(content)
    @content = content
  end

  def longer_than?(other)
    word_count > other.word_count  # Works because protected
  end

  def preview
    truncate(@content)  # Works because we call on self
  end

  protected

  def word_count
    @content.split.size
  end

  private

  def truncate(text)
    text[0..100] + "..."
  end
end
```

## Common Patterns

### Exposing Read-Only Data

```ruby
class Order
  attr_reader :id, :items, :created_at

  def initialize
    @id = SecureRandom.uuid
    @items = []
    @created_at = Time.now
  end

  def add_item(item)
    @items << item
    calculate_total
  end

  def total
    @total
  end

  private

  def calculate_total
    @total = @items.sum(&:price)
  end
end
```

### Immutable Value Objects

```ruby
class Money
  attr_reader :amount, :currency

  def initialize(amount, currency = "USD")
    @amount = amount.freeze
    @currency = currency.freeze
    freeze  # Make entire object immutable
  end

  def +(other)
    raise "Currency mismatch" unless currency == other.currency
    Money.new(amount + other.amount, currency)
  end

  def to_s
    "#{currency} #{amount}"
  end
end

money = Money.new(100, "USD")
money.amount = 200  # => FrozenError
```

### Builder Pattern with Private Setters

```ruby
class EmailBuilder
  def initialize
    @to = []
    @cc = []
  end

  def to(address)
    @to << address
    self
  end

  def cc(address)
    @cc << address
    self
  end

  def subject(text)
    @subject = text
    self
  end

  def body(text)
    @body = text
    self
  end

  def build
    Email.new(@to, @cc, @subject, @body)
  end
end

email = EmailBuilder.new
  .to("alice@example.com")
  .cc("bob@example.com")
  .subject("Hello")
  .body("Hi there!")
  .build
```

## Tips

- Default to `attr_reader`; only add writers when mutation is truly needed
- Use `private` for internal implementation details
- Use `protected` sparingly—mainly for comparing instances
- Custom setters allow validation and transformation
- Remember: `private` is about communicating intent, not enforcing security
- Consider freezing objects for true immutability
- Use `send` for testing private methods, but sparingly

## See Also

- [[Object Oriented Programming]]
- [[Method Visibility]] — Deep dive on access control
- [[Code/Languages/Ruby/Classes|Classes]] — Class fundamentals
- [[Ruby]]
