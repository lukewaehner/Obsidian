---
tags:
  - ruby
type: note
related:
  - '[[Ruby]]'
  - '[[Conditional Logic]]'
---
# Loops

Iteration and looping constructs in Ruby.

## Overview

Ruby provides multiple ways to iterate: traditional loops (`while`, `until`, `for`), numeric iterators (`times`, `upto`, `downto`), and collection iterators (`each`, `map`, `select`). Idiomatic Ruby favors iterator methods over traditional loops.

## Basic Usage

### Loop (Infinite)

The simplest loop—runs forever until `break`:

```ruby
i = 0
loop do
  puts "i is #{i}"
  i += 1
  break if i == 10
end
```

### While Loop

Continues while condition is true:

```ruby
i = 0
while i < 10
  puts "i is #{i}"
  i += 1
end

# Inline (modifier) form
i = 0
puts i += 1 while i < 10
```

### Until Loop

Continues until condition becomes true (opposite of `while`):

```ruby
i = 0
until i >= 10
  puts "i is #{i}"
  i += 1
end

# Practical example
until gets.chomp == "yes"
  puts "Do you like Pizza?"
end
```

### For Loop

Iterates over a range or collection:

```ruby
for i in 0..5
  puts "#{i} zombies incoming!"
end

for letter in ['a', 'b', 'c']
  puts letter
end
```

> **Note:** `for` loops don't create a new scope—the variable `i` persists after the loop. Prefer `each` instead.

### Ranges

```ruby
(1..5)   # Inclusive: 1, 2, 3, 4, 5
(1...5)  # Exclusive: 1, 2, 3, 4

('a'..'d')       # a, b, c, d
('a'..'d').to_a  # => ["a", "b", "c", "d"]

# Check membership
(1..10).include?(5)  # => true
(1..10).cover?(5)    # => true (faster for continuous ranges)
```

## Numeric Iterators

### Times

Repeat a block n times:

```ruby
5.times do
  puts "Hello, World!"
end

# With index (0-based)
5.times do |i|
  puts "Iteration #{i}"  # 0, 1, 2, 3, 4
end

# One-liner
5.times { |i| puts i }
```

### Upto and Downto

```ruby
1.upto(5) { |n| print "#{n} " }    # 1 2 3 4 5
5.downto(1) { |n| print "#{n} " }  # 5 4 3 2 1

# Multi-line
1.upto(5) do |n|
  puts "Number: #{n}"
end
```

### Step

Iterate with a custom increment:

```ruby
0.step(10, 2) { |n| print "#{n} " }  # 0 2 4 6 8 10
10.step(0, -2) { |n| print "#{n} " } # 10 8 6 4 2 0
```

## Collection Iterators

### Each

The most common iterator—doesn't modify the collection:

```ruby
[1, 2, 3].each { |n| puts n }

# With index
['a', 'b', 'c'].each_with_index do |letter, index|
  puts "#{index}: #{letter}"
end

# Hash iteration
{ a: 1, b: 2 }.each do |key, value|
  puts "#{key} => #{value}"
end
```

### Map / Collect

Transform each element, returns new array:

```ruby
[1, 2, 3].map { |n| n * 2 }      # => [2, 4, 6]
["hi", "bye"].map(&:upcase)      # => ["HI", "BYE"]
```

### Select / Reject

Filter elements:

```ruby
[1, 2, 3, 4, 5].select { |n| n.even? }  # => [2, 4]
[1, 2, 3, 4, 5].reject { |n| n.even? }  # => [1, 3, 5]
[1, 2, 3, 4, 5].select(&:even?)         # => [2, 4]
```

### Reduce / Inject

Accumulate values:

```ruby
[1, 2, 3, 4].reduce(0) { |sum, n| sum + n }  # => 10
[1, 2, 3, 4].reduce(:+)                       # => 10
[1, 2, 3, 4].reduce(1, :*)                    # => 24
```

## Key Concepts

### Loop Control

```ruby
# break - exit the loop entirely
10.times do |i|
  break if i == 5
  puts i
end  # Prints 0-4

# next - skip to next iteration
10.times do |i|
  next if i.even?
  puts i
end  # Prints 1, 3, 5, 7, 9

# redo - restart current iteration (use carefully)
i = 0
3.times do
  puts "Attempt #{i}"
  i += 1
  redo if i < 2  # Restarts the block
end
```

### Return Values

```ruby
# each returns the original collection
result = [1, 2, 3].each { |n| n * 2 }
result  # => [1, 2, 3]

# map returns the transformed collection
result = [1, 2, 3].map { |n| n * 2 }
result  # => [2, 4, 6]

# while/until return nil
result = while false; end
result  # => nil
```

## Common Patterns

### Iterating with Multiple Variables

```ruby
# Parallel arrays
names = ["Alice", "Bob"]
ages = [30, 25]
names.zip(ages).each do |name, age|
  puts "#{name} is #{age}"
end

# Enumerable#each_cons (consecutive pairs)
[1, 2, 3, 4].each_cons(2) { |a, b| puts "#{a}, #{b}" }
# 1, 2
# 2, 3
# 3, 4

# Enumerable#each_slice (chunks)
[1, 2, 3, 4, 5, 6].each_slice(2) { |pair| p pair }
# [1, 2]
# [3, 4]
# [5, 6]
```

### Early Termination with Find

```ruby
# find returns first match (stops iterating)
[1, 2, 3, 4, 5].find { |n| n > 3 }     # => 4
[1, 2, 3, 4, 5].find_index { |n| n > 3 } # => 3
```

### Chaining Iterators

```ruby
(1..10)
  .select(&:even?)
  .map { |n| n ** 2 }
  .reduce(:+)
# => 220 (4 + 16 + 36 + 64 + 100)
```

### Infinite Sequences

```ruby
# Lazy evaluation for infinite sequences
(1..Float::INFINITY).lazy.select(&:even?).first(5)
# => [2, 4, 6, 8, 10]
```

## Tips

- Prefer `each` over `for`—it creates a proper scope and is more idiomatic
- Use `map` when transforming data, `each` when performing side effects
- `times` is cleaner than `for i in 0...n` for simple repetition
- Use `&:method_name` shorthand when calling a single method: `[1,2,3].map(&:to_s)`
- `break value` can return a value from a loop
- Avoid modifying a collection while iterating over it
- Use `lazy` for large or infinite sequences to avoid memory issues

## See Also

- [[Code/Languages/Ruby/Arrays]] — Collection methods
- [[Conditional Logic]] — Control flow
- [[Ruby]]
