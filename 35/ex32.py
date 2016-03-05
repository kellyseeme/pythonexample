#!/usr/bin/env python
"""
this is the list and for the loop of for
"""
#this is to define a number list
the_count = [1,2,3,4,5]
#this is define a string list
fruits =["apples","oranges","pears","apricots"]
#this is the number and string list
change = [1,"pennies",2,"dimes",3,"quarters"]

#this is the for loop list numers
for number in the_count:
    print "This is count %d " % number

#this is the other of loop of strings
for i in change:
    print "I got %r" % i

#this is define a empty list
elements = []
#this is a range to addling to a list,and used the list function is append
for i in range(0,6):
    print "Adding %d to the list." % i
    elements.append(i)

#this is element of for loop to print the list
#this is the elements add of the list,and then print it
for i in elements:
    print "Element was: %d " % i
aList =[]
aList = [i for i in range(0,6)]
print aList
