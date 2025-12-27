**Concept**
- UITableView is typically set up in a separate View file following MVC pattern
- Requires registration of custom cells and constraint setup
- View file handles UI layout, ViewController manages data and interaction

---

## Creating the Table in a View File

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
                equalTo: self.safeAreaLayoutGuide.topAnchor,
                constant: 12
            ),
            contactTable.bottomAnchor.constraint(
                equalTo: self.safeAreaLayoutGuide.bottomAnchor,
                constant: -12
            ),
            contactTable.leadingAnchor.constraint(
                equalTo: self.safeAreaLayoutGuide.leadingAnchor,
                constant: 12
            ),
            contactTable.trailingAnchor.constraint(
                equalTo: self.safeAreaLayoutGuide.trailingAnchor,
                constant: -12
            ),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

---

## Key Steps

1. **Declare the table**: `var contactTable: UITableView!`
2. **Initialize in `init(frame:)`**: Create table, register cells, set constraints
3. **Register custom cell**: `register(_:forCellReuseIdentifier:)` with identifier string
4. **Configure properties**: 
   - `translatesAutoresizingMaskIntoConstraints = false`
   - `separatorStyle = .none` (optional, if custom cell has borders)
5. **Add to view**: `self.addSubview(contactTable)`
6. **Set constraints**: Pin to safe area with margins

---

## Connecting to ViewController

```swift
import UIKit

class ViewController: UIViewController {
    let contactTableScreen = ContactTableView()
    var contacts: [Contact] = []
    
    override func loadView() {
        view = contactTableScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        contactTableScreen.contactTable.delegate = self
        contactTableScreen.contactTable.dataSource = self
    }
}
```

**Key Points**:
- Create instance of view: `let contactTableScreen = ContactTableView()`
- Set as main view in `loadView()`: `view = contactTableScreen`
- Assign delegate and dataSource in `viewDidLoad()`
- Access table through view instance: `contactTableScreen.contactTable`

---

## Reloading Data

After modifying the data source array, reload the table:

```swift
func addContact(_ contact: Contact) {
    contacts.append(contact)
    contactTableScreen.contactTable.reloadData()
}
```

**`reloadData()`** triggers the table to call `numberOfRowsInSection` and `cellForRowAt` again, updating the display.

---

**Related**
- [[UITableView]]
- [[Custom UITableViewCell]]
- [[UITableViewDelegate]]
- [[UITableViewDataSource]]
- [[Separate View From The Controller]]
