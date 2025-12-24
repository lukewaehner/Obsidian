---
type: note
tags:
  - ruby
  - rails
  - console
  - development
related:
  - '[[Rails - Boot Process]]'
  - '[[Rails - Gemfile]]'
---
# Rails Console Configuration

The Rails console (`bin/rails console`) loads your entire application environment in an interactive Ruby session. You can customize it for a better development experience.

## Basic Usage

```bash
bin/rails console           # Development environment
bin/rails console -e test   # Test environment
bin/rails console --sandbox # Rollback all changes on exit
```

## Custom Console Helpers

Define helper methods in `config/application.rb` using a `console` block:

```ruby
module MyApp
  class Application < Rails::Application
    console do
      def me
        User.find_by(email: 'dev@example.com')
      end

      def admin
        User.find_by(role: 'admin')
      end
      
      def recent_orders(n = 5)
        Order.order(created_at: :desc).limit(n)
      end
    end
  end
end
```

Now in console:

```ruby
irb> me
=> #<User id: 1, email: "dev@example.com">

irb> recent_orders(3)
=> [#<Order ...>, #<Order ...>, #<Order ...>]
```

## Useful Configurations

Add to your console block or an initializer:

```ruby
console do
  # Colorize output
  ActiveRecord::Base.logger = Logger.new(STDOUT)
  
  # Shorter prompt
  IRB.conf[:PROMPT_MODE] = :SIMPLE
end
```

## Pry Integration

Many developers prefer Pry over IRB. Add to your [[Rails - Gemfile|Gemfile]]:

```ruby
group :development, :test do
  gem 'pry-rails'       # Use Pry as console
  gem 'pry-byebug'      # Add debugging commands
end
```

Now `bin/rails console` opens Pry with:
- Syntax highlighting
- Better history
- `cd` and `ls` for object navigation
- `step`, `next`, `continue` for debugging

## Sandbox Mode

Start console in sandbox to auto-rollback changes:

```bash
bin/rails console --sandbox
```

All database changes are wrapped in a transaction and rolled back on exit. Great for testing destructive operations.

## Tips

- Use `reload!` to reload code changes without restarting
- Use `app.get '/path'` to simulate HTTP requests
- Use `helper.number_to_currency(100)` to test helpers
- Press `Ctrl+R` for reverse history search

## See Also

- [[Rails - Boot Process]] — How the console environment loads
- [[Rails]]
