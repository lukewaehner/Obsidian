
---
Create a separate file
- Click **File $\rightarrow$ New $\rightarrow$ File...**
- Select **Cocoa Touch Class** $\rightarrow$ **Next**
- Enter a class name
- **UIView** as 'Subclass of' selection. Press **Next**
- Press **Create**

---
The name of the Cocoa Touch Class will be the front end code file.

```swift
class FirstScreenView: UIView {
	// Declared elements here
	var label: UILabel!
	
	// MARK: Override the init func
	override init(frame: CGRect) {
		super.init(frame: frame)
		
		self.backgroundColor = .white
		
		setupLabel()
		initConstraints()
	}
	
	func setupLabel() {
		label = UILabel()
		label.text = "Test"
		label.translatesAutoresizingMaskIntoConstraints = false
		self.addSubview(label)
	}
	
	func initConstraints() {
		NSLayoutConstraint.activate([
			label.topAnchor.constraint(equalTo:
				 self.safeAreaLayoutGuide.topAnchor, constant: 32),
			label.centerXAnchor.constraint(equalTo: 
				self.safeAreaLayoutGuide.centerXAnchor)
		])
	}
	
	required init?(coder: NSCoder) {
		fatalError("init(coder): has not been implemented")
	}
}
```

- Declare variables, [[Creating Variables]]
- Initialize elements and constraints: [[Assign Attributes]], [[Setting Constraints]]
- Set a background color

---
## Patch the View class with the ViewController

After you setup a new file, we have to initialize the view in the ViewController. 

`firstScreen` is the instance of the View, `OtherScreenClassName` (whatever is chosen).

Since this will be the first screen, we need to define it when the view is loading, not after it finishes.

```swift
import UIKit

class ViewController: UIViewController {
	// Whatever the class is named
	let firstScreen = OtherScreenClassName()
	
	override func loadView() {
		view = firstScreen
	}
	
	override func viewDidLoad() {
		super.viewDidLoad()
	}
}
```

```folder-overview
id: a9c952f3-0e23-441f-bd48-ffe055fb68da
folderPath: Code/iOS/Separate View From The Controller
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="a9c952f3-0e23-441f-bd48-ffe055fb68da"></span>
<span class="fv-link-list-end" id="a9c952f3-0e23-441f-bd48-ffe055fb68da"></span>
