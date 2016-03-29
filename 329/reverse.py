#!/usr/bin/env python
"""
this is for a string reverse and the key word reverse
"""
#this is define a string text
chars = "this is a string"

#this is the easy way use the slice to reverse the strings by chars
print chars[::-1]

#this is use the split get the word list,then use the list reverse function ,and join to get the string
chars_list = chars.split()
chars_list.reverse()
print " ".join(chars_list)

#this is for the one line,first get the list of split,and then use the slice,and join function get the string
print " ".join(chars.split()[::-1])

#this is use the regule expretion,use the split,then the all space is have ,then there is a different of join function
import re
revsechars = re.split(r'(\s+)',chars)
revsechars.reverse()
print "".join(revsechars)

#this is used the buildin function of reversed to reverse the list,and use the join function to get string
print " ".join(reversed(chars.split()))
