Open the ViewController code and create a variable with:

```swift
import UIKit

class ViewController: UIViewController {
	var labelHello:UILabel!
	
	override func ViewDidLoad() {
		super.viewDidLoad()
	}
}
```

> You must unwrap the UI elements, since they are passed as optionals