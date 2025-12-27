---
tags:
  - rust
  - crates
  - ecosystem
type: note
related:
  - '[[Rust]]'
  - '[[Cargo]]'
  - '[[Async Await]]'
  - '[[Error Handling Patterns]]'
---
# Common Crates

Essential libraries in the Rust ecosystem.

## Overview

The Rust ecosystem has mature crates for most common tasks. This note covers the most popular and useful ones.

## Serialization

### serde

The standard for serialization/deserialization:

```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct User {
    name: String,
    age: u32,
    #[serde(skip_serializing_if = "Option::is_none")]
    email: Option<String>,
}

// To JSON
let user = User { name: "Alice".into(), age: 30, email: None };
let json = serde_json::to_string(&user)?;
let pretty = serde_json::to_string_pretty(&user)?;

// From JSON
let user: User = serde_json::from_str(&json)?;

// Other formats
// serde_yaml, toml, serde_cbor, bincode, etc.
```

## Async Runtime

### tokio

The most popular async runtime:

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
```

```rust
#[tokio::main]
async fn main() {
    let handle = tokio::spawn(async {
        // Async work
    });
    
    tokio::time::sleep(Duration::from_secs(1)).await;
    
    handle.await.unwrap();
}
```

### async-std

Alternative async runtime with std-like API:

```toml
[dependencies]
async-std = { version = "1", features = ["attributes"] }
```

```rust
#[async_std::main]
async fn main() {
    async_std::task::spawn(async { /* ... */ });
}
```

## HTTP

### reqwest

HTTP client:

```toml
[dependencies]
reqwest = { version = "0.11", features = ["json"] }
```

```rust
// Simple GET
let body = reqwest::get("https://httpbin.org/get")
    .await?
    .text()
    .await?;

// With JSON
let client = reqwest::Client::new();
let res: User = client
    .post("https://api.example.com/users")
    .json(&new_user)
    .send()
    .await?
    .json()
    .await?;
```

### axum

Web framework (from Tokio team):

```toml
[dependencies]
axum = "0.6"
```

```rust
use axum::{routing::get, Router, Json};

async fn hello() -> &'static str {
    "Hello, World!"
}

