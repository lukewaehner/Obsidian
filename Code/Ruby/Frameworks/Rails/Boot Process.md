---
type: note
tags:
  - ruby
  - rails
  - internals
related:
  - "[[Binstubs]]"
  - "[[Zeitwerk Autoloading]]"
---
# Rails Boot Process

Understanding how Rails boots helps debug startup issues and configure your application correctly.

## Boot Sequence

```
bin/rails → config/boot.rb → config/application.rb → config/environment.rb
```

### 1. `bin/rails`

The entry point for all Rails commands:

```ruby
#!/usr/bin/env ruby
APP_PATH = File.expand_path("../config/application", __dir__)
require_relative "../config/boot"
require "rails/commands"
```

This sets `APP_PATH` and kicks off the boot process.

### 2. `config/boot.rb`

Sets up Bundler and Bootsnap:

```ruby
ENV['BUNDLE_GEMFILE'] ||= File.expand_path('../Gemfile', __dir__)

require 'bundler/setup'    # Load gems from Gemfile
require 'bootsnap/setup'   # Speed up boot with caching
```

After this, all gems in your [[Gemfile|Gemfile]] are available.

### 3. `config/application.rb`

Defines your application module and class:

```ruby
require_relative "boot"
require "rails/all"

Bundler.require(*Rails.groups)

module MyApp
  class Application < Rails::Application
    config.load_defaults 7.0
    
    # Custom configuration here
  end
end
```

### 4. `config/environment.rb`

Initializes the application:

```ruby
require_relative "application"
Rails.application.initialize!
```

## The Application Module

Rails wraps your app in a module (e.g., `MyApp`). This enables:

- Running multiple Rails apps in the same Ruby process
- Namespacing your application code
- Clean separation from Rails internals

## Configuration Precedence

1. `config/application.rb` — Base configuration
2. `config/environments/*.rb` — Environment-specific overrides
3. `config/initializers/*.rb` — Additional configuration (loaded after framework)

## Bootsnap

Bootsnap caches expensive operations to speed up boot time:

- Compilation caching (Ruby bytecode)
- Path caching (file lookups)

Cache is stored in `tmp/cache/bootsnap/`.

## Tips

- Clear bootsnap cache if you see weird loading issues: `rm -rf tmp/cache/bootsnap`
- Use `rails runner "puts 'hello'"` to test if boot works
- Check `config/boot.rb` first when debugging gem loading issues

## See Also

- [[Binstubs]] — How commands enter the boot process
- [[Zeitwerk Autoloading]] — How code gets loaded after boot
- [[Rails]]
