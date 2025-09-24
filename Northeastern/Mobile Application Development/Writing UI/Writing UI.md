[[Creating Variables]]
[[Assign Attributes]]

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

---

### Adding more elements

```swift
import UIKit

class ViewController: UIViewController {
    
    //MARK: declaring the UI elements...
    var labelHello:UILabel! //"Hello World!" Label...
    var textFieldUser: UITextField! //TextField...
    var buttonClickMe: UIButton! //Button...
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: setting up UI elements...
        setupLabelHello()
        setupTextFieldUser()
        setupButtonClickMe()
        
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
    
    //Defining the TextField attributes...
    func setupTextFieldUser(){
        textFieldUser = UITextField()
        textFieldUser.placeholder = "Put some text"
        textFieldUser.borderStyle = .roundedRect
        textFieldUser.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(textFieldUser)
    }
    
    //Defining the Button attributes...
    func setupButtonClickMe(){
        buttonClickMe = UIButton(type: .system) //You need to set the type when you create a Button. We use default system button...
        buttonClickMe.setTitle("Click Me!", for: .normal)
        buttonClickMe.tintColor = .systemBlue
        buttonClickMe.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonClickMe)
    }
    
    //MARK: Initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate(
            [
                //MARK: constraints for labelHello...
                labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
                labelHello.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                
                //MARK: constraints for textFieldUser...
                textFieldUser.topAnchor.constraint(equalTo: labelHello.bottomAnchor, constant: 16),
                textFieldUser.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                
                //MARK: constraints for buttonClickMe...
                buttonClickMe.topAnchor.constraint(equalTo: textFieldUser.bottomAnchor, constant: 16),
                buttonClickMe.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor)
            ]
        )
    }
    
}
```

---
## Adding button action

Add actions in the `viewDidLoad()` method as this functions as the logical Controller
```swift
override func viewDidLoad() {
    super.viewDidLoad()
    // Do any additional setup after loading the view.
    
    //MARK: setting up UI elements...
    setupLabelHello()
    setupTextFieldUser()
    setupButtonClickMe()
    
    //MARK: adding action...
    buttonClickMe.addTarget(self, 
        action: #selector(onButtonClickMeTapped), 
        for: .touchUpInside
    )
    
    //MARK: initializing the constraints...
    initConstraints()
}
```


---
### Full Code Example

```swift
import UIKit

class ViewController: UIViewController {
    
    //MARK: declaring the UI elements...
    var labelHello:UILabel! //"Hello World!" Label...
    var textFieldUser: UITextField! //TextField...
    var buttonClickMe: UIButton! //Button...
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: setting up UI elements...
        setupLabelHello()
        setupTextFieldUser()
        setupButtonClickMe()
        
        //MARK: adding action...
        buttonClickMe.addTarget(self, 
            action: #selector(onButtonClickMeTapped), 
            for: .touchUpInside
        )
           
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
    
    //Defining the TextField attributes...
    func setupTextFieldUser(){
        textFieldUser = UITextField()
        textFieldUser.placeholder = "Put some text"
        textFieldUser.borderStyle = .roundedRect
        textFieldUser.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(textFieldUser)
    }
    
    //Defining the Button attributes...
    func setupButtonClickMe(){
        buttonClickMe = UIButton(type: .system) //You need to set the type when you create a Button. We use default system button...
        buttonClickMe.setTitle("Click Me!", for: .normal)
        buttonClickMe.tintColor = .systemBlue
        buttonClickMe.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonClickMe)
    }
    
    //MARK: Initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate(
            [
                //MARK: constraints for labelHello...
                labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
                labelHello.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                
                //MARK: constraints for textFieldUser...
                textFieldUser.topAnchor.constraint(equalTo: labelHello.bottomAnchor, constant: 16),
                textFieldUser.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                
                //MARK: constraints for buttonClickMe...
                buttonClickMe.topAnchor.constraint(equalTo: textFieldUser.bottomAnchor, constant: 16),
                buttonClickMe.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor)
            ]
        )
    }
    
    //MARK: buttonClickMe tap action...
    @objc func onButtonClickMeTapped(){
        //print("Button Clicked!!")
        // MARK: fetching the text the user typed...
        let text = textFieldUser.text
        
        //Unwrapping the optional text...
        if let unwrappedText = text{
            //print(unwrappedText)
            
            if(unwrappedText.isEmpty){ //The user didn't put anything...
                showErrorAlert()
            } else{ //The user put some texts...
                showAlertText(text: unwrappedText)
            }
        }
    }
    
    //MARK: Alert controller logics...
    func showErrorAlert(){
        let alert = UIAlertController(title: "Error!", message: "Text Field must not be empty!", preferredStyle: .alert)
        
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        
        self.present(alert, animated: true)
    }
    
    func showAlertText(text:String){
        let alert = UIAlertController(title: "You said:", message: "\(text)", preferredStyle: .alert)
        
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        
        self.present(alert, animated: true)
    }
    
}
```