#!/usr/bin/env python
"""
this exercise is to test the raw_input and argv

the raw_input is to get the value of user keyborard input,
and the argv is in the command line that can be use
this is the differnt of the argv and raw_input
"""
from sys import argv

if len(argv) < 4:
    print "there must have three parameters"
    parameters = raw_input("enter three parameter ans split with spaces")
    argvariables = parameters.split(" ")
    if len(argvariables) == 3:
    	print "the scirpt name is :",argv[0]
 	print "the first variables is :",argvariables[0]
	print "the second variables is:",argvariables[1]
	print "the third valuess is:",argvariables[2]
    else:
        print "there is no more arguments here"
else:
    script,first,second,third = argv
    print "the scirpt name is :",script
    print "the first variables is :",first
    print "the second variables is:",second
    print "the third valuess is:",third
