from pwn import *

print(asm('nop'))
print(asm('nop', arch='arm'))

print("hello pwn")
