---
type: note
tags:
  - ruby
  - rails
  - testing
  - rspec
related:
  - "[[Gemfile]]"
---
# RSpec Setup in Rails

RSpec is a behavior-driven development (BDD) testing framework. It's the most popular alternative to Rails' default Test::Unit.

## Installation

Add to your [[Rails - Gemfile|Gemfile]]:

```ruby
group :development, :test do
  gem 'rspec-rails'
end
```

Then install:

```bash
bundle install
rails generate rspec:install
```

This creates:

```
spec/
├── spec_helper.rb      # RSpec configuration
├── rails_helper.rb     # Rails-specific configuration
└── .rspec              # Command-line options
```

## Directory Structure

RSpec organizes tests by type:

```
spec/
├── models/             # Model specs
├── controllers/        # Controller specs (legacy)
├── requests/           # Request/integration specs (preferred)
├── system/             # Browser tests (Capybara)
├── helpers/            # Helper specs
├── mailers/            # Mailer specs
├── jobs/               # ActiveJob specs
├── services/           # Service object specs
└── support/            # Shared examples, helpers
```

## Running Tests

```bash
bin/rspec                      # Run all specs
bin/rspec spec/models/         # Run model specs
bin/rspec spec/models/user_spec.rb:42  # Run specific line
bin/rspec --format documentation       # Verbose output
```

## Basic Example

```ruby
# spec/models/user_spec.rb
require 'rails_helper'

RSpec.describe User, type: :model do
  describe 'validations' do
    it 'requires an email' do
      user = User.new(email: nil)
      expect(user).not_to be_valid
      expect(user.errors[:email]).to include("can't be blank")
    end
  end

  describe '#full_name' do
    it 'combines first and last name' do
      user = User.new(first_name: 'Jane', last_name: 'Doe')
      expect(user.full_name).to eq('Jane Doe')
    end
  end
end
```

## Useful Gems to Pair

```ruby
group :development, :test do
  gem 'rspec-rails'
  gem 'factory_bot_rails'   # Test fixtures
  gem 'faker'               # Generate fake data
  gem 'shoulda-matchers'    # One-liner matchers
end

group :test do
  gem 'capybara'            # Browser simulation
  gem 'webdrivers'          # Manage browser drivers
end
```

## Tips

- Use `--only-failures` to re-run failed specs
- Prefer request specs over controller specs for integration testing
- Use `let` for lazy-loaded test data, `let!` for eager loading
- Run `rails generate rspec:model User` to generate spec files with generators

## See Also

- [[Gemfile]] — Adding test dependencies
- [[Rails]]
