#! python3

import getpass
import telnetlib

HOST = "192.168.18.10"
# user = input("Enter your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

# tn.read_until(b"Username: ")
# tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"term length 0\n")
tn.write(b"show ver\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
