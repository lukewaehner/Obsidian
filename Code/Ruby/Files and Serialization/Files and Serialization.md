---
tags:
  - ruby
type: moc
related:
  - '[[Ruby]]'
---
# Files and Serialization

Reading, writing, and storing data in Ruby.

## Overview

Files are streams of bytes that your program can read, modify, and save. Ruby provides intuitive tools to work with files as strings or arrays of lines. Serialization converts Ruby objects into storable formats (strings) that can be saved to files or transmitted over networks. This enables data persistence, state saving, and communication with web APIs.

## Core Concepts

- [[File IO]] — Reading and writing files with Ruby's File class
- [[Serialization]] — Converting objects to storable string formats

## Data Formats

- [[JSON in Ruby]] — JavaScript Object Notation for web APIs and data exchange
- [[YAML in Ruby]] — Human-readable format for configuration files

## Why Serialization Matters

Serialization enables three key capabilities:

1. **Persistence** — Save program state to resume later (game saves, user preferences)
2. **Data Transfer** — Send complex objects over HTTP (only strings travel over the network)
3. **Configuration** — Store settings in human-readable files

## Quick Reference

```ruby
# Reading a file
content = File.read('data.txt')           # Entire file as string
lines = File.readlines('data.txt')        # Array of lines

# Writing a file
File.write('output.txt', 'Hello, World!')

# JSON
require 'json'
json_string = { name: 'Alice', age: 30 }.to_json
data = JSON.parse(json_string)

# YAML
require 'yaml'
yaml_string = { name: 'Alice', age: 30 }.to_yaml
data = YAML.safe_load(yaml_string)
```

## See Also

- [[Ruby]]
- [[Input Output]] — Console I/O with puts, print, gets

```folder-overview
id: 03ea913e-3d90-4420-a72f-b454dec7d7f1
folderPath: Code/Ruby/Files and Serialization
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
<span class="fv-link-list-start" id="03ea913e-3d90-4420-a72f-b454dec7d7f1"></span>
- [[Code/Ruby/Files and Serialization/File IO.md|File IO]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Files and Serialization/JSON in Ruby.md|JSON in Ruby]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Files and Serialization/Serialization.md|Serialization]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Files and Serialization/YAML in Ruby.md|YAML in Ruby]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="03ea913e-3d90-4420-a72f-b454dec7d7f1"></span>
