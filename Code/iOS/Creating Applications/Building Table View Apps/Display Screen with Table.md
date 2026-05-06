
> Create the main screen with a UITableView to display contacts.

---

## Overview

The display screen is the root view controller showing a list of contacts. It consists of:
- View file (`ContactTableView.swift`) - UI layout
- Custom cell file (`TableViewContactCell.swift`) - Row design  
- ViewController file (`ViewController.swift`) - Logic and data
- Data model (`Contact.swift`) - Contact structure

---

## 1. Create Data Model

First, define the contact structure.

**File**: `Contact.swift`

```swift
import Foundation

struct Contact {
    var name: String?
    var email: String?
    var phone: String?
    var type: String?
    var address: String?
    
    init(name: String? = nil, email: String? = nil, phone: String? = nil, 
         type: String? = nil, address: String? = nil) {
        self.name = name
        self.email = email
        self.phone = phone
        self.type = type
        self.address = address
    }
}
```

**Key Points**:
- Use `struct` for simple data models
- All properties optional with default `nil` values
- Custom init allows flexible initialization

---

## 2. Create Custom Table View Cell

Design how each row looks.

**File**: `TableViewContactCell.swift`

See [[Custom UITableViewCell]] for complete implementation.

**Key Elements**:
```swift
class TableViewContactCell: UITableViewCell {
    var wrapperCellView: UIView!      // Container for styling
    var nameLabel: UILabel!            // Bold, larger font
    var emailLabel: UILabel!           // Regular font
    var phoneLabel: UILabel!           // Regular font
    var typeLabel: UILabel!            // Phone type (Cell/Work/Home)
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        backgroundColor = .white
        setupWrapperCellView()
        setupLabels()
        initConstraints()
    }
    // ... setup methods
}
```

**Styling Tips**:
- Use wrapper view for borders/corners
- Add margins between cells (8-12pt)
- Bold important info (name)
- Align related labels

---

## 3. Create Table View File

Set up the table in a separate view file.

**File**: `ContactTableView.swift`

See [[UITableView Setup]] for complete implementation.

```swift
import UIKit

class ContactTableView: UIView {
    var contactTable: UITableView!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        setupContactTable()
        initConstraints()
    }
    
    func setupContactTable() {
        contactTable = UITableView()
        contactTable.register(
            TableViewContactCell.self, 
            forCellReuseIdentifier: "contact"
        )
        contactTable.translatesAutoresizingMaskIntoConstraints = false
        contactTable.separatorStyle = .none
        self.addSubview(contactTable)
    }
    
    func initConstraints() {
        NSLayoutConstraint.activate([
            contactTable.topAnchor.constraint(
                equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 12),
            contactTable.bottomAnchor.constraint(
                equalTo: self.safeAreaLayoutGuide.bottomAnchor, constant: -12),
            contactTable.leadingAnchor.constraint(
                equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 12),
            contactTable.trailingAnchor.constraint(
                equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -12),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

**Critical**: Register cell with identifier `"contact"` - must match in `cellForRowAt`.

---

## 4. Create ViewController

Manage data and connect table protocols.

**File**: `ViewController.swift`

```swift
import UIKit

class ViewController: UIViewController {
    var contacts: [Contact] = []
    let contactTableScreen = ContactTableView()
    
    override func loadView() {
        view = contactTableScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationItem.title = "My Contacts"
        navigationItem.rightBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .add,
            target: self,
            action: #selector(addTapped)
        )
        
        contactTableScreen.contactTable.delegate = self
        contactTableScreen.contactTable.dataSource = self
    }
    
    @objc func addTapped() {
        let addController = AddContactViewController()
        addController.delegate = self
        navigationController?.pushViewController(addController, animated: true)
    }
    
    func addContact(_ contact: Contact) {
        contacts.append(contact)
        contactTableScreen.contactTable.reloadData()
    }
}
```

**Key Setup**:
1. Data array: `var contacts: [Contact] = []`
2. View instance: `let contactTableScreen = ContactTableView()`
3. Set view: `view = contactTableScreen` in `loadView()`
4. Assign protocols: `delegate = self`, `dataSource = self`
5. Add button for navigation to add screen

---

## 5. Implement Table Protocols

Add extension for [[UITableViewDelegate]] and [[UITableViewDataSource]].

```swift
extension ViewController: UITableViewDelegate, UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) 
        -> Int 
    {
        return contacts.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) 
        -> UITableViewCell 
    {
        let cell = tableView.dequeueReusableCell(
            withIdentifier: "contact",
            for: indexPath
        ) as! TableViewContactCell
        
        cell.nameLabel.text = contacts[indexPath.row].name
        cell.emailLabel.text = contacts[indexPath.row].email
        cell.phoneLabel.text = contacts[indexPath.row].phone
        cell.typeLabel.text = contacts[indexPath.row].type
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let contact = contacts[indexPath.row]
        let displayScreen = DisplayContactController()
        displayScreen.displayContact = contact
        navigationController?.pushViewController(displayScreen, animated: true)
    }
}
```

**Flow**:
1. `numberOfRowsInSection`: Returns array count
2. `cellForRowAt`: Dequeues cell, populates with data at `indexPath.row`, returns
3. `didSelectRowAt`: Gets contact, creates detail screen, passes data, navigates

---

## Result

You now have a functioning table view that:
- Displays contacts in custom styled cells
- Shows "My Contacts" title
- Has "+" button to add contacts (Step 2)
- Navigates to detail view on row tap (Step 3)

---

**Next**: [[Add Data Screen]]

**Related**:
- [[UITableView]]
- [[Custom UITableViewCell]]
- [[UITableViewDelegate]]
- [[UITableViewDataSource]]
- [[Separate View From The Controller]]
