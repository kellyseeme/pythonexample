#!/usr/bin/env python

import commands
import SocketServer

class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data: break
            cmd = data.strip()
            status,output = commands.getstatusoutput(cmd)
            #send the output size
            self.request.sendall(str(len(output)))
            #sent the content
            self.request.sendall(output)

HOST = '192.168.1.60'
PORT = 9999

s = SocketServer.ThreadingTCPServer((HOST,PORT),MyHandler)
print 'waiting for connection...'
s.serve_forever()
