##############################################################################################################
# 1. This script is to connect to a remote device using paramiko library.
# 2. The script will prompt for a password to connect to the device.
# 3. The script will then connect to the device and run the command.
# 4. The output of the command will be printed to the screen.
# 5. The script will then close the connection to the device.
##############################################################################################################

#! /data/05_Atom_Demo/Atom_P3.6/bin/python3.6
import paramiko
import time
from getpass import getpass
ip = '192.168.18.10'
username = 'pshin'
password = getpass()

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username="pshin",
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'term length 0\n')
DEVICE_ACCESS.send(b'show run\n')
time.sleep(5)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))
SESSION.close()
