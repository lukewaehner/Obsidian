
---

## Start a Playground.
- Open Xcode
- File -> New -> Playground. Select Blank

---

# Variables, Data types, and more

---

## Variables

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

# Collections

---

## Arrays

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

## Sets
- No elements appear twice, each is unique
- Not ordered like an array, no indicies access

```swift
// Create an empty set of strings
var colors = Set<String>()

// adding elements
colors.insert("black")

print(colors) // ["black]
// add some more (one duplicate)
colors.insert("blue")
colors.insert("black")

print(colors) // ["blue", "black"]

let colors = Set(["blue", "black", "red"])
```

---

## Tuples
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

## Dictionaries
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

# Operators

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

# Conditionals

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

# Loops

---

## For Loops
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

## While Loops

```swift
while target <= condition {
	print("Execute")
}
```

---

## Repeat Loops
#unique-syntax 

```swift
var myNum = 1

repeat{
    //code block
    print(myNum)
    myNum += 1
} while myNum <= 50

```

---

## Break Loops
```swift
let breakPoint = 4
var countDown = 1
while breakPoint >= 0 {
    print("I will run!")
    
//  activating break point
    if countDown == breakPoint{
        print("I am tired now!")
        break
    }
    countDown += 1
}
```

## Skipping a loop

```swift
for number in 1...10 {
    //skipping the even numbers
    if number%2 == 0{
        continue
    }
    
    print("This an odd number:\(number)")
}
```

---

# Functions

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

# Closures
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

---
# Optionals
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

---

# Creating DataTypes

---
## Structs
Lets create a simple person struct

```swift
struct Person {
	var name:String
	var age:Int
	var isMale: bool
}
```


In usage:
```swift
var newPerson: Person = Person(name: "Bob Smith", age: 30, city: "Boston")

//print the variable person of type Person...
print(newPerson)
//print newPerson's name...
print(newPerson.name)

//Person(name: "Bob Smith", age: 30, city: "Boston")
//Bob Smith
```

---
### Computed Properties

Not needed to supply a value for these properties
```swift
struct Person{
    var name:String
    var age:Int
    var city:String
    
//    computed property .....
    var isMinor:Bool{
        if age < 18{
            return true
        }else{
            return false
        }
    }
}
```

```swift
if(newPerson.isMinor){
    print("\(newPerson.name) is a minor!")
}else{
    print("\(newPerson.name) is an adult!")
}
// Bob Smith is an adult!
```

---
### Functions inside Structs
They are called methods

```swift
struct Person{
    var name:String
    var age:Int
    var city:String
    
//    computed property .....
    var isMinor:Bool{
        if age < 18{
            return true
        }else{
            return false
        }
    }
//    method printProfile...
    
    func printProfile(){
        print(
            """
            Hi! I am \(name).
            I am \(age) years old.
            And I live in \(city)!
            Happy coding!
            """
        )
    }
}
```

In use:

```swift
//printing the profile intro using the method printProfile...
newPerson.printProfile()
```

We get:
```
Hi! I am Bob Smith.
I am 36 years old.
And I live in Boston!
Happy coding!
```

---
### Initializers
Used to set default data

```swift
struct Person{
    var name:String
    var age:Int
    var city:String
    
//    initializer method...
    init() {
        name = "Unknown"
        age = 18
        city = "Not Given"
    }
    
//    computed property .....
    var isMinor:Bool{
        if age < 18{
            return true
        }else{
            return false
        }
    }
    
//    method printProfile...
    
    func printProfile(){
        print(
            """
            Hi! I am \(name).
            I am \(age) years old.
            And I live in \(city)!
            Happy coding!
            """
        )
    }
}
```


In use:

```swift
//Creating an instance using the init()
var newPerson = Person()

//print the variable person of type Person...
print(newPerson) 

//modifying the properties of newPerson...
newPerson.name = "Bob Smith"
newPerson.age = 36
newPerson.city = "Boston"

//printing newPerson after modifying the properties...
print(newPerson)

//printing the computed property...
if(newPerson.isMinor){
    print("\(newPerson.name) is a minor!")
}else{
    print("\(newPerson.name) is an adult!")
    //prints 
}

//printing the profile intro using the method printProfile...
newPerson.printProfile()
```

