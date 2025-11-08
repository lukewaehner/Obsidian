
---

```c filename=threads.c
#include <pthread.h>

void *worker1(int *arg) {
	// Pre cast the arg to an int, before deferencing
	// Interprets the void pointer as an int pointer
	int no = *((int *) arg); 
	
	printf("Hello from worker, %d\n", no);
	for (unsigned long i = 0; i < 3e9; i++) {
	}
	printf("worker %d done\n", no);
	return NULL;
}

int main(int argc, char **argv) {
	printf("Starting work\n")
	
	pthread_t th1, th2;
	// create a thread:
	// - save its handle into th1
	// - use default attributes (NULL)
	// - in the new thread call function worker1(NULL)
	
	int no1 = 1;
	int no2 = 2;
	
	assert(0 == pthread_create(&th1, NULL, worker, &no1));
	assert(0 == pthread_create(&th2, NULL, worker, &no2));
	
	// wait for both workers to be done
	pthread_join(th1, NULL);
	pthread_join(th2, NULL);
	wait(NULL);
	wait(NULL);
	
	printf("All done!\n");
	
	return 0;
}
```