---
tags:
  - ruby
  - rails
  - web
type: note
related:
  - '[[The Web]]'
  - '[[MVC]]'
  - '[[URLs]]'
  - '[[Rails]]'
---
# REST

RESTful routing conventions for resource-based web applications.

## Overview

REST (Representational State Transfer) is an architectural style for designing web APIs. In Rails, REST means treating your data as resources that can be created, read, updated, and deleted using standard HTTP methods. Rails conventions map these operations to seven controller actions.

## The Seven RESTful Actions

| HTTP Verb | Path | Action | Purpose |
|-----------|------|--------|---------|
| GET | `/posts` | `index` | List all posts |
| GET | `/posts/:id` | `show` | Display one post |
| GET | `/posts/new` | `new` | Form to create post |
| POST | `/posts` | `create` | Save new post |
| GET | `/posts/:id/edit` | `edit` | Form to edit post |
| PATCH/PUT | `/posts/:id` | `update` | Save edited post |
| DELETE | `/posts/:id` | `destroy` | Delete post |

## Basic Usage

### Defining RESTful Routes

```ruby
# config/routes.rb
Rails.application.routes.draw do
  resources :posts
end
```

This single line generates all seven routes:

```bash
$ bin/rails routes
      Prefix Verb   URI Pattern              Controller#Action
       posts GET    /posts(.:format)          posts#index
             POST   /posts(.:format)          posts#create
    new_post GET    /posts/new(.:format)      posts#new
   edit_post GET    /posts/:id/edit(.:format) posts#edit
        post GET    /posts/:id(.:format)      posts#show
             PATCH  /posts/:id(.:format)      posts#update
             PUT    /posts/:id(.:format)      posts#update
             DELETE /posts/:id(.:format)      posts#destroy
```

### RESTful Controller

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
      redirect_to @post, notice: 'Post created.'
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
      redirect_to @post, notice: 'Post updated.'
    else
      render :edit, status: :unprocessable_entity
    end
  end
  
  # DELETE /posts/:id
  def destroy
    @post.destroy
    redirect_to posts_path, notice: 'Post deleted.'
  end
  
  private
  
  def set_post
    @post = Post.find(params[:id])
  end
  
  def post_params
    params.require(:post).permit(:title, :content)
  end
end
```

## Path Helpers

RESTful routes generate helper methods:

```ruby
posts_path          # => "/posts"
post_path(@post)    # => "/posts/42"
new_post_path       # => "/posts/new"
edit_post_path(@post) # => "/posts/42/edit"

# With format
posts_path(format: :json)  # => "/posts.json"

# Full URLs (for emails, external links)
posts_url           # => "https://example.com/posts"
```

## Customizing Resources

### Limiting Actions

```ruby
# Only specific actions
resources :posts, only: [:index, :show]

# All except certain actions
resources :posts, except: [:destroy]
```

### Nested Resources

```ruby
resources :posts do
  resources :comments
end
```

Generates routes like:
- `GET /posts/:post_id/comments` → `comments#index`
- `POST /posts/:post_id/comments` → `comments#create`
- `GET /posts/:post_id/comments/:id` → `comments#show`

```ruby
# In controller
def create
  @post = Post.find(params[:post_id])
  @comment = @post.comments.build(comment_params)
end

# Path helpers
post_comments_path(@post)           # => "/posts/42/comments"
post_comment_path(@post, @comment)  # => "/posts/42/comments/7"
```

### Shallow Nesting

For cleaner URLs when the child can stand alone:

```ruby
resources :posts do
  resources :comments, shallow: true
end
```

- `GET /posts/:post_id/comments` (needs parent context)
- `GET /comments/:id` (doesn't need parent)

### Member and Collection Routes

```ruby
resources :posts do
  member do
    post :publish    # POST /posts/:id/publish
    get :preview     # GET /posts/:id/preview
  end
  
  collection do
    get :search      # GET /posts/search
    get :drafts      # GET /posts/drafts
  end
end
```

### Custom Path Names

```ruby
resources :posts, path: 'articles'
# /articles, /articles/:id, etc.

resources :posts, path_names: { new: 'compose', edit: 'revise' }
# /posts/compose, /posts/:id/revise
```

## HTTP Methods in Forms

HTML forms only support GET and POST. Rails fakes other methods:

```erb
<!-- Rails generates a hidden field -->
<%= form_with model: @post, method: :patch do |f| %>
  <!-- Renders: <input type="hidden" name="_method" value="patch"> -->
<% end %>

<!-- Delete links -->
<%= link_to "Delete", @post, method: :delete, data: { confirm: "Sure?" } %>
<!-- Or with button -->
<%= button_to "Delete", @post, method: :delete %>
```

## Singular Resources

For resources where there's only one (like current user's profile):

```ruby
resource :profile  # Note: singular
```

| Verb | Path | Action |
|------|------|--------|
| GET | `/profile/new` | `new` |
| POST | `/profile` | `create` |
| GET | `/profile` | `show` |
| GET | `/profile/edit` | `edit` |
| PATCH | `/profile` | `update` |
| DELETE | `/profile` | `destroy` |

No `index` action (there's only one) and no `:id` in paths.

## Namespace and Scope

### Namespace

Prefixes path AND controller module:

```ruby
namespace :admin do
  resources :posts
end
# Path: /admin/posts
# Controller: Admin::PostsController (app/controllers/admin/posts_controller.rb)
```

### Scope

Prefix path only:

```ruby
scope '/admin' do
  resources :posts
end
# Path: /admin/posts
# Controller: PostsController
```

## Tips

- Let Rails generate routes with `resources`—don't fight conventions
- Use nested resources sparingly (1 level deep usually)
- Use `shallow: true` to avoid deeply nested URLs
- Member routes act on one resource; collection routes act on all
- Use singular `resource` for things like settings, profile
- Run `bin/rails routes` to see all generated routes
- The HTTP verb matters—GET for safe, POST/PATCH/DELETE for changes

## See Also

- [[The Web]]
- [[MVC]] — How REST fits into Rails architecture
- [[URLs]] — URL components
- [[Rails]]
