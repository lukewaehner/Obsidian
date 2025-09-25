#unique-syntax

```swift
let range = 1...10

for number in range {
	print(number)
	// 1, 2, ... 10
}

var carMakesSecond = ["Toyota", "Honda", "Mazda", "Chevy"]

for item in carMakesSecond{
    print(item)
    // "Toyota", "Honda", "Mazda", "Chevy"
}
```

> Range setting as a variable is unnecessary technically

```swift
for _ in range 1...10 {
	print("Execute") // note, you can't access _
}
```

### With collections:
Let's use the following Dictionary:


```swift
let dictCars: [String: Int] = ["Toyota": 10, "Honda": 20, "Ford": 30]
```


```swift
print("We got:")
for (model, count) in dictCars {
    print("\(count) \(model)s")
}
print ("in our dealership.\n")
```

**Output:**

```
We got:
20 Hondas
30 Fords
10 Toyotas
in our dealership.
```

```swift
print("We got:")
//Omitting values from a dictionary...
for (model, _) in dictCars {
    print("\(model)s")
}
print ("in our dealership.\n")
```

**Output:**

```
We got:
Hondas
Fords
Toyotas
in our dealership.
```

```swift
//MARK: Omitting keys...
var total = 0
for (_, count) in dictCars {
    total += count
}
print ("We got \(total) cars in our dealership.\n")
```

**Output:**

```
We got 60 cars in our dealership.
```

---