
File system:

Root -> /
Subdirectories

---

Print / Write

```c
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>

#define BUFFER_SIZE 1024

int main(int args, char **argv) {
	const char *msg = "Hello, World!\n";
	
	ssize_t bytes = write(1, msg, strlen(msg));
	assert(-1 != bytes);
	printf("Printed %zu bytes.\n", bytes);
	
	return 0;
}
```

> Hello, World!
> Printed 14 bytes.

`strace` -> Finds out write streams and read streams

```c
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>

#define BUFFER_SIZE 1024

int main(int args, char **argv) {
	const char *msg = "Hello, World!\n";
	
	char buffer[BUFFER_SIZE];
	
	ssize_t bytes = write(1, msg, strlen(msg));
	assert(-1 != bytes);
	printf("Printed %zu bytes.\n", bytes);
	
	printf("Write something:\n);
		
	bytes = read(0, buffer, BUFFER_SIZE - 1)
	assert(-1 != bytes)
	
	buffer[bytes] = '\0'; // Insert null at end
	
	printf("Read in %zu bytes. Here: %s\n", bytes, buffer)
}
```

> Hello, World!
> Printed 14 bytes.
> Write something:
> SOMETHING
> Read in 10 bytes. Here: SOMETHING

- 9 Letters + newline symbol, 10 bytes total (10 chars)

```c
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

#define BUFFER_SIZE 1024
int main(int argc, char **argv) {
	char buffer[BUFFER_SIZE];

	int fd = open("file.txt", O_RDONLY);
	
	// File may not exist
	// Not appropriate permissions
	// Device failture, etc
	if (fd == -1) {
		perror("Error opening file");
		exit(1);
	}
	
	ssize_t bytes = read(fd, buffer, BUFFER_SIZE - 1)
	
	if(bytes == -1) {
		perror("Error reading from file");
		exit(1);
	}
	
	buffer[butes] = '\0';
	return 0;
}
```

Args:
Path to the file, control access mode and options

Returns file descriptor (non-negative integer on success);
Returns -1 on error

---

What if we want to read a big file, or something that doesn't have a preset length?

We shouldn't: Make a really large buffer, scan it all in, and dump it all out
We should: Run a loop

Read commands return 0 on file end, we read up to a specified number of bytes, but the OS remembers where we left off, so we can run a buffer loop until we get a 0, and return

```c
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

#define BUFFER_SIZE 1024
int main(int argc, char **argv) {
	char buffer[BUFFER_SIZE];

	int fd = open("file.txt", O_RDONLY);
	
	// File may not exist
	// Not appropriate permissions
	// Device failture, etc
	if (fd == -1) {
		perror("Error opening file");
		exit(1);
	}
	
	ssize_t bytes = read(fd, buffer, BUFFER_SIZE - 1)
	
	while (bytes > 0) {
		buffer[butes] = '\0';
		printf("Read %zu bytes. HERE:\n%s", bytes, buffer);
		bytes = read(fd, buffer, BUFFER_SIZE - 1);
	}
	
	if(bytes == -1) {
		perror("Error reading from file");
		exit(1);
	}
	return 0;
}
```

What we can do to shorten it, is by remembering assignments are conditions we can drop it right into the while loop

```c
ssize_t bytes;
while(0 < (butes = read(fd, buffer, BUFFER_SIZE - 1))) {
	// add null, printf
}
```

---

Finding files:

Open w/ 

```c
int main(int argc, char **argv) {
	
}
```
