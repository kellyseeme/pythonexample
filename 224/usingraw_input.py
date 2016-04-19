#!/usr/bin/env python
print "Enter the file name:"
fname = raw_input(">")
txt = open(fname)
print "your file name is ",fname,"file content is : \n",txt.read()
