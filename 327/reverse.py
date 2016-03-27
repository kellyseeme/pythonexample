#!/usr/bin/env python
"""
this is the test of reverse the string
"""
#this is reverse the chars buy using the slice
kel =  "this is a string"
revchars = kel[::-1]
print "old string:%s ,\nthe reverse string is :%s" % (kel,revchars)

#this is to rever the strings,and the reverse the strings,use the join to do 
revchars = kel.split(" ")
revchars.reverse()
print revchars
print " ".join(revchars)


print " ".join(kel.split()[::-1])
