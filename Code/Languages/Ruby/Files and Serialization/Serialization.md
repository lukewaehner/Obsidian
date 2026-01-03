---
tags:
  - ruby
type: note
related:
  - '[[Files and Serialization]]'
  - '[[JSON in Ruby]]'
  - '[[YAML in Ruby]]'
  - '[[File IO]]'
  - '[[Ruby]]'
---
# Serialization

Converting Ruby objects into storable string formats.

## Overview

Serialization is the process of converting complex data structures (objects, arrays, hashes) into a string format that can be stored in files, transmitted over networks, or saved to databases. Deserialization is the reverse—reconstructing objects from those strings. Ruby supports multiple serialization formats, with JSON and YAML being the most common.

## Why Serialize?

```ruby
# Problem: You can't directly save a Ruby object to a file
game_state = {
  player: Player.new("Alice", health: 100),
  inventory: [Sword.new, Shield.new],
  level: 5
}

File.write('save.dat', game_state)  # Doesn't work as expected!
# => Writes "#<Hash:0x00007f...>" (useless)
```

```ruby
# Solution: Serialize to a string format first
require 'json'

game_state = { player: "Alice", health: 100, level: 5 }
json_string = game_state.to_json
File.write('save.json', json_string)  # Now it works!

# Later, deserialize to restore the object
saved = JSON.parse(File.read('save.json'))
# => {"player"=>"Alice", "health"=>100, "level"=>5}
```

## What Serialization Enables

1. **Persistence** — Save program state and restore it later
   - Game saves
   - User preferences
   - Application state

2. **Data Transfer** — Send objects over HTTP (networks only transmit strings)
   - API requests/responses
   - Webhooks
   - Inter-service communication

3. **Configuration** — Store settings in human-readable files
   - Application config
   - Environment settings
   - Build configurations

## Common Formats

| Format | Best For | Human Readable | Ruby Library |
|--------|----------|----------------|--------------|
| JSON | Web APIs, data exchange | Yes | `json` (stdlib) |
| YAML | Config files, complex structures | Very | `yaml` (stdlib) |
| Marshal | Ruby-only binary serialization | No | Built-in |
| CSV | Tabular data | Yes | `csv` (stdlib) |

## Basic Serialization

### JSON

```ruby
require 'json'

# Ruby object → JSON string
data = { name: "Alice", scores: [98, 87, 94] }
json = data.to_json
# => '{"name":"Alice","scores":[98,87,94]}'

# JSON string → Ruby object
parsed = JSON.parse(json)
# => {"name"=>"Alice", "scores"=>[98, 87, 94]}
```

### YAML

```ruby
require 'yaml'

# Ruby object → YAML string
data = { name: "Alice", scores: [98, 87, 94] }
yaml = data.to_yaml
# => "---\n:name: Alice\n:scores:\n- 98\n- 87\n- 94\n"

# YAML string → Ruby object
parsed = YAML.safe_load(yaml, permitted_classes: [Symbol])
# => {:name=>"Alice", :scores=>[98, 87, 94]}
```

### Marshal (Ruby Binary)

```ruby
# Ruby object → binary string
data = { name: "Alice", scores: [98, 87, 94] }
binary = Marshal.dump(data)
# => "\x04\b{\a:\tname...(binary data)"

# Binary string → Ruby object
restored = Marshal.load(binary)
# => {:name=>"Alice", :scores=>[98, 87, 94]}
```

## Serializing to Files

### Save and Load Pattern

