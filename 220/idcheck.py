#!/usr/bin/env python
import keyword

aStr = raw_input("enter a string name:").strip()

if aStr in keyword.kwlist:
    print "this is the check name!"
else:
   print "good name"
