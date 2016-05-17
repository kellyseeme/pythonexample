#!/usr/bin/env python
import socket

s = socket.socket()
HOST = '192.168.1.60'
PORT = 9999

def recv_all(s,file_size):
    results = ''
    file_size = int(file_size)

    while file_size > 0:
        if file_size <= 1024:
            results += s.recv(1024)
            break
        else:
            results += s.recv(1024)
            file_size -= 1024
    return results

s.connect((HOST,PORT))
while True:
    data = raw_input('>>>')
    if not data:break
    if data.strip() == 'exit':
        break
    s.sendall(data)
    if not data:break
    #first time get the size of the file
    file_size = s.recv(1024)
    contens = recv_all(s,file_size)
    print contens
s.close()

