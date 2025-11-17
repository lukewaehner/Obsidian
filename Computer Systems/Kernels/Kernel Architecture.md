
# Kernel Architecture

## Kernel Space vs User Space

The operating system is divided into two distinct execution modes:

**Kernel Space (Kernel Mode):**
- Privileged execution mode with full hardware access
- Can execute any CPU instruction and access any memory address
- Reserved for core OS components that require direct hardware control

**User Space (User Mode):**
- Restricted execution mode with limited privileges
- Cannot directly access hardware or kernel memory
- Applications run in this mode for system protection

## Protection Principle

Operate in the most restricted mode you can to protect yourself from errors and mistakes.

This principle minimizes the damage that bugs or malicious code can cause. By keeping most code in user mode, the system limits what can go wrong if that code has errors.

## Cross References

- [[Monolithic Kernel]]
- [[System Calls]]
- [[Processes]]
