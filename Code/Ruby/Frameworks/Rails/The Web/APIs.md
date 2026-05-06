---
tags:
  - ruby
  - rails
  - web
  - api
type: note
related:
  - '[[The Web]]'
  - '[[REST]]'
  - '[[Rails]]'
---
# APIs

How applications communicate with each other programmatically.

## Overview

An API (Application Programming Interface) is a way for programs to interact with each other directly, bypassing the browser. While users access websites through the "front door" (HTML pages), servers and applications use APIs as a "side door" to exchange data efficiently. APIs typically return structured data (JSON) instead of HTML.

## APIs vs Web Pages

| Aspect | Web Page | API |
|--------|----------|-----|
| Consumer | Human (browser) | Machine (code) |
| Format | HTML | JSON, XML |
| Purpose | Display | Data exchange |
| Includes | Styling, layout | Just data |

```ruby
# Same controller, different responses
class PostsController < ApplicationController
  def show
    @post = Post.find(params[:id])
    
    respond_to do |format|
      format.html  # Renders show.html.erb for browsers
      format.json { render json: @post }  # Returns JSON for APIs
    end
  end
end
```

## Consuming APIs

### Making Requests

```ruby
require 'net/http'
require 'json'

# GET request to external API
uri = URI('https://api.github.com/users/rails')
response = Net::HTTP.get(uri)
data = JSON.parse(response)

puts data['name']  # => "Rails"
```

### Using HTTParty (Popular Gem)

```ruby
# Gemfile
gem 'httparty'

# Usage
response = HTTParty.get('https://api.example.com/posts')
posts = response.parsed_response

# With authentication
response = HTTParty.get(
  'https://api.example.com/posts',
  headers: { 'Authorization' => 'Bearer token123' }
)
```

### Using Faraday (Flexible Gem)

```ruby
# Gemfile
gem 'faraday'

# Usage
conn = Faraday.new(url: 'https://api.example.com') do |f|
  f.request :json
  f.response :json
end

response = conn.get('/posts')
posts = response.body
```

## Building APIs in Rails

### API-Only Response

```ruby
class Api::PostsController < ApplicationController
  def index
    posts = Post.all
    render json: posts
  end
  
  def show
    post = Post.find(params[:id])
    render json: post
  end
  
  def create
    post = Post.new(post_params)
    if post.save
      render json: post, status: :created
    else
      render json: { errors: post.errors }, status: :unprocessable_entity
    end
  end
end
```

### API Routes

```ruby
# config/routes.rb
namespace :api do
  namespace :v1 do
    resources :posts
  end
end

# Creates: /api/v1/posts, /api/v1/posts/:id, etc.
```

### Customizing JSON Output

```ruby
# Using as_json
class Post < ApplicationRecord
  def as_json(options = {})
    super(options.merge(
      only: [:id, :title, :content],
      include: { author: { only: [:id, :name] } }
    ))
  end
end

# Using Jbuilder (included in Rails)
# app/views/api/posts/show.json.jbuilder
json.id @post.id
json.title @post.title
json.author do
  json.name @post.author.name
end

# Using Active Model Serializers
class PostSerializer < ActiveModel::Serializer
  attributes :id, :title, :content
  belongs_to :author
end
```

### API-Only Rails App

```bash
# Generate Rails app without views, assets, etc.
rails new my_api --api
```

```ruby
# config/application.rb
class Application < Rails::Application
  config.api_only = true  # Slimmer middleware stack
end
```

## Authentication for APIs

### Token-Based Auth

```ruby
class Api::BaseController < ApplicationController
  before_action :authenticate_token!
  
  private
  
  def authenticate_token!
    token = request.headers['Authorization']&.split(' ')&.last
    @current_user = User.find_by(api_token: token)
    
    render json: { error: 'Unauthorized' }, status: :unauthorized unless @current_user
  end
end
```

### JWT (JSON Web Tokens)

```ruby
# Gemfile
gem 'jwt'

# Encoding
token = JWT.encode({ user_id: user.id, exp: 24.hours.from_now.to_i }, secret_key)

# Decoding
decoded = JWT.decode(token, secret_key).first
user_id = decoded['user_id']
```

## HTTP Status Codes

| Code | Meaning | Rails Symbol |
|------|---------|--------------|
| 200 | OK | `:ok` |
| 201 | Created | `:created` |
| 204 | No Content | `:no_content` |
| 400 | Bad Request | `:bad_request` |
| 401 | Unauthorized | `:unauthorized` |
| 403 | Forbidden | `:forbidden` |
| 404 | Not Found | `:not_found` |
| 422 | Unprocessable | `:unprocessable_entity` |
| 500 | Server Error | `:internal_server_error` |

```ruby
render json: @post, status: :created
render json: { error: 'Not found' }, status: :not_found
```

## Common Patterns

### Versioning

```ruby
# URL versioning (most common)
namespace :api do
  namespace :v1 do
    resources :posts
  end
  namespace :v2 do
    resources :posts
  end
end

# Header versioning
request.headers['Accept']  # "application/vnd.myapp.v2+json"
```

### Pagination

```ruby
class Api::PostsController < ApplicationController
  def index
    posts = Post.page(params[:page]).per(20)
    render json: {
      posts: posts,
      meta: {
        current_page: posts.current_page,
        total_pages: posts.total_pages,
        total_count: posts.total_count
      }
    }
  end
end
```

### Error Handling

```ruby
class Api::BaseController < ApplicationController
  rescue_from ActiveRecord::RecordNotFound, with: :not_found
  rescue_from ActionController::ParameterMissing, with: :bad_request
  
  private
  
  def not_found
    render json: { error: 'Resource not found' }, status: :not_found
  end
  
  def bad_request(exception)
    render json: { error: exception.message }, status: :bad_request
  end
end
```

## Tips

- Use proper HTTP status codes—clients depend on them
- Version your API from the start (`/api/v1/`)
- Return consistent JSON structure (always wrap in object)
- Use serializers for complex JSON output
- Document your API (consider Swagger/OpenAPI)
- Handle errors gracefully with meaningful messages

## See Also

- [[The Web]]
- [[REST]] — RESTful API design
- [[JSON in Ruby]] — JSON handling
- [[Rails]]
