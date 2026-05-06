- Synchronous Controllers are good for pre-baked rules-based applications, like games
- But its hard to truly separate controller from view so each one is replaceable.
- Asynchronous Controllers push methods in response to external inputs, they are called callbacks.
- GUI programs work this way, user clicks a button, moves the mouse, etc → a controller method is called
- Mocks:
    - Components that can replace an actual component
        - For testing purposes
        - As a placeholder for simultaneous development (also called a stub)
        - Design that facilitates replacement promotes mocking
            - Good encapsulation → fixed role → easier to replace
            - Design by interface → not dependent on specific implementation
            - Refer to components using interfaces → work with any implementation of that interface
            - Mock implements actual interface, but does so simply or to enable testing
        - Use mocks to
            - Test components that otherwise require I/O
            - Emulate a component that is being concurrently designed/implemented
- Standalone programs need the main method

```java
public class OurMainClass {
	public static void main(String[] args) {
	...
	}
}
```