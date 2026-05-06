**Concept**
- Custom cells allow complete control over row appearance
- Cells are reused for performance via dequeue mechanism
- Subclass `UITableViewCell` and add custom subviews with constraints

---

## Creating a Custom Cell

```swift
import UIKit

class TableViewContactCell: UITableViewCell {
    var wrapperCellView: UIView!
    var nameLabel: UILabel!
    var emailLabel: UILabel!
    var phoneLabel: UILabel!
    var typeLabel: UILabel!
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        backgroundColor = .white
        
        setupWrapperCellView()
        setupLabels()
        initConstraints()
    }
    
    func setupWrapperCellView() {
        wrapperCellView = UITableViewCell()
        wrapperCellView.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.layer.cornerRadius = 10
        wrapperCellView.layer.borderWidth = 1
        wrapperCellView.layer.masksToBounds = true
        wrapperCellView.layer.borderColor = UIColor.gray.cgColor
        wrapperCellView.backgroundColor = .white
        self.addSubview(wrapperCellView)
    }
    
    func setupLabels() {
        nameLabel = UILabel()
        nameLabel.translatesAutoresizingMaskIntoConstraints = false
        nameLabel.font = UIFont.boldSystemFont(ofSize: 18)
        wrapperCellView.addSubview(nameLabel)
        
        emailLabel = UILabel()
        emailLabel.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(emailLabel)
        
        phoneLabel = UILabel()
        phoneLabel.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(phoneLabel)
        
        typeLabel = UILabel()
        typeLabel.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(typeLabel)
    }
    
    func initConstraints() {
        NSLayoutConstraint.activate([
            wrapperCellView.topAnchor.constraint(
                equalTo: self.topAnchor,
                constant: 8
            ),
            wrapperCellView.leadingAnchor.constraint(
                equalTo: self.leadingAnchor,
                constant: 12
            ),
            wrapperCellView.trailingAnchor.constraint(
                equalTo: self.trailingAnchor,
                constant: -12
            ),
            wrapperCellView.bottomAnchor.constraint(
                equalTo: self.bottomAnchor,
                constant: -8
            ),
            
            nameLabel.topAnchor.constraint(
                equalTo: wrapperCellView.topAnchor,
                constant: 4
            ),
            nameLabel.leadingAnchor.constraint(
                equalTo: wrapperCellView.leadingAnchor,
                constant: 4
            ),
            
            emailLabel.topAnchor.constraint(
                equalTo: nameLabel.bottomAnchor,
                constant: 4
            ),
            emailLabel.leadingAnchor.constraint(
                equalTo: nameLabel.leadingAnchor
            ),
            
            phoneLabel.topAnchor.constraint(
                equalTo: emailLabel.bottomAnchor,
                constant: 4
            ),
            phoneLabel.leadingAnchor.constraint(
                equalTo: nameLabel.leadingAnchor
            ),
            phoneLabel.bottomAnchor.constraint(
                equalTo: wrapperCellView.bottomAnchor, 
                constant: -8
            ),
            
            typeLabel.centerYAnchor.constraint(
                equalTo: phoneLabel.centerYAnchor
            ),
            typeLabel.leadingAnchor.constraint(
                equalTo: phoneLabel.trailingAnchor,
                constant: 4
            ),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

---

## Key Components

### **1. Wrapper View Pattern**
- Use a container `UIView` inside the cell
- Add margins around wrapper for visual separation
- Apply styling (borders, corners) to wrapper, not cell itself

```swift
wrapperCellView.layer.cornerRadius = 10
wrapperCellView.layer.borderWidth = 1
wrapperCellView.layer.borderColor = UIColor.gray.cgColor
```

### **2. Custom Subviews**
- Add [[UILabel]], [[UIButton]], [[UIImageView]], etc. to wrapper
- Set `translatesAutoresizingMaskIntoConstraints = false`
- Add to wrapper: `wrapperCellView.addSubview(label)`

### **3. Cell Constraints**
- Pin wrapper to cell with margins for spacing between rows
- Constrain subviews within wrapper
- Use bottom constraint on last element to define cell height

---

## Populating Cells

Cells are populated in [[UITableViewDataSource]]'s `cellForRowAt`:

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

**Key Points**:
- `dequeueReusableCell` reuses cells for performance
- Cast to custom cell type: `as! TableViewContactCell`
- Access custom properties to set data
- Use `indexPath.row` to index into data array

---

**Related**
- [[UITableView]]
- [[UITableView Setup]]
- [[UITableViewDataSource]]
- [[UILabel]]
