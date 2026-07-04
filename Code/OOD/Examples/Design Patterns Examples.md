

Quick reference examples for common OOD design patterns.

---

## Encapsulation & Class Invariants

> Prevent invalid object state, protect class internals.

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

**See also:** [[Encapsulation and Invariants]]

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

**See also:** [[Code/OOD/Intro#Key Concept Comparisons]]

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

**See also:** [[Command Design Pattern]]

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

## Related Notes

- [[Command Design Pattern]] - Full command pattern implementation
- [[Code/OOD/Intro]] - Core OOD principles
- [[Model, View, and Controller#Builder Class]] - Builder pattern
- [[Java Safari]] - Java language features used in patterns