#!/usr/bin/env python

from multiprocessing import Pool
import os
import time

def sleeper((name,sec)):
    print name
    print sec
    time.sleep(2)
    print "Done sleeping"

if __name__ == "__main__":
    pool = Pool(4)
    print "parnet process (id %s)" % os.getpid()
    pool.map(sleeper,zip(range(10),range(10)))
    print "All Done"
