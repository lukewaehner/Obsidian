
---
### Left Pane

On the left side, is the file structure
There will be three swift files, **AppDelegate, SceneDelegate, ViewController**

[[AppDelegate]] manages the application lifecycle, while populating screens, on screen change, etc

[[SceneDelegate]] manages lifecycle of the scenes while the app is running, like when the window is populated, the scene is sent to the background, comes back from background, etc

[[ViewController]] holds the MVC structure of the empty screen we see. Each screen is needs a ViewController. 90% of time is spent here

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
