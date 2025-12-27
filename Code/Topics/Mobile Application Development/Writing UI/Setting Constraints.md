
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