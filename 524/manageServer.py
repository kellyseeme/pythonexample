#!/usr/bin/env python

import paramiko
import threading

HOSTS = ['192.168.1.170','192.168.1.165']

def run(hostname,command):
    c = paramiko.SSHClient()
    c.load_system_host_keys()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(hostname,port=22,username='root',password='root',timeout=4)
    stdin,stdout,stderr = c.exec_command(command)
    return stdout.read()

class MyThread(threading.Thread):
    def __init__(self,name,func,args):
        super(MyThread,self).__init__()
        self.name = name
        self.func = func
        self.args = args
        self.res = ''

    def run(self):
        self.res = self.func(*self.args)
        self.res = (self.name,self.res)

loops = len(HOSTS)

results = []
for i in range(loops):
    t = MyThread(HOSTS[i],run,(HOSTS[i],'df'))
    t.start()

for i in range(loops):
    t.join()
    results.append(t.res)
for i in results:
    print i[0]
    print i[1]
