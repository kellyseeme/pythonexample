#!/usr/bin/env python

import multiprocessing
import time

def f(l,i):
    l.acquire()
    time.sleep(1)
    print 'hello',i
    l.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    for i in range(3):
        p = multiprocessing.Process(target=f,args=(lock,i))
        p.start()
    p.join()
