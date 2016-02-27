#!/usr/bin/env python
"""
this is test when we write the content or read the content,
then the position will changed,then we must remember if we 
use to methods this will change the position

1.file.tell() is get the position
2.file.seek(positon,0/1/2),position is whre to go
  and the 0 is the begining of the file,1 is the current posiotion
  2 is the end of file of position
"""
f = open("kel","w+")
print "this is the curren position"
print f.tell()

f.write("test line 1\n")
print "write some line ,then this position is :"
print f.tell()

f.write("test line 2\n")
print "this is the second line is added ,then print the position"
print f.tell()

f.seek(-12,1)
print "use the current position,then back of 12 bytes,print the position"
print f.tell()
print "the line content"
print f.readline()
f.seek(0,0)
print "to the file begging positon"
print f.readline()
print "this is read the first line and print the positon"
print f.tell()
print f.readline()
print "this is the second line and print the positon"
print f.tell()
f.close()
