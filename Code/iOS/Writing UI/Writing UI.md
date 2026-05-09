
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

%% Begin Waypoint %%
- [[Assign Attributes]]
- [[Button Action]]
- [[Creating Variables]]
- [[Code/iOS/Writing UI/Examples]]
- [[Passing Data]]
- [[Setting Constraints]]

%% End Waypoint %%
