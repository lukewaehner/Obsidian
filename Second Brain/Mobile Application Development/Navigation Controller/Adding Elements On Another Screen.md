
---
- Basic swift writing, just in a separate file after you complete [[Adding Another Page]]. Notice calling `class ShowViewController: UIViewController`
- Also `override func viewDidLoad()`
- Same as just Writing any other UI

```swift
import UIKit

class ShowViewController: UIViewController {
    var messageFromFirstScreen:String? = "No message received!" //First screen can set this variable...
    var labelMessage: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupLabelMessage()
        
        initConstraints()
    }
    

    func setupLabelMessage(){
        labelMessage = UILabel()
        labelMessage.textColor = .systemBlue
        labelMessage.text = messageFromFirstScreen
        labelMessage.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMessage)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            labelMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32)
        ])
    }

}
```

