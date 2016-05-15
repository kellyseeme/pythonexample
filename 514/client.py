#!/usr/bin/env python

import socket

HOST = '192.168.1.60'
PORT = 9999

s = socket.socket()
s.connect((HOST,PORT))
while True:
#    s = socket.socket()
#    s.connect((HOST,PORT))
    kel = raw_input('>>>')
    s.sendall(kel + '\n')
    print s.recv(1024)
    if kel == 'exit':
        break
s.close()
