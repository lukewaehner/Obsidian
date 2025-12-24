---
type: note
tags:
  - ruby
  - rails
  - cli
  - tooling
related:
  - "[[Bundler]]"
  - "[[Boot Process]]"
---
# Binstubs

Binstubs are small wrapper scripts in your `bin/` directory that ensure commands run with the correct gem versions from your bundle.

## The Problem They Solve

Without binstubs, you need `bundle exec` to use the right gem versions:

```bash
bundle exec rails server
bundle exec rspec
bundle exec rake db:migrate
```

Binstubs eliminate this friction by wrapping Bundler setup automatically.

## Default Rails Binstubs

Every new Rails project includes:

| Binstub | Purpose |
|---------|---------|
| `bin/rails` | Rails commands (server, console, generate, etc.) |
| `bin/bundle` | Bundler commands |
| `bin/rake` | Rake tasks (often deleted—`rails` handles these now) |
| `bin/importmap` | Importmap-rails commands |
| `bin/setup` | Project setup script |

## Usage

```bash
bin/rails server
bin/rails console
bin/rails generate model User
```

## Adding Custom Binstubs

For gems you use frequently:

```bash
bundle binstubs rspec-core    # Creates bin/rspec
bundle binstubs rubocop       # Creates bin/rubocop
```

## Using direnv for Automatic PATH

Instead of typing `bin/` every time, add `bin` to your PATH with [direnv](https://direnv.net/):

```bash
# .envrc
PATH_add bin
```

Now you can run commands directly:

```bash
rails server    # Actually runs bin/rails server
rspec           # Actually runs bin/rspec
```

## Tips

- You can safely delete `bin/rake`—Rails handles Rake tasks via `bin/rails`
- Commit binstubs to version control
- If binstubs get corrupted, regenerate with `bundle binstubs --force gem_name`

## See Also

- [[Bundler]] — Why version consistency matters
- [[Boot Process]] — What happens when binstubs run
- [[Rails]]
