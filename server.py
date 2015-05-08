#!/usr/bin/env python

"""
A simple echo server
"""

import socket
import sys

host = ''
port = 50000
backlog = 5
size = 1024

sys.stdout.write('Server running on port: ' + str(port) + '\n\n')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        #client.send(data)
	sys.stdout.write('RECEIVED: \n' + data + '\n')
    client.close()
