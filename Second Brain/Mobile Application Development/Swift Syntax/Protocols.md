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
