#!/usr/bin/env python
import socket

HOST='192.168.1.60'
PORT=55555

s = socket.socket()
s.connect((HOST,PORT))
while True:
    data = s.recv(1024)
    if  data.strip():
        print 'Replay is ',data
        flag = True
        while flag:
            kel = raw_input('Question :>>')
            print 'raw_input values : %r' % kel
            if kel.strip():
                flag=False
        s.sendall(kel)
        if kel == 'exit':
            break
s.close()
