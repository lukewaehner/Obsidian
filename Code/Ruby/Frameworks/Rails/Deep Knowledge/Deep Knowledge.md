---
tags:
  - ruby
  - rails
  - internals
type: moc
related:
  - '[[Rails]]'
---
# Deep Knowledge

Under-the-hood Rails internals and how the framework works.

## Overview

Understanding Rails internals helps you debug issues, configure your application correctly, and work more effectively with the framework. These notes cover what happens behind the scenes when you run Rails commands and how the framework initializes.

## Boot & Initialization

- [[Boot Process]] — How Rails starts up from `bin/rails` to a running app
- [[Binstubs]] — Wrapper scripts that ensure correct gem versions

## Development Environment

- [[Development Mode]] — Hot reloading, debugging, and development-specific behavior

## Code Loading

- [[Zeitwerk Autoloading]] — How Rails automatically loads your classes

## See Also

- [[Rails]]
- [[Ruby]]

%% Begin Waypoint %%
- [[Binstubs]]
- [[Boot Process]]
- [[Development Mode]]

%% End Waypoint %%