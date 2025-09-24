**Concept**  
- Displays alerts and action sheets.  
- Two styles: `.alert` (center popup) and `.actionSheet` (bottom slide-up).  

**Code Example (Alert)**
```swift
let alert = UIAlertController(
    title: "Warning",
    message: "Are you sure you want to continue?",
    preferredStyle: .alert
)

alert.addAction(UIAlertAction(title: "Cancel", style: .cancel))
alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in
    print("User confirmed")
})

present(alert, animated: true)
```

Code Example (Action Sheet)

```swift


let sheet = UIAlertController(
    title: "Options",
    message: nil,
    preferredStyle: .actionSheet
)

sheet.addAction(UIAlertAction(title: "Delete", style: .destructive))
sheet.addAction(UIAlertAction(title: "Cancel", style: .cancel))

present(sheet, animated: true)
```

**Common Uses**
- Confirmation dialogs
- Error messages
- Option menus

Related
- Often triggered by [[UIButton]].