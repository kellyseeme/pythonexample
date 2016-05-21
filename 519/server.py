#!/usr/bin/env python

import time
import SocketServer

HOST = '192.168.1.60'
PORT = 9999

def recv_all(socketobj,file_name,file_size):
    f = open('/tmp/%s' % file_name,'w')
    while file_size > 0:
        if file_size <= 1024:
            data = socketobj.recv(1024)
            f.write(data)
            break
        elif file_size > 1024:
            data = socketobj.recv(1024)
            f.write(data)
            file_size -= 1024
    f.close()

class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            #1.get the commands
            data = self.request.recv(1024)
            print data
            if data.strip() == 'exit' or not data:break
            options = data.strip().split(' ')
            if len(options) == 2:
                file_name = options[1]
                if options[0] == 'put':
                    #2.get the file size
                    file_size = self.request.recv(1024)
                    print file_size
                    file_size = int(file_size)
                    #3.get the file content
                    recv_all(self.request,file_name,file_size)
                    self.request.sendall('DONE')
                elif options[0] == 'get':
                    f = open('/tmp/%s' % file_name)
                    data = f.read()
                    self.request.send(str(len(data)))
                    time.sleep(0.2)
                    self.request.send(data)
                    time.sleep(0.2)
                    self.request.send('DONE')

s = SocketServer.ThreadingTCPServer((HOST,PORT),MyHandler)
print 'waiting for connection...'
s.serve_forever()
