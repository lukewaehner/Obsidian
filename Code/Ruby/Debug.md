---
tags:
  - ruby
  - debugging
  - tools
type: note
related:
  - '[[Ruby]]'
  - '[[Printing]]'
  - '[[Methods]]'
---
# Pry-byebug

Interactive debugging for Ruby with breakpoints and step-through execution.

## Overview

Pry-byebug combines [Pry](https://pry.github.io/) (an enhanced IRB replacement) with [Byebug](https://github.com/deivid-rodriguez/byebug) (a debugger). The REPL provided by Pry is similar to IRB but with added functionality. Pry-byebug adds step-by-step debugging and stack navigation, making it the recommended Ruby gem for debugging.

## Installation

### Standalone

```bash
gem install pry-byebug
```

### In a Project (Gemfile)

```ruby
group :development, :test do
  gem 'pry-byebug'
end
```

```bash
bundle install
```

## Basic Usage

To use Pry-byebug:

1. Require it at the top of your file
2. Add `binding.pry` where you want to pause execution
3. Run your file normally

```ruby
require 'pry-byebug'

def isogram?(string)
  original_length = string.length
  string_array = string.downcase.split

  binding.pry  # Execution pauses here

  unique_length = string_array.uniq.length
  original_length == unique_length
end

isogram?("Odin")
```

Save this to a file (e.g., `script.rb`) and run it:

```bash
ruby script.rb
```

When execution hits `binding.pry`, it opens an interactive REPL session in your terminal where you can inspect variables and evaluate expressions.

## Understanding Scope at Breakpoints

When paused at a breakpoint, you can only access variables that have been evaluated *before* the `binding.pry` line.

```ruby
require 'pry-byebug'

def yell_greeting(string)
  name = string

  binding.pry

  name = name.upcase
  greeting = "WASSAP, #{name}!"
  puts greeting
end

yell_greeting("bob")
```

In the Pry session:

```
[1] pry(main)> name
=> "bob"           # Available - defined before binding.pry
[2] pry(main)> greeting
=> nil             # Not yet evaluated - defined after binding.pry
```

## Debugger Commands

### Navigation Commands

| Command | Shortcut | Description |
|---------|----------|-------------|
| `next` | `n` | Step over to next line (don't enter methods) |
| `step` | `s` | Step into method call |
| `finish` | `f` | Execute until current method returns |
| `continue` | `c` | Continue execution until next breakpoint |

### Information Commands

| Command | Description |
|---------|-------------|
| `whereami` | Show current location in code |
| `backtrace` | Show call stack |
| `up` | Move up the call stack |
| `down` | Move down the call stack |
| `frame` | Show current frame |

### Breakpoint Commands

| Command | Description |
|---------|-------------|
| `break` | List all breakpoints |
| `break <line>` | Set breakpoint at line number |
| `break <Class#method>` | Set breakpoint at method |
| `delete <n>` | Delete breakpoint number n |

### Other Useful Commands

| Command | Description |
|---------|-------------|
| `exit` | Exit current binding.pry |
| `exit!` | Exit program entirely |
| `help` | Show all available commands |
| `ls` | List methods and variables in scope |
| `cd <object>` | Change context into an object |
| `show-source <method>` | Display source code of a method |

## Step-by-Step Example

```ruby
require 'pry-byebug'

def yell_greeting(string)
  name = string

  binding.pry

  name = name.upcase
  greeting = "WASSAP, #{name}!"
  puts greeting
end

yell_greeting("bob")
```

Session walkthrough:

```
[1] pry(main)> name
=> "bob"
[2] pry(main)> greeting
=> nil
[3] pry(main)> next

     5: def yell_greeting(string)
     6:   name = string
     7:
     8:   binding.pry
     9:
    10:   name = name.upcase
 => 11:   greeting = "WASSAP, #{name}!"
    12:   puts greeting
    13: end

[4] pry(main)> name
=> "BOB"
```

After `next`, the line `name = name.upcase` has been evaluated, so `name` now returns `"BOB"`.

## Common Patterns

### Conditional Breakpoints

```ruby
users.each do |user|
  binding.pry if user.name == "Alice"  # Only pause for Alice
  process(user)
end
```

### Debugging Loops

```ruby
items.each_with_index do |item, i|
  binding.pry if i == 5  # Pause on 6th iteration
  process(item)
end
```

### Quick Inspection

```ruby
def complex_calculation(data)
  result = step_one(data)
  binding.pry  # Check intermediate result
  final = step_two(result)
  final
end
```

### Multiple Breakpoints

```ruby
def process(data)
  binding.pry  # First checkpoint
  
  transformed = transform(data)
  
  binding.pry  # Second checkpoint
  
  save(transformed)
end
```

Use `continue` to move between breakpoints.

## Pry-byebug vs puts Debugging

| Approach      | Pros                        | Cons                            |
| ------------- | --------------------------- | ------------------------------- |
| `puts`        | Simple, no setup            | Must re-run code for each check |
| `binding.pry` | Interactive, explore freely | Requires gem installation       |

For complex code, Pry-byebug is faster—you can explore interactively without adding `puts` statements everywhere and re-running your code each time.

## Tips

- Use `binding.pry` like a breakpoint in JavaScript DevTools
- Type `help` in a Pry session to see all available commands
- Use `ls` to see what methods and variables are available
- Use `whereami` if you lose track of where you are in the code
- Remember: only variables *before* `binding.pry` are in scope
- Use `next` to step over, `step` to step into methods
- Remove all `binding.pry` calls before committing code
- In Rails, `pry-byebug` integrates with `rails console` automatically

## See Also

- [[Printing]] — Basic output debugging with puts
- [[Methods]] — Understanding method execution
- [[Ruby]]
