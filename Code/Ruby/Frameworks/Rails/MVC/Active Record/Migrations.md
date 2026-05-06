---
tags:
  - ruby
  - rails
type: note
related:
  - '[[Rails]]'
---
# Migrations

Schema migration, modifying the database schema in place without moving it to a new location.
## Overview

### What are migrations

A script sets up or modifies a database's schema in a reversible and appliable way.

Creating and dropping tables, adding and removing columns, and other modifications are changes to the schema

Adding and removing rows are not.

Multiple migrations can run in sequence like a script, Migrations use schema-altering SQL commands under the hood, like the Model makes SQL queries for you.

### When Migrations are needed

After spinning up a new application, and running necessary commands like
`rails db:create` and `rails generate model Car make:string` then `rails db:migrate`

1. Create a model file in `app/models`, which is done with the `generate`
2. Create a database table that has appropriate columns. If using `generate` just run `rails db:migrate`

### How to create a migratikon file
Two ways
1. `rails generate model YourModelNameHere`
2. Migration generator `rails generate migration NameYourMigration`

#### Using the model generator
Migration files can be created by running generators, which creates a model file and migration file to pair. This also makes specs and test files.

#### Using the migration generator
use `rails generate migration NameYourMigration`, we use this after setup with modifying data table. 

### Writing Migrations
To add instructions to the migration file's contents, add correct Ruby method to the migration file, like `create_table`, and provide necessary parameters.

### Run Migrations
`rails db:migrate` runs all not- run migrations.

### Why are they useful
Migrations can be used to wipe databases and restart with the same schema but new data. It can be used to make duplicate databases (like when you go to prod). 

If we screw up, we can use `rails db:rollback` and the last series of migrations will be reversed. 

For each method used in migrations, we want to specify how to reverse it. The reverse of adding is dropping a table, reverse of adding a column is removing, and so on. 

Most are obvious, and can be created using the `change` method, some are not obvious and need specific `up` and `down` methods. 

1. `up` runs on migrations
2. `down` runs on rollback

Generally

| Situation           | USe                       |
| ------------------- | ------------------------- |
| Schema changes only | change                    |
| Data migrations     | up/down                   |
| Raw sql             | up / down or `reverisble` |
| One-way migration   | up only (intentional)     |
Rollbacks are used for mistakes, its important to know that migrations can remove or drop things like `remove_column` method.

### Naming Conventions

##### Creating A New Table
`CreateXXX` followed by a list of column names and types.

##### Adding Columns
`AddColumnToTable` followed by a list of colum names and types.

```ruby
generate migration AddPartNumberToProducts part_number:string
```

It generates the migration

```ruby
class AddPartNumberToProducts < ActiveRecord::Migration[8.1]
	def change
		add_column :products, :part_number, :string
	end
end
```

Can add indexes too

```ruby
generate migration ADdPartNumberToProducts part_number:string:index
```

Multiple columns are possible too

```ruby
generate migration AddDetailsToProducst part_number: string price_decimal
```

##### Removing Columns 

```ruby
generate migration RemovePartNumberFromProducts part_number:string
```

### Creating Associations
Define relationships between different models so they can interact

One case is creating foreign keys between tables, we can use columns types like `references` to make this process happen.

```ruby
generate migration AddUserRefToProducts user:references
```

```ruby
class AddUserRefToProducst < ActiveRecord::Migreation[8.1]
	def change
		add_reference :products, :user, null: false, foreign_key: true
	end
end
```

We can also make join tables happen with `JoinTable`

```ruby
generate migration CreateJoinTableUserProduct user product
```


```ruby
class CreateJoinTableUserProduct < ActiveRecord::Migration[8.1]
	def change
		create_join_table :users :products do |t|
		# t.idnex [:user_id. :product_id]
		# t.index [:product_id, :user_id]
		end
	end
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
