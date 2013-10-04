from paramiko import SSHClient
from scp import SCPClient
import getpass
import os
import time

#server = raw_input("Server: ")
#port = int(raw_input("Port Number: "))
server = 'shell.geeksoc.org'
port = int(22)
username = raw_input("Username: ")
password = getpass.getpass("Password: ")

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(server, port, username, password)

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())

#scp.put('test2.txt')

var = os.stat('test2.txt').st_mtime
var2 = os.stat('test2.txt').st_mtime

while var == var2:
	var2 = os.stat('test2.txt').st_mtime
	time.sleep(10)

scp.put('test2.txt')