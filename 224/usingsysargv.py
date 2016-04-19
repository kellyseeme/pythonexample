#!/usr/bin/env python
from sys import argv
script,fname = argv
f = open(fname)
print "Your file name is ",script,f.read()
