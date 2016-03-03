#!/usr/bin/env python
"""
this is for lambda test
"""

#lambda is a no name of function,there can have more parameters
#lambda can give this function to a argument,then can give it to a value
a = lambda x:x **x
print a(6)

#this is for the lambda and the map function
#map of the first the function of lambda function,and return the values
aList = [1,2,3]
print map(lambda x:x **x,aList)
