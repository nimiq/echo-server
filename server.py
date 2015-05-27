#!/usr/bin/env python

"""
A simple echo server.

Launch it with:
$ ./server.py
or:
$ ./server.py xml '<?xml version="1.0" encoding="UTF-8" ?><methodResponse><params>\n<param><value><struct>\n<member><name>success</name><value><i4>1</i4></value></member>\n</struct></value></param>\n</params></methodResponse>\n\n\n'

Test it with curl:
curl http://127.0.0.1:50000/api/order/add_order/ -d "id=123456&customer=509347002&reason=whatever&description=nowayyy"
"""

import socket
import sys
import time
from datetime import datetime


def main():
    host = ''
    port = 50000
    backlog = 5
    size = 1024*1024

    sys.stdout.write('%s Server running on port: %s\n' % (datetime.now(), port))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.bind((host,port))
    s.listen(backlog)

    # Loop forever.
    while True:
        # Read the request.
        client, address = s.accept()
        data = client.recv(size)
        # Print the content of the request.
        if data:
            sys.stdout.write('\n\n%s RECEIVED: \n%s\n' % (datetime.now(), data))
        else:
            sys.stdout.write('RECEIVED: \nNo data.\n')
        sys.stdout.flush()
        # Send the response.
        send_response(client)

    client.close()


def send_response(client):
    is_xml = 'xml' in sys.argv[1]
    xml_body = sys.argv[2].replace('\\n', '\n')
    body = 'This is the body of this message\n' if not is_xml else xml_body
    headers = 'Content-Type: text/%s\n' % ('xml' if is_xml else 'plain') + \
              'Content-Length: %s\n' % len(body) + \
              'Connection: close\n'
    client.send('HTTP/1.1 200 OK\n')
    client.send(headers)
    client.send('\n')
    client.send(body)


if __name__ == '__main__':
    main()