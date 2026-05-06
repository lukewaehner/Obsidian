---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Arrays]]'
  - '[[Hashes]]'
  - '[[Enumeration]]'
  - '[[Enumerating Predicates]]'
---
# Nested Collections

Arrays and hashes containing other arrays or hashes for storing complex, structured data.

## Overview

Collections can contain other collections, creating multidimensional or nested structures. Nested arrays are useful for grids, matrices, or grouped data. Nested hashes store complex associated data with multiple levels of key-value pairs. Understanding how to access, modify, and iterate over these structures is essential for working with real-world data.

## Nested Arrays

Arrays containing other arrays, also called multidimensional arrays:

```ruby
# Grouped similar data (student test scores)
test_scores = [
  [97, 76, 79, 93],
  [79, 84, 76, 79],
  [88, 67, 64, 76],
  [94, 55, 67, 81]
]

# Positional data (rows and columns)
teacher_mailboxes = [
  ["Adams", "Baker", "Clark", "Davis"],
  ["Jones", "Lewis", "Lopez", "Moore"],
  ["Perez", "Scott", "Smith", "Young"]
]
```

### Accessing Elements

Use chained indices `array[x][y]` where `x` is the outer index and `y` is the inner index:

```ruby
teacher_mailboxes[0][0]   # => "Adams" (first row, first column)
teacher_mailboxes[1][0]   # => "Jones" (second row, first column)
teacher_mailboxes[2][0]   # => "Perez" (third row, first column)
```

Negative indices count from the end:

```ruby
teacher_mailboxes[0][-1]   # => "Davis" (first row, last column)
teacher_mailboxes[-1][0]   # => "Perez" (last row, first column)
teacher_mailboxes[-1][-2]  # => "Smith" (last row, second to last)
```

### Safe Access with dig

Accessing a nonexistent nested element raises `NoMethodError` because `nil` has no `[]` method:

```ruby
teacher_mailboxes[3][0]    # => NoMethodError (row 3 doesn't exist)
teacher_mailboxes[0][4]    # => nil (column 4 doesn't exist, but row 0 does)
```

Use `dig` to safely return `nil` for any missing level:

```ruby
teacher_mailboxes.dig(3, 0)  # => nil (safe)
teacher_mailboxes.dig(0, 4)  # => nil (safe)
```

### Creating Nested Arrays

**The gotcha**: Using `Array.new(size, default)` with a mutable default creates references to the *same* object:

```ruby
# WRONG: All inner arrays are the same object
mutable = Array.new(3, Array.new(2))
# => [[nil, nil], [nil, nil], [nil, nil]]

mutable[0][0] = 1000
mutable
# => [[1000, nil], [1000, nil], [1000, nil]]  # All changed!
```

**The solution**: Pass a block to create independent objects:

```ruby
# CORRECT: Each inner array is a separate object
immutable = Array.new(3) { Array.new(2) }
# => [[nil, nil], [nil, nil], [nil, nil]]

immutable[0][0] = 1000
immutable
# => [[1000, nil], [nil, nil], [nil, nil]]  # Only first changed
```

This applies to any mutable default: strings, arrays, hashes, or other objects.

### Adding and Removing Elements

Add to the outer array:

```ruby
test_scores << [100, 99, 98, 97]
# => [[97, 76, 79, 93], [79, 84, 76, 79], [88, 67, 64, 76], [94, 55, 67, 81], [100, 99, 98, 97]]
```

Add to a specific inner array:

```ruby
test_scores[0].push(100)
# => [97, 76, 79, 93, 100]
```

Remove from outer or inner:

```ruby
test_scores.pop           # Removes last inner array
test_scores[0].pop        # Removes last element from first inner array
```

### Iterating Over Nested Arrays

Think of nested arrays as rows and columns:

```ruby
teacher_mailboxes.each_with_index do |row, row_index|
  puts "Row:#{row_index} = #{row}"
end
# Row:0 = ["Adams", "Baker", "Clark", "Davis"]
# Row:1 = ["Jones", "Lewis", "Lopez", "Moore"]
# Row:2 = ["Perez", "Scott", "Smith", "Young"]
```

Nest iterators to access individual elements:

```ruby
teacher_mailboxes.each_with_index do |row, row_index|
  row.each_with_index do |teacher, col_index|
    puts "Row:#{row_index} Col:#{col_index} = #{teacher}"
  end
end
# Row:0 Col:0 = Adams
# Row:0 Col:1 = Baker
# ...
```

Use `flatten` when you only need the elements:

```ruby
teacher_mailboxes.flatten.each do |teacher|
  puts "#{teacher} is amazing!"
end
# Adams is amazing!
# Baker is amazing!
# ...
```

## Nested Hashes

Hashes containing other hashes for complex associated data:

```ruby
vehicles = {
  alice: { year: 2019, make: "Toyota", model: "Corolla" },
  blake: { year: 2020, make: "Volkswagen", model: "Beetle" },
  caleb: { year: 2020, make: "Honda", model: "Accord" }
}
```

