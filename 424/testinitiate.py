#!/usr/bin/env python
class Kel(object):
    def __init__(self,name):
        self.name = name
        print 'excuting the init method',self
    def __new__(cls,name):
        print 'excuting the new method',cls
        return super(Kel,cls).__new__(cls,name)

kel = Kel('kel')
