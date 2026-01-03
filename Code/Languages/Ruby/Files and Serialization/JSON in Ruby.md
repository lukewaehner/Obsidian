---
tags:
  - ruby
type: note
related:
  - '[[Files and Serialization]]'
  - '[[Serialization]]'
  - '[[YAML in Ruby]]'
  - '[[File IO]]'
  - '[[Ruby]]'
---
# JSON in Ruby

JavaScript Object Notation for data exchange and web APIs.

## Overview

JSON (JavaScript Object Notation) is the standard format for transmitting data over the web. It's lightweight, human-readable, and supported by virtually every programming language. Ruby's `json` library (part of the standard library) provides seamless conversion between Ruby objects and JSON strings.

## Basic Usage

```ruby
require 'json'
```

### Ruby to JSON (Serialization)

```ruby
# Hash to JSON
data = { name: "Alice", age: 30, active: true }
json = data.to_json
# => '{"name":"Alice","age":30,"active":true}'

# Array to JSON
list = [1, "two", { three: 3 }]
list.to_json
# => '[1,"two",{"three":3}]'

# Primitive types
"hello".to_json    # => '"hello"'
42.to_json         # => '42'
true.to_json       # => 'true'
nil.to_json        # => 'null'
```

### JSON to Ruby (Deserialization)

```ruby
# JSON string to Ruby object
json = '{"name":"Alice","age":30,"active":true}'
data = JSON.parse(json)
# => {"name"=>"Alice", "age"=>30, "active"=>true}

# Access the data
data["name"]    # => "Alice"
data["age"]     # => 30

# Parse with symbol keys
data = JSON.parse(json, symbolize_names: true)
# => {:name=>"Alice", :age=>30, :active=>true}
data[:name]     # => "Alice"
```

## JSON Data Types

| JSON | Ruby |
|------|------|
| `"string"` | `String` |
| `123` / `45.67` | `Integer` / `Float` |
| `true` / `false` | `true` / `false` |
| `null` | `nil` |
| `[1, 2, 3]` | `Array` |
| `{"key": "value"}` | `Hash` |

**Note:** JSON doesn't support:
- Symbols (converted to strings)
- Dates/Times (store as ISO8601 strings)
- Custom Ruby classes (must convert to hashes)

## Working with Files

### Read JSON File

```ruby
require 'json'

# Simple read
data = JSON.parse(File.read('config.json'))

# With error handling
def load_json(path)
  JSON.parse(File.read(path), symbolize_names: true)
rescue Errno::ENOENT
  puts "File not found: #{path}"
  {}
rescue JSON::ParserError => e
  puts "Invalid JSON: #{e.message}"
  {}
end

config = load_json('config.json')
```

### Write JSON File

```ruby
require 'json'

data = {
  users: [
    { name: "Alice", role: "admin" },
    { name: "Bob", role: "user" }
  ],
  settings: { theme: "dark", notifications: true }
}

# Compact (single line)
File.write('data.json', data.to_json)

# Pretty printed (human readable)
File.write('data.json', JSON.pretty_generate(data))
```

### Pretty Printed Output

```ruby
data = { name: "Alice", scores: [98, 87, 94], active: true }

# Compact
data.to_json
# => '{"name":"Alice","scores":[98,87,94],"active":true}'

# Pretty
puts JSON.pretty_generate(data)
# {
#   "name": "Alice",
#   "scores": [
#     98,
#     87,
#     94
#   ],
#   "active": true
# }
```

## Customizing Serialization

### Custom to_json for Classes

```ruby
class User
  attr_reader :name, :email, :created_at

  def initialize(name, email)
    @name = name
    @email = email
    @created_at = Time.now
  end

  # Define what gets serialized
  def as_json
    {
      name: @name,
      email: @email,
      member_since: @created_at.strftime("%Y-%m-%d")
    }
  end

  def to_json(*args)
    as_json.to_json(*args)
  end
end

user = User.new("Alice", "alice@example.com")
user.to_json
# => '{"name":"Alice","email":"alice@example.com","member_since":"2024-01-15"}'
```

