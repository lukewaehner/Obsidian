Modules / Libraries are important in any language.

**Link:** [Cocoapods](https://cocoapods.org)

They are general purpose modules, can cause performance issues.

> **Important:** Only use the common and reputable modules

## Common Modules

| Module       | Reason                        |
| ------------ | ----------------------------- |
| AlamoFire    | HTTP networking               |
| Moya         | abstraction layer             |
| Siesta       | stateful API handling         |
| SDWebImage   | async image loading + caching |
| Realm        | mobile object database        |
| SQLite.swift | wrapper over SQLLite          |
| SnapKit      | Auto Layout DSL               |
| SwiftLint    | style enforcer                |

## Recommended Stack

**Alamofire + SwiftyJSON + Kingfisher + SnapKit + IQKeyboardManagerSwift + SwiftLint**

## Installation

```bash
sudo gem install cocooapods
```

---

## Adding a Pod to a project

1. CD to project directory
2. run `pod init`
	- **Podfile** is created
3. Text edit the Podfile
4. (Likely) write `pod <ModuleName>` in the file
5. Run `pod install`
6. Close the project
7. Open the **.xcworkspace** file for the project
8. 