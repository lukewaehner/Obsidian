---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Strings]]'
  - '[[Basic Datatypes]]'
---
# Symbols

Immutable, memory-efficient identifiers used throughout Ruby.

## Overview

Symbols are lightweight, immutable identifiers. Unlike strings, each symbol exists only once in memory—every reference to `:foo` points to the exact same object. This makes them ideal for hash keys, method names, and anywhere you need a constant identifier.

## Basic Usage

```ruby
:my_symbol
:name
:user_id
:"with spaces"    # Symbols can contain spaces if quoted
:"hello-world"    # Or special characters
```

### Identity vs Equality

```ruby
# Strings: equal but different objects
"string" == "string"                    # => true
"string".object_id == "string".object_id # => false

# Symbols: equal AND same object
:symbol == :symbol                      # => true
:symbol.object_id == :symbol.object_id  # => true
```

## Key Concepts

### Why Symbols Are Faster

Since symbols are stored once in memory, comparison is instant (comparing object IDs) rather than character-by-character:

```ruby
# String comparison: O(n) - checks each character
"a_very_long_string" == "a_very_long_string"

# Symbol comparison: O(1) - checks object ID
:a_very_long_string == :a_very_long_string
```

### Immutability

Symbols cannot be changed:

```ruby
str = "hello"
str[0] = "H"      # => "Hello" (works)

sym = :hello
sym[0] = "H"      # => NoMethodError (symbols don't support mutation)
```

### Conversion

```ruby
# String to Symbol
"hello".to_sym    # => :hello
"hello".intern    # => :hello (alias)

# Symbol to String
:hello.to_s       # => "hello"
```

## Common Patterns

### Hash Keys

Symbols are the standard choice for hash keys:

```ruby
# Symbol keys (preferred)
user = { name: "Alice", age: 30 }
user[:name]       # => "Alice"

# Equivalent older syntax
user = { :name => "Alice", :age => 30 }

# String keys (less common, but sometimes needed)
data = { "Content-Type" => "application/json" }
```

### Method Names

Ruby methods are internally represented as symbols:

```ruby
class User
  def greet
    "Hello!"
  end
end

User.instance_methods.include?(:greet)  # => true

# Call method dynamically
user = User.new
user.send(:greet)       # => "Hello!"
user.method(:greet).call # => "Hello!"
```

### Options Hashes

```ruby
def configure(options = {})
  host = options[:host] || "localhost"
  port = options[:port] || 3000
  puts "Connecting to #{host}:#{port}"
end

configure(host: "example.com", port: 8080)
```

### Enumerating with Symbols

```ruby
# Symbol to proc - shorthand for calling a method on each element
["hello", "world"].map(&:upcase)    # => ["HELLO", "WORLD"]
[1, 2, 3].reduce(&:+)               # => 6

# Equivalent to:
["hello", "world"].map { |s| s.upcase }
```

### Checking Existence

```ruby
# Check if a symbol exists in memory (rarely needed)
Symbol.all_symbols.include?(:foo)
```

## When to Use Symbols vs Strings

| Use Case | Choice | Why |
|----------|--------|-----|
| Hash keys | Symbol | Faster lookup, cleaner syntax |
| Method/attribute names | Symbol | Ruby convention |
| User input | String | Dynamic, unknown at compile time |
| Display text | String | Mutable, interpolatable |
| API/JSON keys | Either | Often strings from external sources |
| Constants/identifiers | Symbol | Semantic clarity |

## Tips

- Use symbols for things that represent "names" or "labels"
- Use strings for actual text content
- Symbols created from user input stay in memory forever (potential memory leak)—use `to_sym` carefully on untrusted input
- In modern Ruby (2.7+), `Symbol#to_proc` is heavily optimized
- Hash rockets (`:key => value`) are older syntax; prefer `key: value` for symbol keys

## See Also

- [[Strings]] — Mutable text data
- [[Basic Datatypes]] — Overview of Ruby types
- [[Ruby]]
