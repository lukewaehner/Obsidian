**JavaScript Object Notation** - The gold standard for representing structured data in text format.

---

## Overview

JSON follows JavaScript object syntax and is the most popular standard for text-based data in Web APIs. Almost all APIs you work with will be structured with JSON.

---

## Structure

JSON is a string that resembles JavaScript object syntax. You can put all basic data types inside a JSON string.

### Basic Object

JSON strings are **Key-Value pairs**:

```json
{
    "name": "Alex F",
    "email": "Alex@email.com",
    "phone": 1234567890
}
```

### Nested Objects

You can represent complex data like an **Address**:

```json
{
    "line1": "100 Winter Street",
    "line2": "Apt 202",
    "city": "Boston",
    "state": "MA",
    "zip": 02115
}
```

### Hierarchical Structure

Parent objects can hold child objects:

```json
{
    "name": "Alex F",
    "email": "alex@email.com",
    "phone": 1234567890,
    "address": {
        "line1": "100 Winter Street",
        "line2": "Apt 202",
        "city": "Boston",
        "state": "MA",
        "zip": 02115
    }
}
```

### Arrays of Objects

Use `[]` (standard array notation) to pass multiple objects:

```json
{
    "contacts": [
        {
            "name": "David Tu"
        },
        {
            "name": "Alice Smith"
        }
    ]
}
```

---

## Representing JSON in Swift

### Mapping to Structs

Translate JSON structure directly into Swift structs:

**JSON:**
```json
{
    "contacts": [
        {
            "name": "David Tu"
        },
        {
            "name": "Alice Smith"
        }
    ]
}
```

**Swift:**
```swift
struct ContactName {
    let name: String
}

struct ContactNames {
    let contacts: [ContactName]
}
```

### Making Structs Codable

Structs are **not encodable/decodable by default**. Adopt the `Codable` protocol:

```swift
struct ContactName: Codable {
    let name: String
}

struct ContactNames: Codable {
    let contacts: [ContactName]
}
```

---

## Parsing JSON

Use `JSONDecoder()` to decode received JSON data:

```swift
let decoder = JSONDecoder()

do {
    // Decode the data
    let receivedData = try decoder
        .decode(ContactNames.self, from: data)
    
    // Loop through the returned object
    for item in receivedData.contacts {
        self.contactNames.append(item.name)
    }
}
```

**Key steps:**
1. Create a `JSONDecoder()` instance
2. Call `.decode(YourStruct.self, from: data)` 
3. Process the decoded Swift objects