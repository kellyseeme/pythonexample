#!/usr/bin/env python
"""
this exercise is for test :
first is use module ,we will see from sys import argv,then learn how to use modules
the second is to use argv,if we use the import sys,then must use sys.argv

must know the argv is a list,and the first parameter is the scipt name
"""
from sys import argv
script,first,second,third = argv

print "the script is called",script
print "the first variable is:",first
print "Your second variable is :",second
print "Your third variable is:",third
