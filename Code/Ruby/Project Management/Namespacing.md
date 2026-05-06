---
tags:
  - ruby
type: note
related:
  - '[[Project Management]]'
  - '[[Require and Require Relative]]'
  - '[[Modules]]'
  - '[[Ruby]]'
---
# Namespacing

Avoiding naming collisions when combining code from multiple files.

## Overview

When you require multiple files, methods, classes, and constants with the same name will collide. Ruby's solution is namespacing with modules—wrapping code in a module to give it a unique prefix. This prevents accidental overwrites and makes code organization clearer.

## The Problem

Without namespacing, later definitions overwrite earlier ones:

```ruby
# file1.rb
def process(data)
  "Processing #{data} with algorithm A"
end

class Parser
  def parse(input)
    "Parsing with simple parser"
  end
end
```

```ruby
# file2.rb
def process(data)
  "Processing #{data} with algorithm B"
end

class Parser
  def parse(input)
    "Parsing with advanced parser"
  end
end
```

```ruby
# main.rb
require_relative 'file1'
require_relative 'file2'

puts process("test")
# => "Processing test with algorithm B" (file1's version is gone!)

puts Parser.new.parse("input")
# => "Parsing with advanced parser" (file1's Parser is overwritten!)
```

## The Solution: Module Namespaces

Wrap code in modules to create unique namespaces:

```ruby
# file1.rb
module File1
  def self.process(data)
    "Processing #{data} with algorithm A"
  end

  class Parser
    def parse(input)
      "Parsing with simple parser"
    end
  end
end
```

```ruby
# file2.rb
module File2
  def self.process(data)
    "Processing #{data} with algorithm B"
  end

  class Parser
    def parse(input)
      "Parsing with advanced parser"
    end
  end
end
```

```ruby
# main.rb
require_relative 'file1'
require_relative 'file2'

puts File1.process("test")
# => "Processing test with algorithm A"

puts File2.process("test")
# => "Processing test with algorithm B"

puts File1::Parser.new.parse("input")
# => "Parsing with simple parser"

puts File2::Parser.new.parse("input")
# => "Parsing with advanced parser"
```

## Basic Usage

### Namespacing Classes

```ruby
# lib/payments/stripe.rb
module Payments
  class Stripe
    def charge(amount)
      "Charging $#{amount} via Stripe"
    end
  end
end

# lib/payments/paypal.rb
module Payments
  class PayPal
    def charge(amount)
      "Charging $#{amount} via PayPal"
    end
  end
end

# main.rb
require_relative 'lib/payments/stripe'
require_relative 'lib/payments/paypal'

stripe = Payments::Stripe.new
paypal = Payments::PayPal.new
```

### Namespacing Methods

Use `self.` to define module-level methods:

```ruby
module StringUtils
  def self.truncate(str, length)
    str.length > length ? str[0...length] + "..." : str
  end

  def self.slugify(str)
    str.downcase.gsub(/\s+/, '-').gsub(/[^a-z0-9-]/, '')
  end
end

StringUtils.truncate("Hello World", 5)  # => "Hello..."
StringUtils.slugify("Hello World!")     # => "hello-world"
```

### Nested Namespaces

```ruby
module MyApp
  module Models
    class User
    end
  end

  module Services
    class AuthService
    end
  end

  module Utils
    module StringHelpers
    end
  end
end

# Access with ::
user = MyApp::Models::User.new
auth = MyApp::Services::AuthService.new
```

### Compact Syntax

```ruby
# These are equivalent:

# Nested style
module MyApp
  module Models
    class User
    end
  end
end

# Compact style (module must already exist)
class MyApp::Models::User
end
```

**Note:** Compact syntax requires parent modules to already be defined.

## Key Concepts

### :: Operator

The scope resolution operator `::` accesses namespaced constants:

```ruby
module Outer
  CONSTANT = "outer"
  
  module Inner
    CONSTANT = "inner"
  end
end

Outer::CONSTANT        # => "outer"
Outer::Inner::CONSTANT # => "inner"

# Leading :: accesses top-level
::String               # Top-level String class (not a namespaced one)
```

### Open Modules

Modules can be reopened across files:

```ruby
# file1.rb
module Utils
  def self.method_a
    "A"
  end
end

# file2.rb
module Utils
  def self.method_b
    "B"
  end
end

# main.rb
require_relative 'file1'
require_relative 'file2'

Utils.method_a  # => "A"
Utils.method_b  # => "B" (both methods are available)
```

### Constants and Namespaces

```ruby
module Config
  DATABASE_URL = "postgres://localhost/myapp"
  API_KEY = "secret123"
  
  module Defaults
    TIMEOUT = 30
    RETRIES = 3
  end
end

Config::DATABASE_URL        # => "postgres://localhost/myapp"
Config::Defaults::TIMEOUT   # => 30
```

## Common Patterns

### Project-Wide Namespace

Most Ruby projects use a single top-level namespace:

```ruby
# lib/my_gem.rb
module MyGem
  VERSION = "1.0.0"
  
  def self.configure
    yield(configuration)
  end
  
  def self.configuration
    @configuration ||= Configuration.new
  end
end

# lib/my_gem/configuration.rb
module MyGem
  class Configuration
    attr_accessor :api_key, :timeout
  end
end

# lib/my_gem/client.rb
module MyGem
  class Client
    def initialize
      @config = MyGem.configuration
    end
  end
end
```

### Include Within Namespace

Selectively expose namespaced methods:

```ruby
module Validators
  def self.email?(str)
    str =~ /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z]+)*\.[a-z]+\z/i
  end
  
  def self.phone?(str)
    str =~ /\A\d{10}\z/
  end
end

class User
  def valid_email?(email)
    Validators.email?(email)
  end
end
```

### Shorthand Access

```ruby
module MyApp
  module Services
    class UserService
    end
  end
end

# Instead of typing MyApp::Services::UserService everywhere:
UserService = MyApp::Services::UserService

service = UserService.new
```

## Tips

- Always namespace your project code under a single top-level module
- Use `::` prefix to access top-level constants when inside a namespace
- Keep namespace depth reasonable (2-3 levels max)
- Match file paths to namespace structure (`MyApp::Models::User` → `my_app/models/user.rb`)
- Reopening modules is fine—it's how Ruby's open classes work
- Use namespaces even for small projects—they scale better

## See Also

- [[Project Management]]
- [[Require and Require Relative]] — Loading namespaced files
- [[Modules]] — Module fundamentals
- [[Ruby]]
