#!/usr/bin/env python
"""this is to test the strings and the text 

%r is used to debugging
%s,%d is used to display
+ is used to contact two strings
when used strings,there can used single-quotes,double-quotes
if there have a TypeError,there must be some format parameter is not suit
"""
#this is use %d to set the values
x = "there are %d typs of people." % 10
binary = "binary"
do_not = "don't"
#this is use two variables to strings and use %s
y= "those who know %s and those who %s." % (binary,do_not)

print x
print y
#use %r to set x ,%s is the string,and the %r is use the repe() function
print "I said: %r." % x
#this is use %s to se value y
print "I also said:%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#this is use hilarious to set the string of %r
print joke_evaluation % hilarious

w = "this is the left side of ..."
e = "a string with a right side."
#use + to concate the two strings
print w + e
