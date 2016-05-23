#!/usr/bin/env python

from threading import Thread
import time

def loop(name,seconds):
    print 'start loop',name,' at:',time.ctime()
    time.sleep(1)
    print 'end loop',name,' at:',time.ctime()
    
class ThreadFunc(Thread):
    def __init__(self,func,args,name=''):
        super(ThreadFunc,self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

if __name__ == '__main__':
    loops = [2,4]
    nloops = range(len(loops))
    threads = []
    print 'starting at :',time.ctime()
    for i in nloops:
        t = ThreadFunc(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    print 'all DONE at :',time.ctime()
