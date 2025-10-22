
Fork -

```c
#include <stdio.h>
#include <assert.h>

int main(int argc, char **argv) {

	printf("Before forking. PID=%d\n", getpid());
	
	pid_t child = fork();
	
	printf("After forking. Fork returned %d. PID=%d\n", child, getpid());
	
	if(child == 0) {
		printf("Only printed in child process.\n");
		exit(0);
	} else {
		pritf("Only printed in parent process.\n");
	}
	
	return 0;
}
```

