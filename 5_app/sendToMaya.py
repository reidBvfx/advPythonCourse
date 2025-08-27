#######################################################################
# Sends the file to maya to be executed, also adds the whole folder into
# the environment before executing and removes it after
#
# Requires this mel command to be run in maya first in a userSetup.mel file
# commandPort -n "localhost:7001" -stp "python";
#
#######################################################################
import os
import sys
import socket
 
HOST = 'localhost'  # the local host
PORT = 7001         # The same port as used by the server
 
file = sys.argv[1]
 
folder_dir = os.path.abspath(os.path.dirname(file))
script_dir = sys.argv[1]
 
# Code to send test script to maya
code = (
    "print(r'# Running {} #')\n".format(file)
    + "import sys\n"
    + "current_directory = r'{}'\n".format(folder_dir)
    + "file = r'{}'\n".format(script_dir)
    + "if current_directory not in sys.path:\n"
    + "\tsys.path.insert(0,current_directory)\n"
    + "try:\n"
    + "\texec(open(file).read(), globals())\n"
    + "\tprint('# Successfully Ended #')\n"
    + "except:\n"
    + "\tprint('# Error while running #')\n"
    + "\tprint(sys.exc_info()[1])\n"
    + "del(sys.path[0])\n"
)
 
# Create a socket and connect
# TODO: Check if connection failed
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
 
# Send the command to maya
client.sendall(code.encode())
 
# Receive erros
# TODO: This should be in a while just in case msg is longer than 4096
# '\n\x00' is the message terminator
 
data = client.recv(4096)
print("\nError: %s" % data.decode())
 
client.close()