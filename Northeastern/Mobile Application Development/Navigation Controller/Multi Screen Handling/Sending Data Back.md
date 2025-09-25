**Goal**: User selects a mood on the second screen → send it back → first screen updates an image.

---

### Step 1: Setup Data

`let moods = ["Happy", "Meh", "Sad"] var selectedMood = "Happy"`

---

### Step 2: Conform to PickerView

Two options:

```swift
// Inline 
class ShowViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource { ... }  
// Or extension 
extension ShowViewController: UIPickerViewDelegate, UIPickerViewDataSource { ... }`
```

`extensions` allows for more separate, very nice.

---
### Step 3: Implement Delegate Methods

```swift
func numberOfComponents(in pickerView: UIPickerView) -> Int { 1 }  
func pickerView(_ pickerView: UIPickerView,                 
				numberOfRowsInComponent component: Int) -> Int {
	moods.count 
}  
func pickerView(_ pickerView: UIPickerView,
				titleForRow row: Int,
				forComponent component: Int) -> String? {
	selectedMood = moods[row]
	return moods[row] }
```

**`numberOfComponents()`**  
  Defines how many columns the picker has.  
  - Our `moodPicker` has only **1 column**, so we return `1`.

- **`pickerView()` Methods (Protocol Overrides):**
  1. **`numberOfRowsInComponent`**  
     - Returns number of rows in the component.  
     - We use `moods.count` since rows = number of moods.
  
  2. **`titleForRow`**  
     - Returns the text for each row.  
     - We show `moods[row]`.  
     - Also updates `selectedMood` with the chosen mood.

---

### Step 4: Connect Picker

```swift
moodPicker.delegate = self 
moodPicker.dataSource = self
```
---

### Quick Reference

- `numberOfComponents` → # of columns (1 here).
    
- `numberOfRowsInComponent` → rows per column (`moods.count`).
    
- `titleForRow` → text for each row, also updates `selectedMood`.

---
## Delegate to ViewController

In ShowViewController.swift we can enable to action.

```swift
@objc func onSendMoodButtonTapped() {
	
}
```

**Write later**

---
First, we want to send the mood back to the first screen, we need to ask
- ViewController to receive the data, and do tasks afterward. 
- We delegate tasks to ViewController after we clock on `buttonSendMood`.
- Create a variable `delegate` in ShowViewController.swift to hold the reference to the instance of ViewController

```swift
class ShowViewController: UIViewController {
	var messageFromFirstScreen:String? = "No message received!"
	var delegate: ViewController!
}
```

Now back in ViewController class we can ensure `delegate` variable value is set before pushing `ShowViewController` into [[Navigation Controller]]. In doing that, we ensure the instance of `ShowViewController` can have access to `ViewController`. 

---

```swift
class ViewController: UIViewController {

	@objc func onButtonSendTapped() {
		var showViewController = showViewController()
		
		if let unwrappedMessage = textFieldMessage.text {
			if !unwrappedMessage.isEmpty {
				showViewController.messageFromFirstScreen = unwrappedMessage
			}
			// Passing through itself to the next object for ref
			showViewController.delegate = self
		}
		// send to stack
		navigationController?.pushViewController(showViewController, animated: true)
	}
}
```

So now we need to write what happens upon return from ShowViewController:

```swift
class ViewController: UIViewController {
	func delegateButtonSendMood(mood: String) {
		print("The user is \(mood)")
	}
}
```

Back in `ShowViewController`, we can call this `deleegateButtonSendMood(mood:String)` method when the user taps on `onSendMoodButton`:

```swift
class ShowViewController: UIViewController {
	var delegate: ViewController!
	
	@objc func onSendMoodButtonTapped() {
		delegate.delegateButtonSendMood(mood: selectedMood)
	}
}
```