---
tags:
  - ruby
type: note
related: []
---
# Blocks

A brief description of what this covers.

## Overview

A block can be declared as a single-line or multi-line block. 
Convention is to use `{}` for single-line and `do..end` for multi=line.
You can pass arguments to a parameter by defining them within pipes `|arg1, arg2|`


## Basic Usage

### Yield Keyword:
Can be called inside a method to relinquish execution to the accompanying block.
```ruby
def logger
	yield
end

logger { puts 'hello' }
# => hello

logger do
	p [1,2,3]
end
# => [1,2,3]
```

> Yield can be called multiple times

#### Working with arguments

```ruby
def param_print
	yield('P1')
	yield('P2')
end

param_print { |param| puts "Param: #{param}" }
# => Param: P1
# => Param: P2
```

#### Yield with each

```ruby
@transactions = [10, -15, 25, 30, -24]

def transaction_statement
	@transactions.each do |t|
		yield t # Pass each transaction to block
	end
end

transaction_statement do |t|
	p "%0.2f" % t # Bank can change the usage here
end
```

#### Safer usage:
Upon calling `yield` it has a return value from the last execution of the block, we can manipulate this to make things safer

```ruby
@transactions = [10, -15, 25, 30, -24]

def transaction_statement
	@transactions.each do |t|
		p yield t # Pass each transaction to block
	end
end

transaction_statement do |t|
	"%0.2f" % t # Bank defines format only
end
```

#### Collecting returned data

```ruby
@transactions = [10, -15, 25, 30, -24]

def transaction_statement
formatted_transactions = []
	@transactions.each do |t|
		formatted_transactions << yield(t) 
	end
	p formatted_transactions
end

transaction_statement do |t|
	"%0.2f" % t # Bank defines format only
end
```

Of course, we can add explicit returns in blocks, could be good for guard clause.

Blocks are forgiving with variable assignment and expectation, they will just not assign the passed argument, and continue with execution.

#### No argument bassed to block

```ruby
def say
	yield # no args
end

say do |word|
	puts "Word is: #{word}"
end
# => Word is:
```

#### Too many arguments passed to block

```ruby
def test
	yield('hello', 'world', 'lorem')
end

test do |first, second|
	puts "Testing: #{first}, #{second}"
end
# => Testing: hello, world
```

#### With hashes

```ruby
def test
	hash = { a: 'a val', b: 'b val' }
	
	hash.each do |key, value|
		yield key, value
	end
end

test { |key, value| puts "#{key}: #{value}" }
```

When writing methods that expect blocks by using `yield`, we need to make sure the caller includes a block

We can use `block_given?`

A conditional check to see if a block was included, if so it returns `true`, else `false`.

```ruby
def maybe
	if block_given?
		puts "All is good"
	else
		raise ArgumentError, "No block passed"
	end
end

maybe {} 
# => All is good

# maybe 
# => "No block passed" (ArgumentError)
```

### Lambas
- Write a block and save it to a variable.
- Can be useful if you're calling different methods but passing the same block to each.

#### Creation:
- `lambda` keyword.
- "stabby lambda" syntax `-> {}`

```ruby
lambda1 = lambda { puts "test" }
lambda2 = -> { puts "other test" }
```

#### Using

`#call` method.

```ruby
lambda1 = -> { puts "test" }
lambda1.call
```

arguments

```ruby
my_name = -> (name) { puts "hello #{name}" }
my_age = lambda { |age| puts "I am #{age}" }

my_name.call("luke")
my_age.call(22)
```

### Procs

An object you can use to store blocks and pass them around like variables. A lambda is just a proc object with some distinct behavior

```ruby
a_proc = Proc.new { puts "proc" }
a_proc.call
```

or

```ruby
a_proc = proc { puts "proc" }
a_proc.call
```

Same argument passing syntax, with some handling differences.

#### Procs vs Lambdas
- Procs do not care if you pass in fewer or more arguments than specified. 
- It doesn't care if you don't pass in anything at all. 
- It will assign `nil` to any parameters named, but not passed through as arguments.

```ruby
a_proc = proc { |a, b| puts "a: #{a} --- b: #{b}" }
a_proc.call("test")
```

This is also why this is possible:

```ruby
nested_arr = [[1,2], [3,4], [5,6]]
nested_arr.select {|a, b| a + b > 10 }
```

Select has two args specified `|a, b|`, we pass in a single element of nested array. 
The inner arrays `[1,2]` are deconstructed automatically so (a = 1, b = 2).
This only works because its a non-lambda proc.
The same code put switching `proc` keyword to `lambda` will cause `ArgumentError`

**Returning**

When writing an explicit return inside a lambda, it returns from the lambda block back to the caller.

```ruby
l1 = -> { return 1 }
l1.call
```

A proc, returns from the embracing method (method *defining* the proc).

```ruby
def m1
	p1 = proc { return }
	puts "printed"
	p1.call
	puts "doesnt reach"
end

m1
```

```ruby
def m1
	p1 = -> { return }
	p "printed"
	p1.call
	p "will reach this"
end

m1
```

Here we can see how procs are called inside the method defining it.

```ruby
def outer
	p1 = proc { return }
	p "will print"
	
	inner(p1)
	p "wont reach, defined in this method"
end

def inner(proc)
	proc.call
	puts "not reached either"
end

outer
# => "will print"
```

Proc is passed to another method which calls it, when `inner` calls the proc, it will return from `outer`. This can cause jumps.

#### Similarities

##### Default Arguments

```ruby
p1 = proc { |name="bob"| puts name }
p1.call

l1 = -> (name="bob again") { puts name }
l1.call
```

##### Method parameters

```ruby
def m1(useful_arg)
	useful_arg.call
end

l1 = -> { puts "lambda" }
p1 = proc { puts "proc" }

m1(l1)
# => lambda

m1(p1)
# => proc

```

#### Capturing blocks

```ruby
def m1(&b)
	b.call
end

m1 { puts "ok" }
```

> Block capturing `&` parameter should always go last

Capturing a block with `&` is known as an explicit block. If its not named in parameter list, its known as an implicit block.

When you capture a block using `&` you can still use `yield` over `#call` to execute the block.

```ruby
a1 = ["1", "2"]

a1.map! { |a| a.to_i }
p a1

a2 = ["1", "2", "3"]

a2.map!(&:to_i)
p a2
```

Looking at `a2` and its execution, we use `&` to create an. anonymous proc and yield each array value to it, since it calls `#to_proc` on the symbol `:to_i`. 
It returns a proc object which responded to the given method indicated by the symbol.

So, for `a2`, `#map` yields each value in the array to the proc object, which calls `#to_i` on it. (Name of methods can be passed around using symbols).
## Key Concepts

Explain the important ideas.

## Common Patterns

```ruby
# Idiomatic Ruby examples
```

## Tips

- Practical advice
- Gotchas to avoid
- Best practices

## See Also

- [[Related Note]]
- [[Ruby]]
