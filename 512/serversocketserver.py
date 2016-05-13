#!/usr/bin/env python

import SocketServer

class MyServer(SocketServer.BaseRequestHandler):
    
    def setup(self):
        pass

    def handle(self):
        print self.client_address
        self.request.send('your are sb?')

    def finish(self):
        pass

if __name__ =='__main__':
    server = SocketServer.ThreadingTCPServer(('192.168.1.60',9999),MyServer)
    server.serve_forever()
