
---
# Creating Apps
1. Open Xcode
2. Create new Xcode Project
3. Select iOS from the top template
4. Select App
5. Set a project name
6. Storyboard as the Interface
7. Set Swift as language
8. Choose where to save project
9. Select iPhone simulator
10. Play opens the emulator

---
## Xcode panes

---
### Left Pane

On the left side, is the file structure
There will be three swift files, **AppDelegate, SceneDelegate, ViewController**

**AppDelegate** manages the application lifecycle, while populating screens, on screen change, etc

**SceneDelegate** manages lifecycle of the scenes while the app is running, like when the window is populated, the scene is sent to the background, comes back from background, etc

**ViewController** holds the MVC structure of the empty screen we see. Each screen is needs a ViewController. 90% of time is spent here

Two Storyboard files are seen as well. These are design boards like prototype builders.
Do **NOT** touch LaunchScene file if you have to

The Main storyboard is where you can create the frontend of your app by dragging and dropping UI elements on the screen, like a prototyper. Storyboards are XML files that define the screen's ui elements, positional constraints, and user interactions

---
### Middle Pane

The work pane, where you write code, design, change settings and preferences, debug, etc.

---
### Right Pane
Configuration and attributes explorer pane, if you click on the Main Storyboard and click the screen preview, the right pane will display the attribute of the screen view

---
# UI Elements

---
### UI Label

`UILabel`is a text pane. To add it use the object library with `Cmd + Shift + L`.

![[IMG-20250915001921570.png]]

**Safe Area** exists inside the view, where there are no interruptions or obstacles like the camera cut.

---
### UITextField

Used to grab user inputs from the keyboard
- The **placeholder** attribute allows the hint text / default text to appear in the TextField

---
### UIButton
Handling the clicks of buttons can be controlled through the ViewController code
Go to menu: `Editor -> Assistant`

This opens a pane with the backend code.
Hold **'control' key** and click on the TextField without releasing.
Drag the mouse pointer to the right to the code file.

Place it inside the ViewController class.
This creates a variable `@IBOutlet var textFieldUser: UITextField!`
`@IBOutlet` means that it's an outlet from the Interface Builder

You can do the same with the button.

In the `viewDidLoad()`method, we can write the logic. This method auto runs upon load finish.

`addTarget()` function has three parameters: target, action, and for.
- target means where we would listen for an event to happen, this case it it self (the current view)
- action means which method to call if an event happens. It asks for a Selector type function.

```swift

class viewController: UIViewController {

	@IBOutlet var buttonClickMe: UIButton!
	@IBOUTLET var textFieldUser: UITextField!
	override func viewDidLoad() {
		super.viewDidLoad()
		buttonClickMe.addTarget(self, action: #selector(onButtonClickMeTapped), for: .touchUpInside)
	}
}
```

---
### UIAlertController

---

## Constraints and Alignments

The tools exist on the bottom right corner of the middle pane.
From left to rights its: **Alignment, Add Constraints, Reset Constraints**


---
