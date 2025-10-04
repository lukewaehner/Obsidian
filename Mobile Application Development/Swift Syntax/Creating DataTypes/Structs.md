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
