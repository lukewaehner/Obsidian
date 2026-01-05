---
tags:
  - ruby
  - rails
  - web
  - security
type: note
related:
  - '[[The Web]]'
  - '[[Authentication and Authorization]]'
  - '[[Rails]]'
---
# Cookies and Sessions

Preserving user state across stateless HTTP requests.

## Overview

HTTP is stateless—each request is completely independent. Without cookies and sessions, every page load would treat you as a brand new user. Cookies are small pieces of data stored in the browser and sent with every request. Sessions use cookies to identify users and store state on the server side.

## Cookies

### What Are Cookies?

Cookies are key-value pairs that:
- Are stored in the browser
- Are sent with every request to the same domain
- Have expiration dates
- Can be secured (HTTPS only, HTTP-only)

### Setting Cookies in Rails

```ruby
class SessionsController < ApplicationController
  def create
    # Simple cookie
    cookies[:username] = "alice"
    
    # Cookie with options
    cookies[:remember_token] = {
      value: generate_token,
      expires: 1.year.from_now,
      httponly: true,      # Can't be read by JavaScript
      secure: true,        # HTTPS only
      same_site: :strict   # CSRF protection
    }
  end
  
  def destroy
    cookies.delete(:remember_token)
  end
end
```

### Reading Cookies

```ruby
class ApplicationController < ActionController::Base
  def current_user
    @current_user ||= User.find_by(remember_token: cookies[:remember_token])
  end
end
```

### Signed and Encrypted Cookies

```ruby
# Signed - tamper-proof (user can read but not modify)
cookies.signed[:user_id] = current_user.id
user_id = cookies.signed[:user_id]

# Encrypted - hidden and tamper-proof
cookies.encrypted[:secret_data] = "sensitive info"
data = cookies.encrypted[:secret_data]
```

## Sessions

### What Are Sessions?

Sessions store user data on the server, identified by a session ID cookie. This is more secure than storing everything in cookies.

```
Browser                          Server
   │                               │
   │  Request + session_id cookie  │
   │  ─────────────────────────►   │
   │                               │  Look up session data
   │                               │  by session_id
   │  Response                     │
   │  ◄─────────────────────────   │
```

### Using Sessions in Rails

```ruby
class SessionsController < ApplicationController
  def create
    user = User.find_by(email: params[:email])
    if user&.authenticate(params[:password])
      session[:user_id] = user.id  # Stored server-side
      redirect_to dashboard_path
    else
      flash[:alert] = "Invalid credentials"
      render :new
    end
  end
  
  def destroy
    session.delete(:user_id)
    # or: reset_session (clears everything)
    redirect_to root_path
  end
end

class ApplicationController < ActionController::Base
  def current_user
    @current_user ||= User.find_by(id: session[:user_id])
  end
  
  def logged_in?
    current_user.present?
  end
end
```

### Session Storage Options

Configure in `config/initializers/session_store.rb`:

```ruby
# Cookie store (default) - encrypted, stored in browser
Rails.application.config.session_store :cookie_store, key: '_myapp_session'

# Database store - for large sessions
Rails.application.config.session_store :active_record_store

# Redis store - for distributed/scalable apps
Rails.application.config.session_store :redis_store, 
  servers: ["redis://localhost:6379/0/session"]

# Memcached store
Rails.application.config.session_store :mem_cache_store
```

## Cookies vs Sessions

| Aspect | Cookies | Sessions |
|--------|---------|----------|
| Storage | Browser | Server (ID in browser) |
| Size limit | ~4KB | Unlimited (server) |
| Security | Visible to user | Hidden on server |
| Use case | Remember me, preferences | User login, cart |

## Flash Messages

Flash is a special session that clears after one request—perfect for notifications:

```ruby
class PostsController < ApplicationController
  def create
    @post = Post.new(post_params)
    if @post.save
      flash[:notice] = "Post created successfully!"
      redirect_to @post
    else
      flash.now[:alert] = "Could not create post"  # For render (same request)
      render :new
    end
  end
  
  def destroy
    @post.destroy
    redirect_to posts_path, notice: "Post deleted"  # Shorthand
  end
end
```

```erb
<!-- app/views/layouts/application.html.erb -->
<% flash.each do |type, message| %>
  <div class="flash flash-<%= type %>">
    <%= message %>
  </div>
<% end %>
```

## Common Patterns

### Remember Me

```ruby
class SessionsController < ApplicationController
  def create
    user = User.authenticate(params[:email], params[:password])
    if user
      if params[:remember_me]
        cookies.encrypted[:user_id] = {
          value: user.id,
          expires: 2.weeks.from_now
        }
      else
        session[:user_id] = user.id
      end
      redirect_to dashboard_path
    end
  end
end

class ApplicationController < ActionController::Base
  def current_user
    @current_user ||= if session[:user_id]
      User.find_by(id: session[:user_id])
    elsif cookies.encrypted[:user_id]
      User.find_by(id: cookies.encrypted[:user_id])
    end
  end
end
```

### Shopping Cart

```ruby
class CartsController < ApplicationController
  def add_item
    cart = session[:cart] ||= {}
    cart[params[:product_id]] ||= 0
    cart[params[:product_id]] += 1
  end
  
  def show
    @cart_items = Product.find(session[:cart]&.keys || [])
  end
end
```

## Security Considerations

### Cookie Security Options

```ruby
cookies[:token] = {
  value: token,
  httponly: true,    # Prevents XSS reading cookie
  secure: Rails.env.production?,  # HTTPS only in production
  same_site: :lax    # Prevents CSRF (lax allows top-level navigation)
}
```

### Session Fixation

```ruby
def create
  user = User.authenticate(params[:email], params[:password])
  if user
    reset_session  # Generate new session ID after login!
    session[:user_id] = user.id
  end
end
```

## Tips

- Use `session` for sensitive data (user ID, auth state)
- Use `cookies` for non-sensitive preferences
- Always use `cookies.signed` or `cookies.encrypted` for important data
- Set `httponly: true` to prevent XSS attacks
- Use `reset_session` after login to prevent session fixation
- Keep session data minimal—store IDs, not objects
- Flash messages auto-clear; use `flash.now` for render (same request)

## See Also

- [[The Web]]
- [[Authentication and Authorization]] — Using sessions for login
- [[Rails]]
