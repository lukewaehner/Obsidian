---
tags:
  - java
  - jvm
  - object-oriented
type: moc
---
# Java

A statically-typed, object-oriented language that runs on the JVM. Verbose but predictable, with a massive ecosystem and strong tooling.

## Core Concepts

### Language Fundamentals
- [[Variables and Types]] — Primitives, references, autoboxing, `var`
- [[Control Flow]] — `if`, `switch` expressions, loops
- [[Methods]] — Signatures, overloading, varargs, `static` vs instance
- [[Strings]] — `String`, `StringBuilder`, formatting, text blocks

### Object-Oriented Programming
- [[Classes and Objects]] — Constructors, fields, `this`, packages
- [[Inheritance]] — `extends`, `super`, method overriding
- [[Polymorphism]] — Dynamic dispatch, upcasting/downcasting
- [[Encapsulation]] — Access modifiers, getters/setters
- [[Interfaces]] — `implements`, default methods, sealed interfaces
- [[Abstract Classes]] — When to choose abstract vs interface
- [[Records and Enums]] — Lightweight data carriers and type-safe constants

### Generics & Collections
- [[Generics]] — Type parameters, bounded types, wildcards
- [[Collections]] — `List`, `Set`, `Map`, `Queue`, implementations and tradeoffs
- [[Streams API]] — `map`, `filter`, `collect`, lazy evaluation
- [[Lambdas]] — Functional interfaces, method references

### Error Handling & I/O
- [[Exception Handling]] — `try`/`catch`/`finally`, try-with-resources, checked vs unchecked
- [[File IO]] — `Files`, `Path`, buffered readers/writers
- [[Serialization]] — `Serializable`, JSON with Jackson/Gson

### Concurrency
- [[Threads]] — `Thread`, `Runnable`, lifecycle
- [[Synchronization]] — `synchronized`, locks, `volatile`, atomics
- [[Executors]] — Thread pools, `Future`, `CompletableFuture`
- [[Concurrent Collections]] — `ConcurrentHashMap`, `BlockingQueue`

### JVM Internals
- [[JVM Memory Model]] — Heap, stack, metaspace, references
- [[Garbage Collection]] — Generational GC, G1, ZGC basics
- [[Classloading]] — Classpath, classloaders, reflection

## Tooling

- [[Maven]] — `pom.xml`, dependencies, lifecycle phases
- [[Gradle]] — Groovy/Kotlin DSL, tasks, multi-project builds
- [[JUnit]] — Unit testing, assertions, parameterized tests
- [[Mockito]] — Mocking dependencies in tests

## Frameworks

- [[Spring]] — DI, Spring Boot, REST controllers, JPA

## Quick Reference

```java
public class Point {
    private final int x, y;
    public Point(int x, int y) { this.x = x; this.y = y; }
}

interface Greet { void say(String name); }
Greet g = name -> System.out.println("Hi " + name);

List<Integer> nums = List.of(1, 2, 3, 4);
int sum = nums.stream().filter(n -> n % 2 == 0).mapToInt(Integer::intValue).sum();

try (var reader = Files.newBufferedReader(path)) {
    reader.lines().forEach(System.out::println);
} catch (IOException e) { e.printStackTrace(); }
```

## Resources

- [Java Documentation](https://docs.oracle.com/en/java/)
- [Baeldung](https://www.baeldung.com/)
- [Spring Guides](https://spring.io/guides)

## See Also

- [[Languages]] — Other programming languages
- [[Code]] — Main programming hub
