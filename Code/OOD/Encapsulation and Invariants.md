
```java
interface ConnectNModel {
  static enum Status { Playing, Stalemate, Won, }

  Status getStatus();
  boolean isGameOver();
  int getNextPlayer();
  int getWinner();

  Integer getPlayerAt(int x, int y);
  boolean isColumnFull(int which);

  int move(int who, int where);

  int getWidth();
  int getHeight();
  int getGoal();
  int getPlayers();
}
```

To implement we need to consider what fields to implement. We need a sequence of sequence of Integers for positioning

```java
public int width;
public int height;
public int goal;
public int players;
```

We need to represent the grid, so we make a list of lists

```java
public List<List<Integer>> columns;
```

We also need state management to tell the client who is the player and whole one.

```java
public Status status;
public int turn;
```

Clearly the fields above will work, but for flexibility we dont want to have turn be an int.

```java
public Object turn;
public List<List<Object>> columns;
```

Or if we do an arbitrary number of dimensions (a k-D) game of grids, we need to have a map from dimension names to their sizes

```java
public Map<String, Integer> dimensions;
public Object hypercolumns;
```

At this point, our game configuration is the map of the dimensions, and two its, goal, and players. We could add these to th map as well so that more properties in the future wont change representation

```java
public Map<String, Integer> configuration;

public Status status;
public Object turn;
public Object hypercolumbns;
```

k-D Connect-N is weird, never played it before and may need more statuses so we can just add

```java
public Map<String, Object> properties;
public Object hypercolumns;
```

Lets just go big and represent everything in one field.

```java
public Map<String, Object> properties;
```

---

With this change, we gained flexibility, but we have changed named fields to amorphous mapping. The design above is almost too flexible.

---

- Width, height, goal, or players permit changes mid game, and they can be zero or negative
- Status or columns field might be null
- The shape of the list-of-lists in columns might not match the dimensions in width and height; columns.size() might differ from width, or it may contain a column whose size exceeds height
- Or columns might contain Integer values that don't stand for players
- The client can look at or change whatever it pleases

---

We should restrict fields.

```java
public final int width;
public final int height;
public final int goal;
public final int players;
```

Lets consider these classes:

```java
package first;

    public class Base {
        private   int privateField;
                  int packageField;
        protected int protectedField;
        public    int publicField;
    }

    class FirstHelper { ... }

package second;

    public class Derived extends Base { ... }

    class SecondHelper { ... }
```

- Every program and privileged user should operate with the least amount of privilege necessary to complete the job.
- for fields, we use private the vast majority of the time. Some exceptions would be:
    - static final constants are often public
    - Fields must be accessible to subclasses can be protected.
    - Multiple classes in the same package are cooperating in some close way such that it doesn't make sense to communicate via interfaces, we can use default access level.