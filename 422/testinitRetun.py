#!/usr/bin/env python

class Kel(object):
    def __init__(self):
        print 'Kel class called'
class J(Kel):
    def __init__(self):
        print 'J class is called'
class M(Kel):
    def __init__(self):
        super(M,self).__init__()
        print 'M class is called'
print '-'*10
kel = Kel()
print '-'*10
j = J()
print '-'*10
m = M()
