#!/usr/bin/env python

from socket import *

HOST='192.168.1.60'
PORT=9999

s = socket()
s.connect((HOST,PORT))
while True:
    message = raw_input('send message:>>')
    s.sendall(message)
    data = s.recv(1024)
    print data
s.close()
