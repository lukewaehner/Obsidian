
---

## Relationships and Cardinality

How entities relate to each other.

---

## Cardinality Types

### One-to-One (1:1)

Each entity on one side relates to at most one entity on the other.

Example: Person -- has -- Passport

### One-to-Many (1:N)

One entity relates to many on the other side.

Example: Department -- employs -- Employee

### Many-to-Many (M:N)

Multiple entities on both sides can relate.

Example: Actor -- plays_in -- Movie

---

## Notation

**Crow's Foot Notation:**
- `|` = one
- `<` or `>` = many
- `O` = zero (optional)

**Min-Max Notation:**
- (0,1) = zero or one
- (1,1) = exactly one
- (0,*) = zero or more
- (1,*) = one or more

---

## Participation

**Total participation** (double line): Every entity must participate in the relationship.

**Partial participation** (single line): Some entities may not participate.
