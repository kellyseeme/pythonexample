#!/usr/bin/env python

from multiprocessing import Pool
import multiprocessing
import time

def f(x):
    print 'start...',x
    time.sleep(21)
    print 'end...',x
    return 'kel'


if __name__ == '__main__':
    p = Pool(500)
    results = []
    for i in  range(1000):
        res = p.apply_async(f,(i,))
        results.append(res)
    for i in results:
        print i.get()
    #for i in p.imap(f,range(10)):
    #    print i
    print 'all process in started'
    print multiprocessing.cpu_count()
    #p.close()
    #p.join()
    print 'subprocess is done'
