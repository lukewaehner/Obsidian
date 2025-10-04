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

```swift
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
```