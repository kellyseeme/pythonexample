#!/usr/bin/env python

#this is for the enumerate function,this function is to print index and the value
for index,value in enumerate(("abcdef")):
   print "this index is %s ,this value is %s " % (index,value)

#this is for the zip funciton,this zip is return the value of tuple,
#and this is iterable the index and value
for firstvalue,secondvalue in zip([1,2,3,],["abc","kel","others"]):
    print "the first list values is %s ,the second list value is %s " % (firstvalue,secondvalue)
#if the two list is not the same long,then return the smaller list length
for firstvalue,secondvalue in zip([1,2,3,4],["abc","kel","others"]):
    print "the first list values is %s ,the second list value is %s " % (firstvalue,secondvalue)
aList =[1,2,3,4]
bList =["abc","some","others"]
print "this is use the zip function to get a dictionary"
print dict(zip(aList,bList))

def add(a):
    a = a + 20
    return a
#this is use the map to call the function add,the parameter is aList
print map(add,aList)

def addab(a,b):
    c = a + b
    return c
#this is test the map function call,if there is less length,there is be a None value
#the default value is None,in the next example,the argument is the aList and cList,then
#thre is all the argument to pass
cList = [1,2,3,4]
print "this is use map to the addab function,and the argument is two list"
print map(addab,aList,cList)

#there have the some more thinkthings is the map ,if the function is None,then is usefule off the zip function,
#then the default value is None
print "this is for the map off None of the function"
print map(None,aList,bList)
