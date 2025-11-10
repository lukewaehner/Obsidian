
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
// !> Multi-threaded sum using a single global variable and mutexes

/** 
 * Usage
 *
 * ./sum <from> <to>
 */
#include <stdio.h>
#include <stdlib.h>

#include <sys/wait.h>
#include <unistd.h>

#include <pthread.h>

#include <assert.h>
long sum = 0;
pthread_mutex_t sum_lock = PTHREAD_MUTEX_INITIALIZER;

typedef struct {
  long from;
  long to;
} sum_args_t;

long sum_from_to(long from, long to) {

  for (long i = from; i <= to; ++i) {
    // enter if allowed, lock entry
    //while (sum_lock) { /* wait */ };
    //sum_lock = 1;
    pthread_mutex_lock(&sum_lock);
    sum += i; // not performed atomically
    pthread_mutex_unlock(&sum_lock);
    //sum_lock = 0; //unlock
    // unlock entry, and exit

    // movq sum, %rax
    // addq %rcx, %rax
    // movq %rax, sum
//
//   sum        Thread 1          Thread 2
//   100        read 100          ---
//   100        add 12 to 100
//   112        write 112 to sum
//   112        read 112 from sum 
//   112        ---               read 112 from sum
//   112                          add 52 to 112
//   164                          write 164 to sum
//   164        add 13 112        ---
//   125        write 125 to sum
  }
  fprintf(stderr, "Completed %ld to %ld\n", from, to);
}

void *sum_thread(void *args) {
  sum_args_t *sum_args = args;
  sum_from_to(sum_args->from, sum_args->to);
  return NULL;
}

int main(int argc, char **argv) {
  assert(argc >= 3);

  long from = atol(argv[1]);
  long to = atol(argv[2]);

  pthread_t th;

  sum_args_t sum_args = { .from = from, .to = to / 2 };
  // perform sum of 'from' to 'to / 2' in helper thread 
  assert(0 == pthread_create(&th, NULL, sum_thread, &sum_args));

  // perform sum of  '(to / 2) + 1' to 'to'
  sum_from_to(to / 2 + 1, to);

  assert(0 == pthread_join(th, NULL));
  printf("%ld\n", sum);

  return 0;
}
```