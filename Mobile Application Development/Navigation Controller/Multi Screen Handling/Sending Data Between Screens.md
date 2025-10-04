using the variable `meessageFromFirstScreen` in the second's screens ViewController we can access that from the First screen.

In ViewController.swift, we can add in `onButtonSendTapped()`

```swift
@objc func onButtonSendTapped(){
	//initializing a new screen with ShowViewController...
	var showViewController = ShowViewController()
	
	//set the message to ShowViewController's
	// messageFromFirstScreen 
	if let unwrappedMessage = textFieldMessage.text{
		if !unwrappedMessage.isEmpty { 
		// checking if the user has message
			//Sending data...
			showViewController.messageFromFirstScreen = 
				unwrappedMessage
			//push the screen to Stack...
	navigationController?.pushViewController(showViewController,	
				animated: true)
		} else {
			//Alert the user to put message....
		}
		
	}
}
```

- You have **two screens** (two `UIViewController` subclasses).
    
    - `ViewController` (first screen).
        
    - `ShowViewController` (second screen).
        
- The **first screen** creates an instance of the second screen (`ShowViewController()`).
    
- The second screen defines a property, for example:
    
    `var messageFromFirstScreen: String?`
    
    That’s just a normal variable in the second VC, available to be set from the outside.
    
- Before pushing the second screen onto the **navigation stack**, the first screen sets that property:
    
    `showViewController.messageFromFirstScreen = unwrappedMessage`
    
- When the second screen is shown, its `messageFromFirstScreen` now holds the value passed in.