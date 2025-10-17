
> Create a form screen to input and validate new contact data, then send it back to the main screen.

---

## Overview

The add screen allows users to create new contacts. It consists of:
- View file (`AddContactView.swift`) - Form UI with text fields and picker
- ViewController file (`AddContactViewController.swift`) - Validation and delegate
- Uses [[Sending Data Back]] pattern with delegate

---

## 1. Create Add Contact View

Design the input form.

**File**: `AddContactView.swift`

```swift
import UIKit

class AddContactView: UIView {
    var addNewContactLabel: UILabel!
    var nameTextField: UITextField!
    var emailTextField: UITextField!
    var addPhoneLabel: UILabel!
    var phoneTypePicker: UIPickerView!
    var phoneNumberField: UITextField!
    var addressField: UITextField!
    var cityStateField: UITextField!
    var zipField: UITextField!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = .white
        setUpUI()
        initConstraints()
    }
    
    func setUpUI() {
        addNewContactLabel = UILabel()
        addNewContactLabel.text = "Add New Contact"
        addNewContactLabel.font = UIFont.systemFont(ofSize: 30)
        addNewContactLabel.translatesAutoresizingMaskIntoConstraints = false
        
        nameTextField = UITextField()
        nameTextField.placeholder = "Name"
        nameTextField.translatesAutoresizingMaskIntoConstraints = false
        nameTextField.borderStyle = .roundedRect
        
        emailTextField = UITextField()
        emailTextField.placeholder = "Email"
        emailTextField.translatesAutoresizingMaskIntoConstraints = false
        emailTextField.borderStyle = .roundedRect
        emailTextField.keyboardType = .emailAddress
        
        addPhoneLabel = UILabel()
        addPhoneLabel.text = "Add Phone"
        addPhoneLabel.font = UIFont.systemFont(ofSize: 30)
        addPhoneLabel.translatesAutoresizingMaskIntoConstraints = false
        
        phoneTypePicker = UIPickerView()
        phoneTypePicker.translatesAutoresizingMaskIntoConstraints = false
        
        phoneNumberField = UITextField()
        phoneNumberField.placeholder = "Phone Number"
        phoneNumberField.translatesAutoresizingMaskIntoConstraints = false
        phoneNumberField.borderStyle = .roundedRect
        phoneNumberField.keyboardType = .phonePad
        
        addressField = UITextField()
        addressField.placeholder = "Address"
        addressField.translatesAutoresizingMaskIntoConstraints = false
        addressField.borderStyle = .roundedRect
        
        cityStateField = UITextField()
        cityStateField.placeholder = "City, State"
        cityStateField.translatesAutoresizingMaskIntoConstraints = false
        cityStateField.borderStyle = .roundedRect
        
        zipField = UITextField()
        zipField.placeholder = "Zip"
        zipField.translatesAutoresizingMaskIntoConstraints = false
        zipField.borderStyle = .roundedRect
        zipField.keyboardType = .numberPad
        
        self.addSubview(addNewContactLabel)
        self.addSubview(nameTextField)
        self.addSubview(emailTextField)
        self.addSubview(addPhoneLabel)
        self.addSubview(phoneTypePicker)
        self.addSubview(phoneNumberField)
        self.addSubview(addressField)
        self.addSubview(cityStateField)
        self.addSubview(zipField)
    }
    
    func initConstraints() {
        let margin: CGFloat = 24
        let rowGap: CGFloat = 24
        NSLayoutConstraint.activate([
            addNewContactLabel.topAnchor.constraint(
                equalTo: safeAreaLayoutGuide.topAnchor, constant: rowGap),
            addNewContactLabel.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: rowGap),
            addNewContactLabel.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -rowGap),
            
            nameTextField.topAnchor.constraint(
                equalTo: addNewContactLabel.bottomAnchor, constant: rowGap),
            nameTextField.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            nameTextField.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
            
            emailTextField.topAnchor.constraint(
                equalTo: nameTextField.bottomAnchor, constant: rowGap),
            emailTextField.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            emailTextField.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
            
            addPhoneLabel.topAnchor.constraint(
                equalTo: emailTextField.bottomAnchor, constant: rowGap),
            addPhoneLabel.centerXAnchor.constraint(
                equalTo: safeAreaLayoutGuide.centerXAnchor),
            
            phoneTypePicker.topAnchor.constraint(
                equalTo: addPhoneLabel.bottomAnchor),
            phoneTypePicker.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            phoneTypePicker.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
            phoneTypePicker.heightAnchor.constraint(equalToConstant: 120),
            
            phoneNumberField.topAnchor.constraint(
                equalTo: phoneTypePicker.bottomAnchor, constant: rowGap / 3),
            phoneNumberField.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            phoneNumberField.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
            
            addressField.topAnchor.constraint(
                equalTo: phoneNumberField.bottomAnchor, constant: rowGap),
            addressField.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            addressField.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
            
            cityStateField.topAnchor.constraint(
                equalTo: addressField.bottomAnchor, constant: rowGap),
            cityStateField.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            cityStateField.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
            
            zipField.topAnchor.constraint(
                equalTo: cityStateField.bottomAnchor, constant: rowGap),
            zipField.leadingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.leadingAnchor, constant: margin),
            zipField.trailingAnchor.constraint(
                equalTo: safeAreaLayoutGuide.trailingAnchor, constant: -margin),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

**Key UI Elements**:
- Multiple [[UITextField]]s for input
- `UIPickerView` for phone type selection
- Appropriate `keyboardType` for each field (`.emailAddress`, `.phonePad`, `.numberPad`)
- Consistent spacing with `rowGap` and `margin` constants

---

## 2. Create Utilities File

Store constants like phone types.

**File**: `Utilities.swift`

```swift
import Foundation

