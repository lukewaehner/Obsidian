
---
# Creating a Variable
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

---
## Assign Attributes

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
## Setting Constraints

We can use `NSLayoutConstraint` system class to set constraints.
`NSLayoutConstraint.activate()` takes an array of constraints and activates them on the current view.

Say we wanted to center to the x-axis and have a gap of 32 points between the top edge of the screen and the top edge of the Label?

```swift
NSLayoutConstraint.activate(
	[
		labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
		labelHello.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor)
	]
)
```

---

### All together:

```swift
import UIKit

class ViewController: UIViewController {
    
    //MARK: declaring the UI elements...
    var labelHello:UILabel! //"Hello World!" Label...
 
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: call methods to setup the attributes of UI elements...
        setupLabelHello()
        
        //MARK: initializing the constraints...
        initConstraints()
        
    }
    
    //Defining the Label attributes...
    func setupLabelHello(){
        labelHello = UILabel()
        labelHello.text = "Hello World!"
        labelHello.font = UIFont.systemFont(ofSize: 24)
        labelHello.textColor = .systemBlue
        labelHello.textAlignment = .center
        labelHello.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelHello)
    }
    
    //Initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate(
            [
                //Constraints for labelHello....
                labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
                labelHello.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor)
            ]
        )
    }

}
```