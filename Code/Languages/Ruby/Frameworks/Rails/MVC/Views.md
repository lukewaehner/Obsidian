---
tags:
  - ruby
  - rails
  - mvc
  - views
type: note
related:
  - '[[Rails]]'
  - '[[Controller]]'
  - '[[MVC]]'
  - '[[Haml Setup]]'
---
# Views

Templates that render HTML by combining static markup with dynamic data from controllers.

## Overview

Views are the "V" in MVC—they handle presentation. Views receive instance variables from controllers and render them into HTML (or JSON, XML, etc.) that gets sent to the browser. Rails uses ERB (Embedded Ruby) by default, allowing you to embed Ruby code directly in HTML templates.

## File Locations

Views follow naming conventions that match controllers and actions:

| Controller | Action | View Path |
|------------|--------|-----------|
| `PostsController` | `index` | `app/views/posts/index.html.erb` |
| `PostsController` | `show` | `app/views/posts/show.html.erb` |
| `UsersController` | `edit` | `app/views/users/edit.html.erb` |

## ERB Syntax

Embedded Ruby lets you mix Ruby with HTML:

| Tag | Purpose | Example |
|-----|---------|---------|
| `<%= %>` | Execute and output result | `<%= @user.name %>` |
| `<% %>` | Execute only (no output) | `<% if logged_in? %>` |
| `<%# %>` | Comment (not executed) | `<%# TODO: fix this %>` |
| `<%- -%>` | Trim whitespace | `<%- @items.each do \|i\| -%>` |

### Basic Example

```erb
<h1>Users</h1>

<% if current_user.signed_in? %>
  <ul>
    <% @users.each do |user| %>
      <li><%= user.first_name %></li>
    <% end %>
  </ul>
<% else %>
  <strong>You must sign in!</strong>
<% end %>
```

### How ERB Works

1. Server receives request
2. Controller sets instance variables (`@users`, `@post`)
3. ERB template is processed—Ruby code executes
4. Final HTML is generated
5. HTML is sent to browser

The `.html.erb` extension tells Rails to preprocess with ERB before serving.

## Layouts

Layouts wrap your views with common structure (DOCTYPE, `<html>`, `<head>`, navigation, footer):

```erb
<!-- app/views/layouts/application.html.erb -->
<!DOCTYPE html>
<html>
  <head>
    <title>My App</title>
    <%= csrf_meta_tags %>
    <%= stylesheet_link_tag "application" %>
  </head>
  <body>
    <%= render "shared/navbar" %>
    
    <main>
      <%= yield %>  <!-- View template inserted here -->
    </main>
    
    <%= render "shared/footer" %>
    <%= javascript_include_tag "application" %>
  </body>
</html>
```

### Custom Layouts

```ruby
# Use a different layout for a controller
class AdminController < ApplicationController
  layout "admin"
end

# Use a different layout for an action
def show
  render layout: "special"
end

# No layout
def api_endpoint
  render layout: false
end
```

### Content For

Pass content from views to layouts:

```erb
<!-- In layout -->
<head>
  <title><%= content_for?(:title) ? yield(:title) : "Default Title" %></title>
  <%= yield :head %>
</head>

<!-- In view -->
<% content_for :title, "My Page Title" %>
<% content_for :head do %>
  <%= stylesheet_link_tag "special_page" %>
<% end %>
```

## Partials

Partials are reusable view fragments. They're named with a leading underscore but called without it:

```erb
<!-- app/views/posts/_form.html.erb -->
<%= form_with model: post do |f| %>
  <div>
    <%= f.label :title %>
    <%= f.text_field :title %>
  </div>
  <div>
    <%= f.label :body %>
    <%= f.text_area :body %>
  </div>
  <%= f.submit %>
<% end %>
```

### Rendering Partials

```erb
<!-- Basic render (looks in current view folder) -->
<%= render "form" %>

<!-- From shared folder -->
<%= render "shared/navbar" %>

<!-- Explicit partial syntax -->
<%= render partial: "form" %>
```

### Passing Variables to Partials

```erb
<!-- Using locals -->
<%= render partial: "user", locals: { user: @user, show_email: true } %>

<!-- Shorthand -->
<%= render "user", user: @user, show_email: true %>
```

In the partial, use local variables (no `@`):

```erb
<!-- app/views/users/_user.html.erb -->
<li>
  <%= user.name %>
  <% if show_email %>
    (<%= user.email %>)
  <% end %>
</li>
```

### Collection Partials

Render a partial for each item in a collection:

```erb
<!-- Long form -->
<ul>
  <% @users.each do |user| %>
    <%= render partial: "user", locals: { user: user } %>
  <% end %>
</ul>

<!-- Shorthand: Rails infers partial name from object -->
<ul>
  <%= render @users %>
</ul>
<!-- Renders _user.html.erb for each user, passing 'user' local -->
```

Rails automatically:
- Finds `_user.html.erb` based on the model name
- Passes each item as a local variable named `user`
- Handles empty collections gracefully

