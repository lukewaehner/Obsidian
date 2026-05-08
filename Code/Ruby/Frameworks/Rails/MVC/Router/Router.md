---
tags:
  - ruby
  - rails
  - routing
type: moc
related:
  - '[[Rails]]'
  - '[[REST]]'
  - '[[MVC]]'
---
# Routing

Mapping URLs to controller actions in Rails.

## Overview

The router is the doorman of your Rails application—it examines incoming requests (HTTP verb + URL) and directs them to the appropriate controller action. Routes are defined in `config/routes.rb` and follow RESTful conventions by default.

## Core Concepts

- [[Root Route]] — The homepage and default landing page
- [[RESTful Routes]] — The seven standard CRUD actions
- [[Route Helpers]] — Path and URL helper methods
- [[Custom Routes]] — Non-RESTful and specialized routes

## Quick Reference

```ruby
# config/routes.rb
Rails.application.routes.draw do
  root 'pages#home'              # Homepage
  resources :posts               # All 7 RESTful routes
  resources :users, only: [:show, :index]  # Limited routes
  get 'about', to: 'pages#about' # Custom route
end
```

```bash
# View all routes
bin/rails routes
bin/rails routes --expanded
# Or visit: localhost:3000/rails/info/routes
```

## See Also

- [[REST]] — RESTful architecture concepts
- [[MVC]] — How routing fits into MVC
- [[Rails]]

```folder-overview
id: e31a10b6-dbfe-4f92-b3bf-8211197dbfd7
folderPath: Code/Ruby/Frameworks/Rails/MVC/Router
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
<span class="fv-link-list-start" id="e31a10b6-dbfe-4f92-b3bf-8211197dbfd7"></span>
- [[Code/Ruby/Frameworks/Rails/MVC/Router/Custom Routes.md|Custom Routes]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Frameworks/Rails/MVC/Router/RESTful Routes.md|RESTful Routes]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Frameworks/Rails/MVC/Router/Root Route.md|Root Route]] <span class="fv-link-list-item"></span>
- [[Code/Ruby/Frameworks/Rails/MVC/Router/Route Helpers.md|Route Helpers]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="e31a10b6-dbfe-4f92-b3bf-8211197dbfd7"></span>
