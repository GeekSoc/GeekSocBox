from paramiko import SSHClient
from scp import SCPClient
import getpass
import os
import time
from os import listdir
from os.path import isfile, join

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

onlyfiles = [ f for f in listdir('/Users/Iain/Documents/Programming/GeekSocBox/') if isfile(join('/Users/Iain/Documents/Programming/GeekSocBox/',f)) ]

f = open("filelist.txt",'w')

print(onlyfiles)
for item in onlyfiles:
	f.write("%s\n" % item)

var = os.stat('test2.txt').st_mtime
var2 = os.stat('test2.txt').st_mtime

scp.put('test2.txt')