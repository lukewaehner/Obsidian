
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


## Locks

```c
// Multi-threaded sum using a single global variable and mutexes
#include <assert.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

static long sum = 0;
static pthread_mutex_t sum_lock = PTHREAD_MUTEX_INITIALIZER;

typedef struct {
  long from;
  long to;
} sum_args_t;

static void sum_from_to(long from, long to) {
  if (from > to) return;
  for (long i = from; i <= to; ++i) {
    pthread_mutex_lock(&sum_lock);
    sum += i;
    pthread_mutex_unlock(&sum_lock);
  }
  fprintf(stdout, "Completed %ld to %ld\n", from, to);
}

static void *sum_thread(void *args) {
  sum_args_t *a = (sum_args_t *)args;
  sum_from_to(a->from, a->to);
  return NULL;
}

int main(int argc, char **argv) {
  assert(argc >= 3);

  long from = strtol(argv[1], NULL, 10);
  long to   = strtol(argv[2], NULL, 10);

  // split correctly at midpoint of [from, to]
  long mid = from + (to - from) / 2;

  pthread_t th;
  sum_args_t a = {.from = from, .to = mid};
  assert(0 == pthread_create(&th, NULL, sum_thread, &a));

  sum_from_to(mid + 1, to);

  assert(0 == pthread_join(th, NULL));
  printf("%ld\n", sum);
  return 0;
}
```