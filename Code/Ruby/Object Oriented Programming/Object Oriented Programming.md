---
tags:
  - ruby
  - oop
type: moc
related:
  - '[[Ruby]]'
---
# Object Oriented Programming

Object-oriented programming concepts and patterns in Ruby.

## Overview

Ruby is a purely object-oriented language—everything is an object, including primitives like numbers and booleans. Ruby's OOP model emphasizes flexibility, duck typing, and developer happiness over strict type hierarchies.

## Core Concepts

- [[Inheritance]] — Single inheritance, `super`, method overriding
- [[Modules as Mixins]] — `include`, `extend`, `prepend` for shared behavior
- [[Encapsulation]] — Controlling access with `public`, `private`, `protected`
- [[Polymorphism]] — Duck typing and flexible interfaces

## Class Design

- [[Class Methods and Variables]] — `self`, `@@` vs `@`, singleton methods
- [[Method Visibility]] — Deep dive on access control
- [[Composition]] — Building objects from other objects

## Related Notes

- [[Code/Languages/Ruby/Classes|Classes]] — Class fundamentals and syntax
- [[Modules]] — Module basics and namespacing

## Key Principles

Ruby's OOP philosophy differs from languages like Java or C++:

1. **Duck Typing** — "If it walks like a duck and quacks like a duck, it's a duck." Ruby cares about what an object *can do*, not what it *is*.

2. **Open Classes** — Classes can be reopened and modified at runtime, allowing monkey-patching and extensions.

3. **Single Inheritance + Mixins** — Ruby uses single inheritance but provides modules for sharing behavior across class hierarchies.

4. **Everything is an Object** — Even classes are objects (instances of `Class`), and methods are objects too.

5. **Message Passing** — Calling a method is really "sending a message" to an object, which can be done dynamically with `send`.

## See Also

- [[Ruby]]

```folder-overview
id: 24c4551e-ef01-4ff2-aec6-d9d2260e58b4
folderPath: Code/Ruby/Object Oriented Programming
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
<span class="fv-link-list-start" id="24c4551e-ef01-4ff2-aec6-d9d2260e58b4"></span>
- [[Code/Ruby/Object Oriented Programming/Class Methods and Variables.md|Class Methods and Variables]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Object Oriented Programming/Composition.md|Composition]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Object Oriented Programming/Encapsulation.md|Encapsulation]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Object Oriented Programming/Inheritance.md|Inheritance]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Object Oriented Programming/Method Visibility.md|Method Visibility]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Object Oriented Programming/Modules as Mixins.md|Modules as Mixins]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Object Oriented Programming/Polymorphism.md|Polymorphism]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="24c4551e-ef01-4ff2-aec6-d9d2260e58b4"></span>
