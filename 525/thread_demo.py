#!/usr/bin/env python

import multiprocessing
import time

def walker():
    time.sleep(100)


for i in range(1100):
    t = multiprocessing.Process(target=walker)
    t.start()

    print t.name

