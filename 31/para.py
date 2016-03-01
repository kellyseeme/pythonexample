#!/usr/bin/env python
"""
this is to test the arguments has a default value

there if have the defalut value,there have more advantiages
1.use this funciton,it will be easy to pass the arguments,and it will be the best way to do it
2.there is not want to know the functions inside ,only to know how to call the function and return the values
3.the default value must behind in the positon arguments
4.the default value must be not changed object
"""
def power(x):
    return x * x

def power(x,n):
    return x**n

def power(x,n=2):
    return x**n

def kel(*args,**kw):
    print "args = ",args,"kw = ",kw


kel(1,2,3,kw = {})
kel(1,2,3,a = "kel")
