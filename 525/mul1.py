#!/usr/bin/env python

from multiprocessing import Queue,Process
from threading import Thread
def f(q,n):
    #q.put([n,'hello'])
    q.append(n)

if __name__ == '__main__':
    #q =Queue()
    q = []
    for i in range(5):
        p = Process(target=f,args=(q,i))
        p.start()
    print q
    for i in range(5):
        print q
