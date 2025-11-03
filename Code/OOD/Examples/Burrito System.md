

---

## 📷 `Burrito.java` (Interface)

### 📌 Purpose:

Defines a **contract** for all burrito objects. It abstracts the structure and operations of a burrito, without imposing implementation details.

### ✅ Key OOD Concepts:

- **Interface segregation**: Only exposes methods relevant to burrito behaviors.
- **Polymorphism**: Allows consumers to work with any `Burrito` implementation (e.g. `CustomBurrito`, `VeggieBurrito`) interchangeably.
- **Abstraction**: Users interact with burritos via meaningful operations like `addProtein`, not internal fields.

### 🔎 Why it's well-designed:

- Encourages **loose coupling** between logic (e.g., ordering system) and specific burrito types.
- Supports multiple variations without changing client code.

---

## 📷 `CustomBurrito.java`

### 📌 Purpose:

Implements `Burrito` for user-defined, flexible burritos with variable ingredients and sizes.

### ✅ Key OOD Concepts:

- **Encapsulation**: Uses private `Map<Protein, PortionSize>` and `Map<Topping, PortionSize>` to hide internal structure.
- **High cohesion**: All fields and methods focus strictly on defining, configuring, and computing burrito contents and cost.
- **Open/Closed Principle (OCP)**: Can support new proteins/toppings via `enum` updates, without modifying this class.
- **Data-driven composition**: Rather than subclassing for every burrito type, it builds burritos through ingredient data.

### 💡 Design Highlights:

- **Cost calculation logic** is entirely data-driven: each ingredient knows its cost and multiplier.
- Extensible to more ingredients or modifiers without needing subclass rewrites.
- Clear separation of size, toppings, and proteins into individual components (single responsibility per concept).

---

## 📷 `VeggieBurrito.java`

### 📌 Purpose:

Represents a **fixed, preconfigured** burrito (a "template burrito") that extends `CustomBurrito`.

### ✅ Key OOD Concepts:

- **Inheritance for specialization**: Builds on `CustomBurrito`, but sets default ingredients.
- **Template object pattern**: This class essentially "stamps" a prebuilt burrito based on fixed business rules.
- **DRY Principle**: No duplication of add logic — reuses inherited methods.

### 💡 Design Highlights:

- Easy to create other preset burritos (e.g., KetoBurrito, SpicyBurrito) by subclassing similarly.
- Still customizable afterward via inherited methods — adds flexibility to fixed presets.

---

## 📷 `Protein.java` (Enum)

### 📌 Purpose:

Represents different protein options for a burrito, each with its own description and base cost.

### ✅ Key OOD Concepts:

- **Enum as object**: Each constant stores state (`description`, `cost`), not just labels.
- **Encapsulation**: Cost and description logic kept together with the data.
- **Cohesion**: Each enum represents one clear ingredient and its metadata.

### 💡 Design Highlights:

- Eliminates the need for lookup tables or string parsing elsewhere.
- Makes cost logic consistent and central (change price once, it's fixed everywhere).

---

## 📷 `Topping.java` (Enum)

### 📌 Purpose:

Like `Protein`, but for burrito toppings.

### ✅ Key OOD Concepts:

- **Single responsibility**: Each enum handles one topping's name and base cost.
- **Consistency**: Uniform interface for `getCost()` used across toppings.

### 💡 Design Highlights:

- Designed for smooth integration with cost calculation logic in `CustomBurrito`.
- Easy to maintain or extend — just add new entries, no logic changes required.

---

## 📷 `Size.java` (Enum)

### 📌 Purpose:

Represents the overall burrito size (e.g., Normal, Jumbo), which affects cost.

### ✅ Key OOD Concepts:

- **Strategy encapsulation**: Each size has a specific cost multiplier that applies to the entire burrito.
- **Minimal, cohesive responsibility**: Knows only how to provide a base cost adjustment.

### 💡 Design Highlights:

- Makes total price scaling simple and centralized.
- Size is a core, shared property across all burrito types, making this enum highly reusable.

---

## 📷 `PortionSize.java` (Enum)

### 📌 Purpose:

Models portion sizes (e.g., Less, Normal, Extra) and their corresponding cost multipliers.

### ✅ Key OOD Concepts:

- **Polymorphic multiplier logic**: `Less` means 0.9x, `Extra` means 1.25x — simple but powerful extension point.
- **Encapsulated variation**: The enum models varying behavior based on selection.

### 💡 Design Highlights:

- Used uniformly in both `Protein` and `Topping` maps.
- Simplifies logic in cost calculation by pushing responsibility to portion-level.

---

# 🧠 Overall Design Assessment (OOD Best Practices)

### ✔️ **Encapsulation**

- Every ingredient-related enum encapsulates its metadata.
- Ingredient logic lives in enums — keeps `Burrito` implementation clean.

### ✔️ **Abstraction & Interface Use**

- The `Burrito` interface abstracts functionality and encourages multiple implementations.
- Clients (ordering systems, UI code) don't care if it's a `CustomBurrito` or `VeggieBurrito`.

### ✔️ **Reusability**

- Common methods like `addProtein`, `cost`, `setSize` are reused in all burrito variants.
- `VeggieBurrito` is a preset wrapper over the generic system.

### ✔️ **Extensibility**

- Easy to add new ingredients, portion sizes, or sizes without rewriting core logic.
- New burrito types can be created by extending or composing existing classes.

### ✔️ **Minimal Coupling**

- `CustomBurrito` doesn't depend on `VeggieBurrito` or any specific enum logic.
- Cost logic and state are decoupled via enums and maps.

---

## Related Concepts

- [[Intro]] - OOD principles demonstrated
- [[Encapsulation and Invariants]] - Private fields with controlled access
- [[Java Safari#Enumerations]] - Enums with state and behavior
- [[Model, View, and Controller#SOLID]] - Open/Closed Principle, Interface Segregation