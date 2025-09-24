**Concept**  
- Single-line input field.  
- Supports placeholder text, editing, and events.  

**Code Example**
```swift
let textField = UITextField()
textField.placeholder = "Enter name"
textField.borderStyle = .roundedRect
textField.delegate = self
view.addSubview(textField)
```

**Key Properties**

- `text`: The current value.
    
- `placeholder`: Hint text.
    
- `borderStyle`: `.none`, `.line`, `.bezel`, `.roundedRect`.
    
- `keyboardType`: `.default`, `.numberPad`, `.emailAddress`.
    

**Events**

- `textFieldDidBeginEditing`
    
- `textFieldDidEndEditing`
    
- `textField(_:shouldChangeCharactersIn:replacementString:)`
    

**Related**

- Often used with [[UIButton]] for form submissions.

