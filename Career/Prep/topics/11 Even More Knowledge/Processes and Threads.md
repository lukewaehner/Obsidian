---
tags:
  - career
  - interview-prep
type: note
parent: "[[Career/Prep/topics/11 Even More Knowledge/11 Even More Knowledge|11 Even More Knowledge]]"
source: coding-interview-university
---

# Processes and Threads

    - [ ] Computer Science 162 - Operating Systems (25 videos):
        - for processes and threads see videos 1-11
        - [Operating Systems and System Programming (video)](https://archive.org/details/ucberkeley-webcast-PL-XXv-cvA_iBDyz-ba4yDskqMDY6A1w_c)
    - [What Is The Difference Between A Process And A Thread?](https://www.quora.com/What-is-the-difference-between-a-process-and-a-thread)
    - Covers:
        - Processes, Threads, Concurrency issues
            - Difference between processes and threads
            - Processes
            - Threads
            - Locks
            - Mutexes
            - Semaphores
            - Monitors
            - How do they work?
            - Deadlock
            - Livelock
        - CPU activity, interrupts, context switching
        - Modern concurrency constructs with multicore processors
        - [Paging, segmentation, and virtual memory (video)](https://youtu.be/O4nwUqQodAg)
        - [Interrupts (video)](https://youtu.be/iKlAWIKEyuw)
        - Process resource needs (memory: code, static storage, stack, heap, and also file descriptors, i/o)
        - Thread resource needs (shares above (minus stack) with other threads in the same process but each has its own PC, stack counter, registers, and stack)
        - Forking is really copy on write (read-only) until the new process writes to memory, then it does a full copy.
        - Context switching
            - [How context switching is initiated by the operating system and underlying hardware?](https://www.javatpoint.com/what-is-the-context-switching-in-the-operating-system)
    - [ ] [threads in C++ (series - 10 videos)](https://www.youtube.com/playlist?list=PL5jc9xFGsL8E12so1wlMS0r0hTQoJL74M)
    - [ ] [CS 377 Spring '14: Operating Systems from University of Massachusetts](https://www.youtube.com/playlist?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)
    - [ ] concurrency in Python (videos):
        - [ ] [Short series on threads](https://www.youtube.com/playlist?list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1)
        - [ ] [Python Threads](https://www.youtube.com/watch?v=Bs7vPNbB9JM)
        - [ ] [Understanding the Python GIL (2010)](https://www.youtube.com/watch?v=Obt-vMVdM8s)
            - [reference](http://www.dabeaz.com/GIL)
        - [ ] [David Beazley - Python Concurrency From the Ground Up LIVE! - PyCon 2015](https://www.youtube.com/watch?v=MCs5OvhV9S4)
        - [ ] [Keynote David Beazley - Topics of Interest (Python Asyncio)](https://www.youtube.com/watch?v=ZzfHjytDceU)
        - [ ] [Mutex in Python](https://www.youtube.com/watch?v=0zaPs8OtyKY)

---

**Work here → [[Career/Prep/work/11 Even More Knowledge/Processes and Threads|Processes and Threads]]** · [[Career/Prep/topics/11 Even More Knowledge/11 Even More Knowledge|11 Even More Knowledge]] · [[Career/Prep/Prep|Prep]]
