```java
/**
 * This interface specifies the operations on a 2D turtle
 * <p>
 * A 2D turtle is characterized by a position (x,y) and a
 * heading (where it is looking).
 * <p>
 * It can be asked to draw the path it has moved using one of
 * the commands below. 
 */
public interface TurtleModel {
    /**
     * Move the turtle by the specified distance along its
     * heading. Do not change heading
     *
     * @param distance
     */
    void move(double distance);

    /**
     * Turn the turtle's heading by the given angle.
     * A positive angle means counter-clockwise
     * turning. The turtle turns in place, i.e. 
     * it does not change position.
     *
     * @param angleDegrees
     */
    void turn(double angleDegrees);

    /**
     * Save the current turtle state (position + heading)
     */
    void save();

    /**
     * Retrieve the last saved turtle state (position + heading)
     */
    void retrieve();

    /**
     * Get the current position of the turtle
     *
     * @return
     */
    Position2D getPosition();

  /**
   * Get the current heading of the turtle
   *
   * @return
   */
    double getHeading();
}
```

```java
/**
 * This class represents a 2D position
 */
public final class Position2D {
  private final double x;
  private final double y;

  /**
   * Initialize this object to the specified position
   */
  public Position2D(double x, double y) {
    this.x = x;
    this.y = y;
  }

  /**
   * Copy constructor
   */
  public Position2D(Position2D v) {
    this(v.x, v.y);
  }

  public double getX() {
    return x;
  }

  public double getY() {
    return y;
  }

  @Override
  public String toString() {
    return String.format("(%f, %f)", this.x, this.y);
  }

  @Override
  public boolean equals(Object a) {
    if (this == a) {
      return true;
    }
    if (!(a instanceof Position2D)) {
      return false;
    }

    Position2D that = (Position2D) a;

    return ((Math.abs(this.x - that.x) < 0.01) && (Math.abs(this.y - that.y) < 0.01));
  }

  @Override
  public int hashCode() {
    return Objects.hash(this.x, this.y);
  }
}
```

Implement TurtleModel interface as a SimpleTurtle class

```java
/**
 * This class manages a 2D turtle and implements all
 * its associated operations
 */
public class SimpleTurtle implements TurtleModel {
  // the position of the turtle
  private Position2D position;
  // the heading of the turtle in degrees
  private double heading;
  // stacks to save and retrieve turtle states
  Stack<Position2D> stackPositions;
  Stack<Double> stackHeadings;

  /**
   * Initializes the turtle to the default state.
   * Default state = position (0,0) and heading (0) meaning
   * looking in the +X direction.
   */
  public SimpleTurtle() {
    this(new Position2D(0, 0), 0);
  }
  /**
   * Initializes the turtle to the given position and heading.
   */
  public SimpleTurtle(Position2D startPos, double startHeading) {
    position = Objects.requireNonNull(startPos);
    heading = startHeading;
    stackPositions = new Stack<>();
    stackHeadings = new Stack<>();
  }

  @Override
  public void move(double distance) {
    //trigonometry to move by distance along angle
    double x = distance * Math.cos(Math.toRadians(heading));
    double y = distance * Math.sin(Math.toRadians(heading));

    position = new Position2D(position.getX() + x, position.getY() + y);
  }

  @Override
  public void turn(double angleDegrees) {
    heading += angleDegrees;
  }

  @Override
  public void save() {
    stackPositions.push(position);
    stackHeadings.push(heading);
  }

  @Override
  public void retrieve() {
    if ((stackPositions.isEmpty()) || (stackHeadings.isEmpty())) {
      throw new IllegalArgumentException("no state to retrieve");
    }
    position = stackPositions.pop();
    heading = stackHeadings.pop();
  }

  @Override
  public Position2D getPosition() {
    return position;
  }

  @Override
  public double getHeading() { return heading;}
}
```

To add drawing, we must extend the interface:

```java
public interface TracingTurtleModel extends TurtleModel {
  /**
   * Move the turtle by the specified distance along its
   * heading. Do not change heading.
   * Draw a line from its initial position to its
   * final position.
   *
   * @param distance
   */
  void trace(double distance);

  /**
   * Get the lines traced by this turtle, caused by the
   * trace method above.
   *
   * @return a list of {@code Line} objects, in the order they were drawn.
   */
  List<Line> getLines();
}

public class SmarterTurtle extends SimpleTurtle implements TracingTurtleModel {
  public SmarterTurtle() {
    super();
    lines = new ArrayList<Line>();
  }

  @Override
  public void trace(double distance) {
    Position2D cur = this.getPosition();
    move(distance);
    lines.add(new Line(cur, this.getPosition()));
  }

  @Override
  public List<Line> getLines() {
    return new ArrayList<>(lines);
  }

  //list of lines traced since this object was created
  List<Line> lines;
}
```

---

Making a controller:

1. Take a one-word command from the user. This command is one of ''move", ''turn", ''trace", ''show" and ''quit".
2. Depending on the command, take additional input (e.g. ''move" requires a distance to move).
3. Call the appropriate operation on the model, or quit (if the command is ''quit").

```java
public class SimpleController {
  public void go() {
    Scanner s = new Scanner(System.in);
    TracingTurtleModel m = new SmarterTurtle();
    while (s.hasNext()) {
      String in = s.next();
      switch(in) {
        case "q":
        case "quit":
          return;
        case "show":
          for (Line l : m.getLines()) {
            System.out.println(l);
          }
          break;
        case "move":
          try {
            double d = s.nextDouble();
            m.move(d);
          } catch (InputMismatchException ime) {
            ...
          }
          break;
        case "trace":
          try {
            double d = s.nextDouble();
            m.trace(d);
          } catch (InputMismatchException ime) {
            ...
          }
          break;
        case "turn":
          try {
            double d = s.nextDouble();
            m.turn(d);
          } catch (InputMismatchException ime) {
            ...
          }
          break;
        default:
          System.out.println(String.format("Unknown command %s", in));
          break;
      }
    }
  }
}
```

Command Design Pattern:

```java
public class Move implements TracingTurtleCommand {
  double d;

  public Move(Double d) {
    this.d = d;
  }

  @Override
  public void go(TracingTurtleModel m) {
    m.move(this.d);
  }
}

public class Trace implements TracingTurtleCommand {
  double d;

  public Trace(Double d) {
    this.d = d;
  }

  @Override
  public void go(TracingTurtleModel m) {
    m.trace(this.d);
  }

  ...

}
```

Now we can change the logic of our controller to:

1. Take a one-word command from the user.
2. **Create the corresponding `TracingTurtleCommand` object.**.
3. **Execute the command object.**

```java
  String in = s.next();
  try {
    switch (in) {
      case "q":
      case "quit":
        return;
     case "show":
       for (Line l : m.getLines()) {
          System.out.println(l);
       }
       break;
     case "move":
        cmd = new Move(s.nextDouble());
        break;
     case "trace":
        cmd = new Trace(s.nextDouble());
        break;
     case "turn":
        cmd = new Turn(s.nextDouble());
        break;
     case "square":
        cmd = new Square(s.nextDouble());
        break;
     default:
        System.out.println(String.format("Unknown command %s", in));
        cmd = null;
        break;
    }
    if (cmd != null) {
      cmd.go(m); //execute the command
      cmd = null;
    }
  } catch (InputMismatchException ime) {
    System.out.println("Bad length to " + in);
  }
```