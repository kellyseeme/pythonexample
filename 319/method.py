#!/usr/bin/env python
"""
this is for test the the method of class
"""
#this is define a new style class
class MyClass(object):
#define a method of the class,then there is use the self pramater
    def foo(self,x):
        print "this is the method of a class, %s %s" % (self,x)

#this is a static method,and the static not have the argument of the class
    @staticmethod
    def static_method(x):
        print "this is the class of static method %s " % x

#this is the class method ,there have the class is passed the parameters
    @classmethod
    def class_method(cls,x):
        print "this is the class method, %s %s " %(cls,x) 

#there have two ways to used the class method and the static method,use the instance or use the class
MyClass.static_method("class method of class")
MyClass.class_method("static method of class")
#if call the plain method ,must use the instance,python for call the method of class,must pass the instant parameter
mc = MyClass()
mc.foo(1)
mc.static_method("static method of instance")
mc.class_method("class method of instance")
#in this class there have the method of static method and the class method,if the class have the sub class,then
#the subclass will inherit the static method and the class method
