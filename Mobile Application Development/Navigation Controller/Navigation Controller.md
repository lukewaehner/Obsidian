
---
# Navigation Controller
#screens #ui #navigation
`Navigation Controller` is a stack data structure. We see the screen from the top of the stack. If we want to move from one screen to another, we can call the `push()` method of the Navigation Controller, pushing **Screen 2** on top of **Screen 1**.

The users sees the Stack from above the Stack, the user will see Screen 2 now. We can then `pop()` Screen 2 from the Stack to move back

---
## Embed Navigation Controller

1. Open the Main storyboard in the project
2. Select ViewController (the preview screen)
3. Click on Embed IN button at the bottom right corner of the middle pane
4. Select navigation controller

> Storyboard tasks are done, all code from now
---
### Right Side Button

```swift
override func viewDidLoad() {
	super.viewDidLoad()
	navigationItem.rightBarButtonItem = UIBarButtonItem (
		barButtonSystemOtem: .add, target: self,
		action: #selector(onRightBarButtonTapped)
		)
}

@objc func onRightBarButtonTapped() {
	// Whatever is needed here
}
```
### Title

```swift
override func viewDidLoad() {
	super.viewDidLoad()
	navigationItem.title = "Title"
}
```
---

[[Adding Another Page]]
[[Adding Elements On Another Screen]]
[[Multi Screen Handling]]

---
