
A set of directives to allow conditional compilation
Compile time conditionals that hide or expose parts of the source file from or to the compiler
- `#ifdef` checks if the given
- Example

```c
#ifdef UNIX
	PATH_SEPARATOR "/"
#elif defined WINDOWS
	PATH_SEPARATOR "\\"
#endif
```

Other example:
```c
for (int i = 0; i < length; i++) {
	sum += array[i];
	#if DEBUG_LEVEL >= 1
		printf("array[%d], = %d, sum = %d\n", i, array[i], sum);
	#endif
}
```