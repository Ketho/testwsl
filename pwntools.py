from pwn import *

print(asm('nop'))
print(asm('nop', arch='arm'))

print("hello pwn")

log.success("This is a success message!")  # Green
log.info("This is an info message.")       # Blue
log.warn("This is a warning message!")     # Yellow
log.failure("This is a failure message.")  # Red

print(term.text.bold_red("This is bold and red!"))
print(term.text.underline("This is underlined!"))
print(term.text.bold_green("Bold green message"))
