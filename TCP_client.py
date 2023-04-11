"""
Author: KidScripto
Date: 04-09-2023
"""
#! ./bhpy/bin/ python3.10

import socket
import sys, getopt
import argparse

#Arguments Definition
parser = argparse.ArgumentParser(description="Get Hostname, Port number and IP address of the target server.")
parser.add_argument('-n', '--hostname', help='Target Hostname', required=False, type=str)
parser.add_argument('-p', '--port', help='Target port', required=True, type=int)
parser.add_argument('-i', '--ip_address', help='Target IP address', required=True, type=str)
args = parser.parse_args()

#Argument Validation
##
#Create socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect the Client
client.connect((args.ip_address,int(args.port)))

##Send some data
client.send((f"GET / HTTP/1.1\r\nHost: {args.hostname}\r\n\r\n".encode("utf-8")))

###Receive some data
response = client.recv(4096)

print(response.decode())
client.close()


'''
def show_usage():
    print("TCP_client.py usage \n\n\t TCP client is a simple python script meant to read in system arguments, attempt to connect to the defined IP and Socket and send a payload. \n\n Command options \n\n -H  Target ip address --P Port number ")
'''