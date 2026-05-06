

## fork()

The `fork()` system call creates a new process by duplicating the calling process.

```c
#include <unistd.h>
pid_t fork(void);
```

**Return Value:**
- **In parent process:** Returns child's PID (> 0)
- **In child process:** Returns 0
- **On error:** Returns -1

### Example

```c
#include <stdio.h>
#include <unistd.h>
#include <assert.h>

int main(int argc, char **argv) {
	printf("Before forking. PID=%d\n", getpid());
	
	pid_t child = fork();
	assert(child != -1); // Check fork succeeded
	
	printf("After forking. Fork returned %d. PID=%d\n", child, getpid());
	
	if(child == 0) {
		printf("Only printed in child process.\n");
		exit(0);
	} else {
		printf("Only printed in parent process.\n");
	}
	
	return 0;
}
```

### What fork() Does

After `fork()`:
- Child process is created with **copy of parent's memory**
- Child gets its own PID
- Child has **same code, but separate execution**
- Both processes continue from the point after `fork()`

---

## wait()

The `wait()` system call makes the parent process wait for a child process to finish.

```c
#include <sys/wait.h>
pid_t wait(int *status);
```

**Purpose:**
- Parent waits for **one** of its child processes to terminate
- Retrieves exit status of child
- Prevents zombie processes

**Return Value:**
- Returns PID of terminated child
- Returns -1 on error

### Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
	pid_t p = fork();
	
	if (p == 0) {
		// Child
		printf("Child process running\n");
		exit(42); // Exit with status 42
	} else {
		// Parent
		int status;
		pid_t child = wait(&status);
		
		if (WIFEXITED(status)) {
			int exit_code = WEXITSTATUS(status);
			printf("Child %d exited with code %d\n", child, exit_code);
		}
	}
	
	return 0;
}
```

**Important:** Code after `wait()` will NOT execute until the child finishes.

---

## exec()

The `exec()` family of functions replaces the current process image with a new program.

```c
#include <unistd.h>

int execl(const char *path, const char *arg, ...);
int execlp(const char *file, const char *arg, ...);
int execle(const char *path, const char *arg, ..., char *const envp[]);
int execv(const char *path, char *const argv[]);
int execvp(const char *file, char *const argv[]);
int execve(const char *path, char *const argv[], char *const envp[]);
```

### What exec() Does

**Replaces current process with new program:**
- **PID** → Stays the same
- **Address space** → Replaced with new program
- **Code, heap, stack, globals** → Discarded and replaced
- **Open file descriptors** → Usually preserved (unless marked `O_CLOEXEC`)

**Critical Behavior:**
- `exec()` does **NOT return** on success
- Only returns (-1) if an error occurs
- Code after `exec()` only runs if exec fails

### Example: fork + exec Pattern

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
	
	if (p == 0) { // Child
		execl("/bin/ls", "ls", "-l", NULL);
		// Only reached if exec fails
		perror("exec failed");
		_exit(1);
	} else { // Parent
		int status;
		pid_t child = wait(&status);
		printf("Parent: child %d finished with code %d\n", 
		       child, WEXITSTATUS(status));
	}
	
	return 0;
}
```

---

## Copy-on-Write (COW)

Modern operating systems optimize `fork()` using **Copy-on-Write**:

**After fork():**
- Parent and child share the same physical memory pages
- Pages are marked **read-only** in both processes
- Virtual pages appear duplicated, but point to same physical memory

**On write attempt:**
1. Page fault occurs (because page is read-only)
2. OS creates a **private copy** of the page
3. Updates page table to point to new copy
4. Marks new page as writable

**Benefits:**
- Reduces memory overhead
- Faster fork() operation
- Only copy pages that are actually modified

---

## Common Pattern: Shell Command Execution

Shells use fork + exec to run commands:

```c
// Simplified shell command execution
pid_t pid = fork();

if (pid == 0) {
	// Child: execute the command
	execvp(command, args);
	perror("Command failed");
	exit(1);
} else {
	// Parent: wait for command to finish
	wait(NULL);
}
```

---

## Related Concepts

- [[Processes]]
- [[File Descriptors]]
- [[Code/Topics/Computer Systems/Processes/File IO]]
- [[Memory Virtualization|Memory Virtualization]] - Copy-on-Write

## Tags
#computer-systems #processes #fork #exec #wait #system-calls