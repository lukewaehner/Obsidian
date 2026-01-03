---
tags:
  - ruby
type: moc
related:
  - '[[Ruby]]'
---
# Project Management

Managing Ruby project structure, dependencies, and file organization.

## Overview

Ruby projects require organizing code across multiple files, managing external dependencies, and structuring directories for maintainability. This section covers the tools and patterns for professional Ruby project management.

## File Organization

- [[Require and Require Relative]] — Loading Ruby files and understanding load paths
- [[Namespacing]] — Avoiding naming collisions with modules

## Dependency Management

- [[Gems and Bundler]] — Installing and managing external packages

## Typical Project Structure

```
my_project/
├── lib/                    # Main application code
│   ├── my_project.rb       # Entry point, requires other files
│   └── my_project/
│       ├── models/
│       ├── services/
│       └── utils/
├── bin/                    # Executable scripts
├── spec/ or test/          # Tests
├── Gemfile                 # Dependency declarations
├── Gemfile.lock            # Locked dependency versions
├── README.md
└── my_project.gemspec      # If building a gem
```

## See Also

- [[Ruby]]
- [[Modules]] — Module basics for namespacing
