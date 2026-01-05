---
tags:
  - ruby
  - rails
  - mvc
type: note
related:
  - "[[Rails]]"
  - "[[Model]]"
  - "[[MVC]]"
  - "[[Views]]"
---
# Controller

The middleman that coordinates between models and views in Rails MVC.

## Overview

Controllers handle incoming HTTP requests, ask models for data, and decide which view to render. They're the "traffic cop" of your application—receiving requests from the router, orchestrating the response, and keeping business logic in the models where it belongs. Controllers should be lightweight, delegating heavy lifting to models.

## Basic Structure

```ruby
# app/controllers/posts_controller.rb
class PostsController < ApplicationController
  def index
    @posts = Post.all
  end
  
  def show
    @post = Post.find(params[:id])
  end
end
```

When Rails reaches the end of a controller action:
1. It gathers all instance variables (`@posts`, `@post`)
2. Passes them to the view
3. Renders the view matching the action name

## Naming Conventions

Rails uses conventions to connect controllers, actions, and views:

| Controller | Action | View Path |
|------------|--------|-----------|
| `PostsController` | `index` | `app/views/posts/index.html.erb` |
| `PostsController` | `show` | `app/views/posts/show.html.erb` |
| `UsersController` | `edit` | `app/views/users/edit.html.erb` |

The controller name comes from `config/routes.rb`:

```ruby
resources :posts  # Maps to PostsController
resources :users  # Maps to UsersController
```

## Rendering

### Implicit Rendering

Rails automatically renders the view matching the action name:

```ruby
def index
  @posts = Post.all
  # Automatically renders app/views/posts/index.html.erb
end
```

### Explicit Rendering

Override the default view:

```ruby
def show
  @post = Post.find(params[:id])
  render :details           # Renders app/views/posts/details.html.erb
  # or
  render "posts/details"    # Explicit path
  # or
  render template: "shared/post"
end
```

### Render Options

```ruby
# Render with status code
render :new, status: :unprocessable_entity

# Render plain text
render plain: "OK"

# Render JSON
render json: @post

# Render nothing
head :ok
head :no_content

# Render inline
render inline: "<h1><%= @post.title %></h1>"
```

## Redirecting

Redirects send a new HTTP request to a different URL:

```ruby
def create
  @post = Post.new(post_params)
  if @post.save
    redirect_to @post                    # Short for post_path(@post)
    # or
    redirect_to post_path(@post)         # Explicit path
    # or
    redirect_to posts_path               # To index
    # or
    redirect_to root_path                # To homepage
  else
    render :new, status: :unprocessable_entity
  end
end
```

### Redirect vs Render

| Aspect | `redirect_to` | `render` |
|--------|---------------|----------|
| HTTP | New request | Same request |
| URL | Changes | Stays the same |
| Instance variables | Lost | Preserved |
| Use when | Action succeeded, go elsewhere | Action failed, show form again |

```ruby
def create
  @post = Post.new(post_params)
  if @post.save
    redirect_to @post           # Success → new request to show page
  else
    render :new, status: :unprocessable_entity  # Failure → re-render form with errors
  end
end
```

### Redirect with Flash

```ruby
redirect_to @post, notice: "Post created successfully!"
redirect_to posts_path, alert: "Post could not be deleted"
```

## Params

The `params` hash contains data from the request:

```ruby
# URL: /posts/42
params[:id]           # => "42"

# URL: /posts?page=2&sort=title
params[:page]         # => "2"
params[:sort]         # => "title"

# Form submission
params[:post][:title] # => "My Title"
params[:post][:body]  # => "Content here"
```

### Strong Parameters

Rails requires you to whitelist allowed parameters to prevent mass assignment vulnerabilities:

```ruby
class PostsController < ApplicationController
  def create
    @post = Post.new(post_params)
    # ...
  end
  
  def update
    @post = Post.find(params[:id])
    @post.update(post_params)
    # ...
  end
  
  private
  
  def post_params
    params.require(:post).permit(:title, :body, :author_id)
  end
end
```

### Modern Syntax (Rails 8+)

```ruby
def post_params
  params.expect(post: [:title, :body, :author_id])
end
```

### Nested Parameters

```ruby
# For nested attributes
def post_params
  params.require(:post).permit(
    :title, 
    :body,
    comments_attributes: [:id, :content, :_destroy]
  )
end

# For arrays
def post_params
  params.require(:post).permit(:title, tag_ids: [])
end
```

## Flash Messages

Flash messages persist for exactly one request—perfect for success/error notifications:

