#!/usr/bin/env python

class PositiveInteger(int):
    def __init__(self,value):
        super(PositiveInteger,self).__init__(self,abs(value))
    def __new__(cls,value):
        super(PositiveInteger,cls).__new__(cls,abs(value))

k = PositiveInteger(-3)
print k
