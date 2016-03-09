#!/usr/bin/env python
"""
this is to test the list function
"""
#this is define a list ,and give some value to the list
animals = ["bear","tiger","penguin","zebra"]
#this is to get the list of first value
bear = animals[0]
print bear

#at the end of the list ,add a list value,use append function
animals.append("kel")
print animals
#pop the value of the end of the list
animals.pop()
print animals
#sort the list use the lis.sort() function
animals.sort()
print animals
#this is used to change the direction of the list
animals.reverse()
print animals
#this is to change the value of the list,to insert the direct position
animals.insert(0,"kel")
print animals
#this is to count the list value,have some values then will conut it
print animals.count("kel")
#this is to remove the value off the list
animals.remove("kel")
print animals
#this is get the list value of the index,sso can have the value of index
print animals.index("bear")
