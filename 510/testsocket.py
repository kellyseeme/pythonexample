#!/usr/bin/env python
import sys,os
import socket

def retBanner(ip,port):
    socket.setdefaulttimeout(2)
    kel = socket.socket()
    try:
        kel.connect((ip,port))
        return kel.recv(1024).strip()
    except:
        return None

def checkVulns(banner,filename):
    for i in open(filename):
        if banner == i.strip():
            return 'server is vulnerble ',banner
            break
    return None

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print filename,' doest exist'
            exit(0)
        if not os.access(filename,os.R_OK):
            print 'access denied ',filename
            exit(0)
    else:
        print 'usage:' ,sys.argv[0] +' <vuln filename>'
        exit(0)
    
    portlist=[21,22,80,443]
    for x in range(165,166):
        ip = '192.168.1.'+str(x)
        for port in portlist:
            banner = retBanner(ip,port)
            kel = checkVulns(banner,filename)
            if kel:
                print ip,port,':',kel
        
if __name__ == '__main__':
    main()
