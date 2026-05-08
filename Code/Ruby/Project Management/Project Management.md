---
tags:
  - ruby
type: moc
related:
  - '[[Ruby]]'
---
# Project Management

Managing Ruby project structure, dependencies, and file organization.

## Overview

Ruby projects require organizing code across multiple files, managing external dependencies, and structuring directories for maintainability. This section covers the tools and patterns for professional Ruby project management.

## File Organization

- [[Require and Require Relative]] — Loading Ruby files and understanding load paths
- [[Namespacing]] — Avoiding naming collisions with modules

## Dependency Management

- [[Gems and Bundler]] — Installing and managing external packages

## Typical Project Structure

```
my_project/
├── lib/                    # Main application code
│   ├── my_project.rb       # Entry point, requires other files
│   └── my_project/
│       ├── models/
│       ├── services/
│       └── utils/
├── bin/                    # Executable scripts
├── spec/ or test/          # Tests
├── Gemfile                 # Dependency declarations
├── Gemfile.lock            # Locked dependency versions
├── README.md
└── my_project.gemspec      # If building a gem
```

## See Also

- [[Ruby]]
- [[Modules]] — Module basics for namespacing

```folder-overview
id: 1fa5b420-083e-4315-aad7-f2760859099a
folderPath: Code/Ruby/Project Management
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
<span class="fv-link-list-start" id="1fa5b420-083e-4315-aad7-f2760859099a"></span>
- [[Code/Ruby/Project Management/Gems and Bundler.md|Gems and Bundler]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Project Management/Namespacing.md|Namespacing]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Project Management/Require and Require Relative.md|Require and Require Relative]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="1fa5b420-083e-4315-aad7-f2760859099a"></span>
