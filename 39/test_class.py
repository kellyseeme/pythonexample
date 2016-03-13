#!/usr/bin/env python
"""
this is for test the class attribute
"""
#define a class of name Thing,this is the new style calss
class Thing(object):
#define a method test,and this is to print the value of test
    def test(hi):
        print "hi"

a = Thing()
#this is call the function of test,this in python will be the test(a,"hello"),then there will pass two arguments
#and this will be a error
a.test("hello")
