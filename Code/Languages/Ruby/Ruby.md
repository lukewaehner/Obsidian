---
tags:
  - ruby
type: moc
---
# Ruby

Ruby is a dynamic, object-oriented programming language designed for developer happiness. It emphasizes readability and productivity with an elegant syntax.

## Core Language

- [[Input Output]] — Input / Output methods (`puts`, `print`, `p`)
- [[Arithmetic]] — Math operations and the Math module
- [[Code/Languages/Ruby/Functions]] — Methods, parameters, and blocks
- [[Modules]] — Namespacing and mixins
- [[Code/Languages/Ruby/Classes]] — Objects, inheritance, and encapsulation
- [[Code/Languages/Ruby/Variables|Variables]] - Data assignment, referencing
- [[Conditional Logic]] - Logic flow
- [[Code/Languages/Ruby/Arrays|Arrays]] - Collection objects
- [[Code/Languages/Ruby/Loops|Loops]] - Iteration

## Data Types

- [[Basic Datatypes]] - See Here

## Collections

- [[Arrays]] — Ordered, indexed collections
- [[Hashes]] — Key-value collections
- [[Nested Collections]] — Multidimensional arrays and hashes
- [[Enumeration]] — Iteration and transformation methods
- [[Enumerating Predicates]] — Boolean tests on collections

## Object-Oriented Programming

- [[Object Oriented Programming]] — OOP concepts overview

Core concepts:
- [[Inheritance]] — Single inheritance, super, method overriding
- [[Modules as Mixins]] — include, extend, prepend
- [[Encapsulation]] — public, private, protected
- [[Polymorphism]] — Duck typing and flexible interfaces

Class design:
- [[Class Methods and Variables]] — self, @@, singleton methods
- [[Method Visibility]] — Access control deep dive
- [[Composition]] — Building objects from other objects

## Frameworks

- [[Rails]] — Full-stack web framework

## Quick Reference

```ruby
# Variables
name = "Ruby"
age = 30
is_fun = true

# String interpolation
puts "Hello, #{name}!"

# Arrays and hashes
numbers = [1, 2, 3]
person = { name: "Alice", age: 30 }

# Iteration
numbers.each { |n| puts n }

# Methods
def greet(name)
  "Hello, #{name}!"
end

# Classes
class Person
  attr_accessor :name
  
  def initialize(name)
    @name = name
  end
end
```

## Resources

- [Ruby Documentation](https://ruby-doc.org/)
- [Ruby Style Guide](https://rubystyle.guide/)
