---
tags:
  - ruby
  - rails
  - web
  - security
type: note
related:
  - '[[The Web]]'
  - '[[Cookies and Sessions]]'
  - '[[Rails]]'
---
# Authentication and Authorization

Identifying users and controlling what they can access.

## Overview

**Authentication** answers "Who are you?"—verifying a user's identity (login). **Authorization** answers "What can you do?"—controlling access based on permissions. These are distinct but related concepts that work together to secure your application.

## Authentication

### The Basic Flow

1. User submits email/password
2. Server verifies credentials against database
3. Server creates session to remember user
4. Subsequent requests include session cookie
5. Server identifies user from session

### Rolling Your Own (Simple)

```ruby
# app/models/user.rb
class User < ApplicationRecord
  has_secure_password  # Requires bcrypt gem, adds password_digest column
  
  validates :email, presence: true, uniqueness: true
end

# Migration
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :email, null: false
      t.string :password_digest, null: false
      t.timestamps
    end
    add_index :users, :email, unique: true
  end
end
```

```ruby
# app/controllers/sessions_controller.rb
class SessionsController < ApplicationController
  def new
    # Login form
  end
  
  def create
    user = User.find_by(email: params[:email])
    
    if user&.authenticate(params[:password])
      reset_session  # Prevent session fixation
      session[:user_id] = user.id
      redirect_to dashboard_path, notice: "Logged in!"
    else
      flash.now[:alert] = "Invalid email or password"
      render :new, status: :unprocessable_entity
    end
  end
  
  def destroy
    reset_session
    redirect_to root_path, notice: "Logged out!"
  end
end

# app/controllers/registrations_controller.rb
class RegistrationsController < ApplicationController
  def new
    @user = User.new
  end
  
  def create
    @user = User.new(user_params)
    if @user.save
      session[:user_id] = @user.id
      redirect_to dashboard_path, notice: "Welcome!"
    else
      render :new, status: :unprocessable_entity
    end
  end
  
  private
  
  def user_params
    params.require(:user).permit(:email, :password, :password_confirmation)
  end
end
```

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  helper_method :current_user, :logged_in?
  
  def current_user
    @current_user ||= User.find_by(id: session[:user_id])
  end
  
  def logged_in?
    current_user.present?
  end
  
  def require_login
    unless logged_in?
      redirect_to login_path, alert: "Please log in first"
    end
  end
end
```

```ruby
# config/routes.rb
Rails.application.routes.draw do
  get  '/login',  to: 'sessions#new'
  post '/login',  to: 'sessions#create'
  delete '/logout', to: 'sessions#destroy'
  
  get  '/signup', to: 'registrations#new'
  post '/signup', to: 'registrations#create'
end
```

### Using Devise

Devise is the standard authentication gem that handles everything:

```ruby
# Gemfile
gem 'devise'

# Install
rails generate devise:install
rails generate devise User
rails db:migrate
```

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  before_action :authenticate_user!  # Require login for all actions
end

# Skip auth for specific controllers
class HomeController < ApplicationController
  skip_before_action :authenticate_user!, only: [:index]
end
```

Devise provides helpers:
- `current_user` — The logged-in user
- `user_signed_in?` — Is someone logged in?
- `authenticate_user!` — Require login or redirect
- `user_session` — Access session data

## Authorization

### Basic Role-Based

```ruby
# app/models/user.rb
class User < ApplicationRecord
  enum role: { user: 0, moderator: 1, admin: 2 }
  
  def can_edit?(resource)
    admin? || resource.user == self
  end
end

# Migration
add_column :users, :role, :integer, default: 0
```

```ruby
# app/controllers/admin/dashboard_controller.rb
class Admin::DashboardController < ApplicationController
  before_action :require_admin
  
  private
  
  def require_admin
    unless current_user&.admin?
      redirect_to root_path, alert: "Access denied"
    end
  end
end
```

### Using Pundit

Pundit provides a clean policy pattern for authorization:

```ruby
# Gemfile
gem 'pundit'

# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  include Pundit::Authorization
  
  rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized
  
  private
  
  def user_not_authorized
    redirect_to root_path, alert: "You are not authorized to do that"
  end
end
```

```ruby
# app/policies/post_policy.rb
class PostPolicy < ApplicationPolicy
  def show?
    true  # Anyone can view
  end
  
  def create?
    user.present?  # Must be logged in
  end
  
  def update?
    user.admin? || record.user == user  # Owner or admin
  end
  
  def destroy?
    user.admin?  # Admin only
  end
  
  class Scope < Scope
    def resolve
      if user.admin?
        scope.all
      else
        scope.where(published: true)
      end
    end
  end
end
```

```ruby
# app/controllers/posts_controller.rb
class PostsController < ApplicationController
  def show
    @post = Post.find(params[:id])
    authorize @post
  end
  
  def update
    @post = Post.find(params[:id])
    authorize @post
    
    if @post.update(post_params)
      redirect_to @post
    else
      render :edit
    end
  end
  
  def index
    @posts = policy_scope(Post)
  end
end
```

### Using CanCanCan

Another popular authorization gem:

```ruby
# Gemfile
gem 'cancancan'

# app/models/ability.rb
class Ability
  include CanCan::Ability
  
  def initialize(user)
    user ||= User.new  # Guest user
    
    can :read, Post, published: true
    
    if user.persisted?
      can :create, Post
      can [:update, :destroy], Post, user_id: user.id
    end
    
    if user.admin?
      can :manage, :all
    end
  end
end
```

```ruby
# app/controllers/posts_controller.rb
class PostsController < ApplicationController
  load_and_authorize_resource
  
  def show
    # @post is automatically loaded and authorized
  end
end
```

## Common Patterns

### Restricting Actions

```ruby
class PostsController < ApplicationController
  before_action :require_login, except: [:index, :show]
  before_action :require_owner, only: [:edit, :update, :destroy]
  
  private
  
  def require_owner
    @post = Post.find(params[:id])
    unless @post.user == current_user
      redirect_to posts_path, alert: "Not your post"
    end
  end
end
```

### Guest vs Logged-In Views

```erb
<% if logged_in? %>
  <p>Welcome, <%= current_user.name %></p>
  <%= link_to "Logout", logout_path, method: :delete %>
<% else %>
  <%= link_to "Login", login_path %>
  <%= link_to "Sign Up", signup_path %>
<% end %>

<% if current_user&.admin? %>
  <%= link_to "Admin Dashboard", admin_path %>
<% end %>
```

### Scoped Queries

```ruby
class PostsController < ApplicationController
  def index
    @posts = if current_user&.admin?
      Post.all
    elsif current_user
      Post.where(published: true).or(Post.where(user: current_user))
    else
      Post.where(published: true)
    end
  end
end
```

## Security Tips

- Always use `has_secure_password` with bcrypt (never store plain passwords)
- Call `reset_session` after login to prevent session fixation
- Use `before_action` for consistent auth checks
- Authorize at the controller level, not just the view
- Use `find_by` (returns nil) not `find` (raises error) for auth lookups
- Implement account lockout after failed attempts
- Use HTTPS in production

## Tips

- Start with simple hand-rolled auth to understand the concepts
- Use Devise for full-featured production auth
- Choose Pundit for object-oriented policies or CanCanCan for DSL-style
- Authentication = who you are, Authorization = what you can do
- Always check authorization in controllers, not just views
- Test your auth logic thoroughly—it's security-critical

## See Also

- [[The Web]]
- [[Cookies and Sessions]] — How auth state is preserved
- [[Rails]]
