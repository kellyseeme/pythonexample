#!/usr/in/env python
import sys
print "this is your script name: ",sys.argv[0]

for i,content in enumerate(sys.argv[1:]):
    print "the ",i,"parameter content is ",content
