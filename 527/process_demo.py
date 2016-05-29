#!/usr/bin/env python

import multiprocessing
import os
import time
def kel(name):
    print name
    print os.getppid()
    time.sleep(100)

if __name__ == '__main__':
    print os.getppid()
    print os.getpid()
    for i in range(12):
        p = multiprocessing.Process(target=kel,args=('kel',))
        p.start()
    p.join()
