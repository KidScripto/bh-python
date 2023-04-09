"""
Author: KidScripto
Date: 04-09-2023
"""


import socket
import sys, getopt


arg_list = sys.argv[1:]

try:
    opts, args = getopt.getopt(arg_list, "H:P:I:")
except getopt.GetoptError as err:
    print(f"The following error was encountered during execution:\n{err}")
    exit()

for opt, arg in opts:
    if opt in ['-H']:  #Exception handling: Should not be able to cast to INT
        host = arg
    elif opt in ['-P']:
        try: 
            port = int(arg)
        except:
            print("The following error was encountered during execution:\nCannot cast -P value to int. Please enter a valid port number.")
            exit()
    elif opt in ['-I']:
        IP = arg     #Exception handling: Should not be able to cast to INT

#Create socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect the Client
client.connect((IP,port))

##Send some data
client.send((f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode("utf-8")))

###Receive some data
response = client.recv(4096)

print(response.decode())
client.close()


'''
def show_usage():
    print("TCP_client.py usage \n\n\t TCP client is a simple python script meant to read in system arguments, attempt to connect to the defined IP and Socket and send a payload. \n\n Command options \n\n -H  Target ip address --P Port number ")
'''