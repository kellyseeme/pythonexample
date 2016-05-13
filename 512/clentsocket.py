#!/usr/bin/env python

import socket

ip_port = '192.168.1.60',9999

s = socket.socket()
s.connect(ip_port)
while True:
    kel = s.recv(1024)
    print 'this is get the data:',kel
    data = raw_input('>>>')
    s.sendall(data)
    if data == 'exit':
        break
s.close()
