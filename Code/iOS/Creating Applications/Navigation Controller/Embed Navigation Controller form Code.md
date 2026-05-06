If we embed the Navigation Controller from code, we can change the first screens `ViewController` to have a different name.

We also will be changing the name of the class

Example:

If we change the name of the first screen view controller to `firstScreenViewController`

All we have to do is open `SceneDelegate.swift`

and update `func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions)`

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
	options connectionOptions: UIScene.ConnectionOptions) {
	
	gurad let windowScene = (scene as? UIWindowScene) else { return }
	
	let rootViewController = FirstScreenViewController()
	
	let navigationController = UINavigationController(
		rootViewController: rootViewController
	)
	
	window = UIWindow(windowScene: windowScene)
	window?.rootViewController = navigationController
	window?.makeKeyAndVisible()
}
```

Then, delete Main.storyboard
1. Delete the storyboard file from explorer
2. Open project's Info.plist
	1. Select project in the Navigator
	2. Select app target
	3. Go to info tab
	4. Expand Application Scene Manifest
	5. Expand Scene Configuration
	6. Expand Application Session Role
	7. Expand Item 0
	8. Delete the row: Storyboard Name (value: Main)
	9. Find Main storyboard file base name or Main interface. Delete the value (set to empty)
		1. Target -> General -> Info