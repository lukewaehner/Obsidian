---
type: note
tags:
  - ruby
  - rails
  - dependencies
related:
  - "[[Gemfile Lock]]"
  - "[[Bundler]]"
---
# Gemfile

The `Gemfile` is a manifest file at the root of your Rails application that declares all gem dependencies.

## Basic Syntax

```ruby
source 'https://rubygems.org'

gem 'rails', '~> 7.0'
gem 'pg'
gem 'puma'
```

Without a version specifier, Bundler uses the latest stable version.

## Version Constraints

```ruby
gem 'nokogiri', '1.5.6'      # Exact version only
gem 'pry-rails', '>= 0.2.2'  # 0.2.2 or higher
gem 'pry-rails', '> 0.2.2'   # Greater than 0.2.2
gem 'decent_exposure', '~> 2.0.1'  # >= 2.0.1 and < 2.1.0 (pessimistic)
```

### The Pessimistic Operator (`~>`)

This is the most commonly used constraint:

- `~> 2.0` allows `2.x` but not `3.0`
- `~> 2.0.1` allows `2.0.x` but not `2.1.0`

Use pessimistic versioning to get bug fixes while avoiding breaking changes.

## Environment Groups

Load gems only in specific environments:

```ruby
group :development, :test do
  gem 'debug', platforms: %i[mri mingw x64_mingw]
  gem 'rspec-rails'
end

group :development do
  gem 'web-console'
end

group :production do
  gem 'redis'
end
```

## Advanced Options

### Custom Require

When the gem name differs from its require path:

```ruby
gem 'webmock', require: 'webmock/rspec'
```

### Local Development

Point to a local copy of a gem:

```ruby
gem 'nokogiri', path: '~/code/nokogiri'
```

### Git Sources

Pull directly from a repository:

```ruby
gem 'rails', git: 'https://github.com/rails/rails.git', branch: 'main'
```

## Tips

- Keep your Gemfile organized: Rails gems first, then grouped by purpose
- Comment why you're using specific version constraints
- Use `bundle outdated` to see which gems have updates available

## See Also

- [[Gemfile Lock]] — The resolved dependency tree
- [[Bundler]] — How dependencies are managed
- [[Rails]]
