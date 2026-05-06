

Solutions and explanations for OOD practice exam questions.

---

## Question 1 — testTwo() Purpose (20 pts)

### **Purpose of Test**

> This test checks whether the same amount of change ($2.50) is dispensed correctly from two different registers with different denominations. It ensures that the register produces the correct total value in change regardless of which coins or bills are available.

### Gets Full Credit Because:

- Focuses on correctness of **value**, not coin combinations
- Ensures functional consistency between different registers
- Does **not** explain line-by-line logic

---

## Question 2 — testThree() Bug & Fix (20 pts)

### a) **What is being tested**

> This test checks whether makeChange() correctly returns the expected change only after the register contains enough money, and fails otherwise.

### b) **Why it fails**

> makeChange() removes coins from the register even if the withdrawal fails, corrupting the internal state.

### c) **Correct Fix: Simulate First, Then Commit**

```java
@Override
public Map<Integer, Integer> makeChange(int dollars, int cents) throws InsufficientCashException {
    int[] denom = {1000, 500, 100, 25, 10, 5, 1};
    Map<Integer, Integer> tempBox = new TreeMap<>(moneyBox);
    Map<Integer, Integer> result = new TreeMap<>();
    int total = dollars * 100 + cents;

    for (int d : denom) {
        int available = tempBox.getOrDefault(d, 0);
        int num = Math.min(available, total / d);
        result.put(d, num);
        tempBox.put(d, available - num);
        total -= d * num;
    }

    if (total > 0) throw new InsufficientCashException("Cannot dispense exact change.");

    moneyBox = tempBox; // commit only after full success
    log.append(String.format("Withdraw: $%.2f\n", dollars + cents / 100.0));
    return result;
}
```

**Key Principle:** Never modify state until you're certain the operation will succeed. Use temporary copies to simulate changes.

**See also:** [[Encapsulation and Invariants]]

---

## Question 3 — Audit Log Bug (25 pts)

### a) **Bug**

> getContents() returns a reference to the internal moneyBox, allowing external code to modify it without using deposit methods, resulting in log-audit mismatches.

**This violates encapsulation** — internal state should never be directly accessible.

### b) **Test That Exposes the Bug**

```java
@Test
public void testAuditBypassBug() {
    ICashRegister reg = new SimpleRegister();
    reg.addDimes(5); // Legit $0.50 deposit

    // External tampering
    Map<Integer, Integer> contents = reg.getContents();
    contents.put(500, 1); // Fake deposit: $5

    try {
        Map<Integer, Integer> change = reg.makeChange(5, 0); // Improper withdrawal
        fail("Should not allow withdrawal of undeclared funds.");
    } catch (InsufficientCashException e) {
        // Expected
    }
}
```

### **Fix:**

```java
public Map<Integer, Integer> getContents() {
    return new TreeMap<>(moneyBox); // Return defensive copy
}
```

**Key Principle:** Always return defensive copies of mutable internal state.

**See also:** [[Encapsulation and Invariants]]

---

## Question 4 — IBetterCashRegister Interface (15 pts)

### **Flexible, Currency-Agnostic Interface**

```java
import java.util.List;
import java.util.Map;

public interface IBetterCashRegister {
    void initializeDenominations(List<Integer> denominations);
    void deposit(int denomination, int quantity);
    Map<Integer, Integer> makeChange(int amount);
    Map<Integer, Integer> getContents();
    String getAuditLog();
}
```

### Design Highlights:

- Accepts arbitrary denominations
- Supports any currency (pence, rupees, yen)
- Omits hardcoded methods like `addDimes()`
- **Extensible**: Can add new denominations without changing interface

**Design Principle:** **Open/Closed Principle** — open for extension, closed for modification.

**See also:** [[Model, View, and Controller#SOLID]]

---

## Question 5 — RegPiggyBank (15 pts)

### **Full Implementation**

```java
import bank.IPiggyBank;
import register.SimpleRegister;
import java.util.Map;

public class RegPiggyBank implements IPiggyBank {
    private final SimpleRegister reg;

    public RegPiggyBank() {
        reg = new SimpleRegister();
    }

    @Override
    public void deposit(int coinValue) {
        switch (coinValue) {
            case 1 -> reg.addPennies(1);
            case 5 -> reg.addNickels(1);
            case 10 -> reg.addDimes(1);
            case 25 -> reg.addQuarters(1);
            default -> throw new IllegalArgumentException("Unsupported coin: " + coinValue);
        }
    }

    @Override
    public int count(int coinValue) {
        return reg.getContents().getOrDefault(coinValue, 0);
    }

    @Override
    public boolean canBuy(int dollars, int cents) {
        int needed = dollars * 100 + cents;
        int total = 0;
        for (Map.Entry<Integer, Integer> entry : reg.getContents().entrySet()) {
            int denom = entry.getKey();
            int count = entry.getValue();
            if (denom <= 25) total += denom * count;
        }
        return total >= needed;
    }
}
```

### Grading Checklist:

- Implements `IPiggyBank`
- Uses `SimpleRegister` instance
- One coin per deposit
- Handles only coins (≤ 25¢)
- Proper logic in all methods

**Design Principle:** **Adapter Pattern** — adapts `SimpleRegister` to work with `IPiggyBank` interface.

**See also:** [[Design Patterns Examples#Adapter Pattern]]

---

## Key Concepts Demonstrated

| Question | OOD Concept |
|----------|-------------|
| Q1 | Test design, functional correctness |
| Q2 | **Encapsulation**, state consistency, atomic operations |
| Q3 | **Defensive copying**, encapsulation violation |
| Q4 | **Open/Closed Principle**, interface design |
| Q5 | **Adapter Pattern**, interface implementation |

---

## Related Notes

- [[Encapsulation and Invariants]] - State protection principles
- [[Model, View, and Controller#SOLID]] - SOLID principles
- [[Design Patterns Examples#Adapter Pattern]] - Adapter pattern
- [[Java Safari#Exceptions]] - Exception handling
- [[Simple Code Examples#Map<K, V>]] - Map usage patterns