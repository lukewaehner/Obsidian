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
