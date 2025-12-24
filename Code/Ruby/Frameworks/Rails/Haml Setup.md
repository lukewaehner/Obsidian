---
type: note
tags:
  - ruby
  - rails
  - templating
  - haml
related:
  - "[[Gemfile]]"
---
# Haml Setup in Rails

Haml is a templating language that replaces ERB with a cleaner, indentation-based syntax. It eliminates closing tags and reduces visual noise.

## Installation

Add to your [[Rails - Gemfile|Gemfile]]:

```ruby
gem 'haml-rails'
```

Then install:

```bash
bundle install
```

## Converting the Application Layout

Convert the default ERB layout to Haml:

```bash
rails generate haml:application_layout convert
```

This converts `app/views/layouts/application.html.erb` to `application.html.haml`.

## ERB vs Haml Comparison

**ERB:**
```erb
<div class="container">
  <h1><%= @title %></h1>
  <ul>
    <% @items.each do |item| %>
      <li class="item"><%= item.name %></li>
    <% end %>
  </ul>
</div>
```

**Haml:**
```haml
.container
  %h1= @title
  %ul
    - @items.each do |item|
      %li.item= item.name
```

## Quick Syntax Reference

| Haml | Meaning |
|------|---------|
| `%tag` | HTML tag |
| `.class` | Class (defaults to div) |
| `#id` | ID (defaults to div) |
| `=` | Output Ruby (escaped) |
| `-` | Execute Ruby (no output) |
| `!=` | Output Ruby (unescaped) |

## Common Patterns

```haml
-# This is a Haml comment (not in HTML output)

/ This is an HTML comment (visible in source)

%div{class: 'card', data: {id: 1}}
  Content here

-# Shorthand for div with class and id:
.card#main-card
  Content here

-# Conditionals
- if @user.admin?
  %span.badge Admin
- else
  %span.badge User
```

## Converting Existing Views

Convert all ERB files in your project:

```bash
gem install html2haml
find . -name '*.erb' | xargs -I {} sh -c 'html2haml "$1" "${1%.erb}.haml" && rm "$1"' _ {}
```

Or convert files one at a time:

```bash
html2haml app/views/users/index.html.erb app/views/users/index.html.haml
```

## Tips

- Indentation is significant—use 2 spaces consistently
- You can mix ERB and Haml files in the same project
- Use `haml-lint` for style checking
- File extension is `.html.haml`

## See Also

- [[Rails - Gemfile]] — Adding dependencies
- [[Rails]]