```ruby
require 'json'

class GameState
  attr_accessor :player_name, :level, :health, :inventory

  def initialize(player_name)
    @player_name = player_name
    @level = 1
    @health = 100
    @inventory = []
  end

  # Convert to serializable hash
  def to_h
    {
      player_name: @player_name,
      level: @level,
      health: @health,
      inventory: @inventory
    }
  end

  # Save to file
  def save(filename)
    File.write(filename, to_h.to_json)
  end

  # Load from file
  def self.load(filename)
    data = JSON.parse(File.read(filename), symbolize_names: true)
    game = new(data[:player_name])
    game.level = data[:level]
    game.health = data[:health]
    game.inventory = data[:inventory]
    game
  end
end

# Usage
game = GameState.new("Alice")
game.level = 5
game.inventory = ["sword", "shield"]
game.save("savegame.json")

# Later...
loaded_game = GameState.load("savegame.json")
loaded_game.player_name  # => "Alice"
loaded_game.level        # => 5
```

### Configuration Files

```ruby
require 'yaml'

# config.yml:
# database:
#   host: localhost
#   port: 5432
#   name: myapp_production
# features:
#   dark_mode: true
#   notifications: false

config = YAML.safe_load(File.read('config.yml'))
# => {"database"=>{"host"=>"localhost", ...}, "features"=>...}

db_host = config['database']['host']  # => "localhost"
```

## Key Concepts

### What Can Be Serialized?

**JSON supports:**
- Strings, numbers, booleans, null
- Arrays, objects (hashes)
- NOT: symbols, dates, custom classes (directly)

**YAML supports:**
- Everything JSON supports
- Symbols, dates, times
- Multi-line strings, comments
- Custom classes (with care)

**Marshal supports:**
- Almost any Ruby object
- Including custom classes with state
- NOT: IO objects, Procs, lambdas, anonymous classes

### Symbol Handling

```ruby
require 'json'

# JSON converts symbols to strings
data = { name: "Alice" }
json = data.to_json
# => '{"name":"Alice"}'  (key is a string now)

# Parse with symbolized keys
parsed = JSON.parse(json, symbolize_names: true)
# => {:name=>"Alice"}  (keys are symbols again)
```

### Security Considerations

```ruby
# DANGER: Never use YAML.load with untrusted data
# It can execute arbitrary code!
YAML.load(untrusted_string)  # BAD!

# SAFE: Use safe_load instead
YAML.safe_load(untrusted_string)  # GOOD

# For trusted data with custom classes:
YAML.safe_load(data, permitted_classes: [Date, Time, Symbol])
```

## Common Patterns

### Custom to_json

```ruby
class User
  attr_reader :name, :email, :created_at

  def initialize(name, email)
    @name = name
    @email = email
    @created_at = Time.now
  end

  def to_json(*args)
    {
      name: @name,
      email: @email,
      created_at: @created_at.iso8601
    }.to_json(*args)
  end

  def self.from_json(json_string)
    data = JSON.parse(json_string, symbolize_names: true)
    user = new(data[:name], data[:email])
    user
  end
end

user = User.new("Alice", "alice@example.com")
json = user.to_json
# => '{"name":"Alice","email":"alice@example.com","created_at":"2024-01-15T..."}'
```

### Deep Serialization

```ruby
require 'json'

class Team
  attr_accessor :name, :members

  def as_json
    {
      name: @name,
      members: @members.map(&:as_json)
    }
  end

  def to_json(*args)
    as_json.to_json(*args)
  end
end

class Player
  attr_accessor :name, :score

  def as_json
    { name: @name, score: @score }
  end

  def to_json(*args)
    as_json.to_json(*args)
  end
end
```

## Tips

- Use JSON for web APIs and cross-language data exchange
- Use YAML for configuration files (more readable)
- Use Marshal only for Ruby-to-Ruby persistence (version-sensitive)
- Always use `YAML.safe_load` with untrusted data
- Define `to_h` or `as_json` methods for clean serialization of custom classes
- Remember: JSON keys become strings; use `symbolize_names: true` if needed
- Test serialization round-trips: `object == deserialize(serialize(object))`

## See Also

- [[Files and Serialization]]
- [[JSON in Ruby]] — Detailed JSON usage
- [[YAML in Ruby]] — Detailed YAML usage
- [[File IO]] — Reading and writing files
- [[Ruby]]
