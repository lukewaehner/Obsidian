---
tags:
  - ruby
  - rails
  - web
  - architecture
type: note
related:
  - '[[The Web]]'
  - '[[REST]]'
  - '[[Rails]]'
---
# MVC

Model-View-Controller architecture that organizes Rails applications.

## Overview

MVC separates a web application into three distinct parts: Models (data and business logic), Views (presentation), and Controllers (coordination). This separation makes code easier to maintain, test, and understand. Rails is built entirely around MVC—the folder structure directly reflects this pattern.

## The Three Components

### Model

The "smart geek in the back room"—handles data and business logic.

- Interacts with the database
- Validates data
- Contains business rules
- Knows nothing about HTTP or HTML

```ruby
# app/models/post.rb
class Post < ApplicationRecord
  belongs_to :author
  has_many :comments
  
  validates :title, presence: true
  
  def published?
    published_at.present?
  end
end
```

### View

"Looks pretty and waits for data"—handles presentation.

- Renders HTML (or JSON, XML, etc.)
- Receives data from the controller
- Contains minimal logic (display only)
- Knows nothing about the database

```erb
<!-- app/views/posts/show.html.erb -->
<article>
  <h1><%= @post.title %></h1>
  <p>By <%= @post.author.name %></p>
  <div><%= @post.content %></div>
</article>
```

### Controller

The "social middleman"—coordinates between Model and View.

- Receives HTTP requests
- Asks models for data
- Passes data to views
- Handles user input
- Doesn't contain business logic

```ruby
# app/controllers/posts_controller.rb
class PostsController < ApplicationController
  def show
    @post = Post.find(params[:id])
  end
  
  def create
    @post = Post.new(post_params)
    if @post.save
      redirect_to @post
    else
      render :new
    end
  end
end
```

## Request Flow

```
Browser Request
      ↓
   Router ─────────→ Which controller/action?
      ↓
  Controller ──────→ Asks Model for data
      ↓
    Model ─────────→ Queries database, applies logic
      ↓
  Controller ──────→ Passes data to View
      ↓
    View ──────────→ Renders HTML template
      ↓
   Response ───────→ Sent to browser
```

### Concrete Example

1. User visits `/posts/42`
2. **Router** maps to `PostsController#show`
3. **Controller** calls `Post.find(42)`
4. **Model** queries database, returns Post object
5. **Controller** assigns `@post` for the view
6. **View** (`show.html.erb`) renders HTML with post data
7. HTML sent back to browser

## Rails Directory Structure

```
app/
├── models/           # Model classes
│   └── post.rb
├── views/            # View templates
│   └── posts/
│       ├── index.html.erb
│       ├── show.html.erb
│       └── _post.html.erb
├── controllers/      # Controller classes
│   └── posts_controller.rb
└── helpers/          # View helper methods
    └── posts_helper.rb
```

## Why MVC?

### Separation of Concerns

Each component has one job:
- Change the database? Edit the Model.
- Change the look? Edit the View.
- Change the flow? Edit the Controller.

### Testability

```ruby
# Test model logic without HTTP
test "post requires title" do
  post = Post.new(title: nil)
  assert_not post.valid?
end

# Test controller flow without database
test "show assigns post" do
  get post_path(posts(:one))
  assert_response :success
end
```

### Maintainability

- Bug in business logic? Check models.
- Display issue? Check views.
- Wrong redirect? Check controllers.

## Common Mistakes

### Fat Controllers

```ruby
# BAD: Business logic in controller
def create
  @post = Post.new(post_params)
  @post.slug = @post.title.parameterize
  @post.published_at = Time.current if params[:publish]
  @post.author = current_user
  # ... more logic
end

# GOOD: Move to model
def create
  @post = current_user.posts.build(post_params)
  @post.publish! if params[:publish]
end
```

### Logic in Views

```erb
<!-- BAD: Complex logic in view -->
<% if @user.posts.where(published: true).count > 10 && @user.created_at < 1.year.ago %>
  <span>Veteran Author</span>
<% end %>

<!-- GOOD: Use model method -->
<% if @user.veteran_author? %>
  <span>Veteran Author</span>
<% end %>
```

### Database Queries in Views

```erb
<!-- BAD: Query in view (N+1 problem) -->
<% @posts.each do |post| %>
  <%= post.author.name %>  <!-- Queries for each post! -->
<% end %>

<!-- GOOD: Eager load in controller -->
# Controller: @posts = Post.includes(:author)
```

## Tips

- Keep controllers thin—delegate to models
- Keep views dumb—only display logic
- Put business logic in models (or service objects)
- Use `before_action` for common controller setup
- Use partials to DRY up views
- Use helpers for complex view formatting

## See Also

- [[The Web]]
- [[REST]] — RESTful controller actions
- [[Rails]]
