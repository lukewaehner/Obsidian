---
tags:
  - rust
  - tooling
  - cargo
type: note
related:
  - "[[Rust]]"
  - "[[Cargo]]"
  - "[[Modules]]"
  - "[[Testing]]"
---
# Projects

Setting up, managing, and building Rust projects from scratch.

## rustup — Toolchain Manager

`rustup` installs and manages Rust versions. It's the first thing you install.

```bash
# Install rustup (and stable Rust)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Update everything
rustup update

# Show what's installed
rustup show

# Check active toolchain
rustup toolchain list
```

### Toolchains

Rust ships three channels:

| Channel | Description |
|---------|-------------|
| `stable` | Current stable release, updated every 6 weeks |
| `beta` | Next release candidate |
| `nightly` | Cuts every night — unstable features, required for some tools |

```bash
# Install a channel
rustup toolchain install nightly
rustup toolchain install stable

# Set default
rustup default stable

# Use a specific toolchain for one command
cargo +nightly build
rustc +nightly --version

# Set toolchain per-project (creates rust-toolchain.toml)
rustup override set nightly
```

### rust-toolchain.toml

Pin a project to a specific toolchain:

```toml
# rust-toolchain.toml (commit this file)
[toolchain]
channel = "stable"          # or "nightly", "1.75.0"
components = ["rustfmt", "clippy"]
targets = ["wasm32-unknown-unknown"]
```

When you `cargo build` in that directory, rustup automatically uses the pinned toolchain.

### Components

Toolchain components are installed separately:

```bash
rustup component add rustfmt      # Code formatter
rustup component add clippy       # Linter
rustup component add rust-analyzer # LSP server (for editors)
rustup component add rust-src     # Standard library source (for IDEs)
rustup component add llvm-tools   # LLVM utilities

rustup component list             # See installed/available
```

---

## How Rust Compiles

Understanding the pipeline helps interpret error messages and compiler flags.

```
Source (.rs)
    ↓  rustc parses + type checks
HIR (High-level Intermediate Representation)
    ↓  borrow checking, trait resolution
MIR (Mid-level Intermediate Representation)
    ↓  optimizations, borrow check again
LLVM IR
    ↓  LLVM optimizes + generates machine code
Object files (.o)
    ↓  linker
Binary / .rlib
```

### rustc directly

Cargo calls `rustc` for you, but you can invoke it directly:

```bash
rustc main.rs                   # Compile single file
rustc main.rs -o my_binary      # Custom output name
rustc main.rs --edition 2021    # Specify edition
rustc --version                 # Compiler version
rustc --print target-list       # All supported targets
```

### What cargo build does

```bash
cargo build           # Debug: target/debug/
cargo build --release # Release: target/release/

# Debug build flags (fast compile, slow binary)
#   opt-level = 0
#   debug symbols included
#   overflow checks enabled

# Release build flags (slow compile, fast binary)
#   opt-level = 3
#   no debug symbols by default
#   LTO possible
```

### Incremental compilation

Rust compiles crate-by-crate. Dependencies are compiled once and cached. `cargo check` skips codegen entirely — use it for fast feedback during development.

```bash
cargo check           # Type check only — fastest
cargo build           # Full build
cargo build --release # Full optimized build
```

---

## Targets — Cross Compilation

A "target" is the machine you're compiling *for* (not necessarily the machine you're compiling *on*).

```bash
# See your default target
rustc -vV | grep host

# List all available targets
rustup target list

# Install a target
rustup target add aarch64-apple-darwin      # macOS ARM
rustup target add x86_64-unknown-linux-musl # Linux static binary
rustup target add wasm32-unknown-unknown    # WebAssembly

# Build for a specific target
cargo build --target x86_64-unknown-linux-musl
```

### Target triple format

```
<arch>-<vendor>-<os>-<env>

x86_64-unknown-linux-gnu    # 64-bit Linux (glibc)
x86_64-unknown-linux-musl   # 64-bit Linux (musl, fully static)
aarch64-apple-darwin         # Apple Silicon macOS
x86_64-apple-darwin          # Intel macOS
x86_64-pc-windows-msvc       # Windows (MSVC)
wasm32-unknown-unknown       # WebAssembly (no OS)
thumbv7em-none-eabihf        # Embedded ARM (no OS)
```

### Cross-compilation setup

For targets other than your host you usually need a linker for that platform:

```toml
# .cargo/config.toml
[target.x86_64-unknown-linux-musl]
linker = "x86_64-linux-musl-gcc"

[target.aarch64-unknown-linux-gnu]
linker = "aarch64-linux-gnu-gcc"
```

`cross` is a tool that handles this automatically via Docker:

