#!/usr/bin/env python

import socket
import threading 
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = '{} :{}'.format(cur_thread.name,data)
        self.request.sendall(response)

class ThreadTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

def client(ip,port,message):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print 'Recived:{}'.format(response)
    finally:
        sock.close()

if __name__ == '__main__':
    HOST,PORT='localhost',9999

    server =ThreadTCPServer((HOST,PORT),ThreadedTCPRequestHandler)
    ip,port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print 'Server loop running in thread:',server_thread.name
    client(ip,port,'HELLO 1')
    client(ip,port,'HELLO 2')
    client(ip,port,'HELLO 3')

    server.shutdown()
    server.server_close()

