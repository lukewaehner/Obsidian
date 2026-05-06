iOS apps can talk to a server over the Internet. We will use remote APIs, fetch data from a server, and send data to a server using those APIs.

---

## Protocol

We need to pass messages around, so we will use Hyper Text Transfer Protocol - [[HTTP]]

We have a **Client** and a **Server** that send requests back to each other.

We can pass data around with [[JSON]]t

---

## API Configuration

Set the API base URL by creating a file named `APIConfigs.swift` to make it easy to manage:

```swift
import Foundation

class APIConfigs {
    static let baseURL = "<base-endpoint-url>"
}
```

---

## Making GET Requests

### Basic Example

```swift
import UIKit
import Alamofire

class ViewController: UIViewController {
    let mainScreen = MainScreenView()
    
    var holdData = [String]()
    
    // LoadView normal
    
    // Call getAllData() in viewDidLoad
    
    func getAllData() {
        if let url = URL(string: APIConfigs.baseURL + "getall") {
            AF.request(url, method: .get)
                .responseString(completionHandler: { 
                    response in print(response.result)
                })
        }
    }
}
```

Just change the closure `response in print(response.result)` to deal with the data after we receive it.

### Handling Response Codes

We need to handle different response codes as well:

```swift
func getAllData() {
    if let url = URL(string: APIConfigs.baseURL + "getall") {
        AF.request(url, method: .get)
            .responseString(completionHandler: { response in
                let status = response.response?.statusCode
                
                switch response.result {
                    case .success(let data):
                        if let uwStatusCode = status {
                            switch uwStatusCode {
                                case 200...299:
                                    var dataExtracted = 
                                        data.components(separatedBy: "\n")
                                    self.holdData = dataExtracted
                                    print(self.holdData)
                                    break
                                case 400...499:
                                    print(data)
                                    break
                                default:
                                    print(data)
                                    break
                            }
                        }
                    case .failure(let error):
                        print(error)
                        break
                }
            })
    }
}
```

---

## Enabling Unencrypted HTTP

See [[App Transport Security]] for instructions on enabling unencrypted HTTP in your app.

---

## Making POST Requests

### General Pattern

1. Make a struct to package the data you want to send
2. Pull the data from input fields into the struct
3. Pass struct through body of request
4. Activate with function call from button or whatever trigger

### Example

```swift
func addANewContact(package: Package) {
    if let url = URL(string: APIConfigs.baseURL + "add") {
        
        AF.request(url, method: .post, parameters:
                    [
                        "field1": package.field1,
                        "field2": package.field2,
                    ])
            .responseString(completionHandler: { response in
                let status = response.response?.statusCode
                
                switch response.result {
                    case .success(let data):
                        if let uwStatusCode = status {
                            switch uwStatusCode {
                                case 200...299:
                                    self.getAllData()
                                    // Clear the text fields / etc
                                    self.clearAddViewFields()
                                    break
                                case 400...499:
                                    print(data)
                                    break
                                default:
                                    print(data)
                                    break
                            }
                        }
                        break
                    case .failure(let error):
                        print(error)
                        break
                }
            })
    } else {
        // Alert that the URL is invalid
    }
}
```

---

## Fetching Specific Data with Table View

### Setup Table View Delegate

```swift
extension ViewController: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView,
                   didSelectRowAt indexPath: IndexPath) {
        getDataDetails(dataId: self.dataArray[indexPath.row])
    }
}
```

### Define the Details Fetching Function

```swift
func getDataDetails(dataId: String) {
    let parameters = ["dataId": dataId]
    
    if let url = URL(string: APIConfigs.baseURL + "details") {
        AF.request(url, method: .get,
                   parameters: ["dataId": dataId],
                   encoding: URLEncoding.queryString)
            .responseString(completionHandler: { response in 
                // Handle status codes and information delegation here
            })
    }
}
```