---
tags:
  - ruby
type: note
related: []
---
# Using Multiple Files

A brief description of what this covers.

## Overview

High-level explanation of the concept.

## Basic Usage

```ruby
├── lib
│   ├── sort
│   │   ├── bogo_sort.rb
│   │   ├── bubble_sort.rb
│   │   └── merge_sort.rb
│   └── sort.rb
└── main.rb
```

### require_relative
`require_relative(string)` $\rightarrow$ true or false.
Ruby attempts to load the library named string relative to the directory containing the requiring file.
`LoadError` is raised on no file existing.

```ruby
# In root:
require_relative 'lib/sort'

# In sort.rb:
require_relative 'sort/bogo_sort'
require_relative 'sort/merge_sort'
```

### require
`require(string)` If the feature is an absolute path (starts with `'/'`), the feature will be loaded directly with the absolute path

```ruby
# In main.rb
require './lib/sort'

# In sort.rb
require './lib/sort/bubble_sort'
require './lib/sort/bogo_sort'
```

`$LOAD_PATH`
Looks for files in the global variable which defines

## Key Concepts

Explain the important ideas.

## Common Patterns

```ruby
# Idiomatic Ruby examples
```

## Tips

- Practical advice
- Gotchas to avoid
- Best practices

## See Also

- [[Related Note]]
- [[Ruby]]
