#!/usr/bin/env python
"""
this is a class to  calculate the process excution time
"""
#this is import the module
import time
import random

#this is define the class of ExcutionTime
class ExcutionTime(object):
    "this is define the class of ExcutionTime"
    def __init__(self):
        "this is the initializition ,set the start time"
        self.startTime = time.time()
    def duration(self):
        "this is get the duration time,is to get the excution time of the process"
        return time.time() - self.startTime
#get the class object
timer = ExcutionTime()
#do the process
my_list = [random.randint(1,1000) for i in range(1,10) if i%2 == 0]
print my_list
#get the excution time
print "this is waste time of %s" % timer.duration()
