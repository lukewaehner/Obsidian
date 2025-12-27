
# POST (Power On Self Test)

POST is a diagnostic testing sequence run by the BIOS during system boot to verify that essential hardware is functioning correctly.

## Purpose

POST ensures that critical system components are operational before attempting to load the operating system. If POST fails, the system typically won't boot.

## Components Tested

- **CPU:** Verifies processor functionality
- **Memory:** Tests RAM for errors
- **Keyboard:** Checks keyboard controller and connection
- **Handlers:** Tests interrupt handlers and system controllers
- **Additional Hardware:** Runs sub-BIOSes on peripheral devices

## Process

1. BIOS initiates POST immediately after loading
2. Each hardware component is tested in sequence
3. Sub-BIOSes on additional hardware devices run their own tests
4. BIOS may emit beep codes or display messages indicating test status
5. If all tests pass, boot process continues to bootstrap sequence
6. If tests fail, system halts or displays error information

## Test Everything Philosophy

POST is designed to test everything possible before the OS loads. This catches hardware failures early and prevents the OS from attempting to use faulty hardware.

## Cross References

- [[BIOS]]
- [[OS Boot Process]]
