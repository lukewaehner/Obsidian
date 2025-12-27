---
tags:
  - ruby
  - oop
type: note
related:
  - '[[Object Oriented Programming]]'
  - '[[Inheritance]]'
  - '[[Modules as Mixins]]'
  - '[[Polymorphism]]'
---
# Composition

Building complex objects by combining simpler objects.

## Overview

Composition is the principle of building objects by combining other objects, rather than inheriting behavior. It models "has-a" relationships (a Car *has* an Engine) rather than "is-a" relationships (a Dog *is* an Animal). Composition is often preferred over inheritance because it's more flexible, easier to test, and avoids the fragile base class problem.

## Composition vs Inheritance

### Inheritance ("is-a")

```ruby
class Vehicle
  def start
    "Starting..."
  end
end

class Car < Vehicle
  def drive
    start + " Driving!"
  end
end
```

### Composition ("has-a")

```ruby
class Engine
  def start
    "Engine starting..."
  end
end

class Car
  def initialize
    @engine = Engine.new
  end

  def drive
    @engine.start + " Driving!"
  end
end
```

### When to Choose Which

| Use Inheritance When... | Use Composition When... |
|------------------------|------------------------|
| True "is-a" relationship | "Has-a" or "uses-a" relationship |
| Subclass is a specialization | Behavior can vary independently |
| You control both classes | You want to swap implementations |
| Shallow hierarchy (2-3 levels) | Deep hierarchies would emerge |

## Basic Composition

### Constructor Injection

Pass dependencies when creating the object:

```ruby
class Logger
  def log(message)
    puts "[LOG] #{message}"
  end
end

class UserService
  def initialize(logger)
    @logger = logger
  end

  def create_user(name)
    @logger.log("Creating user: #{name}")
    User.new(name)
  end
end

logger = Logger.new
service = UserService.new(logger)
service.create_user("Alice")
```

### Setter Injection

Set dependencies after creation:

```ruby
class Report
  attr_writer :formatter

  def generate(data)
    formatted = @formatter.format(data)
    "Report: #{formatted}"
  end
end

class HtmlFormatter
  def format(data)
    "<p>#{data}</p>"
  end
end

class JsonFormatter
  def format(data)
    data.to_json
  end
end

report = Report.new
report.formatter = HtmlFormatter.new
report.generate("Hello")  # => "Report: <p>Hello</p>"

report.formatter = JsonFormatter.new
report.generate("Hello")  # => 'Report: "Hello"'
```

### Default Dependencies

```ruby
class Notifier
  def initialize(mailer: Mailer.new, logger: Logger.new)
    @mailer = mailer
    @logger = logger
  end

  def notify(user, message)
    @logger.log("Notifying #{user.email}")
    @mailer.send_email(user.email, message)
  end
end

# Use defaults
notifier = Notifier.new

# Override for testing
notifier = Notifier.new(mailer: MockMailer.new, logger: NullLogger.new)
```

## Delegation

### Manual Delegation

Forward method calls to composed objects:

```ruby
class ShoppingCart
  def initialize
    @items = []
  end

  def add(item)
    @items << item
  end

  def remove(item)
    @items.delete(item)
  end

  def empty?
    @items.empty?
  end

  def size
    @items.size
  end

  def each(&block)
    @items.each(&block)
  end
end
```

### Using Forwardable

Ruby's standard library for delegation:

```ruby
require 'forwardable'

class ShoppingCart
  extend Forwardable

  def_delegators :@items, :size, :empty?, :first, :last, :each
  def_delegator :@items, :<<, :add
  def_delegator :@items, :delete, :remove

  def initialize
    @items = []
  end

  def total
    @items.sum(&:price)
  end
end

cart = ShoppingCart.new
cart.add(item)
cart.size    # Delegated to @items.size
cart.empty?  # Delegated to @items.empty?
```

### SimpleDelegator

Wrap an object and delegate all methods:

```ruby
require 'delegate'

class UserPresenter < SimpleDelegator
  def full_name
    "#{first_name} #{last_name}"
  end

  def created_at_formatted
    created_at.strftime("%B %d, %Y")
  end
end

user = User.new(first_name: "Alice", last_name: "Smith")
presenter = UserPresenter.new(user)

presenter.first_name           # => "Alice" (delegated)
presenter.full_name            # => "Alice Smith" (presenter method)
presenter.created_at_formatted # => "January 15, 2024"
```

## Common Patterns

### Strategy Pattern

Swap algorithms at runtime through composition:

```ruby
class PaymentProcessor
  def initialize(gateway)
    @gateway = gateway
  end

  def process(amount)
    @gateway.charge(amount)
  end
end

class StripeGateway
  def charge(amount)
    "Charged $#{amount} via Stripe"
  end
end

class PayPalGateway
  def charge(amount)
    "Charged $#{amount} via PayPal"
  end
end

# Easy to swap implementations
processor = PaymentProcessor.new(StripeGateway.new)
processor.process(100)  # => "Charged $100 via Stripe"

processor = PaymentProcessor.new(PayPalGateway.new)
processor.process(100)  # => "Charged $100 via PayPal"
```

