**Concept**  
Auto Layout rules that define size & position.

**Tools (bottom-right of editor)**
- **Alignment** → center, edges, baseline.
- **Add Constraints** → spacing, width, height.
- **Reset Constraints** → clears to defaults.

**Code Example**
```swift
label.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
    label.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20)
])
```
**Related**
- [[Safe Area]]