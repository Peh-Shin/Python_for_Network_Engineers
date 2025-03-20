#! /usr/local/Python_envs/Python3/bin/python3

import paramiko
from getpass import getpass
import time

host = "csr1.test.lab"
# username = 'admin1'
# password = 'cisco'
# password = getpass("Enter password :")

session = paramiko.SSHClient()

# session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# session.load_host_keys('/home/evolve/.ssh/known_hosts')
# session.set_missing_host_key_policy(paramiko.WarningPolicy())
session.load_system_host_keys()

key_pass = getpass("Enter Private Key Password:")
key_file = paramiko.RSAKey.from_private_key_file("/home/evolve/.ssh/01_id", key_pass)

print(f"\n{'#'*50}\nConnecting to the Device {host} \n{'#'*50}")
session.connect(hostname=host,
                username=username,
                # password=password,
                pkey=key_file,
                )

DEVICE_ACCESS = session.invoke_shell()
DEVICE_ACCESS.send('term length 0\n')
DEVICE_ACCESS.send('show ip int brie\n')
DEVICE_ACCESS.send('config t\n')
DEVICE_ACCESS.send('int lo0\n')
DEVICE_ACCESS.send('no shut\n')
#DEVICE_ACCESS.send('more pyenv\n')
time.sleep(.5)
output = DEVICE_ACCESS.recv(65000)
# print (output.decode())
print (output.decode())
session.close()


