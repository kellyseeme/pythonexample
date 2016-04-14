#!/usr/bin/env python
'this is the class of get the inside dictionary'

class Bunch(object):
    def __init__(self,**kwds):
        self.__dict__.update(kwds)

y=3
x=4
threshold=15
point = Bunch(dataum=y,squared=y*y,coord=x)
if point.squared > threshold:
    point.isok = True
print point.squared

class EventSimpleBunch(object):
    def __init__(self,**kwds):
        self.__dict__ = kwds
        self.name = 'kel'

d = {'foo':'bar'}
x = EventSimpleBunch(**d)
print x.foo,x.name
x = Bunch(**d)
print x.foo
print d
x = EventSimpleBunch(**d)
print x.foo
print d
