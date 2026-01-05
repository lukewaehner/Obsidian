---
tags:
  - ruby
  - rails
type: note
related:
  - '[[Rails]]'
---
# Active Record

Data behind the application. Active Record is the interface rails gives between the database and your application.
## Overview

What an ORM is
How and why Active Record can be more useful than just SQL
Two steps to make a new row
Generators in rails

### What is an ORM?
ORM stands for Object-Relational-Mapping. It means that Active Record takes data stored in a database table using rows and columns, and lets us interact as if it were a Ruby object.

If you want to get an array listing all users, instead of writing code to connect and some `SELECT * FROM users` query, we can type User.all, and we get an array filled with user objects.

It also doesn't matter what type of database we are using (given `config/database.yml` is setup properly). 

### Rails Models
You want to store information about users, so we make a model called `User` to reference the database table `users`.

We can use all the methods like `all`, `find`, `create`. 

#### Working with models recap
```ruby
u = User.new(name: "User", email: "user@email.com")
```

If you don't pass a hash you can just add things in with `u.name = "Still User"`

We then need to save it, we can use `u.save`

Both steps run in one with the `#create` method

```ruby
u = User.create(name: "User", email: "user@email.com")
```

We can override the table we are looking at for a given model with `ActiveRecord::Base.table_name=`

```ruby
class Book < ApplicationRecord
	self.table_name = "my_books"
end
```

If we do this, we need to manually define the class name hosting the fixtures (`my_books.yml`). 
Using the `set_fixture_class` method in your test definition

```ruby
# test/models/book_test.rb
class BookTest < ActivefSupport::TestCase
	set_fixture_class my_books: Book
	fixtures :my_books
	# ...
end
```

We can also override the column that is used as the table's primary key

```ruby
class Book < ApplicationRecord
	self.primary_key = "book_id"
end
```



## Basic Usage

```ruby
# Rails example code
```

## Configuration

```ruby
# config/application.rb or initializer settings
```

## Common Patterns

```ruby
# Idiomatic Rails examples
```

## Commands

```bash
bin/rails command_here
```

## Tips

- Practical advice
- Gotchas to avoid
- Best practices

## See Also

- [[Rails]]
- [[Related Note]]
