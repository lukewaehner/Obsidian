**Concept**  
- Manages a single screen in MVC pattern.  
- Holds references to UI elements and user interaction logic.  

**Lifecycle Methods**
- `viewDidLoad()` → called once, after load (setup UI).  
- `viewWillAppear(_:)` → runs each time before appearing.  
- `viewDidAppear(_:)` → after appearing.  
- `viewWillDisappear(_:)` → before leaving.  

**Code Example**
```swift
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        print("Screen loaded")
    }
}
```
Related
- [[UIButton]], [[UILabel]], [[UITextField]]