### Accessing Data

Chain keys with `hash[:x][:y]`:

```ruby
vehicles[:alice][:year]   # => 2019
vehicles[:blake][:make]   # => "Volkswagen"
vehicles[:caleb][:model]  # => "Accord"
```

Use `dig` for safe access:

```ruby
vehicles[:zoe][:year]       # => NoMethodError (zoe doesn't exist)
vehicles.dig(:zoe, :year)   # => nil (safe)
vehicles[:alice][:color]    # => nil (color key doesn't exist)
vehicles.dig(:alice, :color) # => nil (safe)
```

### Adding and Removing Data

Add a new nested hash:

```ruby
vehicles[:dave] = { year: 2021, make: "Ford", model: "Escape" }
```

Add to an existing nested hash:

```ruby
vehicles[:dave][:color] = "red"
# dave is now: { year: 2021, make: "Ford", model: "Escape", color: "red" }
```

Delete an entire nested hash:

```ruby
vehicles.delete(:blake)
# => { year: 2020, make: "Volkswagen", model: "Beetle" }
```

Delete from a nested hash:

```ruby
vehicles[:dave].delete(:color)
# => "red"
```

### Iterating Over Nested Hashes

```ruby
vehicles.each do |owner, data|
  puts "#{owner} owns a #{data[:year]} #{data[:make]} #{data[:model]}"
end
# alice owns a 2019 Toyota Corolla
# caleb owns a 2020 Honda Accord
# dave owns a 2021 Ford Escape
```

## Key Concepts

### The dig Method

Works on both arrays and hashes for safe deep access:

```ruby
# Arrays
matrix = [[1, 2], [3, 4]]
matrix.dig(0, 1)      # => 2
matrix.dig(5, 0)      # => nil

# Hashes
data = { user: { profile: { name: "Alice" } } }
data.dig(:user, :profile, :name)  # => "Alice"
data.dig(:user, :settings, :theme) # => nil

# Mixed nesting
mixed = { users: [{ name: "Alice" }, { name: "Bob" }] }
mixed.dig(:users, 0, :name)  # => "Alice"
```

### Nested Predicate Enumeration

Combine predicates for complex conditions:

```ruby
test_scores = [[97, 76, 79, 93], [79, 84, 76, 79], [88, 67, 64, 76], [94, 55, 67, 81]]

# Did ANY student score above 80 on ALL tests?
test_scores.any? { |scores| scores.all? { |s| s > 80 } }
# => false (no student aced everything)

# Did ALL students score above 80 on ANY test?
test_scores.all? { |scores| scores.any? { |s| s > 80 } }
# => true (every student has at least one score > 80)
```

## Common Patterns

### Filtering Nested Hashes

```ruby
# Find vehicles from 2020 or newer
vehicles.select { |owner, data| data[:year] >= 2020 }
# => { caleb: {...}, dave: {...} }
```

### Extracting Values with Conditions

```ruby
# Get only the owner names (not the full hash)
vehicles.collect { |owner, data| owner if data[:year] >= 2020 }.compact
# => [:caleb, :dave]

# Better: use filter_map (Ruby 2.7+)
vehicles.filter_map { |owner, data| owner if data[:year] >= 2020 }
# => [:caleb, :dave]
```

### Building Nested Structures

```ruby
# Group data by a key
people = [
  { name: "Alice", dept: "Engineering" },
  { name: "Bob", dept: "Sales" },
  { name: "Carol", dept: "Engineering" }
]

people.group_by { |p| p[:dept] }
# => { "Engineering" => [{name: "Alice"...}, {name: "Carol"...}], "Sales" => [...] }
```

### Default Values for Missing Keys

```ruby
# Hash with default empty hash
data = Hash.new { |h, k| h[k] = {} }
data[:new_key][:nested] = "value"
data  # => { new_key: { nested: "value" } }

# Nested default hashes
deep = Hash.new { |h, k| h[k] = Hash.new { |h2, k2| h2[k2] = [] } }
deep[:a][:b] << "item"
deep  # => { a: { b: ["item"] } }
```

## Tips

- Always use `dig` when accessing nested data that might not exist
- Use blocks with `Array.new` when creating nested arrays with mutable defaults
- Use `flatten` before iterating when you don't need the nested structure
- Chain methods like `select`, `collect`, and `compact` for complex queries
- Consider `filter_map` (Ruby 2.7+) to combine mapping and filtering
- Think of nested arrays as rows/columns or grids for mental modeling
- Browse Ruby documentation when you have a specific use case—there's often a built-in method

## See Also

- [[Arrays]] — Array fundamentals
- [[Hashes]] — Hash fundamentals
- [[Enumeration]] — Iteration methods
- [[Enumerating Predicates]] — Conditional checks on collections
- [[Ruby]]