```ruby
class PostsController < ApplicationController
  def create
    @post = Post.new(post_params)
    if @post.save
      flash[:notice] = "Post created successfully!"
      redirect_to @post
    else
      flash.now[:alert] = "Please fix the errors below"
      render :new, status: :unprocessable_entity
    end
  end
  
  def destroy
    @post = Post.find(params[:id])
    @post.destroy
    redirect_to posts_path, notice: "Post deleted"
  end
end
```

### flash vs flash.now

| Method | Use with | Persistence |
|--------|----------|-------------|
| `flash` | `redirect_to` | Next request |
| `flash.now` | `render` | Current request only |

```erb
<!-- app/views/layouts/application.html.erb -->
<% flash.each do |type, message| %>
  <div class="flash flash-<%= type %>">
    <%= message %>
  </div>
<% end %>
```

## Before Actions (Filters)

Run code before specific actions:

```ruby
class PostsController < ApplicationController
  before_action :set_post, only: [:show, :edit, :update, :destroy]
  before_action :require_login, except: [:index, :show]
  before_action :require_owner, only: [:edit, :update, :destroy]
  
  def show
    # @post is already set
  end
  
  def edit
    # @post is already set, user is logged in and is owner
  end
  
  private
  
  def set_post
    @post = Post.find(params[:id])
  end
  
  def require_login
    redirect_to login_path, alert: "Please log in" unless logged_in?
  end
  
  def require_owner
    redirect_to @post, alert: "Not authorized" unless @post.user == current_user
  end
end
```

### Filter Options

```ruby
before_action :method_name, only: [:create, :update]
before_action :method_name, except: [:index, :show]
skip_before_action :require_login, only: [:index]

# Other filter types
after_action :log_activity
around_action :wrap_in_transaction
```

## Common Patterns

### Full RESTful Controller

```ruby
class PostsController < ApplicationController
  before_action :set_post, only: [:show, :edit, :update, :destroy]
  
  # GET /posts
  def index
    @posts = Post.all
  end
  
  # GET /posts/:id
  def show
  end
  
  # GET /posts/new
  def new
    @post = Post.new
  end
  
  # POST /posts
  def create
    @post = Post.new(post_params)
    if @post.save
      redirect_to @post, notice: "Post created."
    else
      render :new, status: :unprocessable_entity
    end
  end
  
  # GET /posts/:id/edit
  def edit
  end
  
  # PATCH/PUT /posts/:id
  def update
    if @post.update(post_params)
      redirect_to @post, notice: "Post updated."
    else
      render :edit, status: :unprocessable_entity
    end
  end
  
  # DELETE /posts/:id
  def destroy
    @post.destroy
    redirect_to posts_path, notice: "Post deleted."
  end
  
  private
  
  def set_post
    @post = Post.find(params[:id])
  end
  
  def post_params
    params.require(:post).permit(:title, :body)
  end
end
```

### Respond to Multiple Formats

```ruby
def show
  @post = Post.find(params[:id])
  
  respond_to do |format|
    format.html  # Renders show.html.erb
    format.json { render json: @post }
    format.xml { render xml: @post }
  end
end
```

### Rescue from Errors

```ruby
class ApplicationController < ActionController::Base
  rescue_from ActiveRecord::RecordNotFound, with: :not_found
  rescue_from ActionController::ParameterMissing, with: :bad_request
  
  private
  
  def not_found
    render file: "#{Rails.root}/public/404.html", status: :not_found
  end
  
  def bad_request(exception)
    render plain: exception.message, status: :bad_request
  end
end
```

## Commands

```bash
# Generate a controller
bin/rails generate controller Posts index show new edit

# Generate with no views
bin/rails generate controller Api::Posts --no-helper --no-assets

# Destroy a controller
bin/rails destroy controller Posts
```

## Tips

- Keep controllers thin—move business logic to models
- Use `before_action` to DRY up common setup
- Always use strong parameters for mass assignment
- Use `redirect_to` after successful writes, `render` after failures
- Use `flash` with redirects, `flash.now` with renders
- `render` and `redirect_to` don't halt execution—use `return` if needed
- Instance variables (`@var`) are passed to views; local variables are not
- Return early with guard clauses to avoid double render errors

## See Also

- [[Code/Languages/Ruby/Frameworks/Rails/MVC/MVC|MVC]] — Controller's role in the architecture
- [[Code/Languages/Ruby/Frameworks/Rails/MVC/Router/Router|Router]] — How requests reach controllers
- [[Views]] — What controllers render
- [[Active Record]] — Model layer
- [[Rails]]
