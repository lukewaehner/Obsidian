
> Display full contact information when user taps a row in the table.

---

## Overview

The detail screen shows complete contact information. It consists of:
- View file (`DisplayContact.swift`) - Layout for displaying data
- ViewController file (`DisplayContactController.swift`) - Receives and displays contact
- Uses [[Sending Data Between Screens]] pattern

---

## 1. Create Display Contact View

Design the detail display layout.

**File**: `DisplayContact.swift`

```swift
import UIKit

class DisplayContact: UIView {
    var nameLabel: UILabel!
    var emailLabel: UILabel!
    var phoneLabel: UILabel!
    var addressLabel: UILabel!
    var addressInputLabel: UILabel!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = .white
        
        initElements()
        initConstraints()
    }
    
    func initElements() {
        nameLabel = UILabel()
        nameLabel.font = UIFont.boldSystemFont(ofSize: 32)
        nameLabel.translatesAutoresizingMaskIntoConstraints = false
        
        emailLabel = UILabel()
        emailLabel.font = UIFont.systemFont(ofSize: 24)
        emailLabel.translatesAutoresizingMaskIntoConstraints = false
        
        phoneLabel = UILabel()
        phoneLabel.font = UIFont.systemFont(ofSize: 24)
        phoneLabel.translatesAutoresizingMaskIntoConstraints = false
        
        addressLabel = UILabel()
        addressLabel.text = "Address:"
        addressLabel.font = UIFont.systemFont(ofSize: 28, weight: .bold)
        addressLabel.translatesAutoresizingMaskIntoConstraints = false
        
        addressInputLabel = UILabel()
        addressInputLabel.font = UIFont.systemFont(ofSize: 24)
        addressInputLabel.translatesAutoresizingMaskIntoConstraints = false
        addressInputLabel.numberOfLines = 0
        addressInputLabel.lineBreakMode = .byWordWrapping
        
        self.addSubview(nameLabel)
        self.addSubview(emailLabel)
        self.addSubview(phoneLabel)
        self.addSubview(addressLabel)
        self.addSubview(addressInputLabel)
    }
    
    func initConstraints() {
        let rowGap: CGFloat = 32.0
        let margin: CGFloat = 16.0
        NSLayoutConstraint.activate([
            nameLabel.topAnchor.constraint(
                equalTo: safeAreaLayoutGuide.topAnchor, constant: rowGap),
            nameLabel.centerXAnchor.constraint(
                equalTo: safeAreaLayoutGuide.centerXAnchor),
            
            emailLabel.topAnchor.constraint(
                equalTo: nameLabel.bottomAnchor, constant: rowGap),
            emailLabel.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            emailLabel.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
            
            phoneLabel.topAnchor.constraint(
                equalTo: emailLabel.bottomAnchor, constant: rowGap),
            phoneLabel.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            phoneLabel.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
            
            addressLabel.topAnchor.constraint(
                equalTo: phoneLabel.bottomAnchor, constant: rowGap),
            addressLabel.centerXAnchor.constraint(
                equalTo: safeAreaLayoutGuide.centerXAnchor),
            
            addressInputLabel.topAnchor.constraint(
                equalTo: addressLabel.bottomAnchor, constant: 8),
            addressInputLabel.centerXAnchor.constraint(
                equalTo: safeAreaLayoutGuide.centerXAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

**Key UI Features**:
- Large, bold name centered at top
- Email and phone with labels
- Multiline address with `numberOfLines = 0`
- Generous spacing with `rowGap: 32.0`
- Static "Address:" header label

---

## 2. Create Display Contact Controller

Receive contact data and populate view.

**File**: `DisplayContactController.swift`

```swift
import UIKit

class DisplayContactController: UIViewController {
    let displayContactView = DisplayContact()
    var displayContact: Contact?
    
    override func loadView() {
        view = displayContactView
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        guard let displayContact else { return }
        
        displayContactView.nameLabel.text = displayContact.name!
        displayContactView.emailLabel.text = "Email: \(displayContact.email!)"
        displayContactView.phoneLabel.text = 
            "Phone: \(displayContact.phone!) (\(displayContact.type!))"
        displayContactView.addressInputLabel.text = displayContact.address!
    }
}
```

**Key Points**:
- `var displayContact: Contact?` - Holds passed data
- `guard let` safely unwraps optional
- Force unwrap (`!`) safe here because validation ensures data exists
- Format strings with labels: "Email: user@example.com"
- Phone includes type in parentheses: "123-456-7890 (Cell)"

---

## 3. Pass Data from Main Screen

In `ViewController.swift`, implement `didSelectRowAt`:

```swift
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    let contact = contacts[indexPath.row]
    let displayScreen = DisplayContactController()
    displayScreen.displayContact = contact
    navigationController?.pushViewController(displayScreen, animated: true)
}
```

**Data Flow**:
1. User taps row
2. Get contact from array using `indexPath.row`
3. Create detail screen controller
4. **Set property before pushing**: `displayScreen.displayContact = contact`
5. Push onto [[Navigation Controller]] stack
6. Detail screen reads `displayContact` in `viewDidLoad()`

This is the [[Sending Data Between Screens]] pattern.

---

## Complete Flow Summary

### **User adds contact**:
1. Tap "+" button on main screen
2. Fill form on add screen
3. Tap "Save"
4. Validation runs
5. If valid, delegate callback: `delegate.addContact(contact)`
6. Main screen appends to array
7. Main screen reloads table: `reloadData()`
8. Add screen pops: `popViewController()`

### **User views contact**:
1. Tap row in table
2. `didSelectRowAt` called
3. Get contact from array
4. Create detail controller
5. Pass contact via property
6. Push detail screen
7. Detail screen displays data in `viewDidLoad()`

---

## Result

You now have a complete three-screen app:
- **Main screen**: Table view of contacts
- **Add screen**: Form with validation, sends data back
- **Detail screen**: Full contact information display

All screens connected via [[Navigation Controller]] with proper data flow.

---

**Related**:
- [[Sending Data Between Screens]]
- [[Sending Data Back]]
- [[Navigation Controller]]
- [[UITableViewDelegate]]
- [[UILabel]]
