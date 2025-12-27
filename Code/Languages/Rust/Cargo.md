---
tags:
  - rust
  - cargo
  - tools
type: note
related:
  - '[[Rust]]'
  - '[[Testing]]'
  - '[[Modules]]'
---
# Cargo

Rust's package manager and build system.

## Overview

Cargo handles building code, downloading dependencies, running tests, generating documentation, and publishing to crates.io. Every Rust project uses Cargo.

## Basic Usage

### Creating Projects

```bash
# New binary project
cargo new my_project
cargo new my_project --bin  # Explicit

# New library project
cargo new my_lib --lib

# Initialize in existing directory
cargo init
cargo init --lib
```

### Project Structure

```
my_project/
├── Cargo.toml      # Project manifest
├── Cargo.lock      # Dependency lock file
├── src/
│   ├── main.rs     # Binary entry point
│   └── lib.rs      # Library entry point
├── tests/          # Integration tests
├── benches/        # Benchmarks
├── examples/       # Example binaries
└── target/         # Build output
```

### Building and Running

```bash
cargo build           # Debug build
cargo build --release # Optimized release build
cargo run             # Build and run
cargo run --release   # Run release build
cargo run -- arg1 arg2 # Pass arguments

cargo check           # Fast syntax/type check (no codegen)
```

### Testing

```bash
cargo test                    # Run all tests
cargo test test_name          # Run specific test
cargo test --lib              # Only library tests
cargo test --doc              # Only doc tests
cargo test -- --nocapture     # Show println! output
cargo test -- --test-threads=1  # Sequential tests
```

## Key Concepts

### Cargo.toml

```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"
authors = ["Your Name <you@example.com>"]
description = "A short description"
license = "MIT"
repository = "https://github.com/you/project"

[dependencies]
serde = "1.0"                    # From crates.io
serde_json = { version = "1.0", features = ["preserve_order"] }
my_lib = { path = "../my_lib" }  # Local path
other = { git = "https://github.com/user/other" }  # Git

[dev-dependencies]
criterion = "0.4"    # Only for tests/benchmarks

[build-dependencies]
cc = "1.0"           # For build.rs

[features]
default = ["std"]
std = []
extra = ["serde/derive"]

[[bin]]
name = "my_binary"
path = "src/bin/main.rs"

[[example]]
name = "demo"
path = "examples/demo.rs"
```

### Version Requirements

```toml
[dependencies]
# Caret (default) - compatible updates
serde = "1.0.0"      # >= 1.0.0 and < 2.0.0
serde = "1.0"        # Same as above
serde = "1"          # Same as above

# Tilde - patch updates only
serde = "~1.0.0"     # >= 1.0.0 and < 1.1.0

# Exact
serde = "=1.0.0"     # Exactly 1.0.0

# Wildcard
serde = "1.*"        # >= 1.0.0 and < 2.0.0

# Comparison
serde = ">=1.0, <2.0"
```

### Cargo.lock

```bash
# Cargo.lock pins exact versions
# Commit for binaries, don't commit for libraries

cargo update          # Update all dependencies
cargo update -p serde # Update specific package
```

### Workspaces

```toml
# Root Cargo.toml
[workspace]
members = [
    "crate_a",
    "crate_b",
    "shared",
]

[workspace.dependencies]
serde = "1.0"
tokio = { version = "1", features = ["full"] }
```

```toml
# crate_a/Cargo.toml
[dependencies]
serde = { workspace = true }
shared = { path = "../shared" }
```

## Common Commands

### Dependencies

```bash
cargo add serde              # Add dependency
cargo add serde --features derive
cargo add tokio -F full      # Short for --features
cargo remove serde           # Remove dependency
cargo tree                   # Show dependency tree
cargo update                 # Update dependencies
```

### Documentation

```bash
cargo doc            # Generate docs
cargo doc --open     # Generate and open in browser
cargo doc --no-deps  # Skip dependencies
```

### Publishing

```bash
cargo login          # Login to crates.io
cargo publish        # Publish to crates.io
cargo publish --dry-run  # Test without publishing
cargo yank --version 1.0.0  # Yank a version
```

### Other Commands

```bash
cargo fmt            # Format code (rustfmt)
cargo clippy         # Lint code
cargo clean          # Remove target directory
cargo bench          # Run benchmarks
cargo audit          # Check for vulnerabilities
cargo outdated       # Check for outdated deps
```

## Common Patterns

### Feature Flags

```toml
[features]
default = ["std"]
std = []
alloc = []
serde = ["dep:serde"]  # Optional dependency

[dependencies]
serde = { version = "1.0", optional = true }
```

```rust
#[cfg(feature = "serde")]
use serde::{Serialize, Deserialize};

#[cfg(feature = "std")]
fn with_std() { /* ... */ }
```

### Build Scripts

```rust
// build.rs
fn main() {
    // Rerun if this file changes
    println!("cargo:rerun-if-changed=build.rs");
    
    // Set environment variable
    println!("cargo:rustc-env=BUILD_TIME={}", chrono::Utc::now());
    
    // Link native library
    println!("cargo:rustc-link-lib=ssl");
}
```

### Multiple Binaries

```toml
[[bin]]
name = "server"
path = "src/bin/server.rs"

[[bin]]
name = "client"
path = "src/bin/client.rs"
```

```bash
cargo run --bin server
cargo run --bin client
```

### Profile Configuration

```toml
[profile.dev]
opt-level = 0
debug = true

[profile.release]
opt-level = 3
lto = true
codegen-units = 1
panic = "abort"

[profile.bench]
opt-level = 3

# Custom profile
[profile.release-with-debug]
inherits = "release"
debug = true
```

### Environment Variables

```bash
RUSTFLAGS="-C target-cpu=native" cargo build --release
CARGO_INCREMENTAL=0 cargo build
RUST_BACKTRACE=1 cargo run
RUST_LOG=debug cargo run
```

## Tips

- Use `cargo check` for fast iteration—it skips code generation
- Use `cargo clippy` to catch common mistakes
- Use `cargo fmt` to maintain consistent style
- Lock exact versions in `Cargo.lock` for reproducible builds
- Use workspaces for multi-crate projects
- Use feature flags to make functionality optional
- Use `--release` for production builds—debug builds are slow
- `cargo add` is easier than editing Cargo.toml manually

## See Also

- [[Testing]] — Running tests with Cargo
- [[Modules]] — Project organization
- [[Rust]]
