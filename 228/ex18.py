#!/usr/bin/env python
"""
this execise is to test the function

there is define a function use def ,and there have a name of the function,
then there have the arguments ,and there have a colon,and have the indent to start
the funtion
"""

#this function is used like the sys.argv,there can unpack the *args to the arguments
#use the *args this is put all arguments in args is a list,like the sys,argv parameter
def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r,arg2:%r" % (arg1,arg2)

#this function is used to the two arguments,because the *args is pointness,just use two arguments,and prints it
def print_two_again(arg1,arg2):
    print "arg1: %r,arg2:%r" % (arg1,arg2)

#this function is used for one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this funciton we used to no arguments,and do some printing
def print_none():
    print "I got nothin.."

#there is to use the function ,and to do some what we want
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
