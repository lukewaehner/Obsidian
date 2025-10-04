- No elements appear twice, each is unique
- Not ordered like an array, no indicies access

```swift
// Create an empty set of strings
var colors = Set<String>()

// adding elements
colors.insert("black")

print(colors) // ["black]
// add some more (one duplicate)
colors.insert("blue")
colors.insert("black")

print(colors) // ["blue", "black"]

let colors = Set(["blue", "black", "red"])
```

---