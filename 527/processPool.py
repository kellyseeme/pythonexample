#!/usr/bin/env python

import multiprocessing
import time
def func(name):
    print 'start process'
    time.sleep(2)
    return name.upper()

if __name__ == '__main__':
    results = []
    p = multiprocessing.Pool(5)
    for i in range(7):
        res = p.apply_async(func,args=('kel',))
        results.append(res)
    for i in results:
        print i.get(2.1)
    #print p.map(func,['kel','smile'])
    #print '------------------'
    #for i in  p.imap(func,['kel','smile']):
    #    print i

