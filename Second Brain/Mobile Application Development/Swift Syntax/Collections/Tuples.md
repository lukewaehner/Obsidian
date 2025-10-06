#unique-syntax 
- Collection of different elements of different data tpes stored in the same place

```swift
var basicTuple = ("Mark", 20)

var customTuple = (name: "Luke", age: 22)

print("\(basicTuple), \(customTuple)")
// basicTuple: ("Mark", 20), customTuple: (name: "Luke", age: 22)
```


### Accessing values

```swift
print(customTuple.0) // Luke
print(customTuple.age) // 22

customTuple.age = 23 // birthday!
print(customTuple.1) // 23. Note updated value, and different accessor
```

---