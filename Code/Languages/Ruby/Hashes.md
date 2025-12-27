---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Symbols]]'
  - '[[Arrays]]'
---
# Hashes

Key-value pairs for storing and retrieving data by named keys.

## Overview

Hashes (also called dictionaries or maps in other languages) store collections of key-value pairs. Unlike arrays which use integer indices, hashes let you use any object as a key—most commonly symbols or strings.

## Creating Hashes

### Hash Literals

```ruby
# Modern syntax (symbol keys)
person = {
  name: "Alice",
  age: 30,
  city: "Boston"
}

# Rocket syntax (any key type)
scores = {
  "math" => 95,
  "english" => 88,
  :science => 92
}

# Mixed types
mixed = {
  1 => "one",
  :two => 2,
  "three" => [1, 2, 3],
  [1, 2] => "array key"
}
```

### Hash.new

```ruby
hash = Hash.new           # Default value is nil
hash = Hash.new(0)        # Default value is 0
hash = Hash.new { |h, k| h[k] = [] }  # Default is new array per key
```

## Accessing Values

### Basic Access

```ruby
person = { name: "Alice", age: 30 }

person[:name]      # => "Alice"
person[:age]       # => 30
person[:missing]   # => nil (no error)
```

### Safe Access with fetch

```ruby
person.fetch(:name)              # => "Alice"
person.fetch(:missing)           # => KeyError!
person.fetch(:missing, "default") # => "default"
person.fetch(:missing) { |k| "No key: #{k}" }  # => "No key: missing"
```

### Dig for Nested Hashes

```ruby
data = { user: { profile: { name: "Alice" } } }

data[:user][:profile][:name]  # => "Alice"
data[:user][:missing][:name]  # => NoMethodError!

data.dig(:user, :profile, :name)   # => "Alice"
data.dig(:user, :missing, :name)   # => nil (safe)
```

## Modifying Hashes

### Adding and Updating

```ruby
hash = { a: 1 }

hash[:b] = 2           # Add new key
hash[:a] = 10          # Update existing
hash.store(:c, 3)      # Same as hash[:c] = 3

hash  # => { a: 10, b: 2, c: 3 }
```

### Removing

```ruby
hash = { a: 1, b: 2, c: 3 }

hash.delete(:b)        # => 2 (returns deleted value)
hash                   # => { a: 1, c: 3 }

hash.delete(:missing)  # => nil
hash.delete(:missing) { |k| "#{k} not found" }  # => "missing not found"
```

### Merging

```ruby
h1 = { a: 1, b: 2 }
h2 = { b: 20, c: 3 }

h1.merge(h2)   # => { a: 1, b: 20, c: 3 } (h2 wins conflicts)
h1             # => { a: 1, b: 2 } (unchanged)

h1.merge!(h2)  # Mutates h1

# With block for conflict resolution
h1.merge(h2) { |key, old, new| old + new }  # => { a: 1, b: 22, c: 3 }
```

## Iteration

```ruby
hash = { a: 1, b: 2, c: 3 }

# Each pair
hash.each { |key, value| puts "#{key}: #{value}" }

# Just keys or values
hash.each_key { |k| puts k }
hash.each_value { |v| puts v }

# Transform
hash.map { |k, v| [k, v * 2] }.to_h  # => { a: 2, b: 4, c: 6 }
hash.transform_values { |v| v * 2 }  # => { a: 2, b: 4, c: 6 }
hash.transform_keys(&:to_s)          # => { "a" => 1, "b" => 2, "c" => 3 }
```

## Common Methods

| Method | Description | Example |
|--------|-------------|---------|
| `keys` | Array of all keys | `{ a: 1, b: 2 }.keys` → `[:a, :b]` |
| `values` | Array of all values | `{ a: 1, b: 2 }.values` → `[1, 2]` |
| `length` / `size` | Number of pairs | `{ a: 1, b: 2 }.size` → `2` |
| `empty?` | Check if empty | `{}.empty?` → `true` |
| `key?` / `has_key?` | Check key exists | `{ a: 1 }.key?(:a)` → `true` |
| `value?` / `has_value?` | Check value exists | `{ a: 1 }.value?(1)` → `true` |
| `invert` | Swap keys and values | `{ a: 1 }.invert` → `{ 1 => :a }` |
| `to_a` | Convert to array | `{ a: 1 }.to_a` → `[[:a, 1]]` |
| `flatten` | Flatten to array | `{ a: 1, b: 2 }.flatten` → `[:a, 1, :b, 2]` |
| `compact` | Remove nil values | `{ a: 1, b: nil }.compact` → `{ a: 1 }` |
| `slice` | Select specific keys | `{ a: 1, b: 2 }.slice(:a)` → `{ a: 1 }` |
| `except` | Exclude specific keys | `{ a: 1, b: 2 }.except(:a)` → `{ b: 2 }` |

