

> **Note:** Not to be confused with push notifications

Central dispatcher of data to broadcast from one part of the app to another. Can be any swift class.

## Overview

There are two screens, Screen 2 takes text input from the user, and it has to send the text to Screen 1 and display the text in a Label. It can be handled using a **NotificationCenter**:

- Its a mediator, a class can post dat to or observe dat from the Notification Center
- Screen 2 can post the text, Screen 1 can observe the text
- Screen 2 posts a new text, NotificationCenter detects and update of data has been made, and alerts the observers of the data
- Screen 1, as an observer of the text, receives the notification that the text has been updated
- Screen 1 reacts to the notification and updates it's local UI elements accordingly, such as updating it's Label with the updated text

---

## Adding an Observer

In this example, we will be sending data from the second screen to the first screen. Thus, observe Notification Center for notifications sent from the second screen.

### Initialize the Notification Center

In the first notification center:

```swift
import UIKit

class ViewController: UIViewController {
	let firstScreen = FirstScreenView()
	
	let notificatoinCenter = NotificationCenter.default
}
```

### Setting up an Observer

Use the method: `notificationCenter.addObserver(observer: Any, selector: Selector, name: NSNotificaiton.Name?, object: Any?`

```swift
class ViewController: UIViewController {
	override func viewDidLoad() {
		notificaitonCenter.addObserver(
			self,
			selector: #selector(notificationReceivedForTextChanged(notification:)),
			name: Notification.Name("textFromSecondScreen"),
			object: nil
		)
	}
	
	@objc func notificaitonReceievedForTextChanged(notificaiton: Notificaiton) {
		firstScreen.labelReceivedText.text = (notificaiton.object as! String)
	}
}
```

**What we do:**
- Set the observer to self (Screen is observing for a notification)
- Add a selector method to handle the data we get back as part of the notification, we define a method to handle it, just setting `labelReceievedText`'s text to the received object
- Give an identifier to the notification with the name, so you can find it when you send out the notification
- Object parameter is `nil` to signal that we don't send an object

---

## Posting Data

Again, init the notification center:

```swift
import UIKit

class SecondScreenViewController: UIViewController {
	let notificationCenter = NotificationCenter.default
}
```

### Post Data to Notification Center

```swift
import UIKit

class SecondScreenViewController: UIViewController {
	override func viewDidLoad() {
		super.viewDidLoad()
		secondScreen.buttonSendBack.addTarget(self, action: #selector(onButtonSendBackTapped), for: .touchUpInside)
	}
	
	@objc func onButtonSendBackTapped() {
		if let text = secondScreen.textFieldSendBack.text {
			notiicationCenter.post(
				name: Notification.Name("textFromSecondScreen"),
				object: text
			)
			navigationController?.popViewController(animated: true)
		} else {
			// Alert for invalid input
		}
	}
}
```

**Parameters:**
- `name`: The same identifier to observe
- `object`: what we are sending to the center

---

## Organizing

- Notification center is used frequently, especially to fetch data from internet and wait for data to update
- It's common for tens of observers to be in a single app
- We should keep names as static variables in a separate class to make it easier for us

```swift
import Foundation

extension Notificaiton.Name {
	static let textFromOtherScreen = Notification.Name("textFromOtherScreen")
}
```

With the extension, we can use `.textFromSecondScreen` instead of `Notification.Name("textFromSecondScreen")`

```folder-overview
id: bfb5cfc4-ef39-436d-a3ff-56547a030e3f
folderPath: Code/iOS/Creating Applications/Notification Center
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
<span class="fv-link-list-start" id="bfb5cfc4-ef39-436d-a3ff-56547a030e3f"></span>
<span class="fv-link-list-end" id="bfb5cfc4-ef39-436d-a3ff-56547a030e3f"></span>
