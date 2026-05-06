---
type: note
tags:
  - ruby
  - rails
  - dependencies
  - version-control
related:
  - "[[Gemfile]]"
  - "[[Bundler]]"
---
# Gemfile.lock

The `Gemfile.lock` is an auto-generated file that represents the complete, resolved dependency tree for your application.

## Purpose

While the [[Gemfile|Gemfile]] declares what you *want*, the lock file records what you *have*—the exact versions of every gem and their dependencies.

## Structure

```
GEM
  remote: https://rubygems.org/
  specs:
    actioncable (7.0.1)
      actionpack (= 7.0.1)
      activesupport (= 7.0.1)
      nio4r (~> 2.0)
      websocket-driver (>= 0.6.1)
    actionpack (7.0.1)
      activesupport (= 7.0.1)
      rack (~> 2.0, >= 2.2.0)

PLATFORMS
  arm64-darwin-21
  x86_64-linux

DEPENDENCIES
  rails (~> 7.0)
  pg

BUNDLED WITH
  2.3.7
```

## When It Updates

| Command | Effect |
|---------|--------|
| `bundle install` | Only updates lock if Gemfile changed |
| `bundle update` | Re-resolves everything, updates lock |
| `bundle update gem_name` | Re-resolves specific gem, updates lock |

## Version Control

> **Always commit `Gemfile.lock` to version control.**

This ensures:
- All developers use identical gem versions
- Production matches development exactly
- Builds are reproducible

## Tips

- If you see merge conflicts in `Gemfile.lock`, resolve by running `bundle install`
- Review lock file changes in PRs—unexpected dependency updates can introduce bugs
- Use `bundle install --frozen` in CI to fail if lock file is out of sync

## See Also

- [[Gemfile]] — Declaring dependencies
- [[Bundler]] — How Bundler manages this file
- [[Rails]]
