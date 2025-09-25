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