
---

A **process** is any running instance of a program.
- python `app.py`, `ls`, `chrome`
- Own memory space, own system resources (PID, stack, registers)

A **Daemon** is a background process running without user interaction
- Starts at boot typically, runs until shotudown
- Often now terminal (detatched from stdin/stdout/stderr)
- `cron`, `sshd`

A **Service** is a managed **daemon** 
- Controlled by a service manager like `systemd`, `launchd`
- Manager handles stop, start, restart, auto-restart policies
- Linux: `systemctl start sshd.service`

---

## CPU and Processes
- Each CPU core performs an instruction at a time, done as part of the **fetch-decode-execute cycle**

![[IMG-20251022125104271.png|350x450]]
- If you have a 4 core CPU, there are 4 FDE cycles going on at the same time
---

## Time Sharing & Limited Execution
