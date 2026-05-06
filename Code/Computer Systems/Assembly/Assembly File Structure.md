---
## Topic:
---
- The assembly programs we will write will have the following general structure:

```nasm
.global main    # any symbols (e.g., functions) that should be visible 
                # outside this module, need to be declared global

.text           # begin the executable code segment

main:           # start of the main function
  enter $0, $0  # set up the call stack (more next time)

  # code
  # ...
  # code
  # ...
  # code

  leave         # clean up the stack space
  ret           # return from the function

# more functions ...

.data           # beginning of the data segment
                # - this is where global variables are defined

format_string:
  .asciz "Hello, my age is: %d\n"

some_long_integer:
  .quad 42
```