Processes:
	Process management
	Creating processes
	Understanding system calls
	How the OS manages a process, behavior that is available
	Memory access, what is available and what is not

Virtual Memory Management:
	Paging
	Address Translation
	

Concurrency:
	What is shared between threads vs processes
	Basic mechanics of mutexes

File I/O:

Some Kernels.


No repeats from Exam 1, but assumed knowing C + Assembly, state of stack at this point, etc.

<!-- Start After Here -->

# Processes:
- Any running instance of a program, with its own memory space, and system stack
- Each CPU core performs Fetch-decode-execute cycle
- Time-sharing - multiple programs starting, running for a bit, then switching between
	- Scheduling (Obtaining CPU) vs Descheduling (Freeing CPU usage from self)
- Interrupts:
	- Async (Hardware) interrupts
		- Data arrival, Ctrl + C
	- Sync interrupts
		- Traps
			- Intentional, always recoverable
				- System calls, breakpoints
		- Faults
			- Unintentional, recoverable
				- page faults, floating point exceptions
		- Aborts
			- Unintentional, unrecoverable
				- Illegal instructions, RAM Parity errors
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <assert.h>
#include <sys/wait.h>
int main(int argc, char **argv) {
	pid_t p = fork();
	assert(p != -1); // Check fork worked
	
	if (p == 0) { // <-- Child -->
		execl("/bin/ls", "ls", "-l", NULL); // Child turns to LS
		_exit(42); // If needed
	} else { // <-- Parent -->
		int status;
		pid_t child = wait(&status);
		printf("Parent: child %d, code %d\n", child, WEXITSTATUS(status));
	}
}
```

- **wait**:
	- Parent process to wait for one of its child processes to finish
	- The print line will not wait until the child finishes execution
- **exec**:
	- After fork, to run a different program call exec()
	- PID -> stays the same
	- Address space -> replaced with new program
	- Code, heap, stack, globals -> discarded
	- Open FDs -> usually preserved unless marked closed-on-exec
	- Important note, **exec()** will return in a child process so code defined after exec will not run **UNLESS** an error occurs. The bubble up from parent will run though.

# File IO:
- Collections of bytes that can be read, written, and addressed using a name
- Properties:
	- User owner
	- Group owner
	- R/W/X permission for user/group/other
	- Access, modification, creation dates
	- Size
- Files get 3 default descriptors upon start up
	- 0 - Standard input (stdin)
	- 1 - Standard output (stdout)
	- 2 - Standard error output (stderr)

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int open(const char *pathname, int flags);
int open(const char *pathname, int flags, mode_t mode);
```
- A filename (with path) and flags
- Flags are specifics on how a flag should be open
- Access mode flag (required one):
	- O_RDONLY - Read only
	- O_WRONLY - Writing only
	- O_RDWR - Reading and Writing
- Others:
	- O_APPEND - writing will add to end of the file
	- O_CREAT - create if not existed, mode is required if this is used
	- O_TRUNC - File is set to 0 (restarted)
- Use multiple with chaining
	  `open("foo.txt", O_RDWR | O_CREAT | O_TRUNC, 0644)`
	  0644 corresponds to rw-r--r-- (User r/w, group read, others read)
- Successful opens return a file descriptor $\geq$ 0
- Errors return -1, errno variable is set to error code
- To close: call close with file descriptor as argument