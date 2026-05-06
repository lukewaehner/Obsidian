**Concept**  
- Layout guide that avoids system-defined UI elements (notches, status bar, home indicator).  
- Ensures content isn’t hidden behind hardware features.  

**Code Example**
```swift
NSLayoutConstraint.activate([
    label.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
    label.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 16)
])
```
**Storyboard**

- Safe Area boundaries appear by default.
    
- Place UI inside to avoid overlap.
    

**Related**

- [[Constraints and Alignments]]