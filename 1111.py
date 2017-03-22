import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(20)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close()


#!/usr/local/bin/python

import os
import socket
import sys


server_socket = socket.socket()
server_socket.bind(('', 2222))
server_socket.listen(11)

while True:
    client_socket, remote_address = server_socket.accept()
    child_pid = os.fork()
    if child_pid == 0:
        request = client_socket.recv(1024)
        client_socket.send(request)
        print '(child {}) {} : {}'.format(client_socket.getpeername(), request)
        client_socket.close()
        sys.exit()
    else:
        client_socket.close()

server_socket.close()