---
tags:
  - ruby
  - oop
type: note
related:
  - '[[Object Oriented Programming]]'
  - '[[Modules]]'
  - '[[Inheritance]]'
  - '[[Composition]]'
---
# Modules as Mixins

Sharing behavior across classes using module inclusion.

## Overview

Since Ruby only supports single inheritance, modules provide a way to share behavior across unrelated classes. When you `include` a module in a class, its methods become available as instance methods. This is called a "mixin" because you're mixing the module's behavior into your class.

## Basic Usage

### include — Instance Methods

```ruby
module Walkable
  def walk
    "#{self.class} is walking"
  end
end

module Swimmable
  def swim
    "#{self.class} is swimming"
  end
end

class Duck
  include Walkable
  include Swimmable
end

class Person
  include Walkable
end

duck = Duck.new
duck.walk  # => "Duck is walking"
duck.swim  # => "Duck is swimming"

person = Person.new
person.walk  # => "Person is walking"
person.swim  # => NoMethodError
```

### extend — Class Methods

```ruby
module Findable
  def find(id)
    "Finding #{self} with id #{id}"
  end
end

class User
  extend Findable
end

User.find(1)      # => "Finding User with id 1"
User.new.find(1)  # => NoMethodError (not an instance method)
```

### prepend — Override Existing Methods

`prepend` inserts the module *before* the class in the lookup chain:

```ruby
module Logging
  def save
    puts "About to save..."
    super
    puts "Saved!"
  end
end

class Record
  prepend Logging

  def save
    puts "Saving record"
  end
end

Record.new.save
# About to save...
# Saving record
# Saved!
```

## Comparison: include vs extend vs prepend

| Method | Adds methods as | Position in ancestor chain |
|--------|-----------------|---------------------------|
| `include` | Instance methods | After the class |
| `extend` | Class methods | On singleton class |
| `prepend` | Instance methods | Before the class |

```ruby
module M
  def greet
    "Hello from M"
  end
end

class A
  include M
end

class B
  prepend M

  def greet
    "Hello from B"
  end
end

A.ancestors  # => [A, M, Object, ...]
B.ancestors  # => [M, B, Object, ...]

A.new.greet  # => "Hello from M" (M is first match after A)
B.new.greet  # => "Hello from M" (M comes BEFORE B)
```

## Key Concepts

### Method Lookup with Modules

Ruby searches in this order:

1. Prepended modules (most recently prepended first)
2. The class itself
3. Included modules (most recently included first)
4. Parent class (repeat 1-3)

```ruby
module M1
  def speak
    "M1"
  end
end

module M2
  def speak
    "M2"
  end
end

class Animal
  include M1
  include M2  # M2 is searched before M1

  def speak
    "Animal"
  end
end

Animal.ancestors  # => [Animal, M2, M1, Object, ...]
Animal.new.speak  # => "Animal" (class method found first)
```

### Calling Multiple Ancestors with super

```ruby
module Greetable
  def greet
    "Hello! " + super
  end
end

module Nameable
  def greet
    "I have a name. " + super
  end
end

class Person
  include Greetable
  include Nameable

  def greet
    "I am a person. "
  end
end

# Lookup: Person -> Nameable -> Greetable
# But Person#greet doesn't call super, so chain stops

class BetterPerson
  include Greetable
  include Nameable

  def greet
    super + "Nice to meet you!"
  end
end

BetterPerson.new.greet
# => "Hello! I have a name. Nice to meet you!"
# Lookup: BetterPerson -> Nameable -> Greetable
```

### The included Callback

Run code when a module is included:

```ruby
module Trackable
  def self.included(base)
    puts "#{self} was included in #{base}"
    base.extend(ClassMethods)
  end

  module ClassMethods
    def track_field(name)
      attr_accessor name
    end
  end

  def tracked_fields
    # instance method
  end
end

class Order
  include Trackable  # Prints: "Trackable was included in Order"
  track_field :status
end
```

### The extended Callback

```ruby
module Searchable
  def self.extended(base)
    puts "#{self} extended #{base}"
  end

  def search(query)
    "Searching for #{query}"
  end
end

class Product
  extend Searchable  # Prints: "Searchable extended Product"
end
```

### The prepended Callback

```ruby
module Auditable
  def self.prepended(base)
    puts "#{self} prepended to #{base}"
  end
end
```

## Common Patterns

### Both Instance and Class Methods

The classic pattern using `included` hook:

```ruby
module Concerns::Timestamps
  def self.included(base)
    base.extend(ClassMethods)
  end

  module ClassMethods
    def has_timestamps
      attr_accessor :created_at, :updated_at
    end
  end

  # Instance methods
  def touch
    self.updated_at = Time.now
  end

  def fresh?
    updated_at && updated_at > Time.now - 3600
  end
end

class Post
  include Concerns::Timestamps
  has_timestamps
end

post = Post.new
post.touch
post.fresh?  # => true
```

### Using concern (Rails-style)

```ruby
# Rails provides ActiveSupport::Concern for cleaner syntax
module Rateable
  extend ActiveSupport::Concern

  included do
    attr_accessor :rating
  end

  class_methods do
    def top_rated
      # class method
    end
  end

  def rate(value)
    self.rating = value
  end
end
```

### Decorator Pattern with prepend

```ruby
module CachingDecorator
  def expensive_operation
    @cache ||= {}
    @cache[__method__] ||= super
  end
end

class DataProcessor
  prepend CachingDecorator

  def expensive_operation
    sleep(2)  # Simulate slow work
    "result"
  end
end

processor = DataProcessor.new
processor.expensive_operation  # Takes 2 seconds
processor.expensive_operation  # Instant (cached)
```

### Standard Library Mixins

```ruby
# Enumerable — get map, select, reduce, etc. by defining each
class Team
  include Enumerable

  def initialize
    @members = []
  end

  def <<(member)
    @members << member
  end

  def each(&block)
    @members.each(&block)
  end
end

team = Team.new
team << "Alice"
team << "Bob"
team.map(&:upcase)  # => ["ALICE", "BOB"]
team.select { |m| m.start_with?("A") }  # => ["Alice"]
```

```ruby
# Comparable — get <, >, <=, >=, ==, between? by defining <=>
class Version
  include Comparable

  attr_reader :major, :minor, :patch

  def initialize(version_string)
    @major, @minor, @patch = version_string.split('.').map(&:to_i)
  end

  def <=>(other)
    [major, minor, patch] <=> [other.major, other.minor, other.patch]
  end
end

Version.new("2.0.0") > Version.new("1.9.9")  # => true
Version.new("1.0.0").between?(Version.new("0.9"), Version.new("1.1"))  # => true
```

## Tips

- Prefer `include` for behavior that instances need
- Use `extend` for class-level utilities (finders, factories)
- Use `prepend` to wrap/decorate existing methods
- Modules can include other modules
- Keep modules focused—one responsibility per module
- Use `included`/`extended` callbacks for setup logic
- Name modules as adjectives (Comparable, Enumerable) or abilities (Walkable, Searchable)

## See Also

- [[Object Oriented Programming]]
- [[Inheritance]] — Class-based behavior sharing
- [[Composition]] — Object-based behavior sharing
- [[Modules]] — Module basics and namespacing
- [[Ruby]]
