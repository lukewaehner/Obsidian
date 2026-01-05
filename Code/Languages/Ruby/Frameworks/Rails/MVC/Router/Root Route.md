---
tags:
  - ruby
  - rails
  - routing
type: note
related:
  - "[[Model]]"
  - "[[RESTful Routes]]"
  - "[[Rails]]"
---
# Root Route

The homepage route that handles requests to your application's base URL.

## Overview

The root route defines where users land when they visit your application's base URL (e.g., `http://example.com/`). It's typically the first route defined in `config/routes.rb` and maps to a controller action that renders your homepage.

## Basic Usage

```ruby
# config/routes.rb
Rails.application.routes.draw do
  root to: "pages#home"
  
  # Shorthand syntax (equivalent)
  root "pages#home"
end
```

This maps `http://yourapp.com/` to `PagesController#home`.

## The Controller

```ruby
# app/controllers/pages_controller.rb
class PagesController < ApplicationController
  def home
    @featured_posts = Post.featured.limit(5)
    @recent_users = User.recent.limit(10)
  end
end
```

```erb
<!-- app/views/pages/home.html.erb -->
<h1>Welcome to Our App</h1>

<section class="featured">
  <% @featured_posts.each do |post| %>
    <%= render post %>
  <% end %>
</section>
```

## Route Helper

```ruby
root_path  # => "/"
root_url   # => "http://example.com/"

# Usage in views
<%= link_to "Home", root_path %>

# Usage in controllers
redirect_to root_path
```

## Common Patterns

### Authenticated vs Guest Homepage

```ruby
# config/routes.rb
Rails.application.routes.draw do
  # Different roots based on authentication
  authenticated :user do
    root to: "dashboard#show", as: :authenticated_root
  end
  
  root to: "pages#home"
end
```

### Namespaced Root

```ruby
# Admin area has its own root
namespace :admin do
  root to: "dashboard#index"  # /admin -> Admin::DashboardController#index
end

root to: "pages#home"  # / -> PagesController#home
```

### API Root

```ruby
namespace :api do
  namespace :v1 do
    root to: "base#index"  # /api/v1 -> Api::V1::BaseController#index
  end
end
```

## Tips

- Define the root route first in `config/routes.rb` for clarity
- Use a dedicated controller (like `PagesController`) for static pages
- The root route only responds to GET requests
- Use `authenticated` blocks (with Devise) for different homepages based on login status

## See Also

- [[Model]]
- [[RESTful Routes]] — Resource-based routing
- [[Rails]]
