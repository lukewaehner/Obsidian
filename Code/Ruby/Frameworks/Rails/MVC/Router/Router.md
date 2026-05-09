---
tags:
  - ruby
  - rails
  - routing
type: moc
related:
  - '[[Rails]]'
  - '[[REST]]'
  - '[[MVC]]'
---
# Routing

Mapping URLs to controller actions in Rails.

## Overview

The router is the doorman of your Rails application—it examines incoming requests (HTTP verb + URL) and directs them to the appropriate controller action. Routes are defined in `config/routes.rb` and follow RESTful conventions by default.

## Core Concepts

- [[Root Route]] — The homepage and default landing page
- [[RESTful Routes]] — The seven standard CRUD actions
- [[Route Helpers]] — Path and URL helper methods
- [[Custom Routes]] — Non-RESTful and specialized routes

## Quick Reference

```ruby
# config/routes.rb
Rails.application.routes.draw do
  root 'pages#home'              # Homepage
  resources :posts               # All 7 RESTful routes
  resources :users, only: [:show, :index]  # Limited routes
  get 'about', to: 'pages#about' # Custom route
end
```

```bash
# View all routes
bin/rails routes
bin/rails routes --expanded
# Or visit: localhost:3000/rails/info/routes
```

## See Also

- [[REST]] — RESTful architecture concepts
- [[MVC]] — How routing fits into MVC
- [[Rails]]

%% Begin Waypoint %%
- [[Custom Routes]]
- [[RESTful Routes]]
- [[Root Route]]
- [[Route Helpers]]

%% End Waypoint %%
