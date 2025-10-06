
---

Async

Sync

Exceptions
- Traps
- Sync - seg faults, aborts

```c
#include <stdio.h>
#include <assert.h>

int main(int argc, char **argv) {

	printf("Before forking. PID=%d\n", )
	
	pid_t child = fork();
	
	printf("After forking. PID=%d\n", )
	
	return 0;
}
```