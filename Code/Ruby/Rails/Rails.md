
## Generate New Rails App
> `rails new name`
> Generates standard rails app 

Configs:
- -d: choose what database
	- Defaults to `sqlite3`
	- Other options include `postgresql` and `mysql`
- Options are skippable, read into each option and choose what is appropriate (all can be added back later)

## Bundler
A dependency of rails itself, automatically included to manage gems throughout application

## Gemfile
Included at the root of the application, a manifest file named `Gemfile` , tracks dependencies including the version of Rails being used. 

### Syntax:
Uses version strings for versioning, or in absense, defaults to the latest stable version

```ruby
gem 'kaminari'
gem 'nokogiri'

# More advanced
gem 'nokogiri', '1.5.6'
gem 'pry-rails', '> 0.2.2'
gem 'decent_exposre', '~> 2.0.1'
```

### Installation:
Similar to `npm i`, we use bundle install to make sure all dependencies in the `Gemfile` are available in the Rails app.

Rails requires all Gems in the Gemfile when starting up, to load a dependency only in a specific environment, we can use environment names as symbols

```ruby
group :development, :test do
	gem "debug", platforms: %i[ mri mingw x64_mingw]
	gem "rspec_rails"
end

group :development do
	gem "web_console"
end
```

Sometimes gems used in require statements differ from the name of the gem in the repository, `:require` options solves it in the `Gemfile`

```ruby
gem 'webmock', require: 'webmock/rspec'
```

You can also use local gems with a `:path` option:

```ruby
gem 'nokogiri', path: `~/code/nokogiri`
```

### Lock file
Every time we run `bundle install` or `bundle update`, bundler calculates the dependency tree for the application. `Gemfile.lock` is a representation of the dependency tree
```ruby
GEM
	remote: https://rubygems.org/
	specs:
		nio4r (~> 2.0)
		mail. (>= 2.7.1)
		activejob (= 7.0.1)
		net-imap
		net-pop
```

> **The Lock File should always be committed to version control, so all development machines can use the same version**

## Binstubs
Running commands prefixed with `bundle exec` ensures code can require all correct gem versions. `Bundler` offers `binstubs` they are small shell scripts that load up Bundler first to ensure you load the correct executable

The following stubs are available by default on every new Rails project
- `bin/bundle`
- `bin/rails`
- `bin/rake` (usually we delete this file, `rails` is used to run Rake tasks now)
- `bin/importmap`

### Adding a binstub
To add a `binstub` of a commonly used executable, invoke `bundle binstubs some-gem-name`.  Another way we can do it is with `direnv`, and enabling `./bin` is in the search path. `direnv` manipulates the path whenever you enter a directory With installation, we can add `PATH_add bin` to the `.envrc` file.

## RSpec and Haml:
These two gems are added at the beginning of every project, RSpec (test framework) and haml (template engine for HTML that supports inlined Ruby)

```ruby
# Haml for templating
gem "haml-rails"

group :development, :test do
	gem "debug", platforms: %i[ mri mingw x64_mingw ]
	
	# RSpec for testing
	gem "rspec-rails"
end
```

Use `rails generate spec:install` to generate the spec directory

We also convert the layout file added to every Rails project to haml with `rails generate haml:application_layout convert:`

## Running an Application:
In bin/rails:
```ruby
#!/usr/bin/env ruby
APP_PATH = File.expand_path("../config/application", __dir__)
require_relative "../config/boot"
require "rails/commands"
```

First line sets up a constnat with the path to our application config `config/application.rb` file, which will be used by the Rails gem

It will the load the `config/boot.rb` file:

```ruby
ENV['BUNDLE_GEMFILE'] ||= File.expand_path('../Gemfile', __dir__)

require 'bundler/setup' # Set up gems listed in Gemfile
require 'bootsnap/setup' # Speed up boot times with caching
```

### Main Module and Class

```ruby
module TimeAndExpenses
	class Application < Rails::Application
		# Init config defaults for Rails version
		config.load_defaults 7.0
		
		# Settings in config/environments/* take precendence 
		# over those specialized here
		# Applicatio config can go into files in config/initializers
		# all .rb files in that directory are auto loaded after
		# framework and gems load
	end
end
```

Creating a module for your application allows multiple Rails applications running in the same Ruby process

## Logging

### Console
Supply a block to console to be evaluated when the Rails env is loaded via the terminal. This enables console-specific configurations.

```ruby
console do
	def obie
		User.where(email: "obie@gmail.com").first
	end
end
```

## Zeitwerk - File Naming
There is a specific naming convention for things to be accessed in Rails.

If the class or module is not nested, insert an underscore between the constant's names and require a file of this name. Example:

- EstimationCalculator becomes `require "estimation_calculator"`
- KittTurboBoost becomes `require "kitt_turbo_boost"`