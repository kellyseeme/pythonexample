#!/usr/bin/env python

class TestMethod(object):
    def foo(self,x):
        print 'excuting foo(%s,%s)' % (self,x)
    @staticmethod
    def static_foo(x):
        print 'excuting static_foo(%s)' % x
    @classmethod
    def class_foo(cls,x):
        print 'excuting class_foo(%s,%s)' % (cls,x)

kel = TestMethod()
kel.foo(1)
kel.static_foo(1)
kel.class_foo(1)
TestMethod.static_foo(1)
TestMethod.class_foo(1)
print (kel.foo)
print (kel.static_foo)
print (kel.class_foo)
