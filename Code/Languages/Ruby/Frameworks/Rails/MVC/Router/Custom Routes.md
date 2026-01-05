---
tags:
  - ruby
  - rails
  - routing
type: note
related:
  - "[[Model]]"
  - "[[RESTful Routes]]"
  - "[[Route Helpers]]"
  - "[[Rails]]"
---
# Custom Routes

Non-RESTful routes and specialized routing patterns.

## Overview

While RESTful `resources` routes handle most cases, sometimes you need custom routes for non-CRUD actions, static pages, or special URL structures. Rails provides flexible routing methods for these cases.

## Basic Custom Routes

```ruby
# config/routes.rb

# HTTP verb + path + destination
get "about", to: "pages#about"
get "contact", to: "pages#contact"
post "contact", to: "pages#submit_contact"

# Shorthand when path matches action
get "pages/terms"  # => PagesController#terms at /pages/terms
```

## Named Routes

Give custom routes a name for helper generation:

```ruby
get "login", to: "sessions#new", as: :login
get "logout", to: "sessions#destroy", as: :logout
get "signup", to: "registrations#new", as: :signup

# Generates helpers:
# login_path   => "/login"
# logout_path  => "/logout"
# signup_path  => "/signup"
```

```erb
<%= link_to "Sign In", login_path %>
<%= link_to "Sign Up", signup_path %>
```

## Member and Collection Routes

Add custom actions to resourceful routes:

### Member Routes (Act on One Record)

```ruby
resources :posts do
  member do
    post :publish      # POST /posts/:id/publish
    post :unpublish    # POST /posts/:id/unpublish
    get :preview       # GET /posts/:id/preview
  end
end

# Shorthand for single route
resources :posts do
  post :publish, on: :member
end
```

```ruby
# Controller
def publish
  @post = Post.find(params[:id])
  @post.publish!
  redirect_to @post
end

# Helpers
publish_post_path(@post)    # => "/posts/42/publish"
preview_post_path(@post)    # => "/posts/42/preview"
```

### Collection Routes (Act on All Records)

```ruby
resources :posts do
  collection do
    get :search        # GET /posts/search
    get :drafts        # GET /posts/drafts
    get :published     # GET /posts/published
    delete :clear_all  # DELETE /posts/clear_all
  end
end

# Shorthand
resources :posts do
  get :search, on: :collection
end
```

```ruby
# Controller
def search
  @posts = Post.search(params[:q])
end

def drafts
  @posts = Post.draft
end

# Helpers (no ID needed)
search_posts_path           # => "/posts/search"
drafts_posts_path           # => "/posts/drafts"
search_posts_path(q: "ruby") # => "/posts/search?q=ruby"
```

## Namespace and Scope

### Namespace

Prefixes path AND expects namespaced controller:

```ruby
namespace :admin do
  resources :posts
  resources :users
end
```

| Route | Controller |
|-------|------------|
| `/admin/posts` | `Admin::PostsController` |
| `/admin/users` | `Admin::UsersController` |

```ruby
# app/controllers/admin/posts_controller.rb
module Admin
  class PostsController < ApplicationController
    # ...
  end
end

# Helpers
admin_posts_path      # => "/admin/posts"
admin_post_path(@post) # => "/admin/posts/42"
```

### Scope

Prefix path only (no controller namespace):

```ruby
scope "/admin" do
  resources :posts
end
```

| Route | Controller |
|-------|------------|
| `/admin/posts` | `PostsController` (not namespaced) |

### Module Scope

Controller namespace only (no path prefix):

```ruby
scope module: :admin do
  resources :posts
end
```

| Route | Controller |
|-------|------------|
| `/posts` | `Admin::PostsController` |

### Custom Path Names

```ruby
# Change URL but keep helper names
resources :posts, path: "articles"
# /articles, /articles/:id, etc.
# But helpers are still: posts_path, post_path(@post)

# Change both path and helpers
resources :posts, path: "articles", as: "articles"
# /articles
# articles_path, article_path(@post)
```

## Route Constraints

### Segment Constraints

```ruby
# ID must be numeric
get "posts/:id", to: "posts#show", constraints: { id: /\d+/ }

# Custom format
get "posts/:year/:month/:day", to: "posts#archive",
    constraints: { year: /\d{4}/, month: /\d{2}/, day: /\d{2}/ }
```

### Request-Based Constraints

```ruby
# Subdomain constraint
constraints subdomain: "api" do
  resources :posts
end
# Only matches: api.example.com/posts

# Custom constraint class
class AdminConstraint
  def matches?(request)
    request.session[:admin] == true
  end
end

constraints AdminConstraint.new do
  namespace :admin do
    resources :posts
  end
end
```

### Format Constraints

```ruby
# Only respond to JSON
resources :posts, constraints: { format: :json }

# Or using defaults
resources :posts, defaults: { format: :json }
```

## Redirects

```ruby
# Simple redirect
get "/old-path", to: redirect("/new-path")

# Dynamic redirect
get "/posts/:id/comments", to: redirect("/posts/%{id}#comments")

# Redirect with status
get "/legacy", to: redirect("/modern", status: 301)

# Block redirect
get "/users/:id", to: redirect { |params, request|
  "/profiles/#{params[:id]}"
}
```

## Catch-All Routes

```ruby
# Must be at the end of routes.rb
get "*path", to: "errors#not_found"

# Or for specific formats
get "*path", to: "pages#show", constraints: { format: :html }
```

## Direct Routes (Rails 5.1+)

Define custom URL helpers:

```ruby
# config/routes.rb
direct :homepage do
  "https://example.com"
end

direct :post_on_medium do |post|
  "https://medium.com/@ourcompany/#{post.slug}"
end

# Usage
homepage_url           # => "https://example.com"
post_on_medium_url(@post) # => "https://medium.com/@ourcompany/my-post"
```

## Common Patterns

### Static Pages

```ruby
# Dedicated static pages
get "about", to: "pages#about"
get "contact", to: "pages#contact"
get "terms", to: "pages#terms"
get "privacy", to: "pages#privacy"

# Or with a catch-all for pages
get "pages/:page", to: "pages#show", as: :page
```

### API Versioning

```ruby
namespace :api do
  namespace :v1 do
    resources :posts
  end
  
  namespace :v2 do
    resources :posts
  end
end
# /api/v1/posts, /api/v2/posts
```

### Subdomain Routing

```ruby
constraints subdomain: "api" do
  scope module: :api do
    resources :posts
  end
end

constraints subdomain: "admin" do
  namespace :admin do
    resources :users
  end
end
```

## Tips

- Use `resources` first, add custom routes only when needed
- Name your routes (`as:`) for clean helpers
- Use `member` for actions on one record, `collection` for actions on all
- Keep routes RESTful when possible—even custom actions
- Use constraints to validate route parameters
- Run `bin/rails routes` to verify your routes work as expected
- Put catch-all routes at the very end of `routes.rb`

## See Also

- [[Model]]
- [[RESTful Routes]] — Standard resource routes
- [[Route Helpers]] — Using generated helpers
- [[Rails]]
