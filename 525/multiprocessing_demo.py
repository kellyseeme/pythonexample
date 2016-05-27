#!/usr/bin/env python

import time
import multiprocessing
import os

def info(title):
    print title
    print 'module name:',__name__
    if hasattr(os,'getppid'):
        print os.getppid()
    time.sleep(1)
    print 'process id:',os.getpid()

def f(name):
    info(name)
    print 'hello',name

if __name__ == '__main__':
    info('main line')
    print '____________'
    p = multiprocessing.Process(target=f,args=('smile',))
    p.start()
    p.join()

