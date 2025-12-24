---
type: note
tags:
  - ruby
  - rails
  - dependencies
related:
  - "[[Gemfile]]"
  - "[[Gemfile Lock]]"
  - "[[Binstubs]]"
---
# Bundler

Bundler is Ruby's dependency manager and comes included with Rails. It ensures your application uses the correct gem versions consistently across all environments.

## Core Responsibilities

- Resolves gem dependencies and their transitive dependencies
- Locks versions to ensure consistency across machines
- Manages gem loading at runtime

## Key Commands

```bash
bundle install    # Install gems from Gemfile.lock (or resolve if missing)
bundle update     # Re-resolve all dependencies and update lock file
bundle update gem_name  # Update only a specific gem
bundle exec       # Run a command in the context of the bundle
```

## How It Works

When you run `bundle install`:

1. Bundler reads your [[Gemfile|Gemfile]]
2. Resolves the dependency tree (finding compatible versions)
3. Writes the resolved versions to [[Gemfile Lock|Gemfile.lock]]
4. Installs any missing gems

## The `bundle exec` Problem

Running commands directly might use the wrong gem version:

```bash
rspec                # Might use system RSpec
bundle exec rspec    # Uses the version from your Gemfile.lock
```

Rails solves this with [[Binstubs|binstubs]]—wrapper scripts that load Bundler first.

## Tips

- Use `bundle install` for day-to-day work
- Use `bundle update` sparingly—it can introduce breaking changes
- When updating, prefer `bundle update gem_name` to update specific gems

## See Also

- [[Gemfile]] — Declaring your dependencies
- [[Gemfile Lock]] — The resolved dependency tree
- [[Binstubs]] — Avoiding `bundle exec`
- [[Rails]]
