---
tags:
  - ruby
  - rails
  - web
type: note
related:
  - '[[The Web]]'
  - '[[REST]]'
  - '[[Rails]]'
---
# URLs

Anatomy of web addresses and how Rails uses their components.

## Overview

URLs (Uniform Resource Locators) are addresses that identify resources on the web. Understanding their components is essential for Rails development—you'll work with paths and parameters constantly when defining routes and building links.

## URL Components

```
https://www.google.com/search?q=what+is+a+url#results
└─┬──┘ └──────┬──────┘└──┬──┘└──────┬───────┘└───┬───┘
protocol     host      path    parameters    fragment
```

| Component | Example | Description |
|-----------|---------|-------------|
| Protocol (Scheme) | `https` | How to communicate (HTTP, HTTPS, FTP) |
| Host | `www.google.com` | The server's address |
| Port | `:3000` | Network port (optional, defaults vary) |
| Path | `/search` | Location of resource on server |
| Parameters (Query) | `q=what+is+a+url` | Key-value data sent to server |
| Fragment | `#results` | Client-side anchor (not sent to server) |

### Breaking Down the Host

```
www.google.com
└┬┘ └──┬──┘└┬┘
sub  domain TLD
domain
```

- **TLD (Top Level Domain)**: `com`, `org`, `net`, `io`
- **Domain**: `google`
- **Subdomain**: `www` (optional)

## In Rails

### Paths Map to Routes

```ruby
# config/routes.rb
get '/search', to: 'search#index'
get '/users/:id', to: 'users#show'
```

```
GET /search        → SearchController#index
GET /users/42      → UsersController#show (params[:id] = "42")
```

### Parameters in Controllers

```ruby
# URL: /search?q=ruby&page=2

class SearchController < ApplicationController
  def index
    query = params[:q]      # => "ruby"
    page = params[:page]    # => "2"
  end
end
```

### Building URLs

```ruby
# In views and controllers
search_path                    # => "/search"
search_path(q: 'ruby')         # => "/search?q=ruby"
user_path(@user)               # => "/users/42"
user_url(@user)                # => "https://example.com/users/42"
```

### Path vs URL Helpers

```ruby
# _path: Relative path (for internal links)
users_path          # => "/users"

# _url: Full URL with protocol and host (for emails, APIs)
users_url           # => "https://example.com/users"
```

## Common Patterns

### RESTful URL Structure

```
/posts              # Index - list all posts
/posts/1            # Show - display post with id 1
/posts/new          # New - form to create post
/posts/1/edit       # Edit - form to edit post 1
```

### Nested Resources

```ruby
# config/routes.rb
resources :posts do
  resources :comments
end
```

```
/posts/1/comments       # Comments for post 1
/posts/1/comments/5     # Comment 5 on post 1
```

### Query Parameters vs Path Parameters

```ruby
# Path parameter - identifies resource
/users/:id          # /users/42 → params[:id] = "42"

# Query parameter - filters/options
/users?role=admin   # params[:role] = "admin"
```

## URL Encoding

Special characters must be encoded:

| Character | Encoded |
|-----------|---------|
| Space | `%20` or `+` |
| `&` | `%26` |
| `=` | `%3D` |
| `?` | `%3F` |

```ruby
# Rails handles encoding automatically
link_to "Search", search_path(q: "ruby & rails")
# => /search?q=ruby+%26+rails
```

## Tips

- Use path helpers (`users_path`) instead of hardcoding URLs
- Use `_url` helpers for external links (emails, redirects)
- Path parameters identify resources; query parameters filter/modify
- The fragment (`#anchor`) is client-side only—never sent to Rails
- Keep URLs RESTful and predictable

## See Also

- [[The Web]]
- [[REST]] — RESTful URL conventions
- [[Rails]]
