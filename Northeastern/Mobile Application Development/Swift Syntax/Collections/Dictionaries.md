- KVP

```swift
var carCounts = [String: Int]()

var carCounts = [
    "Toyota": 2,
    "Mazda": 1,
    "Honda":10
]

print(carCounts)
// ["Toyota": 2, "Mazda": 1, "Honda": 10]
```

### Adding / Updating

```swift
carCounts.updateValue(5, forKey: "Chevy")
// adds Chevy because it didn't exist

// also can use
carCounts["Chevy"] = 5

// sell a Honda
carCounts.updateValue(9, forKey: "Honda")
print(carCounts)
// ["Honda": 9, "Chevy": 5, "Mazda": 1, "Toyota": 2]
```

### Access

```swift
let mazdaCount = carCounts["madza"]
```

---