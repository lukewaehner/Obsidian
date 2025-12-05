
---

## ERD Components

Building blocks of Entity-Relationship Diagrams.

---

## Entities

Rectangles representing objects/concepts.

- Actor
- Movie
- Company

---

## Attributes

Ovals connected to entities.

- **Simple attributes**: Single value (name, year)
- **Multivalued attributes**: Multiple values, shown with double oval (genres)
- **Key attributes**: Underlined (id)

---

## Relationships

Diamonds connecting entities.

- "plays_in" between Actor and Movie
- "employs" between Company and Person

---

## Example: IMDB

```
[Actor] --<plays_in>-- [Movie]
  |                      |
 name                   name
gender                  year
                       ((genres))  <- multivalued
```

- Actors have name and gender
- Movies have name, year, and multiple genres
- Actors can play in multiple movies
- Movies can have multiple actors
