

---

## `SimpleCalc1.java` to `SimpleCalc6.java` (Calculator Implementations)

### **Role:**

Each `SimpleCalcX` class defines a variation of a simple calculator model that performs basic arithmetic. They differ in how they handle input, state, or edge cases.

### Design Principles Observed:

- **Interface-based polymorphism (implied)**: Each implementation follows a shared expected API (e.g., `input()`, `getResult()`).
- **Encapsulation**: Internal state (like the current value or last operation) is stored in private fields.
- **Strategy pattern** potential: These classes could be swapped dynamically if all conform to a shared `Calculator` interface.

### OOD Strengths:

- Encourages separation of behavior per version (good for test-driven iteration).
- Allows mock/test variations (`SimpleCalc4`, `SimpleCalc5`, etc.) without changing the controller.

---

## `CalcController.java`

### **Role:**

Serves as a controller in a typical **MVC architecture** — it receives user input, delegates logic to a calculator model, and drives program behavior.

### Design Features:

- **Dependency injection**: Receives a `SimpleCalcX` instance via constructor.
- **Controller abstraction**: Does not itself perform math — it interprets and routes commands.
- **Encapsulates control flow**: Likely has methods like `run()` that simulate REPL-style interaction.

### OOD Benefits:

- **Loose coupling**: The controller is not tied to a specific calculator implementation.
- **Testability**: The controller can be unit tested using fake calculator objects or mocks.
- **Behavioral encapsulation**: Command parsing, input validation, and loop logic are hidden from the model.

---

## How Mocks Are Supported

### **Test Strategy Overview:**

- Replace `SimpleCalcX` with a "mock" or "spy" implementation that logs method calls.
- Use assertions to verify the controller calls expected methods in sequence with correct arguments.

### OOD Benefits:

- **Mockability**: Interface-driven design makes mocking possible without changing business logic.
- **Isolation testing**: Each component (model/controller) can be tested in isolation using stubs or mocks.

---

# Summary Table: `SimpleCalcX` Roles

| Class | Role or Special Trait |
| --- | --- |
| `SimpleCalc1` | Likely the baseline/basic calculator model |
| `SimpleCalc2` | May introduce error handling or history |
| `SimpleCalc3` | May store sequence of operations |
| `SimpleCalc4-6` | Likely mock-friendly or test-driven variants |

---

# Final Design Evaluation

| OOD Principle | How It's Demonstrated |
| --- | --- |
| **Encapsulation** | State managed privately inside calculator classes |
| **Polymorphism** | Multiple interchangeable calculator implementations |
| **Dependency Injection** | Controller uses a model passed via constructor |
| **Single Responsibility** | Controller vs. calculator clearly separated |
| **Testability via Mocks** | Structure allows mocking for controller tests |
| **Open/Closed Principle** | New calculator types don't require controller edits |

---

## Related Concepts

- [[Controllers and Mocks]] - Controller patterns and testing
- [[Model, View, and Controller]] - MVC architecture
- [[Dumbed Down Code#Example Code Controllers and Mocks]] - Simple mock example