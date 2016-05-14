#!/usr/bin/env python

import socket

HOST = '192.168.1.60'
PORT = 9999

while True:
    s = socket.socket()
    s.connect((HOST,PORT))
    kel = raw_input('>>>')
    s.sendall(kel)
    data=s.recv(1024)
    print data
    s.close()
