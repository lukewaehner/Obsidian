
```swift
// Creates a varoable, one that is mutable
var greeting = "Hello, world"
greeting = "changed"

let noChanging = "constant"
noChanging = "other" // MARK: ERROR HERE!
```

---

## Type safety

Swift is type-safe, once you create a variable, the data type is stuck. Every variable needs a type

```swift
var greeting = "test"
test = 12 // error
```

```swift
var count = 12 // this is created as integer type

var million = 1_000_000 // we can use underscores as thousands delimiters

```


## Type annotations
#unique-syntax

```swift
let myName:string = "Luke"
var myAge:Int = 22
```
---

## Strings

```swift
var multiline = """
Line
Line
Line
"""
// This will logically multiline, so each 'Line' is printed on a newline
```

the command `print()` will print out strings, variables, whatever

---

## Floating point numbers

Double is short for double-precision floating point number. It is 64-but. It holds fractions. 
Float itself is a 32-bit floating point number, less precise than Double, and not need to use unless games or graphic applications are involved

```swift
var myNum = 12.5
print(myNum)
print(type(of: myNum)) // Double
```

Swift uses doubles by default, but if need to assign a float you cast it

```swift
var myFloat:Float = 13
print(type(of: myFloat))
```

---

## String Interpolation

```swift
var myString =
	"My Double number is \(myNum). My float number is \(myFloat)"
print(myString)
```


---

## Comments

```swift
// Single line comment

/*
Multi-line comment
Can keep going
and going
*/
```

---