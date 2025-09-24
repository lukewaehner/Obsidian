Add an event action for `buttonSend` to push `ShowViewController` on the Stack. 

In the ViewController.swift file, we can add the following code to the `viewDidLoad()` method.

```swift
override func viewDidLoad() {
	super.viewDidLoad()
	
	setupTextFieldMessage()
	setupButtonSend()
	
	initConstraints()
	
	buttonSend.addTarget(self, action: #selector(onButtonSendTapped), for: .touchUpInside)
}
```

Then we can define the method to delegate button tap events:

```swift
@objc func onButtonSendTapped() {
	var showViewController = ShowViewController()
	
	navigationController?.pushViewController(showViewController, animated: true)
}
```

The background is black here upon page change. iOS gives a ViewController a transparent background on default. The system has no background, so transparent shows as black. We can just set the background color to white with

```swift
override func viewDidLoad() {
	super.viewDidLoad()
	
	view.backgroundColor = .white
	
	setupLabelMessage()
	
	initConstraints()
}
```
