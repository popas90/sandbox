import socket
import sys
from _thread import *


HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

s.listen(10)
print('Socket listening...')


def clientthread(conn):
    conn.send(bytes('Welcome to the server!\n', 'utf-8'))
    while True:
        data = conn.recv(1024)
        reply = 'OK...' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(bytes(reply, 'utf-8'))
    conn.close()

# now keep talking with the client
while True:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    start_new_thread(clientthread, (conn,))

s.close()
