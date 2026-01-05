---
tags:
  - ruby
  - rails
  - web-framework
type: moc
aliases:
  - rails
related:
  - '[[Ruby]]'
---
# Rails

Rails is a full-stack web application framework for Ruby, built on the Model-View-Controller (MVC) pattern. It emphasizes convention over configuration and developer happiness.

## Getting Started

- [[Creating a New Application]] — Scaffolding a new project with `rails new`

## The Web

Core web concepts for Rails development:

- [[The Web]] — Web fundamentals overview

Architecture:
- [[Code/Languages/Ruby/Frameworks/Rails/The Web/MVC|MVC Concepts]] — Model-View-Controller pattern explained
- [[REST]] — RESTful routing conventions

Fundamentals:
- [[URLs]] — URL components and path helpers
- [[APIs]] — Building and consuming APIs

User State:
- [[Cookies and Sessions]] — Preserving state across requests
- [[Authentication and Authorization]] — Login and access control

## MVC Components

The core building blocks of a Rails application:

- [[Code/Languages/Ruby/Frameworks/Rails/MVC/MVC|MVC]] — MVC architecture overview

- [[Code/Languages/Ruby/Frameworks/Rails/MVC/Controller|Controller]] — Handling requests, params, rendering, and redirecting
- [[Code/Languages/Ruby/Frameworks/Rails/MVC/Views|Views]] — Templates, layouts, and partials
- [[Active Record]] — Models and database interaction
- [[Migrations]] — Database schema changes

## Routing

Mapping URLs to controller actions:

- [[Code/Languages/Ruby/Frameworks/Rails/MVC/Router/Router|Routing]] — Routing overview

- [[Root Route]] — Homepage configuration
- [[RESTful Routes]] — The seven CRUD routes with `resources`
- [[Route Helpers]] — Path and URL helper methods
- [[Custom Routes]] — Non-RESTful and specialized routes

## Deep Knowledge

Rails internals and under-the-hood concepts:

- [[Deep Knowledge]] — Internals overview

Boot & Initialization:
- [[Boot Process]] — How Rails starts up
- [[Binstubs]] — Wrapper scripts for commands

Development:
- [[Development Mode]] — Hot reloading, debugging, dev-specific behavior

Code Loading:
- [[Zeitwerk Autoloading]] — Automatic class loading

## Dependency Management

Rails uses Bundler to manage gem dependencies:

- [[Bundler]] — Ruby's dependency manager
- [[Gemfile]] — Declaring dependencies and version constraints  
- [[Gemfile Lock]] — The resolved dependency tree

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

## See Also

- [[Ruby]]