## Key Concepts

### Symbol Keys vs String Keys

```ruby
# Symbols are preferred for hash keys
{ name: "Alice" }      # Symbol key :name
{ "name" => "Alice" }  # String key "name"

# They're different keys!
h = { name: "Alice", "name" => "Bob" }
h[:name]    # => "Alice"
h["name"]   # => "Bob"
```

**Why use symbols?**
- Immutable and unique in memory
- Faster comparison than strings
- Cleaner syntax with modern notation

### The Two Syntaxes

```ruby
# Rocket syntax (works with any key type)
{ :name => "Alice", "age" => 30, 1 => "one" }

# Symbol syntax (only for symbol keys)
{ name: "Alice", age: 30 }

# These are equivalent:
{ :name => "Alice" }
{ name: "Alice" }
```

### Default Values

```ruby
# nil default (standard)
h = {}
h[:missing]  # => nil

# Custom default value
h = Hash.new(0)
h[:count] += 1  # Works! Default is 0
h[:count]       # => 1

# Block default (unique object per key)
h = Hash.new { |hash, key| hash[key] = [] }
h[:items] << "apple"
h[:items] << "banana"
h[:items]  # => ["apple", "banana"]
```

> **Warning**: `Hash.new([])` shares the SAME array for all keys. Use a block for unique defaults.

## Common Patterns

### Counting Occurrences

```ruby
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = Hash.new(0)
words.each { |word| counts[word] += 1 }
counts  # => { "apple" => 3, "banana" => 2, "cherry" => 1 }

# Or use tally (Ruby 2.7+)
words.tally  # => { "apple" => 3, "banana" => 2, "cherry" => 1 }
```

### Grouping

```ruby
people = [
  { name: "Alice", dept: "Engineering" },
  { name: "Bob", dept: "Sales" },
  { name: "Carol", dept: "Engineering" }
]

by_dept = people.group_by { |p| p[:dept] }
# => { "Engineering" => [...], "Sales" => [...] }
```

### Options Hash

```ruby
def connect(host, options = {})
  port = options.fetch(:port, 3000)
  timeout = options.fetch(:timeout, 30)
  ssl = options.fetch(:ssl, false)
  # ...
end

connect("localhost", port: 8080, ssl: true)
```

### Keyword Arguments (Modern Alternative)

```ruby
def connect(host, port: 3000, timeout: 30, ssl: false)
  # ...
end

connect("localhost", port: 8080, ssl: true)
```

### Converting Arrays to Hashes

```ruby
# Array of pairs
[[:a, 1], [:b, 2]].to_h          # => { a: 1, b: 2 }

# Two arrays
keys = [:a, :b, :c]
values = [1, 2, 3]
keys.zip(values).to_h            # => { a: 1, b: 2, c: 3 }

# With block
%w[alice bob].to_h { |name| [name, name.length] }
# => { "alice" => 5, "bob" => 3 }
```

### Double Splat for Hash Arguments

```ruby
def log(message, **options)
  level = options[:level] || :info
  puts "[#{level}] #{message}"
end

opts = { level: :warn, timestamp: true }
log("Something happened", **opts)
```

## Tips

- Use symbol keys (`:name`) over string keys (`"name"`) for performance
- Use `fetch` when a missing key should raise an error
- Use `dig` for safely accessing nested hashes
- Use `Hash.new(0)` for counters, `Hash.new { |h,k| h[k] = [] }` for grouping
- Prefer keyword arguments over options hashes in modern Ruby
- Remember that `merge` returns a new hash; `merge!` mutates

## See Also

- [[Symbols]] — Why symbols make good hash keys
- [[Arrays]] — Ordered collections
- [[Ruby]]
