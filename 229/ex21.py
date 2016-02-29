#!/usr/bin/env python
"""
this is to test the function can return some values

this is also the functions can be call of the another function.
this is used to the return values then can use this to another functions parameter
"""
def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b
def subtract(a,b):
    print "SUBTRACTING %d = %d" % (a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLAYING %d * %d "% (a,b)
    return a * b

def divide(a,b):
    print "DIVDING %d / %d "% (a,b)
    return a / b

print "Let's do some math with just fuctions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age:%d,Height:%d,Weight:%d,IQ:%d" % (age,height,weight,iq)

print "Here is a puzzle."

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you do it by hand?"

kel = subtract(add(24,divide(34,100)),1023)
print kel
