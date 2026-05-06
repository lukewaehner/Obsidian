
# BIOS (Basic Input/Output System)

BIOS is firmware stored on the motherboard that initializes hardware during the boot process before handing control to the operating system.

## Location

- Stored in ROM (Read-Only Memory) on the motherboard
- Non-volatile storage that persists without power

## Responsibilities

### 1. Initial Loading
- First code that runs when computer powers on
- Loaded automatically by the motherboard

### 2. Configuration
- Loads user settings saved from previous sessions
- Applies hardware configuration preferences

### 3. Hardware Initialization
- Performs basic tests on system hardware
- Sets up initial configurations for devices
- Establishes communication with connected hardware

### 4. Sub-BIOS Execution
- Runs sub-BIOSes on additional hardware devices
- Graphics cards, network cards, and storage controllers may have their own firmware
- Allows specialized hardware to initialize itself

### 5. Boot Handoff
- After POST completes, initiates bootstrap sequence
- Transfers control to boot loader

## Cross References

- [[OS Boot Process]]
- [[POST]]
- [[MBR]]
