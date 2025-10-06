
> Table views in iOS display rows of vertically scrolling content in a single column, each row contains one piece of content. The contacts app displays each contact in a separate row for example.

---

## Creating the Table

```swift
import UIKit

class FirstScreenView: UIView {
	var tableViewExpense: UITableView!
	
	override init(frame: CGRect) {
		super.init(frame: frame)
		backgroundColor = .white
		
		setupTableViewExpense()
		initConstraints()
	}
	
	func setupTableViewExpense() {
		tableViewExpense = UITableView()
		tableViewExpense.translatesAutoresizingMaskIntoConstraints = false
	}
}
```