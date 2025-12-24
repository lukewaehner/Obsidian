---
type: note
tags:
  - ruby
  - rails
  - cli
related:
  - "[[Gemfile]]"
  - "[[Bundler]]"
---
# Creating a New Rails Application

The `rails new` command scaffolds a complete Rails application with sensible defaults.

## Basic Usage

```bash
rails new my_app
```

This generates a standard Rails app with SQLite as the default database.

## Common Options

### Database Selection

Use `-d` to specify your database:

```bash
rails new my_app -d postgresql
rails new my_app -d mysql
```

### Skipping Components

Most options are skippable and can be added back later:

```bash
rails new my_app --skip-test          # Skip Test::Unit (use if adding RSpec)
rails new my_app --skip-action-mailer # Skip email functionality
rails new my_app --skip-javascript    # Skip JS bundling
rails new my_app --minimal            # Minimal install, skip many defaults
```

### API-Only Applications

```bash
rails new my_api --api
```

Creates a slimmed-down app without views, helpers, or assets—ideal for JSON APIs.

## Tips

- Run `rails new --help` to see all available options
- When in doubt, skip less—it's easier to remove than add back
- For new projects, consider starting with `--skip-test` and adding [[RSpec Setup|RSpec]] instead

## See Also

- [[Gemfile]] — Managing dependencies after generation
- [[Bundler]] — How Rails handles gems
- [[Rails]]
