from paramiko import SSHClient
from scp import SCPClient
import getpass

server = raw_input("Server: ")
port = int(raw_input("Port Number: "))
username = raw_input("Username: ")
password = getpass.getpass("Password: ")

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(server, port, username, password)

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())

scp.put('test2.txt')