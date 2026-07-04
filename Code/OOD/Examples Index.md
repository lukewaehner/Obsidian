# OOD Examples Index

This note links practical code examples to their corresponding OOD concepts and patterns.

## Design Patterns

### Command Pattern
- **Concept:** [[Command Design Pattern]]
- **Examples:**
  - [[Dumbed Down Code 2#Command Pattern]] - Coffee maker command implementation
  - [[Practice Exam#Question 5 – RegPiggyBank]] - Command-style deposit operations

### Adapter Pattern
- **Concept:** Referenced in [[Dumbed Down Code 2#Adapter Pattern]]
- **Examples:**
  - [[Dumbed Down Code 2#Adapter Pattern]] - Heater interface adaptation
  - Legacy interface bridging example

### Strategy Pattern
- **Concept:** [[Dumbed Down Code 2#Strategy Pattern]]
- **Examples:**
  - Coffee grind strategy implementation
  - Interchangeable brewing algorithms

### Decorator Pattern
- **Concept:** [[Dumbed Down Code 2#Decorator Pattern]]
- **Examples:**
  - Logging coffee maker wrapper
  - Feature addition without modification

### Builder Pattern
- **Concept:** [[Model, View, and Controller#Builder Class]]
- **Examples:**
  - [[Burrito]] - Complete burrito builder implementation
  - [[Dumbed Down Code#Example MBC – Model, Builder, Controller]] - User builder example

## Architecture Patterns

### Model-View-Controller (MVC)
- **Concept:** [[Model, View, and Controller]]
- **Examples:**
  - [[Model, View, Controller]] - Complete MVC text UI implementation
  - [[Dumbed Down Code#Example MBC – Model, Builder, Controller]] - Simple user MVC

### Controllers and Mocks
- **Concept:** [[Controllers and Mocks]]
- **Examples:**
  - [[Controllers & Mocks]] - Calculator controller with multiple implementations
  - [[Dumbed Down Code#Example Code Controllers and Mocks]] - Mock model testing

## Core OOD Principles

### Encapsulation and Invariants
- **Concept:** [[Encapsulation and Invariants]]
- **Examples:**
  - [[Dumbed Down Code 2#Encapsulation & Class Invariants]] - Water tank with constraints
  - [[Practice Exam#Question 3 – Audit Log Bug]] - Encapsulation violation and fix
  - [[Burrito]] - Private fields with controlled access

### Abstraction
- **Concept:** [[Code/OOD/Intro#Key Concept Comparisons]]
- **Examples:**
  - [[Chess Pieces (Abstraction)]] - Abstract ChessPiece class hierarchy
  - [[Burrito]] - Burrito interface abstraction

### Inheritance vs Composition
- **Concept:** Referenced in [[Dumbed Down Code 2#Code Reuse Inheritance vs Composition]]
- **Examples:**
  - Bad: CoffeeMaker fragile inheritance
  - Good: Composition with delegation

## SOLID Principles Examples

### Single Responsibility
- **Concept:** [[Model, View, and Controller#SOLID]]
- **Examples:**
  - [[Model, View, Controller]] - Separate Model, View, Controller responsibilities
  - [[Chess Pieces (Abstraction)]] - Each piece handles only its movement

### Open/Closed Principle
- **Concept:** [[Model, View, and Controller#SOLID]]
- **Examples:**
  - [[Burrito]] - Extensible via enums without class modification
  - [[Chess Pieces (Abstraction)]] - Add new pieces without changing existing ones

### Liskov Substitution Principle
- **Concept:** [[Model, View, and Controller#SOLID]]
- **Examples:**
  - [[Chess Pieces (Abstraction)]] - Any piece can substitute ChessPiece
  - [[Burrito]] - CustomBurrito and VeggieBurrito are interchangeable

### Interface Segregation
- **Concept:** [[Model, View, and Controller#SOLID]]
- **Examples:**
  - [[Burrito]] - Clean burrito interface with only relevant methods
  - [[Model, View, Controller]] - Separate IModel, IView, IController interfaces

### Dependency Inversion
- **Concept:** [[Model, View, and Controller#SOLID]]
- **Examples:**
  - [[Controllers & Mocks]] - Controller depends on calculator interface
  - [[Model, View, Controller]] - Controller uses interface references

## Java-Specific Features

### Enumerations
- **Concept:** [[Java Safari#Enumerations]]
- **Examples:**
  - [[Burrito]] - Protein, Topping, Size, PortionSize enums with behavior
  - [[Chess Pieces (Abstraction)]] - Color enum for type safety
  - [[Dumbed Down Code#Enum with Logic]] - Size with multiplier

### Exception Handling
- **Concept:** [[Java Safari#Exceptions]]
- **Examples:**
  - [[Practice Exam#Question 2 – testThree() Bug & Fix]] - InsufficientCashException handling
  - [[Dumbed Down Code 2#Encapsulation & Class Invariants]] - IllegalArgumentException for validation

### Collections (Map, List)
- **Concept:** [[Java Safari#Memory]]
- **Examples:**
  - [[Burrito]] - Map<Protein, PortionSize> for ingredients
  - [[Dumbed Down Code#Map<K, V>]] - HashMap examples and iteration
  - [[Practice Exam]] - TreeMap for sorted change calculation

### StringBuilder
- **Concept:** [[Dumbed Down Code#StringBuilder]]
- **Examples:**
  - [[Dumbed Down Code#Using a Mock with StringBuilder]] - Mock logging
  - [[Practice Exam]] - Audit log construction

## Testing Patterns

### Mock Objects
- **Concept:** [[Controllers and Mocks]]
- **Examples:**
  - [[Dumbed Down Code#MockModel.java]] - Mock with log verification
  - [[Controllers & Mocks]] - Calculator mock implementations
  - [[Practice Exam#Question 3]] - Test exposing encapsulation bug

### Unit Testing
- **Examples:**
  - [[Chess Pieces (Abstraction)#Tests]] - QueenTest, BishopTest, RookTest
  - [[Practice Exam#Question 2]] - testThree() debugging
  - [[Practice Exam#Question 3]] - testAuditBypassBug()

## Complete Example Systems

### Burrito Ordering System
- **Location:** [[Burrito]]
- **Demonstrates:**
  - Interface abstraction
  - Enum with state and behavior
  - Builder pattern (implicit)
  - Data-driven composition
  - Extensibility via inheritance

### Chess Piece System
- **Location:** [[Chess Pieces (Abstraction)]]
- **Demonstrates:**
  - Abstract base class
  - Template method pattern
  - Polymorphic behavior
  - Liskov substitution
  - Type safety with enums

### Cash Register System
- **Location:** [[Practice Exam]]
- **Demonstrates:**
  - Encapsulation pitfalls
  - State management
  - Exception handling
  - Audit logging
  - Interface design evolution

### Calculator System
- **Location:** [[Controllers & Mocks]]
- **Demonstrates:**
  - Controller pattern
  - Dependency injection
  - Multiple implementations
  - Mock-driven testing
  - Strategy pattern (implicit)

### Coffee Maker Examples
- **Location:** [[Dumbed Down Code 2]]
- **Demonstrates:**
  - Multiple design patterns (Strategy, Command, Decorator, Adapter)
  - Composition vs inheritance tradeoffs
  - Clean architecture principles

## Quick Reference: Concept → Example

| Concept | Best Example |
|---------|--------------|
| **Interfaces** | [[Burrito]], [[Chess Pieces (Abstraction)]] |
| **Abstract Classes** | [[Chess Pieces (Abstraction)#ChessPiece.java]] |
| **Inheritance** | [[Chess Pieces (Abstraction)]], [[Burrito#VeggieBurrito]] |
| **Composition** | [[Dumbed Down Code 2#Code Reuse]] |
| **Encapsulation** | [[Burrito]], [[Practice Exam#Question 3]] |
| **Polymorphism** | [[Chess Pieces (Abstraction)]], [[Controllers & Mocks]] |
| **MVC** | [[Model, View, Controller]] |
| **Mocking** | [[Dumbed Down Code]], [[Controllers & Mocks]] |
| **Builder** | [[Dumbed Down Code#UserBuilder]], [[Model, View, and Controller#Builder Class]] |
| **Command** | [[Dumbed Down Code 2#Command Pattern]] |
| **Strategy** | [[Dumbed Down Code 2#Strategy Pattern]] |
| **Adapter** | [[Dumbed Down Code 2#Adapter Pattern]] |
| **Decorator** | [[Dumbed Down Code 2#Decorator Pattern]] |

## Study Path

For exam preparation, review examples in this order:

1. **Core Concepts:** [[Burrito]] → [[Chess Pieces (Abstraction)]]
2. **Architecture:** [[Model, View, Controller]] → [[Controllers & Mocks]]
3. **Patterns:** [[Dumbed Down Code 2]] (all patterns)
4. **Testing:** [[Dumbed Down Code]] → [[Practice Exam]]
5. **Practice:** Work through all [[Practice Exam]] questions