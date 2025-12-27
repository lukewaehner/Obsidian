---
tags:
  - rust
  - async
  - concurrency
type: note
related:
  - '[[Rust]]'
  - '[[Concurrency]]'
  - '[[Error Handling Patterns]]'
  - '[[Closures]]'
---
# Async Await

Asynchronous programming with futures in Rust.

## Overview

Async/await allows writing non-blocking code that looks synchronous. Futures are lazy—they don't execute until polled by an async runtime like Tokio or async-std.

## Basic Usage

### Async Functions

```rust
async fn fetch_data() -> String {
    // Async operation
    "data".to_string()
}

async fn process() {
    let data = fetch_data().await;  // Wait for completion
    println!("{}", data);
}
```

### Running Async Code

```rust
// With Tokio runtime
#[tokio::main]
async fn main() {
    let result = fetch_data().await;
    println!("{}", result);
}

// Or manually
fn main() {
    let rt = tokio::runtime::Runtime::new().unwrap();
    rt.block_on(async {
        let result = fetch_data().await;
        println!("{}", result);
    });
}
```

### Async Blocks

```rust
async fn example() {
    let future = async {
        // Async code here
        42
    };
    
    let result = future.await;
}
```

## Key Concepts

### Futures Are Lazy

```rust
async fn expensive() -> i32 {
    println!("Computing...");
    42
}

async fn main() {
    let future = expensive();  // Nothing printed yet!
    println!("Future created");
    let result = future.await;  // "Computing..." printed now
}
```

### Concurrent Execution

```rust
use tokio::join;

async fn task1() -> i32 { /* ... */ 1 }
async fn task2() -> i32 { /* ... */ 2 }

async fn run_both() {
    // Run concurrently, wait for both
    let (r1, r2) = join!(task1(), task2());
    
    // Or with try_join for Results
    let (r1, r2) = tokio::try_join!(task1(), task2())?;
}
```

### Select - First to Complete

```rust
use tokio::select;

async fn race() {
    select! {
        val = task1() => println!("Task 1 won: {}", val),
        val = task2() => println!("Task 2 won: {}", val),
    }
}
```

### Spawning Tasks

```rust
use tokio::spawn;

async fn main() {
    // Spawn independent task
    let handle = spawn(async {
        // Runs concurrently
        expensive_computation().await
    });
    
    // Do other work
    other_work().await;
    
    // Get result
    let result = handle.await.unwrap();
}
```

## Common Patterns

### HTTP Requests with reqwest

```rust
use reqwest;

async fn fetch_url(url: &str) -> Result<String, reqwest::Error> {
    let response = reqwest::get(url).await?;
    let body = response.text().await?;
    Ok(body)
}

#[tokio::main]
async fn main() -> Result<(), reqwest::Error> {
    let body = fetch_url("https://httpbin.org/get").await?;
    println!("{}", body);
    Ok(())
}
```

### Parallel Requests

```rust
use futures::future::join_all;

async fn fetch_all(urls: Vec<&str>) -> Vec<String> {
    let futures: Vec<_> = urls
        .iter()
        .map(|url| fetch_url(url))
        .collect();
    
    let results = join_all(futures).await;
    results.into_iter().filter_map(|r| r.ok()).collect()
}
```

### Timeouts

```rust
use tokio::time::{timeout, Duration};

async fn with_timeout() -> Result<String, &'static str> {
    match timeout(Duration::from_secs(5), slow_operation()).await {
        Ok(result) => Ok(result),
        Err(_) => Err("Operation timed out"),
    }
}
```

### Async Streams

```rust
use tokio_stream::StreamExt;

async fn process_stream() {
    let mut stream = tokio_stream::iter(vec![1, 2, 3]);
    
    while let Some(value) = stream.next().await {
        println!("{}", value);
    }
}
```

### Async Mutex

```rust
use tokio::sync::Mutex;
use std::sync::Arc;

async fn shared_state() {
    let data = Arc::new(Mutex::new(0));
    
    let data_clone = Arc::clone(&data);
    tokio::spawn(async move {
        let mut lock = data_clone.lock().await;
        *lock += 1;
    });
}
```

### Channels in Async

```rust
use tokio::sync::mpsc;

async fn channel_example() {
    let (tx, mut rx) = mpsc::channel(100);
    
    tokio::spawn(async move {
        tx.send("hello").await.unwrap();
        tx.send("world").await.unwrap();
    });
    
    while let Some(message) = rx.recv().await {
        println!("{}", message);
    }
}
```

### Async Traits

```rust
// Requires async-trait crate
use async_trait::async_trait;

#[async_trait]
trait Fetcher {
    async fn fetch(&self, url: &str) -> String;
}

struct HttpFetcher;

#[async_trait]
impl Fetcher for HttpFetcher {
    async fn fetch(&self, url: &str) -> String {
        // Implementation
        String::new()
    }
}
```

## Runtime Configuration

### Tokio Multi-threaded

```rust
#[tokio::main]
async fn main() {
    // Default: multi-threaded runtime
}

// Or explicit
#[tokio::main(flavor = "multi_thread", worker_threads = 4)]
async fn main() { }
```

### Tokio Single-threaded

```rust
#[tokio::main(flavor = "current_thread")]
async fn main() {
    // Single-threaded runtime
}
```

## Error Handling

```rust
async fn fallible() -> Result<String, MyError> {
    let data = fetch().await?;
    let processed = process(data).await?;
    Ok(processed)
}

async fn with_recovery() {
    match fallible().await {
        Ok(data) => println!("Success: {}", data),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

## Tips

- Futures do nothing until `.await`ed or spawned
- Use `join!` for concurrent execution of known futures
- Use `spawn` for independent background tasks
- Async functions return `impl Future<Output = T>`
- Use `tokio::sync::Mutex` instead of `std::sync::Mutex` in async
- Avoid blocking operations in async code—use `spawn_blocking`
- Consider `select!` for racing futures or handling cancellation
- Use `#[tokio::test]` for async test functions

## See Also

- [[Concurrency]] — Thread-based concurrency
- [[Error Handling Patterns]] — Async error handling
- [[Closures]] — Async blocks are closures
- [[Rust]]
