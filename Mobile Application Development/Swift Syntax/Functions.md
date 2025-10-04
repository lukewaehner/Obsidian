
```swift
func functionName(parameter1:DataType, parameter2:DataType, ...) -> ReturnDataType{
    //code block
}
```


```swift
func helloWorld() {
	print("Hello World")
}

helloWorld() // Hello World
```

## Parameters

```swift
//function definition...
func printDetails(name:String, age:Int){
    print(
        """
        The user's name is: \(name).
        The user's age is: \(age).
        \(name) is awesome!
        """
    )
}


//calling the function...
printDetails(name: "Donald", age: 25)
```

## Return Types

```swift
func sumOf(array:[Int]) -> Int{
    var sum = 0
    for item in array{
        sum += item
    }
    
    //returns the value...
    return sum
}

//calling the function with an integer array
print(sumOf(array: [1,2,3,4,5])) // returns 15
```

## Parameter Labels
#unique-syntax 
- Swift can separate internal and external parameters

```swift
//function definition...
func navigate(with vehicle:String, from source:String, to destination:String) -> String{
    return "The user will use a \(vehicle) to travel from \(source) to \(destination)."
}

//calling the function
print(navigate(with: "car", from: "Boston", to: "NYC"))
```

But they can also be **omitted**

```swift
//function definition...
func printHello(_ name:String){
    print("Hello \(name)!")
}

//Calling the function...
printHello("Sakib")
```

And they can be **defaulted**

```swift
//function definition
func printHello2(_ name:String = "Unknown"){
    print("Hello \(name)!")
}
//calling function...
printHello2() // Hello Unknown!
```

Why use?
1. I**mproved Clarity in Function Calls:**
    
    When a function has descriptive external parameter names, it becomes clear what each argument represents when calling it. This helps understand each argument's purpose and makes the function call more readable.
    
2. **Self-Documenting Code:**
    
    By providing meaningful external names, you can make your code self-documenting. This means that someone reading your code can understand the purpose and intent of the function just by looking at the function signature and the way it's called.
    
3. **Avoiding Ambiguity:** In some cases, functions may have parameters with similar data types. Using external names allows you to disambiguate these parameters, making the function call unambiguous and reducing the risk of passing incorrect arguments.
    
4. **Improved Readability and Maintenance:**
    
    By using external names, you can create functions with expressive, almost sentence-like function calls, which can be beneficial when reading and maintaining code.

---