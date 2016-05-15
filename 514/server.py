#!/usr/bin/env python

import SocketServer
import time


HOST = '192.168.1.60'
PORT = 9999

class MyHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.read(1024)
            print data,self.client_address
            self.wfile.write( ' %s %s ' % (data,time.ctime()))
            if data == 'exit':
                break

s = SocketServer.ThreadingTCPServer((HOST,PORT),MyHandler)
s.serve_forever()
