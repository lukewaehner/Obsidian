- We must develop systems by breaking them into smaller parts, thus Cohesion is needed. (Each component serves one purpose).
- Ensure low coupling, so not all components work off each other - replacing components with a new version causes minimal disturbance to other components (Isolation).

---

## SOLID

- **S**ingle Responsibility - single purpose
- **O**pen for extension, closed for modification - can extend functionality, without modifying source
- **L**iskov's Substitution Principle - If `S` is a subtype of `T` , then objects of `T` can be substituted with objects of `S` without altering any expected functionality.
- **I**nterface segregation - No client should be forced to depend on unused methods
- **D**ependency inversion - details should depend on abstraction. (Low level classes depend on high level classes)

---

## MVC

- Three categories: Model, View, Controller (Backend, Frontend, Middleware)
- Isolated behaviors

- Model: implements functionality, does not care about when it is used and how
- Controller: takes user inputs, tells model wat to do and view what to display
- View: displays results to user

---

## Builder Class:

```java
public class CustomerBuilder {
    //maintains fields, one for each field in the actual complex class

    private String firstName;
    private String lastName;
    private String middleInitial;
    private String addressLineOne;
    private String addressLineTwo;
    private String city;
    private String state;
    private int zipcode;
    private String primaryPhone;
    private String cellPhone;
    private String userName; //online profile
    private double businessValue; //total amount earned from this customer
    private double percentageOnline; //percentage of amount earned by online order

    public CustomerBuilder() {
        //assign default values to all the fields as above
    }

    //call this method to change the first name
    public CustomerBuilder firstName(String firstName) {
        this.firstName = firstName;
        return this;
    }

    //call this method to change the zip code
    public CustomerBuilder zipcode(int zipcode) {
        this.zipcode = zipcode;
        return this;
    }

    ...    

    public Customer build() {
        //use the currently set values to create the Customer object
        return new Customer(firstName,lastName,middleInitial,...);
    }
}
```

- Note how the `CustomerBuilder` will reassign the defaulted values, and then invoke the `Customer` constructor when enough values are given.
- Builders can be their own classes, but its often implemented that couples it with the object that is built. You can write it within the class that builds it.

```java
public class Customer {
    ...
    public static CustomerBuilder getBuilder() {
        return new CustomerBuilder();
    }
    ...

    public static class CustomerBuilder {
        ...

        private CustomerBuilder() {
        ...
        }
    }

}
```

---

## Sync vs A-Sync Controllers

- **Sync:** Predictable, liner progressions are noted as synchronous controllers because they follow pre-defined sequences.
    - Basically, runs through a loop with all sequence points being hit
- **ASync:** Many programs are instead reactive by nature. The program does not execute a pre-defined sequence of operations, but executes depending on user input. GUIs behave this way.
    - Each method has a specific action that is called in response to specific user actions.
- The Main Method:
    
    ```java
    class ProgramRunner {
    	public static void main(String[] args) {
    		Model model = new Model(...); // set up before if needed
    		View view = new View(...); // setup details if needed
    		
    		//create controller
    		Controller controller = new Controller(model, view,...);
    		
    		// give control to the controller. Controller relinquishes only when program ends.
    		
    		controller.go();
    	}
    }
    ```
    
    This is the starter of the application, it creates the model, views, controllers, then passing everything to the controller to "go"