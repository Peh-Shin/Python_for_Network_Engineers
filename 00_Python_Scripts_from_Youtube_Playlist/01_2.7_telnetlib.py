#! /usr/bin/python
from telnetlib import Telnet
cmd = raw_input('Enter the Command : ')
tn = Telnet('192.168.18.10')
tn.write('admin\n')
tn.write('admin\n')
tn.write('term length 0\n')
tn.write(cmd + '\n')
tn.write('exit\n')
print tn.read_all()
