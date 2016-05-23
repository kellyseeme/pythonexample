#!/usr/bin/env python

import threading
import time

num = 0

def fun(n):
    time.sleep(1)
    lock.acquire()
    global num
    num += 1
    print '%s' % num
    lock.release()

#lock = threading.Lock()

lock = threading.RLock()
for i in range(210):
    t = threading.Thread(target=fun,args=(i,))
    t.start()
