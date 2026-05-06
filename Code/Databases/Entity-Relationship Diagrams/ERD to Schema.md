
---

## ERD to Schema

Converting ER diagrams to relational tables.

---

## Entities → Tables

Each entity becomes a table with its attributes as columns.

```
Entity: Actor(id, name, gender)
↓
Table: Actor(id INT PRIMARY KEY, name VARCHAR, gender CHAR)
```

---

## 1:1 Relationships

Add foreign key to either table (usually the one with total participation).

---

## 1:N Relationships

Add foreign key to the "many" side table.

```
Department --employs-- Employee (1:N)
↓
Employee table gets department_id foreign key
```

---

## M:N Relationships

Create a new junction/association table.

```
Actor --plays_in-- Movie (M:N)
↓
Create: ActsIn(actor_id, movie_id, role)
  FOREIGN KEY (actor_id) REFERENCES Actor(id)
  FOREIGN KEY (movie_id) REFERENCES Movie(id)
  PRIMARY KEY (actor_id, movie_id)
```

---

## Multivalued Attributes

Create separate table with foreign key back to entity.

```
Movie has genres (multivalued)
↓
Create: MovieGenre(movie_id, genre)
  FOREIGN KEY (movie_id) REFERENCES Movie(id)
  PRIMARY KEY (movie_id, genre)
```