```
Person(name: "Unknown", age: 18, city: "Not Given")
Person(name: "Bob Smith", age: 36, city: "Boston")
Bob Smith is an adult!
Hi! I am Bob Smith.
I am 36 years old.
And I live in Boston!
Happy coding!
```

> **You need to write the init method before all other methods!**

---

### Multiple Initializers
```swift
struct Car{
    var make:String
    var model:String
    var year:Int
    
    init(){
        make = "Not set"
        model = "Not set"
        year = 0
    }
}

//creating an instance of Car...
var car = Car()

//printing the instance...
print(car)
```

```swift
struct Car{
    var make:String
    var model:String
    var year:Int
    
    //default init...
    init(){
        make = "Not set"
        model = "Not set"
        year = 0
    }
    //custom init...
    init(make:String, model:String, year:Int) {
        self.make = make
        self.model = model
        self.year = year
    }
}
```

```swift
//creating an instance of Car using the custom init()...
var car2 = Car(make: "Toyota", model: "Corolla", year: 2020)
print(car2)
```


```
Car(make: "Toyota", model: "Corolla", year: 2020)
```

---
### Struct Initialization and Optionals

```swift
init(make:String, model:String){
    self.make = make
    self.model = model
    //year is left uninitialized...
}
```

This gives an error, we can fix it with an optional
```swift
struct Car{
    var make:String
    var model:String
    var year:Int? //Optional
    
    //omitted other codes...
    init(make:String, model:String){
        self.make = make
        self.model = model
    }
}
```

And in use:

```swift
//creating an instance of Car...
var car3 = Car(make: "Honda", model: "Civic")
print(car3)
//prints: Car(make: "Honda", model: "Civic", year: nil)

//Assigning a value of year after we create the instance
car3.year = 2022
print(car3)
//prints: Car(make: "Honda", model: "Civic", year: Optional(2022))
```

---
### Setters

```swift
struct Car{
    var make:String
    var model:String
    var year:Int?
    
    init(){
        make = "Not set"
        model = "Not set"
        year = 0
    }
    
    init(make:String, model:String, year:Int) {
        self.make = make
        self.model = model
        self.year = year
    }
    
    init(make:String, model:String){
        self.make = make
        self.model = model
    }
    
    func updateYear(_ year:Int){
        self.year = year
    }
}
```

But this gives an error, because structs are value type, not reference type.
So we need to give mutability through the `mutating` keyword

```swift
mutating func updateYear(_ year:Int){
    self.year = year
}
```

---

## Classes
Inherently different from structs
```swift
class Vehicle{
    var type:String
}
```

This causes an error, because you **need an initializer** unlike structs

```swift
class Vehicle{
    var type:String
    
    //mandatory init() method
    init(type:String){
        self.type = type
    }
    
}

var car1 = Vehicle(type: "Car")
var car2 = Vehicle(type: "Truck")
var car3 = Vehicle(type: "Minivan")
print(car1.type) //prints: Car
```


---
### Inheritance

```swift
//The Vehicle class....
class Vehicle{
    var type:String
    
    init(type:String){
        self.type = type
    }
    
}
// defining a new class inheriting Vehicle class
class Car:Vehicle{
    var make:String
    var model:String
    
    init(type:String, make:String, model:String) {
        //initializing this instance's properties...
        self.make = make
        self.model = model
        
        //Calling super class's initializer...
        super.init(type: type)
    }
}
```

With `:` we say that Car inherits properties from the Vehicle
Each class still needs its own init method

### Overriding

```swift
class Vehicle{
    var type:String
    
    init(type:String){
        self.type = type
    }
    
    //method describing a Vehicle...
    func describe(){
        print("This is a \(type).")
    }
    
}
// creating an instance of class Vehicle...
var vehicle = Vehicle(type: "Car")

vehicle.describe() // prints: This is a Car.
```

```swift
//creating an instance of Car...
var car = Car(type: "Car", make: "Toyota", model: "Rav4")

car.describe() //prints: This is a Car.
```

In overriding:

