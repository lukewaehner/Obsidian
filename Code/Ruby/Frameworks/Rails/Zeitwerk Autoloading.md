---
type: note
tags:
  - ruby
  - rails
  - autoloading
  - conventions
related:
  - '[[Rails - Boot Process]]'
---
# Zeitwerk Autoloading

Zeitwerk is Rails' code loader. It automatically loads your classes and modules based on file naming conventions—no `require` statements needed.

## The Core Convention

Class/module names map to file paths using underscores:

| Constant | File Path |
|----------|-----------|
| `User` | `user.rb` |
| `EstimationCalculator` | `estimation_calculator.rb` |
| `KittTurboBoost` | `kitt_turbo_boost.rb` |
| `HTMLParser` | `html_parser.rb` |

## Nested Modules

Namespaces map to directories:

| Constant | File Path |
|----------|-----------|
| `Admin::User` | `admin/user.rb` |
| `Admin::UsersController` | `admin/users_controller.rb` |
| `Api::V1::BaseController` | `api/v1/base_controller.rb` |

## Autoload Paths

By default, Zeitwerk watches:

- `app/models`
- `app/controllers`
- `app/helpers`
- `app/mailers`
- `app/jobs`
- `app/channels`
- And other `app/` subdirectories

Add custom paths in `config/application.rb`:

```ruby
config.autoload_paths << Rails.root.join("lib")
```

## Acronyms and Inflections

By default, `API` becomes `api.rb`. To preserve acronyms:

```ruby
# config/initializers/inflections.rb
ActiveSupport::Inflector.inflections(:en) do |inflect|
  inflect.acronym 'API'
  inflect.acronym 'HTML'
  inflect.acronym 'JSON'
end
```

Now `APIController` maps to `api_controller.rb` (not `a_p_i_controller.rb`).

## Reloading in Development

Zeitwerk reloads code automatically in development. Force a reload:

```ruby
Rails.application.reloader.reload!
```

## Common Gotchas

**File not loading?**
- Check that the filename exactly matches the class name (underscored)
- Verify the file is in an autoload path
- Check for typos in the class definition

**Circular dependency?**
- Use `require_dependency` sparingly, or restructure code
- Consider if classes are too tightly coupled

**Constant not found in production?**
- Zeitwerk uses eager loading in production—all files load at boot
- Run `bin/rails zeitwerk:check` to verify naming

## Debugging

```ruby
# See what Zeitwerk is doing
Rails.autoloaders.main.log!

# Check for naming issues
bin/rails zeitwerk:check
```

## Tips

- Trust the conventions—avoid manual `require` in `app/`
- Keep one class/module per file
- Match the constant name exactly (case-sensitive on some systems)

## See Also

- [[Rails - Boot Process]] — When Zeitwerk initializes
- [[Rails]]
