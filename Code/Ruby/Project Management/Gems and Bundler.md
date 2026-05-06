---
tags:
  - ruby
type: note
related:
  - '[[Project Management]]'
  - '[[Require and Require Relative]]'
  - '[[Ruby]]'
---
# Gems and Bundler

Managing Ruby packages and dependencies.

## Overview

Gems are Ruby's package format—reusable libraries that extend Ruby's functionality. Bundler is the standard tool for managing gem dependencies in Ruby projects, ensuring consistent versions across development, testing, and production environments.

## Gems

### Installing Gems

```bash
# Install a gem globally
gem install nokogiri
gem install rails -v 7.0.0  # Specific version

# List installed gems
gem list

# Show gem info
gem info nokogiri

# Uninstall
gem uninstall nokogiri
```

### Using Gems in Code

```ruby
require 'nokogiri'
require 'httparty'
require 'json'  # Standard library (included with Ruby)

doc = Nokogiri::HTML("<html><body>Hello</body></html>")
response = HTTParty.get('https://api.example.com/data')
```

### Finding Gems

- [RubyGems.org](https://rubygems.org) — Official gem repository
- [Ruby Toolbox](https://www.ruby-toolbox.com) — Categorized gem directory

## Bundler

Bundler manages project-specific gem dependencies via a `Gemfile`.

### Setup

```bash
# Install bundler (if not already installed)
gem install bundler

# Initialize a new project with a Gemfile
bundle init

# Or create Gemfile manually
```

### The Gemfile

```ruby
# Gemfile

# Specify Ruby version (optional but recommended)
ruby '3.2.0'

# Gem sources
source 'https://rubygems.org'

# Dependencies
gem 'rails', '~> 7.0'           # ~> means >= 7.0.0 and < 8.0
gem 'pg', '>= 1.0'              # Any version >= 1.0
gem 'puma', '5.6.4'             # Exact version
gem 'nokogiri'                  # Latest version

# Development/test only gems
group :development, :test do
  gem 'rspec'
  gem 'rubocop'
  gem 'pry'
end

group :development do
  gem 'solargraph'  # LSP for editors
end

group :test do
  gem 'factory_bot'
  gem 'faker'
end

group :production do
  gem 'redis'
end

# Gems from Git
gem 'my_gem', git: 'https://github.com/user/my_gem.git'
gem 'my_gem', git: 'https://github.com/user/my_gem.git', branch: 'develop'

# Local gems (development)
gem 'my_local_gem', path: '../my_local_gem'
```

### Version Constraints

| Syntax | Meaning | Example |
|--------|---------|---------|
| `'1.0'` | Exactly 1.0 | `gem 'rails', '7.0.0'` |
| `'>= 1.0'` | 1.0 or higher | `gem 'pg', '>= 1.0'` |
| `'~> 1.0'` | >= 1.0, < 2.0 | `gem 'rails', '~> 7.0'` |
| `'~> 1.0.0'` | >= 1.0.0, < 1.1.0 | `gem 'puma', '~> 5.6.0'` |
| `'>= 1.0', '< 2.0'` | Range | `gem 'nokogiri', '>= 1.0', '< 2.0'` |

The `~>` (pessimistic) operator is most common—it allows patch updates but not major/minor changes.

### Installing Dependencies

```bash
# Install all gems from Gemfile
bundle install

# Install without development/test gems (for production)
bundle install --without development test

# Update gems
bundle update              # Update all gems
bundle update nokogiri     # Update specific gem

# Show installed gems
bundle list

# Show where a gem is installed
bundle show nokogiri
```

### Gemfile.lock

Bundler creates `Gemfile.lock` to record exact versions:

```
GEM
  remote: https://rubygems.org/
  specs:
    nokogiri (1.14.0)
      mini_portile2 (~> 2.8.0)
    mini_portile2 (2.8.1)

PLATFORMS
  ruby

DEPENDENCIES
  nokogiri

RUBY VERSION
   ruby 3.2.0p0

BUNDLED WITH
   2.4.0
```

**Important:** Always commit `Gemfile.lock` to version control. It ensures everyone uses identical gem versions.

### Running Code with Bundler

```bash
# Run a script with bundled gems
bundle exec ruby my_script.rb

# Run any command with bundled gems
bundle exec rspec
bundle exec rails server

# Start a console with bundled gems
bundle exec irb
```

### In Your Code

```ruby
# At the top of your entry point file
require 'bundler/setup'  # Sets up load path for bundled gems

# Or load all gems from a group
Bundler.require(:default, :development)

# Now all gems are available
require 'nokogiri'
```

## Common Commands

```bash
# Initialize
bundle init                    # Create new Gemfile

# Managing gems
bundle add nokogiri            # Add gem to Gemfile and install
bundle remove nokogiri         # Remove gem from Gemfile
bundle install                 # Install from Gemfile
bundle update                  # Update gems to latest allowed versions

# Information
bundle list                    # List installed gems
bundle show gem_name           # Show gem installation path
bundle outdated                # Show gems with newer versions
bundle info gem_name           # Show gem details

# Execution
bundle exec command            # Run command with bundled gems
bundle console                 # IRB with bundled gems

# Troubleshooting
bundle doctor                  # Check for common issues
bundle pristine                # Restore gems to pristine condition
```

## Common Patterns

### Basic Project Setup

```bash
mkdir my_project
cd my_project
bundle init
bundle add rspec --group test
bundle add pry --group development
```

### Gemfile Organization

```ruby
# Gemfile
source 'https://rubygems.org'

ruby '3.2.0'

# Core dependencies
gem 'pg'
gem 'redis'

# Web framework
gem 'sinatra'
gem 'puma'

# Utilities
gem 'dotenv'
gem 'zeitwerk'

group :development do
  gem 'pry'
  gem 'rubocop'
end

group :test do
  gem 'rspec'
  gem 'rack-test'
end
```

### Requiring Bundled Gems

```ruby
# Option 1: Explicit requires (recommended for libraries)
require 'bundler/setup'
require 'nokogiri'
require 'httparty'

# Option 2: Auto-require all (common in Rails apps)
require 'bundler'
Bundler.require(:default, ENV['RACK_ENV'] || 'development')
```

## Tips

- Always use Bundler for projects with dependencies
- Commit `Gemfile.lock` to version control
- Use `bundle exec` to ensure correct gem versions
- Use `~>` for version constraints to allow safe updates
- Group gems appropriately (development, test, production)
- Run `bundle outdated` periodically to check for updates
- Use `bundle add` instead of manually editing Gemfile
- Pin Ruby version in Gemfile for consistency

## See Also

- [[Project Management]]
- [[Require and Require Relative]] — Loading gems in code
- [[Ruby]]
