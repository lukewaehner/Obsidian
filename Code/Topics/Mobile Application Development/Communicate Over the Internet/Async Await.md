Writing clean code for asynchronous operations in Swift to avoid callback hell and spaghetti code.

---

## The Problem with Nested Callbacks

Previously, we handled sequential API calls by nesting them in callbacks:

```swift
// Pseudocode - NOT recommended approach
func addANewContact(contact: Contact) {
    callAddContactAPI() { response in // Async callback
        if response.statusCode == 200 {
            // A ton of other code....
            callGetAllContactsAPI() // Next API call
            // A ton of remaining code....
        }
    }
}
```

**Problems:**
- Creates spaghetti code
- Hard to read and maintain
- Not reusable
- Gets exponentially worse with 3+ sequential calls

---

## The Solution: Async/Await

With async/await, we can write sequential async calls that look synchronous:

```swift
// Pseudocode - Much cleaner!
func addANewContact(contact: Contact) {
    await callAddContactAPI() // Stop and wait until call finishes
    await callGetAllContactsAPI() // When done, will have updated list
}
```

**Benefits:**
- More readable
- Highly reusable
- Sequential flow without nesting
- Cleaner error handling

---

## How Async/Await Works

### Basic Example

```swift
import Foundation

// 1. Define an async function
func delayedGreeting() async -> String {
    try? await Task.sleep(nanoseconds: 5_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchronous world, I waited 5 seconds to print this!"
}

// 2. Call it from a Task block
func start() {
    Task { // Creates an asynchronous context
        print("Starting an asynchronous task...")
        let greeting = await delayedGreeting() // Await the result
        print(greeting)
    }
    print("Hello from synchronous world, I don't wait for the asyncs!")
}

start()
```

**Output:**
```
Hello from synchronous world, I don't wait for the asyncs!
Starting an asynchronous task...
Hello from the asynchronous world, I waited 5 seconds to print this!
```

The synchronous print happens immediately, while the Task block runs asynchronously in the background.

---

## Sequencing Multiple Async Calls

Within a `Task{...}` block, all async calls are sequenced one after another:

```swift
func delayedGreeting5() async -> String {
    try? await Task.sleep(nanoseconds: 5_000_000_000) // 5 seconds
    return "Hello from the asynchronous world, I waited 5 seconds to print this!"
}

func delayedGreeting3() async -> String {
    try? await Task.sleep(nanoseconds: 3_000_000_000) // 3 seconds
    return "Hello from the asynchronous world, I waited 3 seconds to print this!"
}

func start() {
    Task {
        print("Starting an asynchronous task...")
        
        let greeting5 = await delayedGreeting5() // Wait 5 seconds
        print(greeting5)
        
        let greeting3 = await delayedGreeting3() // Then wait 3 more seconds
        print(greeting3)
    }
}

start()
```

**Output:**
```
Starting an asynchronous task...
Hello from the asynchronous world, I waited 5 seconds to print this!
Hello from the asynchronous world, I waited 3 seconds to print this!
```

Total execution time: 8 seconds (5 + 3 sequentially)

---

## Important Rules

1. **Defining async functions:** Use `async` keyword in declaration
   ```swift
   func myAsyncFunction() async -> String { ... }
   ```

2. **Calling async functions:** Use `await` keyword when calling
   ```swift
   let result = await myAsyncFunction()
   ```

3. **Context requirement:** `await` can only be called from:
   - Inside another `async` function
   - Inside a `Task{}` block

4. **Task blocks:** Create asynchronous execution contexts
   ```swift
   Task {
       // async/await code goes here
   }
   ```

---

## Applying to API Calls

This pattern makes API code much cleaner:

```swift
func addContactAndRefresh(contact: Contact) {
    Task {
        do {
            // Sequential API calls - clean and readable
            try await addContactAPI(contact)
            let contacts = try await getAllContactsAPI()
            
            // Update UI on main thread
            await MainActor.run {
                self.updateUI(with: contacts)
            }
        } catch {
            print("Error: \(error)")
        }
    }
}
```

---

## Related Topics

- [[HTTP]] - Understanding HTTP requests and responses
- Error handling with async/await
- MainActor for UI updates
- Structured concurrency patterns