```swift
class Car:Vehicle{
    var make:String
    var model:String
    
    init(type:String, make:String, model:String) {
        //initializing this instance's properties...
        self.make = make
        self.model = model
        
        //Calling super class's initializer...
        super.init(type: type)
    }
    
    //overriding super.describe()...
    override func describe() {
        print(
            """
            This is a \(type).
            It is a \(make) \(model).
            """
        )
    }
}

//creating an instance of Car...
var car = Car(type: "Car", make: "Toyota", model: "Rav4")
car.describe()
```

It prints:

```
This is a Car.
It is a Toyota Rav4.
```

---
### Value vs Reference
In copying a struct, you get a copied value, instead of reference.
In example:

```swift
struct User{
    var name:String
}

//creating an instance of User...
var user1 = User(name: "John Smith")

//copying the instance to a new instance...
var user2 = user1

//changing the name in the copied instance...
user2.name = "Bob Smith"

print(
    """
    User name of user1 = \(user1.name)
    User name of user2 = \(user2.name)
    """
)

```

Both are now independent, so `user2.name = "Bob Smith"` does not change `user1`
This is not the same for classes, so the same exact idea, but with a `class User` would have different effects:

```swift
class Person{
    var name:String
    init(name:String){
        self.name = name
    }
}

//creating an instance of Person...
var person1 = Person(name: "John Snow")

//copying the instance to a new instance...
var person2 = person1

//changing the name in the copied instance...
person2.name = "Arya Stark"

print(
    """
    Name of person1 = \(person1.name)
    Name of person2 = \(person2.name)
    """
)
```

It prints

```
Name of person1 = Arya Stark
Name of person2 = Arya Stark
```

---
# Protocols
#unique-syntax 
Similar to interfaces in Java, they are like standards or guides

```swift
protocol SomeProtocol{
    //protocol definition goes here...
}
```

---
```swift
protocol USBMad{
    var id:Int{get}
    var supportsDisplayAdapter:Bool{get}
    var supportsAudio:Bool{get}
    func chargeAccessories()
    func transferData()
}
```

The `{get}` marker signals that the value can be retrieved. Obviously `{set}` exists, and thus `{get set}` is proper as well.

---
### Using a protocol
```swift
struct MyLaptop: USBMad{
    //struct's own properties
    var name:String
    var architecture:String
    
    //adopted/conformed variables and methods
    var id: Int
    var supportsDisplayAdapter: Bool
    var supportsAudio: Bool
    
    //adopted and to be implemented methods
    func chargeAccessories() {
        //MyLaptop's implementation of adopted method
        print("I am able to charge the accessories!")
    }
    func transferData() {
        //MyLaptop's implementation of adopted method
        print("You can send/receive data to/from me!")
    }   
}
```

```swift
let myLaptop = MyLaptop(
    name: "Sakib's Macbook",
    architecture: "ARM64",
    id: 1,
    supportsDisplayAdapter: true,
    supportsAudio: true
)

myLaptop.chargeAccessories()
//prints: I am able to charge the accessories!

myLaptop.transferData()
//prints: You can send/receive data to/from me!
```

You can add more as well, things outside the protocols' guide

```swift
struct MyLaptop: USBMad{
    //struct's own properties
    var name:String
    var architecture:String
    
    //adopted/conformed variables and methods
    var id: Int
    var supportsDisplayAdapter: Bool
    var supportsAudio: Bool
    
    //adopted and to be implemented methods
    func chargeAccessories() {
        //MyLaptop's implementation of adopted method
        print("I am able to charge the accessories!")
    }
    func transferData() {
        //MyLaptop's implementation of adopted method
        print("You can send/receive data to/from me!")
    }
    
    //MyLaptop's own method...
    func describe(){
        print(
            """
            My name is \(name).
            I use \(architecture) architecture.
            I have a USBMad interface with id: \(id).
            """
        )
        self.chargeAccessories()
        self.transferData()
    }
}
```

---
### Combining multiple protocols:
```swift
//protocol for payment...
protocol Payment{
    func biweeklyPayment() -> Double
}

//protocol for TA training...
protocol TATraining{
    func completeTraining()
}

//protocol for TA rating...
protocol RatedByProfessor{
    func rate() -> Int
}
```

Consolidate them all:

```swift
// Some code//consolidating to a single protocol...
protocol TeachingAssistant: Payment, TATraining, RatedByProfessor{
    //properties and methods for TeachingAssistant protocol...
}
```

