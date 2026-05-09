---
tags:
  - ruby
  - rails
  - mvc
  - architecture
type: moc
related:
  - '[[Rails]]'
  - '[[Controller]]'
  - '[[Views]]'
  - '[[Active Record]]'
---
# MVC

Model-View-Controller architecture in Rails applications.

## Overview

MVC is the architectural pattern at the heart of every Rails application. It separates your code into three interconnected components, each with a distinct responsibility. This separation makes applications easier to develop, test, and maintain.

```
Browser Request
      ↓
   Router ─────────→ Which controller/action?
      ↓
  Controller ──────→ Asks Model for data
      ↓
    Model ─────────→ Queries database, applies business logic
      ↓
  Controller ──────→ Passes data to View
      ↓
    View ──────────→ Renders HTML template
      ↓
   Response ───────→ Sent to browser
```

## Components

### Model (Active Record)

The data layer—interacts with the database and contains business logic:

- [[Active Record]] — ORM fundamentals and CRUD operations
- [[Migrations]] — Database schema changes

### View

The presentation layer—renders HTML from templates:

- [[Views]] — ERB templates, layouts, and partials

### Controller

The coordination layer—handles requests and orchestrates responses:

- [[Controller]] — Actions, params, rendering, and redirecting

### Router

The entry point—maps URLs to controller actions:

- [[Code/Languages/Ruby/Frameworks/Rails/MVC/Router/Router|Router]] — Routing overview
- [[Root Route]] — Homepage configuration
- [[RESTful Routes]] — The seven CRUD routes
- [[Route Helpers]] — Path and URL helpers
- [[Custom Routes]] — Non-RESTful routes

## The Flow

1. **Request arrives** — User visits `/posts/42`
2. **Router matches** — Maps to `PostsController#show` with `id: 42`
3. **Controller acts** — Calls `Post.find(42)`, sets `@post`
4. **Model queries** — Retrieves data from database
5. **View renders** — `show.html.erb` uses `@post` to build HTML
6. **Response sent** — HTML returned to browser

## Directory Structure

```
app/
├── models/           # Business logic and database interaction
│   ├── application_record.rb
│   ├── user.rb
│   └── post.rb
├── views/            # Presentation templates
│   ├── layouts/
│   │   └── application.html.erb
│   ├── users/
│   │   ├── index.html.erb
│   │   └── show.html.erb
│   └── posts/
│       ├── index.html.erb
│       ├── show.html.erb
│       └── _post.html.erb
├── controllers/      # Request handling
│   ├── application_controller.rb
│   ├── users_controller.rb
│   └── posts_controller.rb
└── helpers/          # View helper methods
    └── application_helper.rb
```

## Key Principles

### Separation of Concerns

Each component has one job:
- **Models** — Data and business rules (no HTTP knowledge)
- **Views** — Presentation only (minimal logic)
- **Controllers** — Coordination (no business logic)

### Fat Models, Skinny Controllers

Keep business logic in models, not controllers:

```ruby
# BAD: Logic in controller
class PostsController < ApplicationController
  def publish
    @post = Post.find(params[:id])
    @post.published = true
    @post.published_at = Time.current
    @post.slug = @post.title.parameterize
    @post.save
  end
end

# GOOD: Logic in model
class PostsController < ApplicationController
  def publish
    @post = Post.find(params[:id])
    @post.publish!
  end
end

class Post < ApplicationRecord
  def publish!
    update(
      published: true,
      published_at: Time.current,
      slug: title.parameterize
    )
  end
end
```

### Dumb Views

Views should only display data, not compute it:

```erb
<!-- BAD: Logic in view -->
<% if @user.posts.where(published: true).count > 10 && @user.created_at < 1.year.ago %>
  <span class="badge">Veteran Author</span>
<% end %>

<!-- GOOD: Logic in model/helper -->
<% if @user.veteran_author? %>
  <span class="badge">Veteran Author</span>
<% end %>
```

## See Also

- [[Code/Languages/Ruby/Frameworks/Rails/The Web/MVC|MVC Concepts]] — Conceptual overview
- [[Rails]]
- [[Ruby]]

%% Begin Waypoint %%
- **[[Active Record]]**
- **[[Router]]**
- [[Controller]]
- [[Views]]

%% End Waypoint %%
