
```swift
import UIKit

class ViewController: UIViewController {
	var labelHello:UILabel!
	
	override func ViewDidLoad() {
		super.viewDidLoad()
		
		setupLabelHello()
	}
	
	func setupLabelHello() {
		labelHello = UILabel()
		labelHello.text = "Hello World!"
		labelHello.font = UIFont.systemFont(ofSize: 24)
		labelHello.textColor = .systemBlue
		labelHello.textAlignment = .center
		labelHello.translatesAutoresizingMaskIntoConstraints = false
		view.addSubview(labelHello)
	}
}
```

We have defined attributes for the label:

| Attribute                                            | Meaning                                       |
| ---------------------------------------------------- | --------------------------------------------- |
| labelHello.text                                      | The text inside                               |
| labelHello.font                                      | Font                                          |
| labelHello.textColor                                 | Color of the text use `.` to choose options   |
| labelHello.textAlignment                             | `.`{Option}                                   |
| labelHello.translatesAutoresizingMaskIntoConstraints | Set to false so we can move it how we want to |
| view.addSubView(labelHello)                          | Here is where we add it to the screen itself  |

---