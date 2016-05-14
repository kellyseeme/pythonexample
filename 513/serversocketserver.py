#!/usr/bin/env python

import SocketServer

class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print self.request.recv(1024),self.client_address
        self.request.sendall('this is a handler of file')

HOST = '192.168.1.60'
PORT = 9999
tcpserver = SocketServer.ThreadingTCPServer((HOST,PORT),MyHandler)
print ' waiting for conenctions...'
tcpserver.serve_forever()
