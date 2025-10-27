
---

## Enumerations

```java
public enum Day {
	MONDAY, TUESDAY, WEDNESDAY, THURSDAU, FRIDAY, SATURDAY, SUNDAY
}
```

```java
public enum Level {
    LOW(1), MEDIUM(2), HIGH(3);

    private final int severity;

    Level(int severity) {
        this.severity = severity;
    }

    public int getSeverity() {
        return severity;
    }
}
```

---

## Switch Cases

Supported Types:

- Primitive Types: `byte`, `short`, `char`, `int`
- Wrapper classes: `Byte`, `Short` , `Character`, `Integer`
- `String`
- `enum` types

```java
switch (expression) {
	case value1:
    // code block
    break;
  case value2:
    // code block
    break;
  default:
    // default code block
}
```

---

## Arrays

```java
type[] name;
// ----
int[] numbers;
```

**Initialization**

```java
numbers = new int[5]; // Array of 5 ints, all default to 0
String[] fruits = new String[3]; // 3 null strings
```

**With values:**

```java
int[] primes = {2, 3, 5, 7, 11};
```

**Iteration**

```java
for (int prime : primes) {
	System.out.println(prime);
}

for (int i = 0; i < primes.length; i++) {
	System.out.println(primes[i]);
}
```

**Varargs**

```java
public void printNumbers(int... numbers) {
	for (int num : numbers) {
		System.out.println(num);
	}
}

printNumbers(1, 2, 3);
```

---

## Memory

Boxed primitives are wrappers for primitive types. They are the overarching objects.

You get to use the object method from them, but sometimes have to jump around to do the same things that you can easily with primitives

---

## Good Practices

**Null**

- Null is annoying
- Only used to represent the absence of a reference
- Document where its allowed always
- Quickly fail with null

**Equality**

- Shallow equality → same memory location
- Deep equality → same memory contents, different location
- Intensional vs. Extensional - Same as Shallow vs Deep
- Nominal vs. Structural (are objects of two classes with same instance variables and values equal?)
- Physical vs. Logical (Are HMSDuration and CompactDuration objects with same duration equal?)
- == vs. equals()?

---

Default equals returns true when two objects have the same location in memory, and are thus the same

```java
final class Posn {
	...
	private final int x;
	private final int y;

	public boolean equals(Object obj) {
		if (this == obj) return true; // Fast path
		
		if (! (object instanceof Posn))
			return false; //Incompatible type
		Posn that = (Posn) obj;
		//what we mean by ''the same points''
		return this.x == that.x && this.y == that.y;
	}
}
assetEquals( new Posn(2, 4), new Posn(2, 4) ); // Works now even though they are in different memory locations
```

---

## Exceptions

```java
try {
	int fd = open(path, flags);
	write(fd, buf1, size2);
	write(fd, buf2, size2);
} catch (IOException e) {
	// Cleanup code
}
```

Types

Checked

Extends Exception

Possibly recoverable

e.g. network error

must appear in throw clauses

Unchecked

extends Error or RuntimeException

Probably bail out

e.g. programming error

may appear in throw clauses

---

How to use:

```java
// Extend:
class IllegalMoveException extends IllegalStateException { ... }
// Throw:
throw new IllegalMoveException(reason);
// Catch:

try {
	somethingThatMightThrow();
} catch (IllegalMoveException e) {
	logError(e);
}
```

---

Checked Exceptions

IOException is a checked exception, so it appears in method signatures:

```java
void myBigIOMethod(...) throws IOException {
	... new FileReader(someFile) ...
}
```

Methods that call a method that that throws and don't catch it also throw

```java
void innocuousLookingMethods() throws IOException {
	myBigIoMethod(3, true);
}
```

---

AssertThrows, throw-able run-ables

```java
public interface Duration {
	inSeconds
}
```