### Nested Objects

```ruby
class Team
  attr_accessor :name, :members

  def initialize(name)
    @name = name
    @members = []
  end

  def as_json
    {
      team_name: @name,
      member_count: @members.size,
      members: @members.map(&:as_json)
    }
  end

  def to_json(*args)
    as_json.to_json(*args)
  end
end

class Player
  attr_accessor :name, :score

  def initialize(name, score = 0)
    @name = name
    @score = score
  end

  def as_json
    { name: @name, score: @score }
  end

  def to_json(*args)
    as_json.to_json(*args)
  end
end

team = Team.new("Ruby Rebels")
team.members << Player.new("Alice", 100)
team.members << Player.new("Bob", 85)

puts JSON.pretty_generate(team)
# {
#   "team_name": "Ruby Rebels",
#   "member_count": 2,
#   "members": [
#     { "name": "Alice", "score": 100 },
#     { "name": "Bob", "score": 85 }
#   ]
# }
```

### Deserializing to Objects

```ruby
class User
  attr_accessor :name, :email

  def self.from_json(json_string)
    data = JSON.parse(json_string, symbolize_names: true)
    user = new
    user.name = data[:name]
    user.email = data[:email]
    user
  end
end

json = '{"name":"Alice","email":"alice@example.com"}'
user = User.from_json(json)
user.name   # => "Alice"
user.email  # => "alice@example.com"
```

## API Interactions

### Fetching JSON from Web

```ruby
require 'json'
require 'net/http'
require 'uri'

uri = URI('https://api.example.com/users/1')
response = Net::HTTP.get(uri)
user = JSON.parse(response, symbolize_names: true)

puts user[:name]
```

### Sending JSON to API

```ruby
require 'json'
require 'net/http'
require 'uri'

uri = URI('https://api.example.com/users')
http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true

request = Net::HTTP::Post.new(uri.path)
request['Content-Type'] = 'application/json'
request.body = { name: "Alice", email: "alice@example.com" }.to_json

response = http.request(request)
result = JSON.parse(response.body)
```

## Common Patterns

### Safe Parsing

```ruby
def safe_parse(json_string)
  JSON.parse(json_string, symbolize_names: true)
rescue JSON::ParserError => e
  { error: "Invalid JSON: #{e.message}" }
end

safe_parse('{"valid": true}')  # => {:valid=>true}
safe_parse('not json')         # => {:error=>"Invalid JSON: ..."}
```

### Handling Dates

```ruby
require 'json'
require 'date'

# Serializing
event = {
  name: "Meeting",
  date: Date.today.iso8601,           # "2024-01-15"
  time: Time.now.iso8601              # "2024-01-15T10:30:00-05:00"
}
json = event.to_json

# Deserializing
data = JSON.parse(json)
date = Date.parse(data["date"])       # Back to Date object
time = Time.parse(data["time"])       # Back to Time object
```

### Merging JSON

```ruby
defaults = '{"theme":"light","font_size":14}'
user_prefs = '{"theme":"dark"}'

config = JSON.parse(defaults).merge(JSON.parse(user_prefs))
# => {"theme"=>"dark", "font_size"=>14}
```

## Tips

- Always use `require 'json'` (it's stdlib, but not auto-loaded)
- Use `symbolize_names: true` for cleaner hash access
- Use `JSON.pretty_generate` for human-readable output
- Dates/Times should be stored as ISO8601 strings
- Define `as_json` and `to_json` for custom class serialization
- Wrap `JSON.parse` in error handling for untrusted input
- JSON keys are always strings; symbols are converted

## See Also

- [[Files and Serialization]]
- [[Serialization]] — Serialization concepts
- [[YAML in Ruby]] — Alternative format for config files
- [[File IO]] — Reading/writing JSON files
- [[Ruby]]
