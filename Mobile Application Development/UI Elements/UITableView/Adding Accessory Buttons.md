Adding interactive menu buttons to UITableView cells using accessory views.

---

## Overview

Accessory buttons provide additional actions for table view cells without navigating to a new screen. Common use cases include edit/delete menus, settings, or quick actions.

---

## Implementation

Add the accessory button configuration inside `cellForRowAt`:

```swift
func tableView(_ tableView: UITableView, 
               cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    
    let cell = tableView.dequeueReusableCell(withIdentifier: "names", 
                                              for: indexPath) as! ContactsTableViewCell
    cell.labelName.text = contactNames[indexPath.row]
    
    // Create the accessory button
    let buttonOptions = UIButton(type: .system)
    buttonOptions.sizeToFit()
    buttonOptions.showsMenuAsPrimaryAction = true
    
    // Set icon from SF Symbols
    buttonOptions.setImage(UIImage(systemName: "slider.horizontal.3"), 
                           for: .normal)
    
    // Configure menu with actions
    buttonOptions.menu = UIMenu(title: "Edit/Delete?",
                                children: [
                                    UIAction(title: "Edit", handler: { (_) in
                                        self.editSelectedFor(contact: indexPath.row)
                                    }),
                                    UIAction(title: "Delete", handler: { (_) in
                                        self.deleteSelectedFor(contact: indexPath.row)
                                    })
                                ])
    
    // Set button as cell accessory
    cell.accessoryView = buttonOptions
    
    return cell
}
```

---

## Key Components

### 1. Create the Button
```swift
let buttonOptions = UIButton(type: .system)
buttonOptions.sizeToFit()
buttonOptions.showsMenuAsPrimaryAction = true
```

- `type: .system` - Uses system button styling
- `sizeToFit()` - Automatically sizes button to content
- `showsMenuAsPrimaryAction = true` - Shows menu on tap (no need for separate tap handler)

### 2. Set the Icon
```swift
buttonOptions.setImage(UIImage(systemName: "slider.horizontal.3"), 
                       for: .normal)
```

Uses SF Symbols for consistent iOS iconography. Common options:
- `"slider.horizontal.3"` - Settings/options
- `"ellipsis.circle"` - More options
- `"pencil"` - Edit
- `"trash"` - Delete

### 3. Configure the Menu
```swift
buttonOptions.menu = UIMenu(title: "Edit/Delete?",
                            children: [
                                UIAction(title: "Edit", handler: { (_) in
                                    self.editSelectedFor(contact: indexPath.row)
                                }),
                                UIAction(title: "Delete", handler: { (_) in
                                    self.deleteSelectedFor(contact: indexPath.row)
                                })
                            ])
```

- `UIMenu` - Container for menu actions
- `UIAction` - Individual menu items with handlers
- Handler closure executes when user selects the action

### 4. Attach to Cell
```swift
cell.accessoryView = buttonOptions
```

Sets the button as the cell's accessory view (appears on the right side).

---

## Handler Functions

Implement the action handlers referenced in the menu:

```swift
func editSelectedFor(contact index: Int) {
    // Handle edit action
    let contact = contactNames[index]
    // Show edit screen or inline editing
}

func deleteSelectedFor(contact index: Int) {
    // Handle delete action
    let contact = contactNames[index]
    // Confirm deletion and remove from data source
}
```

---

## Related Topics

- [[UITableView]] - Main table view documentation
- [[Custom UITableViewCell]] - Creating custom cell layouts
- [[UITableViewDelegate]] - Handling cell interactions