# Chess Pieces System

# ♟️ Chess Pieces — Object-Oriented Design Notes

---

## 📷 `ChessPiece.java` (Abstract Class)

### 📌 Purpose:

Provides a **base abstraction** for all chess pieces. Declares shared state (position, color) and common operations (`getRow()`, `getColumn()`, etc.).

### ✅ Key OOD Concepts:

- **Abstraction**: Defines general behavior for chess pieces without specifying their unique moves.
- **Encapsulation**: Stores common fields like `row`, `column`, and `color`.
- **Template Method pattern**: Leaves `canMove` abstract — each subclass must define how it moves.

### 💡 Design Highlights:

- Reduces duplication across `Rook`, `Bishop`, `Queen`, etc.
- Any new piece can extend `ChessPiece` to inherit shared functionality (e.g., `Knight`, `Pawn`).
- Follows **Liskov Substitution Principle** — any subclass can be used as a `ChessPiece`.

---

## 📷 `Color.java` (Enum)

### 📌 Purpose:

Defines the **two valid colors** in chess: `WHITE` and `BLACK`.

### ✅ Key OOD Concepts:

- **Type safety**: Prevents the use of invalid color values.
- **Centralization**: Guarantees consistency across the app when dealing with piece color.

### 💡 Design Highlights:

- Cleaner than using strings or booleans.
- Ready for future extension (e.g., highlighting colors, themes).

---

## 📷 `Rook.java`

### 📌 Purpose:

Represents a rook and implements its legal move logic (straight lines only).

### ✅ Key OOD Concepts:

- **Inheritance**: Extends `ChessPiece` and overrides `canMove`.
- **Single Responsibility**: Focuses only on move logic for rooks.
- **Polymorphism**: Implements `canMove` in a way that can be called via `ChessPiece`.

### 💡 Design Highlights:

- Move logic is cleanly encapsulated and uses chess rules accurately.
- No repeated logic for state — it all comes from the superclass.

---

## 📷 `Bishop.java`

### 📌 Purpose:

Represents a bishop, moving diagonally across the board.

### ✅ Key OOD Concepts:

- Same inheritance and override strategy as `Rook`.

### 💡 Design Highlights:

- Uses math (`Math.abs(...)`) to implement diagonal logic elegantly.
- Can be reused or extended (e.g., `SuperBishop` in variants).

---

## 📷 `Queen.java`

### 📌 Purpose:

Represents a queen, which can move like both a rook and a bishop.

### ✅ Key OOD Concepts:

- **Reuses behavior** logically instead of duplicating it.
- Contains simplified logic by combining `Rook` and `Bishop` rules.

### 💡 Design Highlights:

- Demonstrates how polymorphism can support **multiple behavioral patterns** in one class.
- Avoids subclass explosion by composing movement logic.

---

## 📷 Tests (`QueenTest.java`, `BishopTest.java`, `RookTest.java`)

### 📌 Purpose:

Each test class verifies valid and invalid movement patterns of the corresponding piece.

### ✅ Key OOD Concepts:

- **Encapsulation validation**: Confirms private state behaves as expected through public interfaces.
- **Black-box testing**: Tests behavior, not internal implementation.

### 💡 Design Highlights:

- Modular test files reflect modular class structure.
- Easily extendable for other pieces or custom rules.

---

# 🧠 Overall Design Evaluation

| Principle | How it applies |
| --- | --- |
| **Abstraction** | `ChessPiece` defines what a piece *can do*, not how it does it. |
| **Inheritance** | All pieces inherit shared state and behavior from `ChessPiece`. |
| **Polymorphism** | Code can operate on a `ChessPiece` reference and call `canMove()` without knowing the specific piece type. |
| **Encapsulation** | Each piece manages its own state and rules; tests validate externally observable behavior. |
| **Open/Closed Principle** | Easy to add new pieces (e.g., Knight) without changing existing ones. |
| **DRY** | Shared logic is centralized in the abstract superclass; repeated movement logic is minimal. |

---

## Related Concepts

- [[Intro]] - Abstraction and Liskov Substitution Principle
- [[Java Safari#Enumerations]] - Color enum for type safety
- [[Encapsulation and Invariants]] - State management in base class
- [[Model, View, and Controller#SOLID]] - Open/Closed Principle demonstrated