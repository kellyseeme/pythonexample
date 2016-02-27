#!/usr/bin/env python
"""
this is to test the open file,so this use the write mode of open with w
and import os,must use os.linesep,then the os line sequence use
this is use while and write function
this will write the user input to the file name you input,and
use the . to quit this program
"""
import os
filename = raw_input("enter file name:")
fobj = open(filename,"w")
while True:
    aLine = raw_input("Enter a line('.' is to quit):")
    if aLine != ".":
        fobj.write("%s%s" % (aLine,os.linesep))
    else:
        break
fobj.close()
