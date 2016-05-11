#!/usr/bin/env python

from socket import *

HOST = '192.168.1.60'
PORT = 55555
s = socket()
s.bind((HOST,PORT))
s.listen(5)
conn,addr = s.accept()
print 'connected by ',addr
while True:
    data = conn.recv(1024)
    if not data:break
    conn.sendall(data)
conn.close()
    
