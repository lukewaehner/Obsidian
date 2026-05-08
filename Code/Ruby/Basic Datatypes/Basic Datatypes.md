---
tags:
  - ruby
type: moc
---
# Basic Datatypes

Core data types in Ruby for representing primitive values.

## Overview

Ruby is dynamically typed—variables don't have fixed types, but values do. Everything in Ruby is an object, including basic types like integers and booleans.

## Types

- [[Strings]] — Mutable text sequences
- [[Symbols]] — Immutable identifiers
- [[Booleans]] — True, false, and nil

## Numbers

Ruby has several numeric types:

```ruby
# Integer (arbitrary precision)
42
1_000_000      # Underscores for readability

# Float (double precision)
3.14
2.5e6          # Scientific notation

# Rational (exact fractions)
Rational(1, 3) # => (1/3)
1/3r           # => (1/3)

# Complex
Complex(2, 3)  # => (2+3i)
2 + 3i         # => (2+3i)
```

## Type Checking

```ruby
42.class           # => Integer
3.14.class         # => Float
"hello".class      # => String
:symbol.class      # => Symbol
true.class         # => TrueClass
nil.class          # => NilClass

# Check type
42.is_a?(Integer)  # => true
42.is_a?(Numeric)  # => true (parent class)
```

## Type Conversion

```ruby
# To String
42.to_s            # => "42"
3.14.to_s          # => "3.14"

# To Integer
"42".to_i          # => 42
3.9.to_i           # => 3 (truncates)

# To Float
"3.14".to_f        # => 3.14
42.to_f            # => 42.0

# To Symbol
"name".to_sym      # => :name

# To Array
"a,b,c".split(",") # => ["a", "b", "c"]
(1..3).to_a        # => [1, 2, 3]
```

## Quick Reference

| Type | Example | Mutable | Use Case |
|------|---------|---------|----------|
| Integer | `42` | No | Whole numbers |
| Float | `3.14` | No | Decimal numbers |
| String | `"hello"` | Yes | Text content |
| Symbol | `:name` | No | Identifiers, hash keys |
| TrueClass | `true` | No | Boolean logic |
| FalseClass | `false` | No | Boolean logic |
| NilClass | `nil` | No | Absence of value |

## See Also

- [[Ruby]]

```folder-overview
id: e144d1bb-bac6-4c6d-8b58-30e26cbe3603
folderPath: Code/Ruby/Basic Datatypes
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
<span class="fv-link-list-start" id="e144d1bb-bac6-4c6d-8b58-30e26cbe3603"></span>
- [[Code/Ruby/Basic Datatypes/Booleans.md|Booleans]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Basic Datatypes/Strings.md|Strings]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Basic Datatypes/Symbols.md|Symbols]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="e144d1bb-bac6-4c6d-8b58-30e26cbe3603"></span>
