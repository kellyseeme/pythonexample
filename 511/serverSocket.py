#!/usr/bin/env python

import socket

HOST='192.168.1.60'
PORT=55555

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
#s.listen(10)
while True:
    conn,addres = s.accept()
    conn.send('HELLO')
    while True:
        data = conn.recv(1024)
        print data,addres
        if data =='exit':
            print 'byebye'
            break
        if not data.strip():
            continue
        flag = True
        while flag:
            info = raw_input('Answer:>>')
            if info.strip():
                flag=False
        conn.sendall(' %s' % info)
    conn.close()
