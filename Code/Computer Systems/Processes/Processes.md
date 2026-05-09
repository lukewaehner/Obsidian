
---
See:
[[Code/Topics/Computer Systems/Processes/File IO|File IO]]
[[Creating New Processes]]
[[Concurrency|Concurrency]] - Process-based vs thread-based concurrency

---
A **process** is any running instance of a program.
- python `app.py`, `ls`, `chrome`
- Own memory space, own system resources (PID, stack, registers)

A **Daemon** is a background process running without user interaction
- Starts at boot typically, runs until shutdown
- Often now terminal (detached from stdin/stdout/stderr)
- `cron`, `sshd`

A **Service** is a managed **daemon** 
- Controlled by a service manager like `systemd`, `launchd`
- Manager handles stop, start, restart, auto-restart policies
- Linux: `systemctl start sshd.service`

---

## CPU and Processes
- Each CPU core performs an instruction at a time, done as part of the **fetch-decode-execute cycle**

![[IMG-20251224201244606.png|350x450]]
- If you have a 4 core CPU, there are 4 FDE cycles going on at the same time
---

## Time Sharing & Limited Execution

- Multiple programs can start, each runs for a bit, then we switch to the next one
- This is called *time sharing*
- Each process can be running or ready
- We will need more than two states to manage the processes?
	- Disk reads and network requests are expensive
-  A third state - *blocked*, will be helpful, to signal that some [[Code/Topics/Computer Systems/Processes/File IO|File IO]] operation is in progress and it cannot run until the operation is completed
	- The OS is also in charge of returning the result to the process

---
### Scheduling
- Letting the process take control of the CPU

### Descheduling
- Removing the process from the CPU to use it for something else

---

## Cooperative Multitasking
- The process can give back control of the CPU to the OS
- Each program runs, rests, passes control to the OS, which schedules another pgoram

- But what if your program has
```c
while (1) {
}
```

> How do we get control back from a non-cooperating program?
---

## Interrupts

Asynchronous (Hardware) Interrupts
- Caused by external events
- Timer interrupts, Ctrl + C, data available from disk, data arrives from net

Synchronous
- Traps
	- Intentional triggers
		- System calls
		- Breakpoints
	- System calls are the primary mechanism of how user programs interact with the OS
	- Used to request a service from the OS - Service code needs to execute in privileged mode
- Faults
	- Unintentionally triggered
	- Potentially recoverable
	- Page faults, floating point exception
- Aborts
	- Unintentionally triggered
	- Unrecoverable
	- Illegal instruciton, RAM parity errors

%% Begin Waypoint %%
- [[Creating New Processes]]
- [[File Descriptors]]
- [[File IO]]

%% End Waypoint %%