class Utilities {
    static let phoneTypes = ["Cell", "Work", "Home"]
}
```

**Pattern**: Use static properties for app-wide constants.

---

## 3. Create Add Contact ViewController

Handle picker, validation, and delegate callback.

**File**: `AddContactViewController.swift`

```swift
import UIKit

class AddContactViewController: UIViewController {
    let addContactScreen = AddContactView()
    var selectedType = "Cell"
    var delegate: ViewController!
    
    override func loadView() {
        view = addContactScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        addContactScreen.phoneTypePicker.delegate = self
        addContactScreen.phoneTypePicker.dataSource = self
        
        navigationItem.rightBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .save,
            target: self,
            action: #selector(saveContact)
        )
        
        let tapRecognizer = UITapGestureRecognizer(
            target: self, 
            action: #selector(hideKeyboardOnTap)
        )
        tapRecognizer.cancelsTouchesInView = false
        view.addGestureRecognizer(tapRecognizer)
    }
    
    @objc func saveContact() {
        guard let sendContact = validateInputs() else {
            return
        }
        delegate.addContact(sendContact)
        navigationController?.popViewController(animated: true)
    }
    
    @objc func hideKeyboardOnTap() {
        view.endEditing(true)
    }
}
```

**Key Setup**:
- `var delegate: ViewController!` - Reference to main screen (see [[Sending Data Back]])
- Set picker's `delegate` and `dataSource` to `self`
- Save button calls `saveContact()` 
- Tap gesture dismisses keyboard

---

## 4. Implement Picker Protocols

```swift
extension AddContactViewController: UIPickerViewDelegate, UIPickerViewDataSource {
    
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, 
                    numberOfRowsInComponent component: Int) -> Int {
        return Utilities.phoneTypes.count
    }
    
    func pickerView(_ pickerView: UIPickerView, 
                    titleForRow row: Int, 
                    forComponent component: Int) -> String? {
        selectedType = Utilities.phoneTypes[row]
        return Utilities.phoneTypes[row]
    }
}
```

**How it works**:
- `numberOfComponents`: Number of columns (1 for simple picker)
- `numberOfRowsInComponent`: Number of options (array count)
- `titleForRow`: Text for each row, also updates `selectedType`

---

## 5. Implement Validation

Add extension for input validation.

```swift
extension AddContactViewController {
    
