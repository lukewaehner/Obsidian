**Concept**
- Protocol that provides data to populate the table
- Two required methods: `numberOfRowsInSection` and `cellForRowAt`
- ViewController conforms to protocol and implements these methods

---

## Conforming to Protocol

```swift
extension ViewController: UITableViewDelegate, UITableViewDataSource {
    // DataSource methods here
}
```

---

## Required Methods

### **numberOfRowsInSection**
Returns number of rows to display in the table.

```swift
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) 
    -> Int 
{
    return contacts.count
}
```

**Common Pattern**: Return the count of your data array.

---

### **cellForRowAt**
Provides a configured cell for each row.

```swift
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
```

**Key Steps**:
1. **Dequeue reusable cell**: `dequeueReusableCell(withIdentifier:for:)`
   - Identifier string must match registration in [[UITableView Setup]]
   - `for: indexPath` required parameter
2. **Cast to custom type**: `as! TableViewContactCell`
3. **Populate with data**: Access array using `indexPath.row`
4. **Return configured cell**

---

## Cell Reuse Mechanism

**Why dequeue?**
- iOS reuses cells for performance
- Only creates enough cells to fill screen
- As you scroll, cells leaving screen are reused for new rows
- Much more memory efficient than creating cell for every row

**Identifier String**:
- Must match what you registered: `register(_:forCellReuseIdentifier:)`
- Used to distinguish different cell types in same table

---

## Optional Methods

### **numberOfSections**
Returns number of sections (groups) in table. Default is 1.

```swift
func numberOfSections(in tableView: UITableView) -> Int {
    return 1
}
```

### **titleForHeaderInSection**
Provides title text for section headers.

```swift
func tableView(_ tableView: UITableView, 
               titleForHeaderInSection section: Int) -> String? 
{
    return "My Contacts"
}
```

---

## Data Management Pattern

```swift
class ViewController: UIViewController {
    var contacts: [Contact] = []
    let contactTableScreen = ContactTableView()
    
    func addContact(_ contact: Contact) {
        contacts.append(contact)
        contactTableScreen.contactTable.reloadData()
    }
}
```

**Pattern**:
1. Store data in ViewController array
2. Modify array (append, remove, etc.)
3. Call `reloadData()` to refresh table
4. Table automatically calls `numberOfRowsInSection` and `cellForRowAt` again

---

## Setup in ViewController

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    contactTableScreen.contactTable.delegate = self
    contactTableScreen.contactTable.dataSource = self
}
```

---

**Related**
- [[UITableView]]
- [[UITableView Setup]]
- [[Custom UITableViewCell]]
- [[UITableViewDelegate]]
