#!/usr/bin/env python

from threading import Thread
import time
from Queue import Queue

def writeQ(queue,i):
    while True:
        time.sleep(1)
        if queue.full():
            time.sleep(1)
        else:
            queue.put('xxx')
            print 'producting object for Q..',i

def readQ(queue,i):
    while True:
        time.sleep(1)
        if queue.empty():
            time.sleep(1)
            print 'empty'
        else:
            val = queue.get()
            print 'consumed object from Q..size now:',queue.qsize(),' consumer ' ,i

class Producter(Thread):
    def __init__(self,func,args,name=''):
        super(Producter,self).__init__()
        self.name = name
        self.args = args
        self.func = func

    def run(self):
        self.res = self.func(*self.args)
        #return self.res

class Consumer(Thread):
    def __init__(self,func,args,name=''):
        super(Consumer,self).__init__()
        self.name = name
        self.args = args
        self.func = func

    def run(self):
        self.res = self.func(*self.args)
        #return self.res

if __name__ =='__main__':
    q = Queue(100)
    for i in range(20):
        p = Producter(writeQ,(q,'production %s ' % i))
        p.start()
    for i in range(2):
        c = Consumer(readQ,(q,'consumer %s ' % i))
        c.start()
