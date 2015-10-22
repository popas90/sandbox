import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Failed to create socket. Error code: {0}, Error message: {1}"
          .format(str(msg[0]), msg[1]))
    sys.exit()
print("Socket created")

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting...')
    sys.exit()

print('IP address of {0} is {1}'.format(host, remote_ip))

s.connect((remote_ip, port))
print('Socket connected to {0} on IP {1}'.format(host, remote_ip))

# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    # Set the whole string
    s.sendall(bytes(message, 'UTF-8'))
except socket.error:
    # Send failed
    print('Send failed')
    sys.exit()

print('Message sent successfully')

# Now receive data
reply = s.recv(4096)

print(reply)

s.close()
