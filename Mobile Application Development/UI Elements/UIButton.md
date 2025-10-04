**Concept**  
- Tappable button for user actions.  
- Created via storyboard or in code.  

**Code Example**
```swift
let button = UIButton(type: .system)
button.setTitle("Tap Me", for: .normal)
button.addTarget(self, action: #selector(onButtonTap), for: .touchUpInside)
view.addSubview(button)

@objc func onButtonTap() {
    print("Button tapped!")
}
```

**Common Properties**

- `setTitle(_:for:)` → button text.
    
- `setTitleColor(_:for:)` → text color.
    
- `backgroundColor`
    
- `isEnabled`, `isHidden`
    

**Events**

- `.touchUpInside` → most common.
    
- `.touchDown`
    
- `.touchDragOutside`
    

**Related**

- Works with [[UITextField]] or [[UIAlertController]].