In rotating the screen, we might lose elements. We should make it scrollable.

## Setting Up UIScrollView

```swift
class ScrollScreenView: UIView {
	var contentWrapper: UIScrollView!
	
	override init(frame: CGRect) {
		super.init(frame: frame)
		setupContentWrapper()
		initConstraints()
	}
	
	func setupContentWrapper() {
		contentWrapper = UIScrollView()
		contentWrapper.translatesAutoresizingMaskIntoConstraints = false
		self.addSubview(contentWrapper)
	}
	
	func initConstraints() {
		NSLayoutConstraint.activate([
			contentWrapper.topAnchor.constraint(equalTo:
				self.safeAreaLayoutGuide.topAnchor),
			contentWrapper.leadingAnchor.constraint(equalTo:
				self.safeAreaLayoutGuide.leadingAnchor),
			contentWrapper.widthAnchor.constraint(equalTo:
				self.safeAreaLayoutGuide.widthAnchor),
			contentWrapper.heightAnchor.constraint(equalTo:
				self.safeAreaLayoutGuide.heightAnchor),
		])
	}
}
```

## Setting Up the Controller

```swift
class ViewController: UIViewController {
	let homeScreen = ScrollScreenView()
	
	override func loadView() {
		view = homeScreen
	}
	
	override func viewDidLoad() {
		super.viewDidLoad()
	}
}
```

Now you can scroll within this container (the whole screen is the container).