### Decorator Pattern

Add behavior by wrapping objects:

```ruby
class Coffee
  def cost
    2.0
  end

  def description
    "Coffee"
  end
end

class MilkDecorator
  def initialize(beverage)
    @beverage = beverage
  end

  def cost
    @beverage.cost + 0.5
  end

  def description
    @beverage.description + " + milk"
  end
end

class SugarDecorator
  def initialize(beverage)
    @beverage = beverage
  end

  def cost
    @beverage.cost + 0.25
  end

  def description
    @beverage.description + " + sugar"
  end
end

coffee = Coffee.new
coffee = MilkDecorator.new(coffee)
coffee = SugarDecorator.new(coffee)

coffee.cost         # => 2.75
coffee.description  # => "Coffee + milk + sugar"
```

### Null Object Pattern

Avoid nil checks with a "do nothing" object:

```ruby
class RealLogger
  def log(message)
    puts "[#{Time.now}] #{message}"
  end
end

class NullLogger
  def log(message)
    # Do nothing
  end
end

class Service
  def initialize(logger: NullLogger.new)
    @logger = logger
  end

  def perform
    @logger.log("Starting...")  # Safe to call, no nil check needed
    # ...
    @logger.log("Done!")
  end
end

# With logging
Service.new(logger: RealLogger.new).perform

# Without logging (no conditional logic needed)
Service.new.perform
```

### Repository Pattern

Abstract data access through composition:

```ruby
class UserRepository
  def initialize(database)
    @database = database
  end

  def find(id)
    @database.query("SELECT * FROM users WHERE id = ?", id)
  end

  def save(user)
    @database.execute("INSERT INTO users...", user.attributes)
  end
end

class PostgresDatabase
  def query(sql, *params)
    # Real database query
  end

  def execute(sql, *params)
    # Real database execution
  end
end

class InMemoryDatabase
  def initialize
    @data = {}
  end

  def query(sql, *params)
    # Return from @data
  end

  def execute(sql, *params)
    # Store in @data
  end
end

# Production
repo = UserRepository.new(PostgresDatabase.new)

# Testing
repo = UserRepository.new(InMemoryDatabase.new)
```

### Builder Pattern

Construct complex objects step by step:

```ruby
class Computer
  attr_accessor :cpu, :ram, :storage, :gpu

  def specs
    "CPU: #{cpu}, RAM: #{ram}, Storage: #{storage}, GPU: #{gpu}"
  end
end

class ComputerBuilder
  def initialize
    @computer = Computer.new
  end

  def set_cpu(cpu)
    @computer.cpu = cpu
    self
  end

  def set_ram(ram)
    @computer.ram = ram
    self
  end

  def set_storage(storage)
    @computer.storage = storage
    self
  end

  def set_gpu(gpu)
    @computer.gpu = gpu
    self
  end

  def build
    @computer
  end
end

computer = ComputerBuilder.new
  .set_cpu("Intel i9")
  .set_ram("32GB")
  .set_storage("1TB SSD")
  .set_gpu("RTX 4080")
  .build

computer.specs
# => "CPU: Intel i9, RAM: 32GB, Storage: 1TB SSD, GPU: RTX 4080"
```

## Key Concepts

### Dependency Inversion

Depend on abstractions, not concrete implementations:

```ruby
# Bad: Hard dependency
class OrderService
  def initialize
    @mailer = SmtpMailer.new  # Concrete class
  end
end

# Good: Injected dependency
class OrderService
  def initialize(mailer)
    @mailer = mailer  # Any object with send_email method
  end
end
```

### Favor Composition Over Inheritance

The classic OOP advice exists because composition:

- Avoids tight coupling to parent class
- Makes dependencies explicit
- Allows runtime behavior changes
- Simplifies testing with mock objects
- Prevents fragile base class problems

```ruby
# Inheritance: Tightly coupled
class AdminUser < User
  # Inherits everything, even what we don't want
end

# Composition: Explicit and flexible
class AdminUser
  def initialize(user, admin_permissions)
    @user = user
    @permissions = admin_permissions
  end

  def can?(action)
    @permissions.allows?(action)
  end
end
```

## Tips

- Prefer constructor injection for required dependencies
- Use setter injection for optional dependencies
- Provide sensible defaults where appropriate
- Use `Forwardable` to reduce delegation boilerplate
- Think "has-a" before "is-a"
- Composition makes unit testing easier—inject mocks
- Small, focused classes compose better than large ones
- If you're inheriting just to reuse code, consider composition instead

## See Also

- [[Object Oriented Programming]]
- [[Inheritance]] — When "is-a" is appropriate
- [[Modules as Mixins]] — Another way to share behavior
- [[Polymorphism]] — Duck typing enables composition
- [[Ruby]]