```bash
cargo install cross
cross build --target aarch64-unknown-linux-gnu
```

---

## Project Structure

### Standard layout

```
my_project/
├── Cargo.toml          # Package manifest
├── Cargo.lock          # Locked dependency versions (commit for binaries)
├── rust-toolchain.toml # Pin toolchain version (optional)
├── .cargo/
│   └── config.toml     # Project-local cargo config
├── src/
│   ├── main.rs         # Binary entry point
│   ├── lib.rs          # Library entry point
│   └── bin/
│       ├── server.rs   # Additional binary: `cargo run --bin server`
│       └── client.rs
├── tests/              # Integration tests (each file = separate crate)
│   └── integration.rs
├── benches/            # Benchmarks
│   └── bench.rs
├── examples/           # Runnable examples: `cargo run --example demo`
│   └── demo.rs
└── target/             # Build output (gitignore this)
```

### .cargo/config.toml

Project-level cargo settings — affects all cargo commands in that directory:

```toml
# .cargo/config.toml
[build]
target = "x86_64-unknown-linux-musl"  # Default target

[alias]
b = "build"
t = "test"
r = "run"
rr = "run --release"

[env]
RUST_LOG = "debug"

[target.x86_64-unknown-linux-musl]
linker = "x86_64-linux-musl-gcc"

[net]
offline = true  # Don't hit the network (useful in CI)
```

---

## Core Tools

### rustfmt — Formatter

```bash
cargo fmt             # Format entire project
cargo fmt -- --check  # Check without modifying (CI)
rustfmt src/main.rs   # Format single file
```

Configure in `rustfmt.toml`:

```toml
edition = "2021"
max_width = 100
tab_spaces = 4
```

### clippy — Linter

```bash
cargo clippy                    # Run lints
cargo clippy -- -D warnings     # Treat warnings as errors (CI)
cargo clippy --fix              # Auto-fix where possible
```

Suppress a specific lint inline:

```rust
#[allow(clippy::needless_pass_by_value)]
fn my_fn(s: String) { }
```

### rust-analyzer — LSP

The language server for editor integration (VS Code, Neovim, etc.). Provides autocomplete, go-to-definition, inline errors, and refactoring.

```bash
rustup component add rust-analyzer
```

Configure in `.vscode/settings.json` or equivalent editor config.

### cargo audit — Security

```bash
cargo install cargo-audit
cargo audit              # Check dependencies for known vulnerabilities
```

### cargo expand — Macro Debugging

```bash
cargo install cargo-expand
cargo expand             # Show expanded macros
cargo expand my_module   # Expand specific module
```

### cargo flamegraph — Profiling

```bash
cargo install flamegraph
cargo flamegraph         # Profile and generate SVG flamegraph
```

---

## Editions

Rust releases new *editions* that allow backward-incompatible syntax changes. Old code still compiles — editions are per-crate in `Cargo.toml`.

| Edition | Key changes |
|---------|-------------|
| 2015 | Original |
| 2018 | `use` path changes, `async`/`await`, NLL borrow checker |
| 2021 | Closure capture improvements, `IntoIterator` for arrays, `or_patterns` |

```toml
[package]
edition = "2021"   # Always use this for new projects
```

Migrate an old project:

```bash
cargo fix --edition    # Auto-migrate to next edition
```

---

## Environment Variables

Useful env vars when running/building:

```bash
# Show full backtrace on panic
RUST_BACKTRACE=1 cargo run
RUST_BACKTRACE=full cargo run    # Include std library frames

# Logging level (with the `log` crate)
RUST_LOG=debug cargo run
RUST_LOG=my_crate=trace cargo run

# Compiler flags
RUSTFLAGS="-C target-cpu=native" cargo build --release
RUSTFLAGS="-D warnings" cargo build   # Warnings as errors

# Disable incremental compilation (useful for profiling)
CARGO_INCREMENTAL=0 cargo build
```

---

## Common Workflows

### Starting a new project

```bash
rustup update                       # Make sure you're current
cargo new my_project && cd my_project
cargo add serde --features derive   # Add a dependency
cargo run                           # First run
```

### Before committing

```bash
cargo fmt                           # Format
cargo clippy -- -D warnings         # Lint
cargo test                          # Test
cargo build --release               # Verify release builds
```

### Debugging a panic

```bash
RUST_BACKTRACE=1 cargo run          # See where it panicked
RUST_BACKTRACE=full cargo run       # Full stack trace
```

### Checking compile times

```bash
cargo build --timings               # Opens HTML report of per-crate build times
```

---

## See Also

- [[Cargo]] — Dependency management, Cargo.toml, workspaces
- [[Modules]] — Code organization within a project
- [[Testing]] — Writing and running tests
- [[Rust]]
