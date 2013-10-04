from paramiko import SSHClient
from scp import SCPClient
import getpass
import os
import time
from os import listdir
from os.path import isfile, join

dot = '.'
files = []
times = []
filelist = open("filelist.txt",'r')
timelist = open("timelist.txt",'r')
for filename in filelist:
	files.append(filename.rstrip())

for filetime in timelist:
	times.append(filetime.rstrip())

filelist.close()
timelist.close()

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

try:
    while True:
        for i in range(len(times)):
        	if files[i][:1] != dot:
        		if times[i] < os.stat(files[i]).st_mtime:
        			scp.put(files[i])
        			times[i] = os.stat(files[i]).st_mtime 
        			print "update"
except KeyboardInterrupt:
    pass # do cleanup here

files = [ f for f in listdir('/Users/Iain/Documents/Programming/GeekSocBox/') if isfile(join('/Users/Iain/Documents/Programming/GeekSocBox/',f)) ]

filelist = open("filelist.txt",'w')
timelist = open("timelist.txt",'w')

for i in range(len(files)):
	filelist.write("%s\n" % files[i].rstrip())
	timelist.write("%s\n" % times[i].rstrip())


filelist.close()
timelist.close()

scp.put('test2.txt')