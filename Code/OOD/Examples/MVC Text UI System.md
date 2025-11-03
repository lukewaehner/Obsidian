

---

## 📦 Overall Architecture

The system follows the **Model-View-Controller (MVC)** architecture, split into:

- `Model.java` – core logic/state
- `TextView.java` – user interface (console-based)
- `TextController.java` – coordinator between model and view
- `MVCExampleTextUI.java` – app runner

Interface layers:

- `IModel`, `IView`, `IController` ensure loose coupling and easy testing

---

## 🔷 `IModel.java` & `Model.java`

### **Role:**

Defines and implements the **domain logic and application state**.

### 🔍 Design Features:

- `IModel` declares operations like `getMessage()` and `setMessage()`
- `Model` encapsulates state (`String message`) and implements those behaviors

### ✅ OOD Highlights:

- **Encapsulation**: Internal state is private and accessed via controlled methods.
- **Interface segregation**: Clean abstraction for model operations.
- **Single Responsibility**: Only handles data, not display or input.

---

## 🔷 `IView.java` & `TextView.java`

### **Role:**

Handles **output responsibilities** in a text-based interface.

### 🔍 Design Features:

- `IView` defines `renderMessage(String message)`
- `TextView` implements rendering by printing to standard output

### ✅ OOD Highlights:

- **View abstraction**: View is unaware of the model or controller.
- **Loose coupling**: Changes to how data is shown don't affect logic.
- **Reusable for testing**: Easy to replace `TextView` with a mock or logging view.

---

## 🔷 `IController.java` & `TextController.java`

### **Role:**

Mediates between model and view, handling user input and coordinating behavior.

### 🔍 Design Features:

- `IController` defines a `go()` method (entry point)
- `TextController` takes `IModel`, `IView`, and `Readable input` in its constructor
- Uses a loop to read commands and update the model/view accordingly

### ✅ OOD Highlights:

- **Dependency Injection**: Controller takes model/view at construction, enabling test mocks.
- **Command parsing**: Uses string-based command dispatch — extensible via `if`/`switch`.
- **High cohesion**: Controller focuses only on interpreting input and coordinating updates.

---

## 🔷 `MVCExampleTextUI.java`

### **Role:**

**Main class** that sets up the model, view, and controller, then starts the app.

### ✅ OOD Highlights:

- Demonstrates **composition root** — ties all dependencies together.
- Clearly shows the MVC separation in action.

---

# 🧠 Final Design Evaluation

| Principle | Implementation |
| --- | --- |
| **Encapsulation** | Model manages state privately |
| **Abstraction** | Interfaces (`IModel`, `IView`, `IController`) decouple logic |
| **Loose Coupling** | Each component interacts only via interfaces |
| **Single Responsibility** | Model (data), View (output), Controller (input coordination) |
| **Testability** | Any component can be mocked/replaced |
| **Reusability** | View/controller could be reused in GUI or web-based variants |

---

## Related Concepts

- [[Model, View, and Controller]] - MVC architecture principles
- [[Controllers and Mocks]] - Controller patterns and testing
- [[Intro#Key Concept Comparisons]] - OO vs Functional design
- [[Simple Code Examples#MBC — Model, Builder, Controller]] - Simpler MBC example