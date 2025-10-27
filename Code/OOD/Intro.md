1. Object-Oriented Design (OOD) helps:
    - Hide implementation details (encapsulation).
    - Promote code reusability.
    - Improve readability and maintainability.
2. Objects should have a single, focused purpose.
    - They can be extended (e.g., via inheritance), but ideally not modified directly.
3. Subtypes follow the Liskov Substitution Principle.
    - A `Dog` can be used wherever an `Animal` is expected.
4. Abstractions should not depend on implementation details (Dependency Inversion Principle).
5. Good software should be:
    - Correct, efficient, secure, maintainable, robust, portable, reliable, testable, usable, and scalable.

---

## Key Concept Comparisons

- **Functional vs. Object-Oriented Design**
    - *Functional:* Separates data from behavior; functions operate on data.
    - *OO Design:* Encapsulates data and its behavior together in self-contained objects.
- **Advantage of Functional Design**
    - Easier to add new behaviors without changing existing data structures; flexible when expanding operations.
- **Advantage of OO Design**
    - More structured; ensures consistent behavior via interfaces and encapsulation of methods with data.

---

## Typed vs. Dynamically Typed Languages

- **Advantages of Strong Typing (e.g., Java):**
    1. Catches type mismatches at compile time, improving safety.
    2. Enforces interface implementation, ensuring consistency across object behavior.