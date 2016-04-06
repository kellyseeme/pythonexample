#!/usr/bin/env python
"""
this is for a method to a variable,then this is the bound method
"""
import itertools

#this is assist function,use first argument is the predicate,this is a function,second argument is a sequence
def anyTrue(predicate,sequence):
#this return the value True or False,used to check the conditions
    return True in itertools.imap(predicate,sequence)
#this funtion s is a string,then use the function to bount the method of endswith,end have more endings is a list,then return True or False
def endsWith(s,*endings):
    return anyTrue(s.endswith,endings)

#this is the example of use the two function
import os
#use os.listdir to get the current path file
for filename in os.listdir('.'):
#use two assist functions to get the correct filename
    if endsWith(filename,'.jpeg','.gif','.jpg'):
        print filename
#this is use one function,is the assist function,bound the method of the first place
for filename in os.listdir('.'):
    if anyTrue(filename.endswith,['.jpeg','.jpg','.gif']):
        print filename
