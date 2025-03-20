#! /usr/local/Python_envs/Python3/bin/python3

import paramiko
from getpass import getpass
import time

host = "csr1.test.lab"
# username = 'admin1'
# password = 'cisco'
# password = getpass("Enter password :")

cmd1 = ["show ip int brie",
        "config t",
        "int loopback0",
        "ip address 1.1.1.1 255.255.255.0",
        "no shut",
        "int loopback1",
        "ip address 5.5.5.5 255.255.255.0",
        "no shut",
        "do sh ip int brie",
        "exit"]
cmd2 = ["show run int lo0",
        "show run int lo5",
        "abc"]

session = paramiko.SSHClient()

# session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# session.load_host_keys('/home/evolve/.ssh/known_hosts')
# session.set_missing_host_key_policy(paramiko.WarningPolicy())
session.load_system_host_keys()

# key_pass = getpass("Enter Private Key Password:")
key_file = paramiko.RSAKey.from_private_key_file("/home/evolve/.ssh/id_rsa")

def cisco_exec(ip,commands):
    print(f"\n{'#'*50}\nConnecting to the Device {ip} \n{'#'*50}")
    try:
        session.connect(hostname=ip,
                        username=username,
                        # password=password,
                        pkey=key_file,
                        )

        DEVICE_ACCESS = session.invoke_shell()
        for command in commands:
                DEVICE_ACCESS.send(f"{command}\n")
                time.sleep(.5)
                output = DEVICE_ACCESS.recv(65000)
                print (output.decode(), end='')
            # print (output.decode('ascii'),end='')

        session.close()
    except:
        print("Can not connect to the device")


cisco_exec('csr1.test.lab',cmd1)
cisco_exec('csr1.test.lab',cmd2)
cisco_exec('192.168.0.23',cmd1)


print(f"\n{'#'*50}\nFinished Executing the script \n{'#'*50}")

