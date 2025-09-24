**Concept**  
- Displays static or dynamic text.  
- Added from Object Library (`Cmd + Shift + L`) or programmatically.  
- Respects [[Safe Area]].

**Code Example**
```swift
let label = UILabel()
label.text = "Hello World"
label.textColor = .black
label.font = UIFont.systemFont(ofSize: 18)
label.textAlignment = .center
view.addSubview(label)
```

**Common Properties**

- `text`: String to display.
    
- `textColor`: `UIColor` of text.
    
- `font`: Font and size.
    
- `textAlignment`: `.left`, `.center`, `.right`.
    
- `numberOfLines`: `0` for multiline.
    

**Common Methods**

- `sizeToFit()` → resizes to fit content.
    
- `adjustsFontSizeToFitWidth = true` → auto shrink.
    

**Related**

- Often paired with [[UITextField]] or [[UIButton]].

---


