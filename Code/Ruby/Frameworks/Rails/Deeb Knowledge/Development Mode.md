---
tags:
  - ruby
  - rails
  - development
type: note
related:
  - '[[Deep Knowledge]]'
  - '[[Boot Process]]'
  - '[[Rails]]'
---
# Development Mode

How Rails behaves differently in development for faster iteration.

## Overview

Rails development mode prioritizes developer convenience over performance. Code reloads automatically, errors show detailed debugging information, and caching is disabled by default. Understanding these behaviors helps you develop efficiently and avoid confusion when deploying to production.

## Key Development Behaviors

### Code Reloading

Rails automatically reloads your code when files change:

```ruby
# config/environments/development.rb
config.cache_classes = false           # Reload classes on each request
config.eager_load = false              # Load code on demand, not at boot
config.file_watcher = ActiveSupport::EventedFileUpdateChecker
```

**How it works:**
- Zeitwerk watches for file changes
- On the next request, modified classes are unloaded and reloaded
- No server restart needed

**Force a reload in console:**
```ruby
reload!
```

### Detailed Error Pages

Development shows full stack traces with source code:

```ruby
config.consider_all_requests_local = true
```

Includes:
- Full exception backtrace
- Source code snippets
- Request parameters
- Session data

### Asset Handling

Assets compile on-demand without concatenation:

```ruby
config.assets.debug = true              # Serve each file separately
config.assets.quiet = true              # Silence asset request logs
```

### Caching (Disabled by Default)

```ruby
config.action_controller.perform_caching = false
```

Toggle caching temporarily:
```bash
bin/rails dev:cache
# Creates/removes tmp/caching-dev.txt
```

Check if caching is enabled:
```ruby
Rails.application.config.action_controller.perform_caching
```

## Configuration

### Full Development Config

```ruby
# config/environments/development.rb
Rails.application.configure do
  # Code reloading
  config.cache_classes = false
  config.eager_load = false
  
  # Error handling
  config.consider_all_requests_local = true
  
  # Caching
  config.action_controller.perform_caching = false
  config.cache_store = :null_store
  
  # Action Mailer
  config.action_mailer.raise_delivery_errors = true
  config.action_mailer.perform_caching = false
  config.action_mailer.default_url_options = { host: 'localhost', port: 3000 }
  
  # Active Storage
  config.active_storage.service = :local
  
  # Logging
  config.log_level = :debug
  
  # Raise on missing translations
  config.i18n.raise_on_missing_translations = true
  
  # Raise on unpermitted params
  config.action_controller.raise_on_unpermitted_parameters = true
  
  # Annotate rendered views with file names
  config.action_view.annotate_rendered_view_with_filenames = true
end
```

### Environment Detection

```ruby
Rails.env.development?  # => true
Rails.env               # => "development"

# Conditional code
if Rails.env.development?
  # Development-only behavior
end

# In views
<% if Rails.env.development? %>
  <%= debug @user %>
<% end %>
```

## Common Tools

### Debug Output

```erb
<!-- In views -->
<%= debug @user %>
<%= @user.inspect %>

<!-- Pretty print -->
<pre><%= JSON.pretty_generate(@user.as_json) %></pre>
```

```ruby
# In controllers/models
Rails.logger.debug "User: #{@user.inspect}"
pp @user  # Pretty print
```

### Rails Console

```bash
bin/rails console
# or
bin/rails c
```

```ruby
# In console
User.first                    # Query database
app.get '/users'              # Make request
helper.link_to 'Home', '/'    # Test helpers
reload!                       # Reload code
```

### Rails Server

```bash
bin/rails server              # Default port 3000
bin/rails s -p 4000           # Custom port
bin/rails s -b 0.0.0.0        # Bind to all interfaces
```

### Database Commands

```bash
bin/rails db:migrate          # Run migrations
bin/rails db:rollback         # Undo last migration
bin/rails db:seed             # Run seeds
bin/rails db:reset            # Drop, create, migrate, seed
```

## Common Patterns

### Development-Only Gems

```ruby
# Gemfile
group :development do
  gem 'web-console'           # In-browser console on error pages
  gem 'rack-mini-profiler'    # Performance insights
  gem 'better_errors'         # Enhanced error pages
  gem 'binding_of_caller'     # REPL in error pages
end

group :development, :test do
  gem 'debug'                 # Debugger
  gem 'pry-rails'             # Better console
  gem 'factory_bot_rails'     # Test factories
end
```

### Debugging with debug gem

```ruby
# Add to code
debugger  # Execution stops here

# In terminal
(rdbg) n           # Next line
(rdbg) c           # Continue
(rdbg) p @user     # Print variable
(rdbg) bt          # Backtrace
```

### Web Console

```erb
<!-- In views during errors, or add explicitly: -->
<% console %>

<!-- Opens interactive console in browser -->
```

## Development vs Production

| Aspect | Development | Production |
|--------|-------------|------------|
| Code reloading | On every request | Never (cached) |
| Eager loading | Off (lazy) | On (at boot) |
| Error pages | Detailed | Generic |
| Asset compilation | On-demand | Precompiled |
| Caching | Off by default | On |
| Logging | Debug level | Info level |

## Tips

- Use `reload!` in console after changing code
- Run `bin/rails dev:cache` to test caching locally
- Use `better_errors` gem for enhanced error pages
- Add `debugger` anywhere to pause execution
- Check `log/development.log` for detailed request logs
- Use `Rails.logger.debug` for temporary debugging output
- Remember: development behavior differs significantly from production

## See Also

- [[Deep Knowledge]] — Rails internals overview
- [[Boot Process]] — How Rails initializes
- [[Rails]]
