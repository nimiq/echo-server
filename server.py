#!/usr/bin/env python

"""
A simple echo server.

You can test it with curl:
curl http://127.0.0.1:50000/api/order/add_order/ -d "id=123456&customer=509347002&reason=whatever&description=nowayyy"
"""

import socket
import sys
import time


def main():
    host = ''
    port = 50000
    backlog = 5
    size = 1024

    sys.stdout.write('Server running on port: ' + str(port) + '\n\n')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.bind((host,port))
    s.listen(backlog)
    while 1:
        client, address = s.accept()
        data = client.recv(size)
        if data:
            #client.send(data)
    	   sys.stdout.write('RECEIVED: \n' + data + '\n')

        #time.sleep(2)
        send_response(client)
        client.close()


def send_response(client):
    body = 'This is the body of this message\n'
    headers = 'Content-Type: text/html\n' + \
              'Content-Length: %s\n' % len(body) + \
              'Connection: close\n'

    client.send('HTTP/1.1 200 OK\n')
    client.send(headers)
    client.send('\n')
    client.send(body)


if __name__ == '__main__':
    main()