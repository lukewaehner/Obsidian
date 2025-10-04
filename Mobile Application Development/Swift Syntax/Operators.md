
---

## Arithmetic Operators

```swift
let num1 = 5
let num2 = 33

//Addition...
let sum = num1 + num2

//Subtraction...
let difference = num2 - num1

//Multiplication...
let product = num1 * num2

//Division (and remainder)...
let divided = num2 / num1
let remainder = num2 % num1

print(
    """
    Results:
    Sum = \(sum)
    Difference = \(difference)
    Product = \(product)
    Division result = \(divided)
    Division remainder = \(remainder)
    """
)

/*
Results:
Sum = 38
Difference = 28
Product = 165
Division result = 6
Division remainder = 3
*/
```

### Caveats

```swift
let myInt:Int = 20
let myDouble:Double = 30.5

let sum:Int = myInt + myDouble
// ERROR: cannot convert value of type 'Double' to expected argument type int
```

---

## Operator overloading
- Operators like `+` has different ways of operating on different data types

```swift
let firstName = "Luke"
let lastName = "Waehner"
let fullName = firstName + " " + lastName
print(fullName)

let listNumOne = [1,2,3]
let listNumTwo = [4,5,6]
let listNum = listNumOne + listNumTwo
print(listNum)
```

```
Luke Waehner
[1, 2, 3, 4, 5, 6]
```

```swift
let listOne = [1,2,3]
let listTwo = ["four", "five"]
let listOneTwo = listOne + listTwo
// Doesn't work, two different data types
```

Shortcuts

```swift
var budget = 30_000
let expense = 5_000
budget -= expense

// Others:
//Increment...
var count = 0
count += 1 
// count = 1

//Multiply...
var number = 5
number *= 4 
// number = 20

//Divide...
var number2 = 10
number2 /= 2 
// number2 = 5

//String operations (concatenation)...
var name = "Mark"
var surname = "Webber"
name += surname 
// name = "MarkWebber"
```


---

## Comparison Operators & Booleans

## Comparison Operators

| Operator | Description              |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | not equal to             |
| <        | less than                |
| >        | greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

## Booleans

```swift
var myBool: Bool = false
var yourBool = true
```

```swift
// Comparison operators and Booleans...
let a = 10
let b = 12

let isEqual = a == b

print(isEqual)
print(type(of: isEqual))

/*
false
Bool
*/
```

---