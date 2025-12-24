---
type: moc
tags:
  - ruby
  - rails
  - web-framework
aliases:
  - rails
---
# Rails

Rails is a full-stack web application framework for Ruby, built on the Model-View-Controller (MVC) pattern. It emphasizes convention over configuration and developer happiness.

## Getting Started

- [[Creating a New Application]] — Scaffolding a new project with `rails new`

## Dependency Management

Rails uses Bundler to manage gem dependencies:

- [[Bundler]] — Ruby's dependency manager
- [[Gemfile]] — Declaring dependencies and version constraints  
- [[Gemfile Lock]] — The resolved dependency tree

## Project Structure & Tooling

- [[Binstubs]] — Wrapper scripts for running commands
- [[Boot Process]] — How Rails initializes your application

## Conventions

- [[Zeitwerk Autoloading]] — Automatic code loading based on naming conventions

## Development Setup

Common additions to new Rails projects:

- [[RSpec Setup]] — BDD testing framework
- [[Haml Setup]] — Clean templating syntax
- [[Console Configuration]] — Customizing the interactive console

## Quick Reference

```bash
# Create new app
rails new my_app -d postgresql

# Common commands
bin/rails server          # Start development server
bin/rails console         # Interactive Ruby with app loaded
bin/rails generate        # Code generators
bin/rails db:migrate      # Run migrations
bin/rails routes          # List all routes
```

## Resources

- [Rails Guides](https://guides.rubyonrails.org/) — Official documentation
- [Rails API](https://api.rubyonrails.org/) — API reference
