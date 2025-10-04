
---
[[Sorting Arrays]]

```swift
// create an empty array
var carMakes = [String]()

// creates an array with predefined values
var carMakesSecond = ["Toyota", "Honda"]

// append to array
carMakes.append("Mazda")
carMakes.append("Toyota")
carMakes.append("Honda")

print("Appended: \(carMakes)") // Appended: ["Mazda", "Toyota", "Honda"]

print(carMakes.count) // returns 3

```


### Accessing elements

```swift
print(carMakes[0]) // Mazda
```

### Removing elements

```swift
carMakes.remove(at: 1)
// Mazda, Honda
```

---