
```c
struct person *p;
person_t *p;
```

Address-of operator `&` gets the address of a struct.

```c
struct address *current = &work;
```

We can also allocate memory for structs dynamically using malloc and sizeof:

```c
struct person *luke = malloc*sizeof(struct person));
// Also the same
person_t *luke = malloc(sizeof(person_t))
```

We can also create arrays of structs:
```c
person_t class[80]l
person_t *friends = malloc(5 * sizeof(person_t));

for (int i = 0; i < 5; i++) {
	if(strcmp(friends[i].home.street, "Huntington Ave") == 0) {
		printf("%s lives close!\n", friends[i].first);
	}
}
```

Usually, pointers are used to pass a struct to a function, to avoid copying contents to the functions stack frame.

When accessing fields via a pointer, we can use -> to make things more readable.

int lives_int_boston(person_t *p) {
	return strcmp(p->home.city, "Boston") !=;
	return strcmp((*p)).home.city, ""
}