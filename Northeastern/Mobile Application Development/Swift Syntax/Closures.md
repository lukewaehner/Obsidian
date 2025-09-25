#unique-syntax 
- These are anonymous functions in a nutshell

```swift
let printHello = {
	print("Hello")
}

printHello()
```

---
## With parameters

```swift
let sayHelloTo = { (name:String) in
    print("Hello \(name)!")
}

//calling closure with parameter...
sayHelloTo("Donald")
```

---
## Returning values

```swift
let sumOfArray = {(array:[Int]) -> Int in
    var sum = 0
    for item in array{
        sum += item
    }
    
    //returns the value...
    return sum
}

//calling the closure with an integer array
let sum = sumOfArray([1,2,3,4,5])
print(sum)
```

---
## Closures as parameters
Why write closures when they can just be functions?
Well, we can define them to be function parameters

```swift
let drive = {
    print("I am driving!")
}

let fly = {
    print("I am taking a flight!")
}
```

```swift
//taking a closure as the parameter 'how'
func travel(from source:String, to destination:String, how: ()->Void){
    
    print("I need to travel from \(source) to \(destination).")
    how()
}
```

In the function travel, we are taking in a closure as `how`, so we can use the drive or fly closures to specify type of travel

So in calling we can say
```swift
travel("LA", "BOS", fly)
// I am travelling from LA to BOS.
// I am taking a flight
```

---
### Closures accepting parameters and returning values
```swift
//defining three closures to add, subtract, and multiply two numbers
let add = {(num1:Int, num2:Int) -> Int in
    return num1+num2
}

let subtract = {(num1:Int, num2:Int) -> Int in
    return num1-num2
}

let multiply = {(num1:Int, num2:Int) -> Int in
    return num1*num2
}
```

Lets write a calculate function
```swift
// calculate function...
func calculate(operation: (_:Int, _:Int)-> Int, num1:Int, num2:Int) -> Int{
    
    let result = operation(num1, num2)
    
    return result
}
```

We should close out the two accepted ints in the closure, using `(_:Int, _:Int)` because it doesn't matter for the closure itself, which exists inside

We then call it using:
```swift
//calling function to multiply...
print(calculate(operation: multiply, num1: 2, num2: 23))
```
