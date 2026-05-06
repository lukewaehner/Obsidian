

Quick reference code snippets demonstrating OOD concepts.

---

## Controllers and Mocks

### `IModel.java` (interface)

```java
public interface IModel {
  void increment();
  int getValue();
}
```

---

### `CounterModel.java` (real implementation)

```java
public class CounterModel implements IModel {
  private int value = 0;

  public void increment() {
    value++;
  }

  public int getValue() {
    return value;
  }
}
```

---

### `Controller.java`

```java
public class Controller {
  private final IModel model;

  public Controller(IModel model) {
    this.model = model;
  }

  public void handleIncrement() {
    model.increment();
  }

  public void displayValue() {
    System.out.println("Value is: " + model.getValue());
  }
}
```

---

### `MockModel.java` (used for testing)

```java
public class MockModel implements IModel {
  public StringBuilder log = new StringBuilder();
  private int value = 42;

  public void increment() {
    log.append("increment called\n");
  }

  public int getValue() {
    log.append("getValue called\n");
    return value;
  }
}
```

---

### `TestController.java` (test with mock)

```java
public class TestController {
  public static void main(String[] args) {
    MockModel mock = new MockModel();
    Controller controller = new Controller(mock);

    controller.handleIncrement();
    controller.displayValue();

    System.out.println("Log from mock:\n" + mock.log);
  }
}
```

---

### Output (for test)

```
Value is: 42
Log from mock:
increment called
getValue called
```

---

### What This Shows:

- The **controller** works only through the interface (`IModel`) — it doesn't care which implementation it gets.
- The **mock model** lets us verify if the controller called the correct methods.
- Great for **unit testing** without depending on actual logic or state changes.

**See also:** [[Controllers and Mocks]]

---

## MBC — Model, Builder, Controller

---

### `User.java` (Model)

```java
public class User {
  private final String name;
  private final int age;

  // Package-private constructor — only builder can access
  User(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public String getName() {
    return name;
  }

  public int getAge() {
    return age;
  }

  public String greet() {
    return "Hello, " + name + "! You are " + age + " years old.";
  }
}
```

---

### `UserBuilder.java` (Builder)

```java
public class UserBuilder {
  private String name = "Anonymous";
  private int age = 0;

  public UserBuilder setName(String name) {
    this.name = name;
    return this;
  }

  public UserBuilder setAge(int age) {
    this.age = age;
    return this;
  }

  public User build() {
    return new User(name, age);
  }
}
```

---

### `UserController.java` (Controller)

```java
public class UserController {
  private final User user;

  public UserController(User user) {
    this.user = user;
  }

  public void greetUser() {
    System.out.println(user.greet());
  }
}
```

---

### `Main.java` (App Entry)

```java
public class Main {
  public static void main(String[] args) {
    // Build the model
    User user = new UserBuilder()
                   .setName("Alice")
                   .setAge(30)
                   .build();

    // Use controller to drive behavior
    UserController controller = new UserController(user);
    controller.greetUser();
  }
}
```

---

### Output:

```
Hello, Alice! You are 30 years old.
```

---

## OOD Highlights:

| Role | Responsibility |
| --- | --- |
| `User` | Encapsulates user data and logic (Model) |
| `UserBuilder` | Constructs and configures a `User` object (Builder) |
| `UserController` | Coordinates behavior using the model (Controller) |

### Benefits:

- **Separation of concerns**: Model is clean, no complex constructors.
- **Builder flexibility**: Easily supports optional values or validation.
- **Controller clarity**: Delegates user interaction cleanly.

**See also:** [[Model, View, and Controller#Builder Class]]

---

## `StringBuilder`

Used for efficient string concatenation (vs `+`, which creates new strings).

### Key Methods:

| Method | Description |
| --- | --- |
| `append(String s)` | Adds to the end |
| `toString()` | Converts to a normal `String` |
| `insert(int, s)` | Inserts at position |
| `delete(int, int)` | Removes a substring |

### Example:

```java
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(" World");
System.out.println(sb.toString()); // Hello World
```

**See also:** [[Java Safari]]

---

## `Map<K, V>`

Stores key—value pairs. Common types: `HashMap`, `TreeMap`.

### Key Methods:

| Method | Description |
| --- | --- |
| `put(K key, V value)` | Add or replace value |
| `get(K key)` | Retrieve value by key |
| `containsKey(K key)` | Checks if key exists |
| `remove(K key)` | Deletes entry by key |
| `keySet()`, `entrySet()` | Useful for looping |

---

## Looping Through a `Map`

### Key Pattern:

```java
Map<String, Integer> map = new HashMap<>();
map.put("apple", 3);
map.put("banana", 5);

for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

---

## Enum with Logic

Enums can hold **data and methods**, not just constants.

### Example:

```java
public enum Size {
  SMALL(1.0), LARGE(1.5);

  private final double multiplier;

  Size(double multiplier) {
    this.multiplier = multiplier;
  }

  public double getMultiplier() {
    return multiplier;
  }
}
```

**See also:** [[Java Safari#Enumerations]], [[Burrito System]]

---

## Object-Oriented Principles in Code

| Concept | Java Technique |
| --- | --- |
| **Abstraction** | Interfaces (e.g., `IModel`) |
| **Encapsulation** | Private fields + public getters |
| **Inheritance** | `extends` (e.g., `CustomBurrito extends Burrito`) |
| **Polymorphism** | Interface-based references (`IModel m = new Model()`) |

**See also:** [[Intro]]

---

## Good Test Helper Tools

### Using a Mock with `StringBuilder`

```java
public class MockModel implements IModel {
  StringBuilder log = new StringBuilder();

  public void increment() {
    log.append("increment called\n");
  }

  public int getValue() {
    log.append("getValue called\n");
    return 42;
  }
}
```

---

## Other Helpful Java Methods & Concepts

| Concept | Use | Example |
| --- | --- | --- |
| `List<T>` (`ArrayList`) | Dynamic arrays | `List<String> l = new ArrayList<>();` |
| `Scanner` | User input | `new Scanner(System.in)` |
| `try-catch` | Error handling | Prevent program from crashing |
| `equals()` vs `==` | Object content vs reference | Always use `.equals()` for Strings |
| `String.format()` | Clean formatted strings | `String.format("%.2f", value)` |
| `Comparator<T>` | Sorting custom logic | `Collections.sort(list, comparator)` |

**See also:** [[Java Safari]]

---

## Patterns to Recognize

| Pattern | Where You Saw It | Benefit |
| --- | --- | --- |
| **Builder** | `UserBuilder`, [[Burrito System]] | Simplifies object construction |
| **Adapter** | [[Design Patterns Examples#Adapter Pattern]] | Bridges incompatible interfaces |
| **Controller** | [[Calculator Controller System]] | Coordinates model + view |
| **Mocking** | `MockModel` | Verifies interaction without real logic |
| **Template** | [[Burrito System#VeggieBurrito]] | Pre-filled object variant |

---

## Related Notes

- [[Controllers and Mocks]] - Controller pattern concepts
- [[Model, View, and Controller]] - MVC architecture
- [[Java Safari]] - Java language features
- [[Design Patterns Examples]] - More pattern examples