#unique-syntax 

```swift
var myInt:Int
print(myInt) // ERROR: undefined
```

Instead we can do

```swift
var myInt:Int?
print(myInt) // nil
```

 It prints out nil, similar to null.

We can assign a value, but it's still wrapped in an optional

```swift
var myInt:Int?
//assigning a value...
myInt = 10
print(myInt) //prints Optional(10)
```

---
### If-Let
This lets us unwrap optionals

```swift
var myInt:Int?
//assigning a value...
myInt = 10

//optional binding with if-let...
if let unwrappedMyInt = myInt{
    //value present
    print(unwrappedMyInt)
} else {
    // handling nil
    print("Optional value myInt must be initialized!")
}
```

---
### Forceful Unwrapping
Forces the unwrapping of an optional, but it can unwrap nil which is dangerous

```swift
//forced unwrapping...
print(myInt!)
// prints 10
```
