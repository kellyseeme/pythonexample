#!/usr/bin/env python

import string
a = raw_input("enter a string:").strip()

b = raw_input("enter another string:").strip()

a =  a.upper()

if a.find(b) == -1:
    print "this is not in the string"
else:
    print "sucecess"