---
### Inheriting a Superclass and adopting Protocols combined

```swift
//super class Student...
class Student{
    var name: String
    init(name:String) {
        self.name = name
    }
}
```

```swift
//UndergradTA inherits Student, and adopts/conforms TeachingAssistant protocol...

class UndergradTA: Student, TeachingAssistant{
    //own property course...
    var course:String
    
    //initializer for UndergradTA...
    init(name: String, course:String) {
        self.course = course
        super.init(name: name)
    }
    
    //defining adopted methods from TeachingAssistant...
    func biweeklyPayment() -> Double {
        return 1_500.00
    }
    
    func completeTraining() {
        print("\(name) completed the TA training.")
    }
    
    func rate() -> Int {
        return 5
    }
    
    // own describe method of UndergradTA...
    func describe(){
        print(
            """
            \(name) is a TA of \(course) course.
            They were rated \(self.rate())/5 by the professor.
            They are paid \(self.biweeklyPayment()) biweekly.
            """
        )
        self.completeTraining()
    }
}

```

A class only inherits one superclass, but can inherit multiple protocols

```swift
let alice = UndergradTA(
    name: "Alice",
    course: "Mobile App Development"
)

alice.describe()

/*
 alice.describe() prints:
 Alice is a TA of Mobile App Development course.
 They were rated 5/5 by the professor.
 They are paid 1500.0 biweekly.
 Alice completed the TA training.
 */
```

---

# Sorting Arrays

---
### Increasing Order
```swift
var arrayOfInt:[Int] = [1,56,89,23,4,6]

print(arrayOfInt.sorted())

// prints: [1, 4, 6, 23, 56, 89]
```

What about an array of things

```swift
//array of Strings ...

var arrayOfStrings = ["apple", "orange", "pineapple", "a", "b"]

print(arrayOfStrings.sorted())

//prints: ["a", "apple", "b", "orange", "pineapple"]
```

Its lexicographical

---
### Decreasing Order
We need to use the `sort(by: <comparator>)` syntax for this

```swift
//function to compare two values to find which if value1 is greater than value2...
func decreasing(value1:Int, value2:Int)->Bool{
    return value1 > value2
}
```

Call it with:

```swift
var arrayOfInt:[Int] = [1,56,89,23,4,6]

//sort the array by using the comparator function decreasing...
arrayOfInt.sort(by: decreasing)

print(arrayOfInt)
//prints: [89, 56, 23, 6, 4, 1]
```

---
### With Closures

```swift
arrayOfIntC.sort(by: { (value1:Int, value2:Int) -> Bool in
    return value1 > value2
})
```

```swift:
var arrayOfIntC = [34,6,89,56,78,14]

print(arrayOfIntC)
//prints: [89, 78, 56, 34, 14, 6]
```

---
### Sorting Custom Data

```swift
import UIKit

struct User{
    var name: String
    var age: Int
    var city: String
}

var users = [
    User(name: "Alice", age: 12, city: "Boston"),
    User(name: "Bob", age: 21, city: "Charlotte"),
    User(name: "Chris", age: 45, city: "NYC"),
    User(name: "David", age: 23, city: "Boston"),
    User(name: "Dillon", age: 89, city: "San Francisco"),
]

//MARK: sort by name in decreasing order
users.sort(by: { (user1:User, user2:User)-> Bool in
    return user1.name > user2.name
})

for user in users{
    print(user)
}
/*prints:
User(name: "Dillon", age: 89, city: "San Francisco")
User(name: "David", age: 23, city: "Boston")
User(name: "Chris", age: 45, city: "NYC")
User(name: "Bob", age: 21, city: "Charlotte")
User(name: "Alice", age: 12, city: "Boston")
 */

//MARK: sort by age in increasing order
users.sort(by: { (user1:User, user2:User)-> Bool in
    return user1.age < user2.age
})

for user in users{
    print(user)
}
/* prints:
User(name: "Alice", age: 12, city: "Boston")
User(name: "Bob", age: 21, city: "Charlotte")
User(name: "David", age: 23, city: "Boston")
User(name: "Chris", age: 45, city: "NYC")
User(name: "Dillon", age: 89, city: "San Francisco")
*/

```
