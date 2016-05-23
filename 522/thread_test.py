#!/usr/bin/env python

from threading import Thread
from time import sleep

i=0
def testThread():
    print i 

while True:
    i += 1
    t = Thread(target=testThread)
    t.start()
