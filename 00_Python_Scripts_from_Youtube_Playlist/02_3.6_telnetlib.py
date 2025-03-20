#! /data/Python_envs/Python3/bin/python3

##############################################################################################################
# This script is to telnet to a device and run a command
# The script will prompt for a command to run
# The script will then connect to the device and run the command
# The output of the command will be printed to the screen       
##############################################################################################################
    
from telnetlib import Telnet

cmd = input('Enter command (e.g., show ip int br): ')
tn = Telnet('192.168.18.10')
PASSWORD = "cisco"

tn.read_until(b"Password: ")
tn.write(PASSWORD.encode("ascii") + b"\n")

tn.write(b'terminal length 0\n')
tn.write(cmd.encode('ascii') + b'\n')
tn.write(b'exit\n')

output = tn.read_all().decode('ascii')
print("Command Output:\n" + output)