### Collection with Spacer

```erb
<%= render partial: "post", collection: @posts, spacer_template: "post_divider" %>
```

## Helper Methods

Rails provides helpers to generate HTML:

### Link Helpers

```erb
<%= link_to "Home", root_path %>
<%= link_to "View Post", @post %>
<%= link_to "Edit", edit_post_path(@post), class: "btn" %>
<%= link_to "Delete", @post, method: :delete, data: { confirm: "Sure?" } %>

<!-- Button that submits -->
<%= button_to "Add to Cart", cart_path, method: :post %>
```

### Form Helpers

```erb
<%= form_with model: @post do |f| %>
  <%= f.label :title %>
  <%= f.text_field :title %>
  
  <%= f.label :body %>
  <%= f.text_area :body, rows: 10 %>
  
  <%= f.label :category %>
  <%= f.select :category, ["Tech", "Life", "News"] %>
  
  <%= f.check_box :published %>
  <%= f.label :published, "Publish now?" %>
  
  <%= f.submit "Save Post" %>
<% end %>
```

### Asset Tag Helpers

```erb
<%= stylesheet_link_tag "application" %>
<%= javascript_include_tag "application" %>
<%= image_tag "logo.png", alt: "Company Logo", class: "logo" %>
<%= favicon_link_tag "favicon.ico" %>
```

Renders:

```html
<link rel="stylesheet" href="/assets/application.css">
<script src="/assets/application.js"></script>
<img src="/assets/logo.png" alt="Company Logo" class="logo">
```

### Number and Text Helpers

```erb
<%= number_to_currency(1234.56) %>      <!-- $1,234.56 -->
<%= number_to_percentage(65.5) %>       <!-- 65.500% -->
<%= number_with_delimiter(12345678) %>  <!-- 12,345,678 -->
<%= truncate(@post.body, length: 100) %>
<%= simple_format(@post.body) %>        <!-- Converts \n to <br> and <p> -->
<%= pluralize(5, "comment") %>          <!-- "5 comments" -->
```

### Date and Time Helpers

```erb
<%= time_ago_in_words(@post.created_at) %>  <!-- "3 days ago" -->
<%= distance_of_time_in_words(Time.now, @event.starts_at) %>
<%= @post.created_at.strftime("%B %d, %Y") %>  <!-- "January 15, 2024" -->
```

## Custom Helpers

Define helpers in `app/helpers/`:

```ruby
# app/helpers/posts_helper.rb
module PostsHelper
  def post_status_badge(post)
    status = post.published? ? "published" : "draft"
    content_tag :span, status.capitalize, class: "badge badge-#{status}"
  end
  
  def format_post_date(post)
    post.created_at.strftime("%B %d, %Y at %l:%M %p")
  end
end
```

```erb
<!-- In view -->
<%= post_status_badge(@post) %>
<%= format_post_date(@post) %>
```

### Application-Wide Helpers

```ruby
# app/helpers/application_helper.rb
module ApplicationHelper
  def page_title(title)
    content_for(:title) { title }
  end
  
  def flash_class(type)
    case type.to_sym
    when :notice then "alert-success"
    when :alert then "alert-danger"
    else "alert-info"
    end
  end
end
```

## Common Patterns

### Flash Messages

```erb
<!-- app/views/layouts/application.html.erb -->
<% flash.each do |type, message| %>
  <div class="alert <%= flash_class(type) %>">
    <%= message %>
  </div>
<% end %>
```

### Conditional Content

```erb
<% if @posts.any? %>
  <%= render @posts %>
<% else %>
  <p>No posts yet. <%= link_to "Create one!", new_post_path %></p>
<% end %>
```

### Safe HTML Output

```erb
<!-- Escaped by default (safe) -->
<%= @user.bio %>  <!-- <script> becomes &lt;script&gt; -->

<!-- Raw HTML (use carefully!) -->
<%= raw @post.formatted_body %>
<%= @post.formatted_body.html_safe %>
<%= sanitize @post.body %>  <!-- Strips dangerous tags -->
```

## Commands

```bash
# Views are created with controller generator
bin/rails generate controller Posts index show new edit

# Or scaffold
bin/rails generate scaffold Post title:string body:text
```

## Tips

- Keep logic out of views—use helpers or presenters
- Always use `<%= %>` for output, `<% %>` for logic
- Partial names start with underscore, but render without it
- Pass data to partials explicitly with `locals:`
- Use `render @collection` shorthand for cleaner code
- Content is escaped by default—use `raw` or `html_safe` carefully
- Use `content_for` to pass content from views to layouts
- Prefer helpers over complex ERB logic

## See Also

- [[Code/Languages/Ruby/Frameworks/Rails/MVC/MVC|MVC]] — Views in the architecture
- [[Controller]] — What passes data to views
- [[Haml Setup]] — Alternative templating syntax
- [[Rails]]
