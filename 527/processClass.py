#!/usr/bin/env python

import multiprocessing

class MyProcess(multiprocessing.Process):
    def __init__(self,name,func,args):
        super(MyProcess,self).__init__()
        self.name = name
        self.func = func
        self.args = args
        self.res = ''

    def run(self):
        self.res = self.func(*self.args)

def func(name,q):
    print 'start process...'
    child_conn.send(name.upper())

if __name__ == '__main__':
    processes = []
    parent_conn,child_conn = multiprocessing.Pipe()
    for i in range(3):
        p = MyProcess('process',func,('kel',child_conn))
        processes.append(p)
    for i in processes:
        i.start()
    for i in processes:
        i.join()
    for i in processes:
        print parent_conn.recv()
