
---

## If statements

```swift
let num = 5
if num == 5 {
	print("True")
}
```

---

## If-else

```swift
if myNum == 5 {
	print("It is 5)
} else if myNum == 3{
	print("It is 3")
} else {
	print("False")
}
```

---

## Switch Statements

```swift
//switch statements...
let day = 5
switch day {
case 1:
    print("Sunday")
case 2:
    print("Monday")
case 3:
    print("Tuesday")
case 4:
    print("Wednesday")
case 5:
    print("Thursday")
case 6:
    print("Friday")
case 7:
    print("Saturday")
default:
    print("Invalid day")
}
```

---

## Combining Operators

```swift
let myAge = 24

if myAge >= 18 && myAge <= 65 {
    print("Eligible for the user study!")
}

if myAge < 18 || myAge > 65 {
    print("Not eligible!")
}
```

---

## Range Operators
#unique-syntax

```swift
let today = 8

switch today{
    case 1...5:
        print("Weekday!")
    case 6..<8:
        print("Weekend!")
    default:
        print("Invalid day!")
}
```

---