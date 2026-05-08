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
- [[Blocks]] — Block syntax, `yield`, `Proc`, and `lambda`
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

## Files and Serialization

- [[Files and Serialization]] — Overview of file I/O and data formats

- [[File IO]] — Reading and writing files
- [[Serialization]] — Converting objects to storable formats
- [[JSON in Ruby]] — Web APIs and data exchange
- [[YAML in Ruby]] — Configuration files and human-readable data

## Project Management

- [[Project Management]] — Project structure overview

- [[Require and Require Relative]] — Loading files and libraries
- [[Namespacing]] — Avoiding naming collisions with modules
- [[Gems and Bundler]] — Package management and dependencies

## Frameworks

- [[Rails]] — Full-stack web framework

## Tooling

- [[Debug]] — `puts`, `pp`, `binding.irb`, and debugger workflows

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

```folder-overview
id: 4ae36011-2e9a-49e3-b185-61d6a4faa2e0
folderPath: Code/Ruby
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="4ae36011-2e9a-49e3-b185-61d6a4faa2e0"></span>
- [[Code/Ruby/Arithmetic.md|Arithmetic]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Arrays.md|Arrays]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Blocks.md|Blocks]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Classes.md|Classes]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Conditional Logic.md|Conditional Logic]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Debug.md|Debug]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Enumerating Predicates.md|Enumerating Predicates]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Enumeration.md|Enumeration]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Hashes.md|Hashes]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Input Output.md|Input Output]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Loops.md|Loops]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Methods.md|Methods]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Modules.md|Modules]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Nested Collections.md|Nested Collections]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Pattern Matching.md|Pattern Matching]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Variables.md|Variables]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="4ae36011-2e9a-49e3-b185-61d6a4faa2e0"></span>
