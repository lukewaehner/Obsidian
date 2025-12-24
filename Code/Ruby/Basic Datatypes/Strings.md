---
tags:
  - ruby
type: note
related:
  - "[[Ruby]]"
  - "[[Input Output]]"
---
# Strings

String creation, manipulation, and common operations in Ruby.

## Overview

Strings in Ruby are mutable sequences of characters. Ruby provides both destructive (mutating) and non-destructive versions of most string methods—destructive methods end with `!`.

## Basic Usage

### Creating Strings

```ruby
# Double quotes (allows interpolation and escape sequences)
"Hello, World!"

# Single quotes (literal, no interpolation)
'Hello, World!'

# Heredoc (multi-line)
<<~TEXT
  This is a
  multi-line string
TEXT

# %Q and %q syntax
%Q(Hello, #{name}!)  # Like double quotes
%q(Hello, World!)    # Like single quotes
```

### Concatenation

```ruby
"Hello" + " World" + "!"  # => "Hello World!"

# Shovel operator (mutates the original)
str = "Hello"
str << " World"           # => "Hello World"

# Concat chaining
"Hello".concat(" World").concat("!")  # => "Hello World!"
```

### Substrings

```ruby
"hello"[0]      # => "h"
"hello"[0..1]   # => "he"  (inclusive range)
"hello"[0...1] # => "h"  (exclusive range)
"hello"[0, 4]   # => "hell" (start index, length)
"hello"[-1]     # => "o"   (negative index)
"hello"[-2..-1] # => "lo"  (last two characters)
```

### Interpolation

Only works in double-quoted strings:

```ruby
name = "Luke"
puts "Hello, #{name}!"       # => Hello, Luke!
puts "2 + 2 = #{2 + 2}"      # => 2 + 2 = 4
puts 'Hello, #{name}!'       # => Hello, #{name}! (no interpolation)
```

### Escape Characters

| Character | Usage           |
|-----------|-----------------|
| `\\`      | Backslash       |
| `\b`      | Backspace       |
| `\r`      | Carriage Return |
| `\n`      | Newline         |
| `\s`      | Space           |
| `\t`      | Tab             |
| `\"`      | Double Quote    |
| `\'`      | Single Quote    |

## Key Concepts

### Mutability

Strings are mutable in Ruby, unlike some languages:

```ruby
str = "hello"
str[0] = "H"
str  # => "Hello"

# Freeze to make immutable
str.freeze
str[0] = "h"  # => FrozenError
```

### Bang Methods (`!`)

Methods ending in `!` modify the string in place:

```ruby
str = "hello"
str.upcase   # => "HELLO" (returns new string)
str          # => "hello" (unchanged)

str.upcase!  # => "HELLO" (mutates in place)
str          # => "HELLO" (changed)
```

### Symbols vs Strings

Symbols are immutable and unique—use them for identifiers:

```ruby
:name.object_id == :name.object_id  # => true (same object)
"name".object_id == "name".object_id  # => false (different objects)

# Convert between them
"hello".to_sym  # => :hello
:hello.to_s     # => "hello"
```

## Common Methods

| Method | Use Case | Example |
|--------|----------|---------|
| `include?(sub)` | Check if substring exists | `"hello".include?("ell")` → `true` |
| `upcase` | Uppercase entire string | `"hello".upcase` → `"HELLO"` |
| `downcase` | Lowercase entire string | `"HELLO".downcase` → `"hello"` |
| `capitalize` | Capitalize first letter | `"hello".capitalize` → `"Hello"` |
| `swapcase` | Swap case of each char | `"Hello".swapcase` → `"hELLO"` |
| `empty?` | Check if string is empty | `"".empty?` → `true` |
| `length` / `size` | Get character count | `"hello".length` → `5` |
| `reverse` | Reverse the string | `"hello".reverse` → `"olleh"` |
| `split(delim)` | Split into array | `"a,b,c".split(",")` → `["a","b","c"]` |
| `strip` | Remove leading/trailing whitespace | `"  hi  ".strip` → `"hi"` |
| `lstrip` / `rstrip` | Remove left/right whitespace | `"  hi".lstrip` → `"hi"` |
| `chomp` | Remove trailing newline | `"hello\n".chomp` → `"hello"` |
| `chop` | Remove last character | `"hello".chop` → `"hell"` |
| `sub(pat, rep)` | Replace first match | `"hello".sub("l","L")` → `"heLlo"` |
| `gsub(pat, rep)` | Replace all matches | `"hello".gsub("l","L")` → `"heLLo"` |
| `insert(i, str)` | Insert at index | `"hello".insert(2, "XX")` → `"heXXllo"` |
| `delete(chars)` | Remove characters | `"hello".delete("l")` → `"heo"` |
| `prepend(str)` | Add to beginning | `"world".prepend("hello ")` → `"hello world"` |
| `chars` | Convert to char array | `"hi".chars` → `["h", "i"]` |
| `bytes` | Convert to byte array | `"hi".bytes` → `[104, 105]` |
| `to_i` | Convert to integer | `"42".to_i` → `42` |
| `to_f` | Convert to float | `"3.14".to_f` → `3.14` |
| `to_sym` | Convert to symbol | `"name".to_sym` → `:name` |

## Common Patterns

### String Formatting

```ruby
# sprintf / format
sprintf("Price: $%.2f", 19.5)   # => "Price: $19.50"
format("ID: %05d", 42)          # => "ID: 00042"

# % operator
"Hello, %s!" % "World"          # => "Hello, World!"
"%.2f" % 3.14159                # => "3.14"
```

### Regex Matching

```ruby
"hello world".match?(/world/)   # => true
"hello world".scan(/\w+/)       # => ["hello", "world"]
"hello world".gsub(/\w+/, &:capitalize)  # => "Hello World"
```

### Building Strings Efficiently

```ruby
# Use array + join for many concatenations
parts = []
parts << "Hello"
parts << "World"
parts.join(" ")  # => "Hello World"

# Or StringIO for very large strings
require 'stringio'
buffer = StringIO.new
buffer << "Hello"
buffer << " World"
buffer.string  # => "Hello World"
```

### Checking Content

```ruby
str = "Hello, World!"

str.start_with?("Hello")  # => true
str.end_with?("!")        # => true
str.match?(/World/)       # => true
str.count("l")            # => 3
str.index("o")            # => 4 (first occurrence)
str.rindex("o")           # => 8 (last occurrence)
```

## Tips

- Use double quotes by default (interpolation is handy even when not immediately needed)
- Prefer `<<` over `+` for building strings in loops (more efficient, avoids creating new objects)
- Use `strip` when processing user input to remove accidental whitespace
- `gsub` accepts blocks: `"hello".gsub(/./) { |c| c.upcase }`
- Use `freeze` on string constants for slight performance gains and safety
- `nil.to_s` returns `""`, useful for safe string conversion

## See Also

- [[Input Output]] — Output methods
- [[Ruby]]
