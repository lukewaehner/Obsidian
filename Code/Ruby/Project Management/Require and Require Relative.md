---
tags:
  - ruby
type: note
related:
  - '[[Project Management]]'
  - '[[Namespacing]]'
  - '[[Gems and Bundler]]'
  - '[[Ruby]]'
---
# Require and Require Relative

Loading Ruby files and libraries into your program.

## Overview

Ruby uses `require` and `require_relative` to load code from other files. Understanding the difference between them and how Ruby's load path works is essential for organizing multi-file projects.

## require_relative

Loads files relative to the current file's location:

```ruby
# Project structure:
# ├── lib/
# │   ├── sort/
# │   │   ├── bogo_sort.rb
# │   │   ├── bubble_sort.rb
# │   │   └── merge_sort.rb
# │   └── sort.rb
# └── main.rb

# In main.rb (at project root):
require_relative 'lib/sort'

# In lib/sort.rb:
require_relative 'sort/bogo_sort'
require_relative 'sort/bubble_sort'
require_relative 'sort/merge_sort'
```

### Behavior

- Path is relative to the file containing the `require_relative` call
- Returns `true` if file was loaded, `false` if already loaded
- Raises `LoadError` if file doesn't exist
- File extension `.rb` is optional

```ruby
require_relative 'helper'      # Loads helper.rb from same directory
require_relative '../utils'    # Loads utils.rb from parent directory
require_relative 'lib/parser'  # Loads lib/parser.rb relative to current file
```

## require

Loads files from the load path or by absolute path:

```ruby
# Absolute path (starts with /)
require '/home/user/project/lib/helper'

# Relative to current working directory (starts with ./)
require './lib/sort'

# From $LOAD_PATH or installed gems
require 'json'        # Standard library
require 'nokogiri'    # Installed gem
```

### The Load Path ($LOAD_PATH)

Ruby searches for required files in directories listed in `$LOAD_PATH`:

```ruby
puts $LOAD_PATH
# => ["/usr/lib/ruby/3.0.0", "/usr/lib/ruby/gems/...", ...]

# Add a directory to load path
$LOAD_PATH.unshift('./lib')

# Now you can require without path prefix
require 'sort'  # Finds ./lib/sort.rb
```

### Behavior

- Searches `$LOAD_PATH` directories in order
- If not found, searches installed gems
- Returns `true` if loaded, `false` if already loaded
- Raises `LoadError` if not found anywhere

## require vs require_relative

| Aspect | `require` | `require_relative` |
|--------|-----------|-------------------|
| Path basis | `$LOAD_PATH` or absolute | Current file's directory |
| Use for | Gems, stdlib, absolute paths | Project's own files |
| With `./` prefix | Relative to working directory | Not needed |
| Typical usage | External libraries | Internal project files |

```ruby
# For your own project files, prefer require_relative
require_relative 'lib/my_class'

# For gems and standard library, use require
require 'json'
require 'rails'
```

## What Gets Loaded

When you require a file, Ruby executes it and makes available:

**Loaded:**
- Classes and modules
- Constants
- Methods defined at top level
- Global variables

**Not loaded (scoped to original file):**
- Local variables

```ruby
# helper.rb
HELPER_VERSION = "1.0"      # Constant - available after require
$debug_mode = true          # Global - available after require
local_var = "secret"        # Local - NOT available after require

class Helper                 # Class - available after require
  def help
    "Helping!"
  end
end

# main.rb
require_relative 'helper'

puts HELPER_VERSION         # => "1.0"
puts $debug_mode            # => true
puts Helper.new.help        # => "Helping!"
puts local_var              # => NameError: undefined local variable
```

## load vs require

`load` always executes the file, even if previously loaded:

```ruby
require 'helper'   # Executes helper.rb
require 'helper'   # Does nothing (already loaded)

load 'helper.rb'   # Executes helper.rb
load 'helper.rb'   # Executes helper.rb again
```

Use `load` for:
- Reloading code in development
- Configuration files that might change

## Common Patterns

### Entry Point File

Create a main file that requires all components:

```ruby
# lib/my_app.rb
require_relative 'my_app/version'
require_relative 'my_app/config'
require_relative 'my_app/models/user'
require_relative 'my_app/models/post'
require_relative 'my_app/services/auth'

module MyApp
  # Main module code
end
```

### Conditional Requires

```ruby
# Only require if not already loaded
require 'json' unless defined?(JSON)

# Platform-specific requires
if RUBY_PLATFORM =~ /win32/
  require 'win32/process'
else
  require 'posix/spawn'
end
```

### Autoload (Lazy Loading)

```ruby
module MyApp
  autoload :Parser, 'my_app/parser'     # Loaded when MyApp::Parser is first used
  autoload :Formatter, 'my_app/formatter'
end

# Parser isn't loaded yet
MyApp::Parser.new  # NOW parser.rb is loaded
```

## Tips

- Always use `require_relative` for your project's own files
- Use `require` for gems and standard library
- Don't include `.rb` extension (works without it)
- Files are only loaded once per `require`/`require_relative`
- Use a single entry point file to organize requires
- Remember: local variables don't cross file boundaries

## See Also

- [[Project Management]]
- [[Namespacing]] — Avoiding collisions when requiring files
- [[Gems and Bundler]] — Managing external dependencies
- [[Modules]] — Organizing code with modules
- [[Ruby]]
