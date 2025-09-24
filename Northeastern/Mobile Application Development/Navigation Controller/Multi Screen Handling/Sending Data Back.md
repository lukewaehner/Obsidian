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