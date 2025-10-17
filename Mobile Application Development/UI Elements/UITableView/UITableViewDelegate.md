**Concept**
- Protocol for handling user interactions with table rows
- Manages row selection, display customization, and user actions
- Conformed to by ViewController alongside [[UITableViewDataSource]]

---

## Conforming to Protocol

```swift
extension ViewController: UITableViewDelegate, UITableViewDataSource {
    // Delegate methods here
}
```

**Using extensions** keeps code organized by separating table view logic from other ViewController code.

---

## Key Methods

### **didSelectRowAt**
Called when user taps a row, commonly used for navigation.

```swift
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    let contact = contacts[indexPath.row]
    let displayScreen = DisplayContactController()
    displayScreen.displayContact = contact
    navigationController?.pushViewController(displayScreen, animated: true)
}
```

**Parameters**:
- `tableView`: The table view instance
- `indexPath`: Contains `section` and `row` - use `indexPath.row` to access data

**Common Pattern**:
1. Get data from array using `indexPath.row`
2. Create new view controller
3. Pass data to new controller (see [[Sending Data Between Screens]])
4. Push onto [[Navigation Controller]] stack

---

## Other Common Methods

### **heightForRowAt**
Specify custom height for rows.

```swift
func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) 
    -> CGFloat 
{
    return 100
}
```

### **willDisplay**
Called before cell appears, useful for animations.

```swift
func tableView(_ tableView: UITableView, 
               willDisplay cell: UITableViewCell, 
               forRowAt indexPath: IndexPath) 
{
    cell.alpha = 0
    UIView.animate(withDuration: 0.3) {
        cell.alpha = 1
    }
}
```

### **didDeselectRowAt**
Called when row is deselected.

```swift
func tableView(_ tableView: UITableView, didDeselectRowAt indexPath: IndexPath) {
    print("Row \(indexPath.row) deselected")
}
```

---

## Setup in ViewController

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    contactTableScreen.contactTable.delegate = self
    contactTableScreen.contactTable.dataSource = self
}
```

**Must set both** `delegate` and `dataSource` for table to function properly.

---

**Related**
- [[UITableView]]
- [[UITableViewDataSource]]
- [[Navigation Controller]]
- [[Sending Data Between Screens]]