async fn get_user() -> Json<User> {
    Json(User { name: "Alice".into(), age: 30 })
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(hello))
        .route("/user", get(get_user));
    
    axum::Server::bind(&"0.0.0.0:3000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
```

### actix-web

High-performance web framework:

```rust
use actix_web::{web, App, HttpServer, Responder};

async fn hello() -> impl Responder {
    "Hello, World!"
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().route("/", web::get().to(hello))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
```

## CLI

### clap

Command-line argument parsing:

```toml
[dependencies]
clap = { version = "4", features = ["derive"] }
```

```rust
use clap::Parser;

#[derive(Parser)]
#[command(name = "myapp")]
#[command(about = "Does awesome things")]
struct Cli {
    /// Input file
    #[arg(short, long)]
    input: String,
    
    /// Verbose output
    #[arg(short, long, default_value_t = false)]
    verbose: bool,
    
    /// Number of iterations
    #[arg(short, long, default_value_t = 1)]
    count: u32,
}

fn main() {
    let cli = Cli::parse();
    println!("Input: {}", cli.input);
}
```

## Error Handling

### anyhow

Simple error handling for applications:

```toml
[dependencies]
anyhow = "1.0"
```

```rust
use anyhow::{Context, Result, bail};

fn main() -> Result<()> {
    let config = load_config()
        .context("Failed to load configuration")?;
    
    if !config.valid {
        bail!("Invalid configuration");
    }
    
    Ok(())
}
```

### thiserror

Derive macro for custom errors:

```toml
[dependencies]
thiserror = "1.0"
```

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum DataError {
    #[error("Failed to read: {0}")]
    Io(#[from] std::io::Error),
    
    #[error("Invalid data at line {line}")]
    Parse { line: usize },
}
```

## Logging

### tracing

Structured logging and diagnostics:

```toml
[dependencies]
tracing = "0.1"
tracing-subscriber = "0.3"
```

```rust
use tracing::{info, warn, error, instrument, Level};

#[instrument]
fn process(data: &str) {
    info!("Processing data");
    warn!(length = data.len(), "Large input");
}

fn main() {
    tracing_subscriber::fmt()
        .with_max_level(Level::DEBUG)
        .init();
    
    process("hello");
}
```

### log + env_logger

Simple logging:

```toml
[dependencies]
log = "0.4"
env_logger = "0.10"
```

```rust
use log::{info, warn, error};

fn main() {
    env_logger::init();  // RUST_LOG=debug
    info!("Starting up");
}
```

## Database

### sqlx

Async SQL with compile-time checking:

```toml
[dependencies]
sqlx = { version = "0.7", features = ["runtime-tokio", "postgres"] }
```

```rust
use sqlx::postgres::PgPool;

#[derive(sqlx::FromRow)]
struct User {
    id: i32,
    name: String,
}

async fn get_users(pool: &PgPool) -> Result<Vec<User>, sqlx::Error> {
    sqlx::query_as!(User, "SELECT id, name FROM users")
        .fetch_all(pool)
        .await
}
```

### diesel

Type-safe ORM:

```rust
use diesel::prelude::*;

#[derive(Queryable)]
struct User {
    id: i32,
    name: String,
}

fn get_users(conn: &mut PgConnection) -> Vec<User> {
    users::table.load(conn).expect("Error loading users")
}
```

## Utilities

### regex

Regular expressions:

```rust
use regex::Regex;

let re = Regex::new(r"(\d{4})-(\d{2})-(\d{2})").unwrap();
let text = "2024-01-15";

if let Some(caps) = re.captures(text) {
    let year = &caps[1];
    let month = &caps[2];
    let day = &caps[3];
}
```

### chrono

Date and time:

```rust
use chrono::{DateTime, Utc, Local, Duration};

let now: DateTime<Utc> = Utc::now();
let local: DateTime<Local> = Local::now();

let tomorrow = now + Duration::days(1);
let formatted = now.format("%Y-%m-%d %H:%M:%S");
```

### rand

Random number generation:

```rust
use rand::Rng;

let mut rng = rand::thread_rng();
let n: u32 = rng.gen();
let range: i32 = rng.gen_range(1..=100);
let coin: bool = rng.gen();
```

### rayon

Parallel iteration:

```rust
use rayon::prelude::*;

let sum: i32 = (0..1000)
    .into_par_iter()
    .map(|x| x * 2)
    .sum();

let results: Vec<_> = data
    .par_iter()
    .filter(|x| x.is_valid())
    .collect();
```

### once_cell / lazy_static

Lazy initialization:

```rust
use once_cell::sync::Lazy;

static CONFIG: Lazy<Config> = Lazy::new(|| {
    load_config().expect("Failed to load config")
});

fn main() {
    println!("{:?}", *CONFIG);
}
```

## Summary Table

| Category | Crate | Purpose |
|----------|-------|---------|
| Serialization | `serde` | Serialize/deserialize data |
| Async | `tokio` | Async runtime |
| HTTP Client | `reqwest` | HTTP requests |
| Web Framework | `axum`, `actix-web` | Web servers |
| CLI | `clap` | Argument parsing |
| Errors | `anyhow`, `thiserror` | Error handling |
| Logging | `tracing`, `log` | Logging |
| Database | `sqlx`, `diesel` | Database access |
| Regex | `regex` | Pattern matching |
| Time | `chrono` | Date/time |
| Random | `rand` | Random numbers |
| Parallel | `rayon` | Parallel iteration |

## See Also

- [[Cargo]] — Dependency management
- [[Async Await]] — Async programming
- [[Error Handling Patterns]] — Error crates in depth
- [[Rust]]
