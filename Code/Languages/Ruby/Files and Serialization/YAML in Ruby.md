---
tags:
  - ruby
type: note
related:
  - '[[Files and Serialization]]'
  - '[[Serialization]]'
  - '[[JSON in Ruby]]'
  - '[[File IO]]'
  - '[[Ruby]]'
---
# YAML in Ruby

Human-readable serialization format for configuration and data storage.

## Overview

YAML (YAML Ain't Markup Language) is a human-friendly data serialization format. It's widely used in Ruby projects for configuration files (Rails uses it extensively) because it's easy to read and write by hand. YAML supports comments, multi-line strings, and complex nested structures more elegantly than JSON.

## Basic Usage

```ruby
require 'yaml'
```

### Ruby to YAML (Serialization)

```ruby
# Hash to YAML
data = { name: "Alice", age: 30, active: true }
yaml = data.to_yaml
# => "---\n:name: Alice\n:age: 30\n:active: true\n"

puts yaml
# ---
# :name: Alice
# :age: 30
# :active: true

# Array to YAML
list = ["apple", "banana", "cherry"]
puts list.to_yaml
# ---
# - apple
# - banana
# - cherry
```

### YAML to Ruby (Deserialization)

```ruby
yaml_string = <<~YAML
  name: Alice
  age: 30
  active: true
YAML

# Parse YAML (safe method)
data = YAML.safe_load(yaml_string)
# => {"name"=>"Alice", "age"=>30, "active"=>true}

# With symbols permitted
data = YAML.safe_load(yaml_string, permitted_classes: [Symbol], symbolize_names: true)
```

## YAML Syntax

### Basic Types

```yaml
# Strings
name: Alice
quoted: "Hello, World"
single_quoted: 'Also works'

# Numbers
integer: 42
float: 3.14
scientific: 1.0e-5

# Booleans
active: true
disabled: false

# Null
value: null
also_null: ~

# Dates and times
date: 2024-01-15
datetime: 2024-01-15T10:30:00-05:00
```

### Collections

```yaml
# Arrays (lists)
fruits:
  - apple
  - banana
  - cherry

# Inline array
colors: [red, green, blue]

# Hashes (maps)
person:
  name: Alice
  age: 30
  city: Boston

# Inline hash
point: {x: 10, y: 20}
```

### Nested Structures

```yaml
company:
  name: Acme Corp
  employees:
    - name: Alice
      role: Developer
      skills:
        - Ruby
        - Python
    - name: Bob
      role: Designer
      skills:
        - Figma
        - CSS
```

### Multi-line Strings

```yaml
# Literal block (preserves newlines)
description: |
  This is a long description
  that spans multiple lines.
  Newlines are preserved.

# Folded block (joins lines)
summary: >
  This is a long summary
  that will be folded into
  a single line with spaces.

# Preserving trailing newline
with_newline: |
  Has trailing newline

# Stripping trailing newline
no_newline: |-
  No trailing newline
```

### Comments

```yaml
# This is a comment
name: Alice  # Inline comment

# Comments are ignored by the parser
# database:
#   host: old-server.com  # Commented out config
```

## Working with Files

### Read YAML File

```ruby
require 'yaml'

# config.yml:
# database:
#   host: localhost
#   port: 5432
#   name: myapp
# features:
#   dark_mode: true

config = YAML.safe_load(File.read('config.yml'))
# => {"database"=>{"host"=>"localhost", ...}, "features"=>...}

config['database']['host']  # => "localhost"
config['features']['dark_mode']  # => true
```

### Write YAML File

```ruby
require 'yaml'

config = {
  'database' => {
    'host' => 'localhost',
    'port' => 5432,
    'name' => 'myapp'
  },
  'features' => {
    'dark_mode' => true,
    'notifications' => false
  }
}

File.write('config.yml', config.to_yaml)
```

### Load with ERB (Dynamic Config)

```ruby
require 'yaml'
require 'erb'

# config.yml:
# database:
#   host: <%= ENV['DB_HOST'] || 'localhost' %>
#   port: <%= ENV['DB_PORT'] || 5432 %>

template = ERB.new(File.read('config.yml'))
yaml_content = template.result
config = YAML.safe_load(yaml_content)
```

## Security: safe_load vs load

### The Danger of YAML.load

```ruby
# NEVER use YAML.load with untrusted data!
# It can execute arbitrary Ruby code

# Malicious YAML could contain:
# --- !ruby/object:Gem::Installer
# i: x
# --- !ruby/object:Gem::SpecFetcher
# i: y

# This could execute system commands!
YAML.load(untrusted_input)  # DANGEROUS!
```

### Safe Loading

```ruby
# Always use safe_load for untrusted data
YAML.safe_load(yaml_string)

# Permit specific classes if needed
YAML.safe_load(yaml_string, permitted_classes: [Date, Time, Symbol])

# Permit all symbols
YAML.safe_load(yaml_string, permitted_symbols: [], symbolize_names: true)

# For trusted data only (your own config files)
YAML.load_file('config.yml', permitted_classes: [Symbol])  # Ruby 3.1+
```

### Permitted Classes

```ruby
yaml = <<~YAML
  date: 2024-01-15
  time: 2024-01-15 10:30:00 -05:00
YAML

# Without permitted_classes, dates stay as strings
data = YAML.safe_load(yaml)
data['date'].class  # => String

# With permitted_classes
data = YAML.safe_load(yaml, permitted_classes: [Date, Time])
data['date'].class  # => Date
```

## Common Patterns

### Application Configuration

```ruby
# config/database.yml
# development:
#   adapter: postgresql
#   host: localhost
#   database: myapp_dev
#
# production:
#   adapter: postgresql
#   host: <%= ENV['DB_HOST'] %>
#   database: myapp_prod

require 'yaml'
require 'erb'

class Config
  def self.load(file, environment = 'development')
    template = ERB.new(File.read(file))
    yaml = YAML.safe_load(template.result, permitted_classes: [Symbol])
    yaml[environment]
  end
end

db_config = Config.load('config/database.yml', 'production')
```

### Fixtures and Test Data

```yaml
# test/fixtures/users.yml
alice:
  name: Alice Smith
  email: alice@example.com
  admin: true

bob:
  name: Bob Jones
  email: bob@example.com
  admin: false
```

```ruby
users = YAML.safe_load(File.read('test/fixtures/users.yml'))
users['alice']['name']  # => "Alice Smith"
```

### Storing Application State

```ruby
require 'yaml'

class GameState
  attr_accessor :player, :level, :score, :inventory

  def initialize
    @player = "Unknown"
    @level = 1
    @score = 0
    @inventory = []
  end

  def save(filename)
    File.write(filename, to_yaml)
  end

  def self.load(filename)
    return new unless File.exist?(filename)
    YAML.safe_load(
      File.read(filename),
      permitted_classes: [GameState, Symbol]
    )
  end

  def to_yaml
    {
      'player' => @player,
      'level' => @level,
      'score' => @score,
      'inventory' => @inventory
    }.to_yaml
  end
end
```

### Environment-Specific Config

```ruby
# Common Rails pattern
class AppConfig
  def self.settings
    @settings ||= begin
      env = ENV['RACK_ENV'] || 'development'
      path = "config/settings.yml"
      all_settings = YAML.safe_load(File.read(path))
      all_settings[env] || all_settings['default']
    end
  end
end

AppConfig.settings['api_key']
```

## YAML vs JSON

| Feature | YAML | JSON |
|---------|------|------|
| Human readable | Very | Good |
| Comments | Yes | No |
| Multi-line strings | Native | Escape characters |
| File extension | `.yml`, `.yaml` | `.json` |
| Symbol support | Yes | No |
| Primary use | Config files | APIs, data exchange |
| Parsing speed | Slower | Faster |

## Tips

- Use `YAML.safe_load` for any untrusted or external data
- YAML is great for configuration; JSON is better for APIs
- Use ERB templates for dynamic configuration values
- Comments make YAML configs self-documenting
- Indent with 2 spaces (YAML standard)
- Be careful with symbols—they persist in memory
- Use `.yml` extension (Ruby convention) or `.yaml`
- Multi-document YAML files use `---` as separators

## See Also

- [[Files and Serialization]]
- [[Serialization]] — Serialization concepts
- [[JSON in Ruby]] — Alternative format for APIs
- [[File IO]] — Reading/writing YAML files
- [[Ruby]]
