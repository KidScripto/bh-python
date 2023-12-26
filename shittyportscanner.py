import sys
from datetime import datetime
import socket

# Target Defintion
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid syntax")

# Banner
print('-'*50)
print(f'Scanning target: {target}')
print(f'Started at {str.datetime.now()}')
print('-'*50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f'Port {port} is open')
        s.close()

except KeyboardInterrupt:
    print("Interrupted; exiting...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except Exception as e:
    print("Unexpected error occured: {e}")
    sys.exit()
