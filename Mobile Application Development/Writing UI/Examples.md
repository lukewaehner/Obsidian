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