#!/usr/bin/env python

from multiprocessing import Process
import os

def f(name):
    print 'hello',name

def info(title):
    print title
    print 'module name:,',__name__
    if hasattr(os,'getpid'):
        print 'parent process:',os.getppid()
    print 'process id:',os.getpid()

def f(name):
    info('function f')
    print 'hello',name


if __name__ == '__main__':
    info('main line')
    p = Process(target=f,args=('kel',))
    p.start()
    p.join()

def kel():
    p = Process(target=f,args=('kel',))
    p1 = Process(target=f,args=('deng',))
    p.start()
    p1.start()
    print '%d' % p.pid
    print '%d' % p1.pid
    p.join()
    p1.join()