    func validateInputs() -> Contact? {
        guard
            let name = addContactScreen.nameTextField.text, !name.isEmpty,
            let email = addContactScreen.emailTextField.text, !email.isEmpty,
            let phoneNumber = addContactScreen.phoneNumberField.text, 
                !phoneNumber.isEmpty,
            let address = addContactScreen.addressField.text, !address.isEmpty,
            let cityState = addContactScreen.cityStateField.text, 
                !cityState.isEmpty,
            let zipCode = addContactScreen.zipField.text, !zipCode.isEmpty
        else {
            showAlert(title: "Error", message: "Please fill all fields")
            return nil
        }
        
        if !isValidEmail(email) {
            showAlert(title: "Error", message: "Please enter a valid email")
            return nil
        }
        
        if !isValidPhoneNumber(phoneNumber) {
            showAlert(title: "Error", 
                     message: "Please enter a valid phone number")
            return nil
        }
        
        if !isValidZip(zipCode) {
            showAlert(title: "Error", message: "Please enter a valid zip code")
            return nil
        }
        
        let addressCombined = """
            \(address)
            \(cityState)
            \(zipCode)
            """
        
        let contact = Contact(
            name: name,
            email: email,
            phone: phoneNumber,
            type: selectedType,
            address: addressCombined
        )
        return contact
    }
    
    func isValidEmail(_ email: String) -> Bool {
        let emailRegEx = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}"
        let emailPred = NSPredicate(format: "SELF MATCHES %@", emailRegEx)
        return emailPred.evaluate(with: email)
    }
    
    func isValidPhoneNumber(_ num: String) -> Bool {
        let digits = num.filter { $0.isNumber }
        if digits.count == 10 {
            return true  // 123-456-7890
        } else if digits.count == 11, digits.first == "1" {
            return true  // 1-123-456-7890
        } else {
            return false
        }
    }
    
    func isValidZip(_ zip: String) -> Bool {
        let digits = zip.filter { $0.isNumber }
        guard digits.count == 5, let value = Int(zip) else { return false }
        return (1...99950).contains(value)
    }
}
```

**Validation Pattern**:
1. Check all fields filled with `guard let` and `!isEmpty`
2. Validate email with regex pattern
3. Validate phone (10 or 11 digits)
4. Validate zip (5 digits, 1-99950 range)
5. Return `Contact` if valid, `nil` if invalid
6. Show [[UIAlertController]] for errors

---

## 6. Add Alert Helper

```swift
extension AddContactViewController {
    func showAlert(title: String = "Notice", message: String) {
        let alert = UIAlertController(
            title: title,
            message: message,
            preferredStyle: .alert
        )
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        present(alert, animated: true)
    }
}
```

---

## 7. Connect Delegate in Main Screen

Back in `ViewController.swift`, set delegate when pushing:

```swift
@objc func addTapped() {
    let addController = AddContactViewController()
    addController.delegate = self  // Critical!
    navigationController?.pushViewController(addController, animated: true)
}

func addContact(_ contact: Contact) {
    contacts.append(contact)
    contactTableScreen.contactTable.reloadData()
}
```

**Flow**:
1. Main screen creates add screen
2. Sets `delegate = self` so add screen can call back
3. Add screen validates and calls `delegate.addContact(contact)`
4. Main screen appends to array and reloads table
5. Add screen pops itself: `navigationController?.popViewController()`

---

## Result

You now have:
- Form screen with validation
- Picker for phone type
- Data sent back to main screen via delegate
- New contact appears in table

---

**Next**: [[Detail Display Screen]]

**Related**:
- [[Sending Data Back]]
- [[UITextField]]
- [[UIAlertController]]
- [[Navigation Controller]]
