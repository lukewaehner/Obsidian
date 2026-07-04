# Design Pattern Examples

Class: [[OOD]]
Related: [[Examples Index]]

This note contains simplified examples of various design patterns covered in OOD.

---

## Encapsulation & Class Invariants

### Water Tank Example

```java
public class WaterTank {
  private final int capacity;
  private int currentLevel;

  public WaterTank(int capacity) {
    if (capacity <= 0) throw new IllegalArgumentException("Must be > 0");
    this.capacity = capacity;
    this.currentLevel = capacity; // full tank
  }

  public void useWater(int amount) {
    if (amount < 0 || amount > currentLevel)
      throw new IllegalArgumentException("Invalid amount");
    currentLevel -= amount;
  }

  public int getLevel() {
    return currentLevel;
  }
}
```

**Why:** Enforces class rules (like "you can't draw more water than available") and keeps the tank always valid.

**Related:** [[Encapsulation and Invariants]]

---

## Code Reuse: Inheritance vs Composition

### Bad: Inheritance causing fragile overrides

```java
public class CoffeeMaker {
  public void brew() {
    System.out.println("Brewing basic coffee...");
  }
}

public class CountingCoffeeMaker extends CoffeeMaker {
  private int count = 0;

  @Override
  public void brew() {
    super.brew();
    count++;
  }

  public int getCount() {
    return count;
  }
}
```

If `CoffeeMaker.brew()` internally changes logic, `CountingCoffeeMaker` breaks.

### Good: Composition with delegation

```java
public class CountingCoffeeMaker {
  private final CoffeeMaker base;
  private int count = 0;

  public CountingCoffeeMaker(CoffeeMaker base) {
    this.base = base;
  }

  public void brew() {
    base.brew();
    count++;
  }

  public int getCount() {
    return count;
  }
}
```

**Why:** Keeps `CountingCoffeeMaker` safe from internal changes to `CoffeeMaker`. Loose coupling = safer reuse.

**Related:** [[Code/OOD/Intro#Key Concept Comparisons]]

---

## Adapter Pattern

> Make incompatible interfaces work together.

### Legacy interface:

```java
public interface LegacyHeater {
  void turnOn();
  void turnOff();
}
```

### New expected interface:

```java
public interface Heater {
  void heat();
}
```

### Adapter:

```java
public class HeaterAdapter implements Heater {
  private final LegacyHeater legacy;

  public HeaterAdapter(LegacyHeater legacy) {
    this.legacy = legacy;
  }

  @Override
  public void heat() {
    legacy.turnOn();
  }
}
```

**Why:** Allows new CoffeeMaker logic expecting `Heater` to use old `LegacyHeater` without changes.

---

## Strategy Pattern

> Swap behavior dynamically, e.g., how to grind beans.

```java
public interface GrindStrategy {
  void grind();
}

public class FineGrind implements GrindStrategy {
  public void grind() {
    System.out.println("Grinding beans finely");
  }
}

public class CoarseGrind implements GrindStrategy {
  public void grind() {
    System.out.println("Grinding beans coarsely");
  }
}

public class CoffeeMaker {
  private final GrindStrategy grindStrategy;

  public CoffeeMaker(GrindStrategy strategy) {
    this.grindStrategy = strategy;
  }

  public void makeCoffee() {
    grindStrategy.grind();
    System.out.println("Brewing coffee...");
  }
}
```

**Why:** Easily switch strategies: espresso = fine grind, French press = coarse grind.

**Related:** [[Model, View, and Controller#SOLID]]

---

## Command Pattern

> Encapsulate actions (like brewing) as objects.

```java
public interface Command {
  void execute();
}

public class BrewCommand implements Command {
  private final CoffeeMaker maker;

  public BrewCommand(CoffeeMaker maker) {
    this.maker = maker;
  }

  @Override
  public void execute() {
    maker.brew();
  }
}

public class CoffeeController {
  private final List<Command> queue = new ArrayList<>();

  public void addCommand(Command cmd) {
    queue.add(cmd);
  }

  public void run() {
    for (Command cmd : queue) {
      cmd.execute();
    }
  }
}
```

**Why:** Decouple input (UI/buttons/automation) from logic. Supports undo/redo, batching, scripting.

**Related:** [[Command Design Pattern]]

---

## Decorator Pattern

> Add new features (e.g. logging) without modifying original.

```java
public class LoggingCoffeeMaker extends CoffeeMaker {
  private final CoffeeMaker base;

  public LoggingCoffeeMaker(CoffeeMaker base) {
    this.base = base;
  }

  @Override
  public void brew() {
    System.out.println("Starting brew...");
    base.brew();
    System.out.println("Brew complete.");
  }
}
```

**Why:** Adds logging transparently. Can stack multiple decorators like temperature logging, timers, etc.

---

## Builder Pattern

### User Builder Example

```java
public class User {
  private final String name;
  private final int age;

  // Package-private constructor – only builder can access
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

// Usage
User user = new UserBuilder()
               .setName("Alice")
               .setAge(30)
               .build();
```

**Why:** Simplifies object construction with many optional parameters.

**Related:** [[Model, View, and Controller#Builder Class]]

---

## Mock Objects for Testing

### Mock Model Example

```java
public interface IModel {
  void increment();
  int getValue();
}

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

// Test
MockModel mock = new MockModel();
Controller controller = new Controller(mock);

controller.handleIncrement();
controller.displayValue();

System.out.println("Log from mock:\n" + mock.log);
```

**Why:** Verify if the controller called the correct methods without depending on actual logic.

**Related:** [[Controllers and Mocks]]

---

## Enumerations with Behavior

### Size Enum Example

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

**Why:** Enums can hold data and methods, not just constants.

**Related:** [[Java Safari#Enumerations]]